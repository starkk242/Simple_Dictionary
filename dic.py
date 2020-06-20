import tkinter as tk
from PyDictionary import PyDictionary

def evaluate(event):
    word = entry.get()
    dictionary=PyDictionary()
    meaning = dictionary.meaning(word)
    print(meaning)
    
    res.configure(text = "Result: " + str(meaning))
    
w = tk.Tk()
w.geometry("500x500")
tk.Label(w, text="Find Meaning Of:").pack()
entry = tk.Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w,wraplength=300)
res.pack()
w.mainloop()