import BASIC_Keywords as KEY

def BASIC_Load_Lines () :
    filename = "start.BASIC"

    with open(filename) as f:
        lines = f.read().splitlines()
    BASIC_Parse_Line(lines)


def BASIC_Parse_Line(lines):
    for row in lines: 
        if (row.find("CLS") != -1):
            KEY.BASIC_CLS()
        elif (row.find("PRINT") != -1):
            KEY.BASIC_PRINT(row)
        elif (row.find("INPUT") != -1):
            KEY.BASIC_INPUT(row)
        
#=====MAIN=====
BASIC_Load_Lines()