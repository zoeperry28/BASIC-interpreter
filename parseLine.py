import BASIC_Keywords as KEY

def BASIC_Parse_Line(lines):
    for LINE in lines: 
        if (LINE[1].find("CLS") != -1):
            KEY.BASIC_CLS()
        elif ((LINE[1].find("PRINT") != -1) or ((LINE[1].find("?") != -1 ))):
            KEY.BASIC_PRINT(LINE[2])
        elif (LINE[1].find("INPUT") != -1):
            KEY.BASIC_INPUT(LINE[2])
        elif (LINE[1].find("END") != -1):
            KEY.BASIC_END(LINE[2])
        elif (LINE [1].find("GOTO") != -1):
            KEY.BASIC_GOTO(LINE, lines)
       
def BASIC_Parse_Single_Line(LINE):
        if (LINE[1].find("CLS") != -1):
            KEY.BASIC_CLS()
        elif ((LINE[1].find("PRINT") != -1) or ((LINE[1].find("?") != -1 ))):
            KEY.BASIC_PRINT(LINE[2])
        elif (LINE[1].find("INPUT") != -1):
            KEY.BASIC_INPUT(LINE[2])
        elif (LINE[1].find("END") != -1):
            KEY.BASIC_END(LINE[2])
        elif (LINE [1].find("GOTO") != -1):
            KEY.BASIC_GOTO(LINE, LINE)
       