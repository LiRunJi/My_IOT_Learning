# from tkinter import *
import tkinter as tk


apple=6.5
pear=5.4
bana=7.2
top=tk.Tk()
top.title("物联网竞赛")
labels=[]
entrys=[]

label1=tk.Label(top,text="请输入苹果的重量:")
label2=tk.Label(top,text="请输入梨的重量:")
label3=tk.Label(top,text="请输入香蕉的重量:")
entry1=tk.Entry(top)
entry2=tk.Entry(top)
entry3=tk.Entry(top)
# t1=tk.Text(top)
labels.append(label1)
labels.append(label2)
labels.append(label3)

entrys.append(entry1)
entrys.append(entry2)
entrys.append(entry3)
def load_vertical_lables_entrys(labels:list,entrys:list):
    for i in range(len(labels)):
        labels[i].pack()
        entrys[i].pack()
# label1
# entry1.setvar("sssss")
load_vertical_lables_entrys(labels,entrys)

# list=tk.Listbox(top)
def button_clicked():
    count1 = float(entry1.get())
    count2 = float(entry2.get())
    count3 = float(entry3.get())
    text = "名称   数量   价格"
    text1 = "苹果  " + str(count1) + "k   " + str(apple * count1)
    text2 = "梨      " + str(count2) + "k   " + str(pear * count2)
    text3 = "香蕉  " + str(count3) + "k   " + str(bana * count3)
    text4 = "总价  " + str(apple * count1 + pear * count2 + bana * count3)
    list.insert(0, text)
    list.insert(1, text1)
    list.insert(2, text2)
    list.insert(3, text3)
    list.insert(4, text4)



# btn=tk.Button(top,text="结算",command=button_clicked)
# btn.pack()

top.mainloop()