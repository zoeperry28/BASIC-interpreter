
def BASIC_Split_String(lines):
    # a BASIC line will be <line no> <command> <text>
    LINE_NO = 0
    COMMAND = ""
    TEXT = ""
    PROGRAM_SET = [0,"",""]
    count = 0 
    test = []

    for LINE_TO_CHECK in lines:
        # Gets the line number from the string
        for lin in range(0, len(LINE_TO_CHECK)): 
            CURRENT_CHAR = LINE_TO_CHECK[lin]
            
            if (CURRENT_CHAR.isspace() == 1):
                LINE_NO = LINE_TO_CHECK[0:lin]
                count = lin
                break;    
       
        for com in range((count+1), len(LINE_TO_CHECK)): 
            CURRENT_CHAR = str(LINE_TO_CHECK[com])
            if ((CURRENT_CHAR.isspace() == 1) or (CURRENT_CHAR == '?')):
                
                if(CURRENT_CHAR.find('?') == -1) :
                    COMMAND = LINE_TO_CHECK[(count+1):com]
                    count = com
                else:
                    COMMAND = "?"
                    count = com + 1
                
                break;    
        
        TEXT = LINE_TO_CHECK[count:len(LINE_TO_CHECK)]  
        test.append([LINE_NO, COMMAND, TEXT] )
    return test