"""Synthetic mathematical checks only; no empirical observations or conclusions."""
import itertools
import math
import unittest

import numpy as np
from scipy.stats import t

from transition_models import (
    NIGPrior, adoption_share, annual_differences, corner_bounds,
    cumulative_fuel_ratio, fit_nig, fuel_ratio, latest_forecast,
    predictive_intensity, required_deployment_rate, rolling_forecast,
    run, sobol_stress_test,
)


class ForecastChecks(unittest.TestCase):
    def test_conjugate_posterior_and_horizon_variance(self):
        posterior = fit_nig([-0.01, 0.01], NIGPrior())
        self.assertEqual(posterior.n, 2)
        self.assertEqual(posterior.kappa, 3)
        self.assertEqual(posterior.alpha, 3)
        self.assertAlmostEqual(posterior.mu, 0)
        self.assertAlmostEqual(posterior.beta, 0.0026)
        forecast = predictive_intensity(0.3, posterior, horizon=3)
        expected_scale = math.sqrt(0.0026 / 3 * (3 + 9 / 3))
        self.assertAlmostEqual(forecast["log_scale"], expected_scale)
        self.assertAlmostEqual(forecast["median"], 0.3)
        self.assertAlmostEqual(forecast["intervals"]["95"]["upper"],
                               math.exp(math.log(.3) + t.ppf(.975, 6) * expected_scale))
        self.assertEqual(forecast["point_summary"], "median")

    def test_skip_and_exact_two_fold_small_sample(self):
        short = [{"year": 2000 + k, "i": 0.3 * math.exp(-.01 * k)} for k in range(8)]
        self.assertEqual(rolling_forecast(short)["status"], "skipped_insufficient_valid_differences")
        eleven_years = [{"year": 2015 + k, "i": 0.3 * math.exp(-.01 * k)} for k in range(11)]
        result = rolling_forecast(eleven_years)
        self.assertEqual(result["n_test_origins"], 2)
        self.assertEqual(result["scores"]["all"]["B0"]["test_years"], [2024, 2025])
        self.assertTrue(result["small_test_sample_warning"])
        self.assertLess(result["scores"]["all"]["B1"]["MAE"], 1e-14)
        self.assertGreater(result["scores"]["all"]["B0"]["MAE"], 0)

    def test_no_future_data_leakage(self):
        rows = [{"year": 2000 + k, "i": .4 * math.exp(-.02 * k)} for k in range(15)]
        baseline = rolling_forecast(rows)
        perturbed = [dict(row) for row in rows]
        perturbed[-1]["i"] *= 3
        changed = rolling_forecast(perturbed)
        for old, new in zip(baseline["forecasts"], changed["forecasts"]):
            self.assertEqual(old["prediction"], new["prediction"])
            self.assertLess(old["training_max_year"], old["target_year"])
        self.assertNotEqual(baseline["forecasts"][-1]["actual"], changed["forecasts"][-1]["actual"])

    def test_missing_and_excluded_years_never_bridge(self):
        years = list(range(2010, 2026))
        rows = [{"year": year, "i": .3 * math.exp(-.01 * (year - 2010))} for year in years]
        clean = annual_differences(rows, {2020, 2021, 2022})
        self.assertEqual(len(clean), 11)  # 15 increments, four touch excluded years.
        self.assertTrue(all(x["end"] - x["start"] == 1 for x in clean))
        self.assertFalse(any({x["start"], x["end"]} & {2020, 2021, 2022} for x in clean))
        missing = annual_differences([row for row in rows if row["year"] != 2018])
        self.assertEqual(len(missing), 13)  # Both increments adjoining a missing year disappear.
        self.assertFalse(any(x["start"] == 2017 and x["end"] == 2019 for x in missing))

    def test_zero_mase_denominator_is_undefined(self):
        rows = [{"year": 2000 + k, "i": .3} for k in range(11)]
        result = rolling_forecast(rows)
        for model in ("B0", "B1", "B2"):
            self.assertIsNone(result["scores"]["all"][model]["MASE"])
            self.assertEqual(result["scores"]["all"][model]["n_MASE"], 0)

    def test_actual_difference_set_controls_latest_skip(self):
        rows = [{"year": 2015 + k, "i": .3 * math.exp(-.01 * k)} for k in range(11)]
        self.assertEqual(latest_forecast(rows)["status"], "completed")
        sensitivity = latest_forecast(rows, exclude_years={2020, 2021, 2022})
        self.assertEqual(sensitivity["n_valid_differences"], 6)
        self.assertEqual(sensitivity["status"], "skipped_insufficient_valid_differences")


