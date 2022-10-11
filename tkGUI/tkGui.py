# from tkinter import *
from connection_pool.uart_connection import ble_uart
import tkinter as tk


apple=6.5
pear=5.4
bana=7.2
top=tk.Tk()
top.geometry("500x500")
top.title("物联网竞赛")
labels=[]
entrys=[]
def make_show(temperature,humidity,smoke):
    s=f'''
    温度: {temperature}
    湿度: {humidity}
    烟雾: {smoke}
    '''
    return s

def refreshText(text:tk.Text,str_show):
    text.delete(0.0, tk.END)
    text.insert(tk.INSERT, str_show)
    text.update()


label1=tk.Label(top,text="要发送的控制指令:")
label3=tk.Label(top,text="当前的信息:")
entry1=tk.Text(top,width=200,height=20)
# entry2=tk.Entry(top)
entry3=tk.Text(top,width=200,height=10)
labels.append(label1)
# labels.append(label2)
labels.append(label3)

entrys.append(entry1)
# entrys.append(entry2)
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
    try:
       s=entry1.get("0.0","end").strip()
       s=s.replace("\n",'')
       s=s.replace("\r\n",'')
       ble_uart.write(bytes(s,encoding='utf-8'))
       ble_uart.write(bytes('\n',encoding='utf-8'))
       print( entry1.get("0.0", "end").strip())
       print(entry1.get("0.0", "end"))
       refreshText(entry1,'发送成功!')
    except Exception as e:
        refreshText(entry1, e)




btn=tk.Button(top,text="发送控制",command=button_clicked)
btn.pack()

def ui_main():
    top.mainloop()