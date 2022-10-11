import tkinter as tk

global i
i = 0


def refreshText(text:tk.Text,str_show):
    text.delete(0.0, tk.END)
    text.insert(tk.INSERT, i)
    text.update()



windows = tk.Tk()
windows.geometry('500x500')  ## 规定窗口大小500*500像素
windows.resizable(False, False)  ## 规定窗口不可缩放
text1 = tk.Text(windows, width=15, height=1)
text1.grid(row=0, column=1, padx=10, pady=10)
windows.after(1000, refreshText)
windows.mainloop()
