import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Weight coverter")
root.iconbitmap(r'C:\Users\Dessalegn\Downloads\weight coverter icon.ico')

def weight_convertion():
    kg = float(entry_kg.get())
    weight_in_lb = (kg*2.205)
    label_result['text'] = f"weight in lb: {weight_in_lb}"

label_kg = tkinter.Label(root, text="KG:")
label_kg.pack()

entry_kg = tkinter.Entry(root)
entry_kg.pack()

Button_calculate = tkinter.Button(root, text='Change into lb', command=weight_convertion)
Button_calculate.pack()

label_result = tkinter.Label(root, text="weight in lb:")
label_result.pack()

root.mainloop()

root.quit()