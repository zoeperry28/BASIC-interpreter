import BASIC_Keywords as KEY
import parseLine as PARSE
import BSC_Format as FORM

def BASIC_Load_Lines () :
    filename = "basic_c64.BASIC"
    with open(filename) as f:
        lines = f.read().splitlines()
    lines = FORM.BASIC_Split_String(lines)
    #result = PARSE.BASIC_Parse_Line(lines)

#=====MAIN=====
BASIC_Load_Lines()