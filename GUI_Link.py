import start as run

class LINK:
    
    lines = []        # class variable shared by all instances

    def __init__(self, program_text):
        self.program_text = program_text    # instance variable unique to each instance
        self.lines = program_text

    def check_conventions(self):
        print("ok")
        
    def run_all_lines(self):
        print("ok")
        run.BASIC_Load_Lines()