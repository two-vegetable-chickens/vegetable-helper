from tkinter import *
from functools import partial
import re
import tkinter
from math import *
from decimal import Decimal
from decimal import getcontext 
from tkinter import ttk
 
import tkinter.simpledialog as dl 
import tkinter.messagebox as mb
 
getcontext().prec=5
 
global value1,value2,data 
global var_Firstinput,diyige,dierge 
global var_Secondinput_2 
value1='美元'
value2='人民币'
def huoquzhi1(*args):
    global value1
    value1=myCombox_1.get()
    
def huoquzhi2(*args):
    global value2
    value2=myCombox_2.get()
def zhuanhuan():
    global value1,value2,data 
    global var_Firstinput,diyige,dierge 
    global var_Secondinput_2 
     
 #   if test(diyige):
    diyi_1= diyige.get()
    diyi_2=float(diyige.get())
    var_Secondinput =str(diyi_2/ data[value1]* data[value2])
    dierge.delete(0,END)
    dierge.insert(END,var_Secondinput )    
   #except:
      # print("出错") 
url='http://http://www.hl.anseo.cn/'
data={
'人民币':6.713700,
'美元':1.000000,
'日元':105.23
}
 


def test(entry):
    abc=entry.get()
    for char in abc:
        if '\u4e00' <= char <= '\u9fa5':
            entry.delete(0, END)
            entry.insert(END, '你好歹输入个数好吗')
            return False
    return True       


 

    
  
     
     
#def  xialakuang_get(*args):
 #   value=myCombox_1.get()
 #   print(value)
def moneychange():
    global value1,value2,data 
    global var_Firstinput,diyige 
    global var_Secondinput_2,dierge  
    hui=Tk()
    hui.title("菜鸡汇率器")
    #一个钱币选择表
    global myCombox_1,myCombox_2
    myComboList_1=['人民币','美元','日元']
    myCombox_1 = ttk.Combobox(hui, values=myComboList_1 )
    myCombox_1.configure(state="readonly")
    myCombox_1.current(1)
    myCombox_1 .pack()
    myCombox_1.bind("<<ComboboxSelected>>",huoquzhi1)
    #一个金钱输入框
    global var_Firstinput 
    var_Firstinput= StringVar()
    global diyige
    diyige=Entry(hui,textvariable=var_Firstinput)
    diyige.pack()
  
    #转换的钱币选择表
    myComboList_2=['人民币','美元','日元']
    myCombox_2 = ttk.Combobox(hui, values=myComboList_2 )
    myCombox_2.configure(state="readonly")
    myCombox_2.current(0)
    myCombox_2 .pack()
    myCombox_2.bind("<<ComboboxSelected>>",huoquzhi2)
    #金钱输出框
    global var_Secondinput_2
    var_Secondinput_2= StringVar()
    global dierge
    dierge= Entry(hui,textvariable=var_Secondinput_2)
    dierge.pack()
    #dierge.pack()
    #整个转换按钮
    bt =  Button(hui, text='转换', command=zhuanhuan)
    bt.pack()
    
     
    
    
    hui.mainloop()
    
    

         
 
#print(data['人民币']*data['美元'])

