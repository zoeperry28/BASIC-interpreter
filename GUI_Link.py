import start as run

class LINK:
    
    lines = []        # class variable shared by all instances
    LEN_OF_LINE_NO = 0 
    
    def __init__(self, program_text):
        self.program_text = program_text    # instance variable unique to each instance
        self.lines = program_text

    def check_conventions(self):
        
        for i in range (0, len(self.lines)):
            # Check for <NO> <COM>            
            for lin in range(0, len(self.lines[i])): 
                CURRENT_CHAR = self.lines[i][lin]
                
                if (CURRENT_CHAR.isspace() == 1):
                    LINE_NO = self.lines[0:lin]
                    LEN_OF_LINE_NO = len(LINE_NO)
                    print(LINE_NO)
                    return True;
            
            
                if(CURRENT_CHAR.isnumeric() == False):
                    return False;
                    
    def run_all_lines(self):
        print("ok")
    
        VALID_BASIC = self.check_conventions()
        
        if(VALID_BASIC):
            f = open("DEMO.BASIC", "w")
            
            for i in range(0,len(self.lines)) :  
                f.write(self.lines[i])
            f.close()

            run.BASIC_Load_Lines("DEMO.BASIC")
        else : 
            print("i dont recognise this...")
            
