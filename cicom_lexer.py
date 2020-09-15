from sly import Lexer

class CicomLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { INT, ID, IF, THEN, ELSE, LET, IN,
                MAP, TO, BOOL, EMPTY, ISEQUAL, NEQUAL,  
                PLUS, MINUS, TILDE, STAR, SLASH, EQUAL,
                LETHAN, GETHAN, LTHAN, GTHAN, AMPERSAND,
                BAR, PRIM }

    literals = { '(', ')', '{', '}', ',', ';' }

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    PRIM = r'number\?|function\?|list\?|empty\?|cons\?|cons|first|rest|arity'
    BOOL = r'true|false'
    EMPTY = r'empty'
    ISEQUAL = r':='
    NEQUAL = r'!='
    LETHAN = r'<='
    GETHAN = r'>='
    EQUAL = r'='
    PLUS = r'\+'
    MINUS = r'-'
    STAR = r'\*'
    SLASH = r'/'
    LTHAN = r'<'
    GTHAN = r'>'
    AMPERSAND = r'&'
    BAR = r'\|'
    TILDE = r'~'

    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t

    ID = r'[a-zA-Z_\?][a-zA-Z0-9_\?]*'
    ID['if'] = IF
    ID['in'] = IN
    ID['to'] = TO 
    ID['map'] = MAP
    ID['let'] = LET
    ID['then'] = THEN
    ID['else'] = ELSE

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


if __name__ == '__main__':
    f = open("test.txt", "r")
    data = f.read()
    lexer = CicomLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))