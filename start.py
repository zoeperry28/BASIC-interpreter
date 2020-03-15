import BASIC_Keywords as KEY
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)
        panel.SetBackgroundColour('#887ecb')

        sizer = wx.GridBagSizer(0,0)
            
        wx.StaticText(panel, -1, "**** COMMODORE 64 BASIC V2 ****", (100, 10))
        center = wx.StaticText(panel, -1, "64K RAM SYSTEM 38911 BASIC BYTES FREE", (100, 25), (160, -1), wx.ALIGN_CENTER)
    

        text1 = wx.StaticText(panel, label = "READY") 
        sizer.Add(text1, pos = (2, 1), flag = wx.ALL, border = 3) 

        
        temporary = BASIC_Load_Lines()
        k = 0
        for i in range (3, len(temporary)):
            text1 = wx.StaticText(panel, label = str(temporary[k])) 
            sizer.Add(text1, pos = (i, 1), flag = wx.ALL, border = 3) 
            k+=1
        panel.SetSizer(sizer)
        

        
def BASIC_Load_Lines () :
    filename = "start.BASIC"

    with open(filename) as f:
        lines = f.read().splitlines()
    #BASIC_Parse_Line(lines)
    return lines


def BASIC_Parse_Line(lines):
    for row in lines: 
        if (row.find("CLS") != -1):
            KEY.BASIC_CLS()
        elif (row.find("PRINT") != -1):
            KEY.BASIC_PRINT(row)
        elif (row.find("INPUT") != -1):
            KEY.BASIC_INPUT(row)
        
def BASIC_OPEN_WINDOW():
    app = wx.App()
    ex = Example(None, title='Border')
    ex.Show()
    app.MainLoop()
    
#=====MAIN=====
BASIC_OPEN_WINDOW()
BASIC_Load_Lines()
