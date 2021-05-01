import tkinter
from tkinter.font import Font
import PyDictionary
import pyttsx3


tk = tkinter.Tk()
tk.title('Dictionary')
tk.geometry('200x400')
tk.config(bg='yellow')
tk.iconbitmap('1.ico')

def findMeaning():
    word = myInput.get()
    fontInput4 = Font(size=20, slant='italic')
    meaning = PyDictionary.PyDictionary.meaning(word)
    global meaningLabel
    meaningLabel = tkinter.Label(tk, text='The meaning of {} is {}'.format(word, meaning), bg='green', bd=0, font=fontInput4, fg='white', pady=20, padx=20)
    meaningLabel.pack(padx=1, pady=1)
    talk = pyttsx3.init()
    talk.say(meaningLabel['text'])
    talk.runAndWait()


fontInput1 = Font(size=20, slant="italic")
fontInput2 = Font(size=40, weight="bold", family='Courier')
fontInput3 = Font(size=20, family='Roboto')
Heading = tkinter.Label(tk, text='Dictionary', font=fontInput2, bg='yellow')
Heading.pack()
myInput = tkinter.Entry(tk, width=30, borderwidth=5, textvariable=1, font=fontInput1)
myInput.insert(0, 'Enter a word')
myInput.pack(padx=10, pady=10, ipady=10)
# tk.maxsize(200, 400)
# tk.minsize(0, 0)
btn = tkinter.Button(tk, text='Click Me', padx=20, pady=10, font=fontInput3, bg='black', fg='white', command=findMeaning)
btn.pack(padx=10, pady=10)
tk.mainloop()