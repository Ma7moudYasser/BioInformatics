from tkinter import *

from cairo import HINT_STYLE_SLIGHT







myMain = Tk()
myMain.title('Bioinformatics tool box')
myMain.geometry('1000x870')
myMain.resizable(False, False)


title = Label(myMain, text = 'Bioinformatics-ToolBox', font = ('tajawal', 15), fg = 'blue')
title.pack()


frame = Frame(myMain, width = '400', height= '200', bg = 'blue')
frame.place(x= 0,y = 30)





frame2 = Frame(myMain, width = '400', height= '200', bg = 'blue')
frame2.place(x = 650, y = 30)


frame3 = Frame(myMain, width = '400', height = '200', bg = 'blue')
frame3.place(x = 0, y = 270)

frame4 = Frame(myMain, width = '400', height = 200, bg = 'blue' )
frame4.place(x= 650, y = 270)








myMain.mainloop()