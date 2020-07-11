import BASIC_Keywords as KEY
import parseLine as PARSE
import BSC_Format as FORM

def BASIC_Load_Lines (filename, OUTPUT_TO_GUI) :
    with open(filename) as f:
        lines = f.read().splitlines()
    lines = FORM.BASIC_Split_String(lines)
    result = PARSE.BASIC_Parse_Line(lines)
    
    if(len(result) != 0):
        OUTPUT_TO_GUI.ACTIVE_OUT = True
        OUTPUT_TO_GUI.OUT = result
        print(result)
    
    return OUTPUT_TO_GUI
    
    
#=====MAIN=====
#BASIC_Load_Lines("basic_c64.BASIC")