class DeploymentChecks(unittest.TestCase):
    @staticmethod
    def config():
        # Deliberately synthetic domains used only to verify numerical behavior.
        return {"horizon": 10, "target_fuel_ratio": 1,
                "ranges": {"g": [0, .05], "b": [0, .02],
                           "theta": [.1, .5], "r": [.01, .3]},
                "tau_values": [0, 2, 5], "sobol_power": 5,
                "check_convergence": True, "seed": 13}

    def test_boundary_cases(self):
        baseline = math.exp((.04 - .01) * 10)
        self.assertEqual(adoption_share(0, 1, 0), 0)
        self.assertEqual(adoption_share(2, 1, 2), 0)
        self.assertEqual(adoption_share(3, 1, 2), 1)
        self.assertAlmostEqual(fuel_ratio(10, .04, .01, 0, .2, 2), baseline)
        self.assertAlmostEqual(fuel_ratio(10, .04, .01, .3, 0, 2), baseline)
        self.assertAlmostEqual(fuel_ratio(10, .04, .01, .3, .2, 10), baseline)
        self.assertAlmostEqual(fuel_ratio(10, .04, .01, .3, 1, 2), baseline * .7)
        self.assertAlmostEqual(cumulative_fuel_ratio(10, 0, 0, 0, 0, 0), 10)

    def test_frontier_substitution_and_impossibility(self):
        threshold = required_deployment_rate(10, .04, .01, .5, 2)
        self.assertEqual(threshold["status"], "deployment_threshold_exists")
        r = threshold["required_r"]
        self.assertAlmostEqual(fuel_ratio(10, .04, .01, .5, r, 2), 1, places=13)
        self.assertLess(fuel_ratio(10, .04, .01, .5, r + .01, 2), 1)
        self.assertGreater(fuel_ratio(10, .04, .01, .5, r - .01, 2), 1)
        self.assertEqual(required_deployment_rate(10, .05, 0, .1, 0)["status"],
                         "impossible_even_with_full_adoption")
        self.assertEqual(required_deployment_rate(10, .04, .01, .5, 10)["status"],
                         "impossible_before_deployment_begins")
        self.assertEqual(required_deployment_rate(10, .04, .01, 0, 0)["status"],
                         "impossible_zero_technical_benefit")
        self.assertEqual(required_deployment_rate(10, 0, .01, .5, 0)["required_r"], 0)

    def test_exact_full_adoption_and_monotonicity(self):
        theta = 1 - math.exp(-.3)
        threshold = required_deployment_rate(10, .04, .01, theta, 0)
        self.assertAlmostEqual(threshold["required_r"], 1, places=12)
        args = {"h": 10, "g": .04, "b": .01, "theta": .3, "r": .1, "tau": 2}
        base = fuel_ratio(**args)
        for parameter, value in (("b", .02), ("theta", .4), ("r", .2)):
            self.assertLess(fuel_ratio(**{**args, parameter: value}), base)
        for parameter, value in (("g", .05), ("tau", 3)):
            self.assertGreater(fuel_ratio(**{**args, parameter: value}), base)

    def test_corners_enclose_full_grid_and_sobol_points(self):
        config = self.config()
        bounds = corner_bounds(config)
        low = bounds["best_corner"]["terminal_fuel_ratio"]
        high = bounds["worst_corner"]["terminal_fuel_ratio"]
        inputs = [config["ranges"][name] for name in ("g", "b", "theta", "r")]
        for g, b, theta, r, tau in itertools.product(*inputs, config["tau_values"]):
            value = fuel_ratio(config["horizon"], g, b, theta, r, tau)
            self.assertGreaterEqual(value + 1e-14, low)
            self.assertLessEqual(value - 1e-14, high)
        simulated = sobol_stress_test(config, save_draws=True)
        self.assertEqual(simulated["analysis_type"], "conditional_uncalibrated_deployment_scenarios")
        self.assertEqual(len(simulated["design_points"]), 3 * 2 ** 5)
        self.assertEqual(len(simulated["resolution_comparison"]), 3)
        self.assertTrue(all(low <= row["terminal_fuel_ratio"] <= high for row in simulated["design_points"]))
        self.assertEqual(simulated, sobol_stress_test(config, save_draws=True))

    def test_explicit_configuration_required_and_constant_ranges_work(self):
        with self.assertRaises(ValueError):
            sobol_stress_test({"horizon": 10})
        config = self.config()
        config["ranges"] = {"g": [0, 0], "b": [0, 0], "theta": [0, 0], "r": [0, 0]}
        result = sobol_stress_test(config)
        self.assertTrue(result["exact_domain_bounds"]["entire_domain_meets_target"])
        self.assertTrue(all(row["terminal_fuel_ratio_design_quantiles"]["0.5"] == 1
                            for row in result["delay_summaries"]))
        self.assertEqual(run([])["conditional_deployment_scenarios"]["status"],
                         "skipped_no_explicit_scenario_configuration")


if __name__ == "__main__":
    unittest.main(verbosity=2)
