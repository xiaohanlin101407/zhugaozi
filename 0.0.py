#-*- coding: UTF-8 -*-
from tkinter import *
from tkinter.messagebox import *
import getpass,os

#start from this
def start():
    computeruser = getpass.getuser()
    temprery = os.path.isdir('C:/users/'+computeruser+'Desktop/zhugaozigames')
    if temprery:
        denglu()
    else:
        showinfo(title='提示',message='检测到您还未注册，关闭此窗口以注册')
        zhuce()

def denglu():
    dengluchuangkou = Tk()
    #label
    Label(dengluchuangkou,text = '账号：').grid(row=1,column=1)
    Label(dengluchuangkou,text = '密码：').grid(row=2,column=1)
    #entry
    zhanghao = Entry(dengluchuangkou)
    zhanghao.grid(row=1,column=2)
    password = Entry(dengluchuangkou)
    password.grid(row=2,column=2)
    Button(dengluchuangkou,text='登录',command=bijiao),Grid(row=3,column=2)

def zhuce():
    dengluchuangkou = Tk()
    #label
    Label(dengluchuangkou,text = '注册账号：').grid(row=1,column=1)
    Label(dengluchuangkou,text = '注册密码：').grid(row=2,column=1)
    #entry
    zhanghao = Entry(dengluchuangkou)
    zhanghao.grid(row=1,column=2)
    password = Entry(dengluchuangkou)
    password.grid(row=2,column=2)
    Button(dengluchuangkou,text='注册',command=xieru).grid(row=3,column=2)
    dengluchuangkou.mainloop()

def bijiao():
    print('bijiao')

def xieru():
    print('xieru')

start()