
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers.nsis import NSISLexer

code = '''
Function .onInit
  ${If} ${Foo}
    MessageBox MB_OK "Asdf \\
Asdf asdf"
  ${EndIf}
FunctionEnd
'''

lexer = NSISLexer()
formatter = HtmlFormatter(full=True, linenos=True)
highlighted_code = highlight(code, lexer, formatter)

# ��������浽 HTML �ļ���
with open("highlighted_code.html", "w") as f:
    f.write(highlighted_code)
