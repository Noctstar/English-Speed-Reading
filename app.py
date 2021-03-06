import tkinter as tk
import tkinter.messagebox, tkinter.filedialog
from tkinter import font, StringVar, Label, Message, ttk
import os
from nltk.tokenize import sent_tokenize

class Content:

    def __init__(self, output, count):
        self.output  = output
        self.count = count

    def display_sentence(self):
        if self.count == len(self.output):
            win.quit()
        else:
            wait_time = 2000 + (output[self.count].count(' '))*300
            buff.set(output[self.count])
            win.after(wait_time, self.display_sentence)
            self.count += 1


win = tk.Tk()
win.configure(background='gray10')
win.title('Speed Reading')
win.geometry("1000x300")
font1 = font.Font(family="メイリオ", size=15)

fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tk.messagebox.showinfo('Select text file','テキストファイルを選択してください。')
file = tk.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

buff = StringVar()
buff.set('')
message = tk.Message(win, textvariable=buff, font=font1, width=700, bg='gray10', fg='gray87')
message.pack(fill=tk.BOTH, expand=1)

def on_config(event):
    event.widget.config(width=win.winfo_width())
message.bind("<Configure>", on_config)

file_content = open(file, encoding="utf8", errors='ignore').read()
output = sent_tokenize(file_content)
for i in range(len(output)):
    output[i] = output[i].replace('\n', ' ')

content = Content(output, 0)
content.display_sentence()

win.mainloop()
