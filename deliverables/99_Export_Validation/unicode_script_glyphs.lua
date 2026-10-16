-- PDF-only display fallback: preserve superscript/subscript meaning with
-- standard LaTeX text commands when the CJK font lacks the Unicode glyph.
local super = {
  [0x2070]="0", [0x00B9]="1", [0x00B2]="2", [0x00B3]="3",
  [0x2074]="4", [0x2075]="5", [0x2076]="6", [0x2077]="7",
  [0x2078]="8", [0x2079]="9"
}
local sub = {
  [0x2080]="0", [0x2081]="1", [0x2082]="2", [0x2083]="3",
  [0x2084]="4", [0x2085]="5", [0x2086]="6", [0x2087]="7",
  [0x2088]="8", [0x2089]="9", [0x2099]="n"
}
function Str(el)
  if not FORMAT:match("latex") then return nil end
  local result, buffer, changed = pandoc.List(), "", false
  for _,cp in utf8.codes(el.text) do
    local value, command = super[cp], "\\textsuperscript"
    if not value then value,command=sub[cp],"\\textsubscript" end
    if value then
      if #buffer>0 then result:insert(pandoc.Str(buffer));buffer="" end
      result:insert(pandoc.RawInline("latex",command.."{"..value.."}"))
      changed=true
    else buffer=buffer..utf8.char(cp) end
  end
  if #buffer>0 then result:insert(pandoc.Str(buffer)) end
  if changed then return result end
end

function Code(el)
  if not FORMAT:match("latex") then return nil end
  if #el.text>=40 and el.text:match("^[0-9a-fA-F]+$") then
    local chunks={}
    for i=1,#el.text,8 do chunks[#chunks+1]=el.text:sub(i,i+7) end
    return pandoc.RawInline("latex","\\texttt{"..table.concat(chunks,"\\allowbreak{}").."}")
  end
end
