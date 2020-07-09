import os
import time
import re
import sys
import parseLine as PARSE
def BASIC_CLS():
    time.sleep(2)
    clear = lambda: os.system('clear')
    
def BASIC_PRINT(OUTSTRING):
    i = 0 
    end = 0
    PARAM = []
    LOCATIONS = [] 
    STRINGS_FOUND = ""
    ALLSTR = []
    if (OUTSTRING.find("\"") != -1):
        for m in re.finditer('\"', OUTSTRING):
            end = m.end() + 1
            i+=1
            LOCATIONS.append(end)
            if (len(LOCATIONS) == 2):
                PARAM.append(LOCATIONS)
                LOCATIONS = []

        for i in range(len(PARAM)):
            j = int(PARAM[i][0]) - 1
            while j != (PARAM[i][1] - 2):
                STRINGS_FOUND += OUTSTRING[j]
                j+=1
        ALLSTR.append(STRINGS_FOUND)
        if(OUTSTRING.find("$") != -1):
            return ALLSTR
        elif (OUTSTRING.find("$") == -1):
            for i in range(len(ALLSTR)):
                print(ALLSTR[i])
    else:
        print("")

def BASIC_INPUT(OUTSTRING):

    TO_PRINT = ""
    current_char = ""
    i = OUTSTRING.find("\"") + 1

    time.sleep(2)

    while current_char != "\"":
        TO_PRINT += current_char
        current_char = OUTSTRING[i]
        i+=1

    g = input(TO_PRINT) 
    
def BASIC_END(OUTSTRING):
    quit()
    
def BASIC_GOTO(GOTO_LINE, ALL_LINES):
    count  = 1 
    LINE_TO_GOTO = GOTO_LINE[2].replace(" ", "") 
    for row in ALL_LINES:
        count = count + 1
        if (row[0].find(LINE_TO_GOTO) != -1):
            PARSE.BASIC_Parse_Single_Line(row)
            if(count == len(ALL_LINES)):
                while(1):
                  PARSE.BASIC_Parse_Single_Line(row)  
            else: 
               PARSE.BASIC_Parse_Line(ALL_LINES)  