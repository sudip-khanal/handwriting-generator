import pywhatkit as pk 
from tkinter import *



def data():
    txt=text_area.get(1.0,END) 
    pk.text_to_handwriting(txt,"handwriting.png",[0,0,138])
    print("End")


root = Tk()


root.title("Text To Handwriting Converter")
root.geometry("500x500")
root.resizable(height=False,width=False)
root.config(bg="orange")

top_header=Frame(root,bg="white",width=900,height=100)
top_header.place(x=0,y=0)
Label(top_header,text="Text To Handwriting",bg="white",font="arial 20 bold",fg="black").place(x=100,y=20)

text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=130,height=300,width=350)



btn=Button(root,text="Submit",compound=LEFT,font="arial 14 bold" ,command=data)
btn.place(x=20,y=450)


root.mainloop()