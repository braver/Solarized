undefined
xui
window     = this
string     = new String('string')
document   = window.document
simpleExpr = /^#?([\w-]+)$/
idExpr     = /^#/
tagExpr    = /<([\w:]+)/

slice      = (e) ->
  [].slice.call(e, 0)

try
  a = slice(document.documentElement.childNodes)[0].nodeType
catch e
  slice = (e) ->
    ret = []
    for i in e[i]
      ret.push(e[i])
    return ret

window.x$ = window.xui = xui = (q, context) ->
  new xui.fn.find(q, context)
