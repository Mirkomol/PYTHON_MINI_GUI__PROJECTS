import time
from tkinter import *

# for i in range(30,0, -1):
#     print(i)
#     time.sleep(1)
#
pencere = Tk()

i = 0
def yaz():
    global i
    i = i+1
    l.configure(text=str(i))
    pencere.after(1000,yaz)

l = Label(text=0, font = "Verdana 16 bold")
l.place(x=10,y=10)

yaz()


pencere.mainloop()