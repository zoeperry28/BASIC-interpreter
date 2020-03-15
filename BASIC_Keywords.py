import os
import time
import re

def BASIC_CLS():
    time.sleep(2)
    clear = lambda: os.system('clear')
    clear()

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
    print(g) 

