
from tkinter import *
import tkinter.messagebox
import re
window = Tk()
window.title("Word Format")
window.geometry("600x500+30+30")

frame1 = Frame(window,highlightbackground="red",highlightthickness=1,bd=5,height=150,width=580)
frame1.place(x=10,y=0)

label1 = Label(frame1, text = "Choose your output options:",bd=5)
label1.place(x=0, y=10)

var=IntVar()
R1 = Radiobutton(frame1, text="As Entered", value=1,variable=var)
R2 = Radiobutton(frame1, text="Reverse",value=2,variable=var)
R1.place(x=0,y=30)
R2.place(x=0,y=55)

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
C1 = Checkbutton(frame1, text = "Count words", variable = v1,onvalue=1)
C2 = Checkbutton(frame1, text = "Count letters", variable = v2,onvalue=2)
C3 = Checkbutton(frame1, text = "Count digits", variable = v3,onvalue=3)
C1.place(x=140,y=30)
C2.place(x=140,y=55)
C3.place(x=140,y=80)

frame2 = Frame(window,highlightbackground="red",highlightthickness=1,bd=5,height=140,width=580)
frame2.place(x=10,y=160)
label2 = Label(frame2, text ="Enter your text:")
label2.place(x=0,y=10)
txtfld=Entry(frame2)
txtfld.place(x=100,y=10,width=400)


val=0
def print_message():
    text1 = txtfld.get()
    word_split = text1.split()
    label4.config(text=word_split)
    #return word_split

def reverse():
    text = txtfld.get()
    rev = text[::-1]
    rev_split = rev.split()
    label4.config(text=rev_split)

def count_word():
    text= txtfld.get()
    word_split= text.split()
    word_count=len(word_split)
    #word_count= len(re.findall(r'\w+',text))
    return word_count

def count_letters_digits():
    digit = letter = 0
    text = txtfld.get()
    for ch in text:
        if ch.isdigit():
            digit = digit + 1
        elif ch.isalpha():
            letter = letter + 1
        else:
            pass
    return {'letter':letter,'digit':digit}

#Button: Run
def onClick():
    if (v1.get() != 1) and (v2.get() != 2) and (v3.get() != 3):
        if var.get()==1:
            print_message()
    if (v1.get() != 1) and (v2.get() != 2) and (v3.get() != 3):
        if var.get() == 2:
            reverse()

    if (v1.get() == 1) and (v2.get()!=2) and (v3.get() != 3):
        if var.get()==1:
            print_message()
            val = count_word()
            #tkinter.messagebox.showinfo("Analysis Results", "- Number of words: "+str(val['word_count'])+'\n'+"- Number of Letters: "+str(val['letter'])+'\n'+"- Number of Digits: "+str(val['digit']))
            tkinter.messagebox.showinfo("Analysis Results", "- Number of words: " + str(val))
    if (v1.get() == 1) and (v2.get()!=2) and (v3.get() != 3):
        if var.get()==2:
            reverse()
            val = count_word()
            #tkinter.messagebox.showinfo("Analysis Results", "- Number of words: "+str(val['word_count'])+'\n'+"- Number of Letters: "+str(val['letter'])+'\n'+"- Number of Digits: "+str(val['digit']))
            tkinter.messagebox.showinfo("Analysis Results", "- Number of words: " + str(val))

    if (v2.get() == 2) and (v1.get() != 1) and (v3.get() != 3):
        # if v2.get()==2:
        if var.get() == 2:
            reverse()
            val=count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of letters: " + str(val['letter']))

    if (v2.get() == 2) and (v1.get()!=1) and (v3.get() != 3):
       #if v2.get()==2:
        if var.get()==1 :
            print_message()
            val= count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of letters: " + str(val['letter']))

    if (v3.get() == 3) and (v2.get() != 2) and (v1.get() != 1):
        if var.get()==1:
            print_message()
            val=count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of digits: " + str(val['digit']))
    if (v3.get() == 3) and (v2.get() != 2) and (v1.get() != 1):
        if var.get() == 2:
            reverse()
            val=count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of digits: " + str(val['digit']))
    if (v1.get() == 1) and (v2.get()==2) and (v3.get() == 3):
        if var.get()==1: # or  var.get() == 2:
            print_message()
            val = count_word()
            val1= count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of words: "+str(val)+'\n'+"- Number of Letters: "+str(val1['letter'])+'\n'+"- Number of Digits: "+str(val1['digit']))
    if (v1.get() == 1) and (v2.get()==2) and (v3.get() == 3):
        if var.get() == 2:
            reverse()
            val = count_word()
            val1= count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of words: "+str(val)+'\n'+"- Number of Letters: "+str(val1['letter'])+'\n'+"- Number of Digits: "+str(val1['digit']))

    if (v1.get() == 1) and (v2.get() == 2) and (v3.get() != 3):
        if var.get() == 1: # or  var.get() == 2:
            print_message()
            val = count_word()
            val1=count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of words: "+str(val)+'\n'+"- Number of Letters: "+str(val1['letter']))
    if (v1.get() == 1) and (v2.get() == 2) and (v3.get() != 3):
        if var.get() == 2:
            reverse()
            val = count_word()
            val1 = count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results",
                                        "- Number of words: " + str(val) + '\n' + "- Number of Letters: " + str(
                                            val1['letter']))

    if (v1.get() == 1) and (v2.get() != 2) and (v3.get() == 3):
        if var.get() == 1: #or  var.get() == 2:
            print_message()
            val = count_word()
            val1=count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of words: " + str(val) + '\n' + "- Number of digits: " + str(val1['digit']))
    if (v1.get() == 1) and (v2.get() != 2) and (v3.get() == 3):
        if var.get() == 2:
            reverse()
            val = count_word()
            val1 = count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results",
                                        "- Number of words: " + str(val) + '\n' + "- Number of digits: " + str(
                                            val1['digit']))

    if (v1.get() != 1) and (v2.get() == 2) and (v3.get() == 3):
        if var.get() == 1: # or  var.get() == 2:
            print_message()
            val=count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of Letters: " + str(val['letter']) + '\n' + "- Number of digits: " + str(val['digit']))
    if (v1.get() != 1) and (v2.get() == 2) and (v3.get() == 3):
        if var.get() == 2:
            reverse()
            val=count_letters_digits()
            tkinter.messagebox.showinfo("Analysis Results", "- Number of Letters: " + str(val['letter']) + '\n' + "- Number of digits: " + str(val['digit']))

#Button 2: reset
def clear_text():
    txtfld.delete(0,END)

B1 = Button(frame2, text ="Run",command=onClick)
B1.place(x=100,y=40)

B2 = Button(frame2, text ="reset",command=clear_text)
B2.place(x=140,y=40)

B3 = Button(frame2, text ="Quit",command=window.destroy)
B3.place(x=180,y=40)

frame3 = Frame(window,highlightbackground="red",highlightthickness=1,width=580,height=180,bd=5)
frame3.place(x=10,y=310)

label3 = Label(frame3, text = "Here is the output:")
label4 = Label(frame3)  # for printing the output
label3.place(x=0,y=10)
label4.place(x=100,y=10)

window.mainloop()