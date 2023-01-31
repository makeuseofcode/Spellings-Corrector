from tkinter import *
from spellchecker import SpellChecker

corrector = SpellChecker()

def clearAll():
    word1_field.delete(0, END)
    word2_field.delete(0, END)

def correction():
    input_word = word1_field.get()
    corrected_word = corrector.correction(input_word)
    word2_field.delete(0, END)
    word2_field.insert(0, corrected_word)

root = Tk()
root.configure(background='aqua')
root.geometry("900x450")
root.title("Spellings Corrector")

headlabel = Label(root, text='Spellings Corrector', fg='white', bg="blue", font=10)
label1 = Label(root, text="Input Word", fg='black', bg='violet', font=10)
label2 = Label(root, text="Corrected Word",fg='black', bg='violet', font=10)

headlabel.grid(row=0, column=1)
label1.grid(row=1, column=0)
label2.grid(row=3, column=0, padx=100)

word1_field = Entry(font=10)
word2_field = Entry(font=10)
word1_field.grid(row=1, column=1, padx=100, pady=50)
word2_field.grid(row=3, column=1, padx=100, pady=50)

button1 = Button(root, text="Correction", bg="orange", fg="black", font=8, command=correction)
button1.grid(row=2, column=1)
button2 = Button(root, text="Clear", bg="orange", fg="black", font=8, command=clearAll)
button2.grid(row=4, column=1)

root.mainloop()
