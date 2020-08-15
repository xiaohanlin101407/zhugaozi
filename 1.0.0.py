#-*- coding: UTF-8 -*-


#import and make global items 
from tkinter import *
from tkinter.messagebox import *
from bs4 import BeautifulSoup
import tkinter.font as f
import getpass,os,requests,zipfile,shutil,random,send2trash
computeruser = "C:\\Users\\"+getpass.getuser()+"\\Desktop\\"
zhanghao,password,dengluchuangkou,zhucechuangkou,main,guess,game1tk,number=None,None,Tk(),None,None,None,None,None
font1 = f.Font(size=30)
version = ['1.0.0.py']



#require from this
def require():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou
    try:
        res = requests.get("https://github.com/Xiaohanlin1014/record")
        result = requests.get("https://github.com/Xiaohanlin1014/record/archive/master.zip")
        with open(computeruser+"master.zip", "wb") as file:  
            file.write(result.content)
            file.close()
            res.close()
            result.close()
            print(computeruser+"zhugaozigames")
            unpackedzip(computeruser+"master.zip",computeruser,1)
    except Exception as err:
        print(str(err)+'in line 34')



#unpacking .zip after getting file
def unpackedzip(address,unpackaddress,mode):
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou,version
    try:
        aimzip = zipfile.ZipFile(address)
        aimzip.extractall(unpackaddress)
        aimzip.close()
        os.unlink(address)
    except Exception as err:
        print(str(err)+'in line 47')
    if mode == 1:
        if len(version) < len(os.listdir(computeruser+'/zhugaozigames/zhugaozi-master')):
            shutil.move(computeruser+'/zhugaozigames/zhugaozi-master'+os.chdir(computeruser+'/zhugaozigames/zhugaozi-master')[-1],computeruser+'/zhugaozigames')
            send2trash.send2trash(computeruser+'/zhugaozigames/'+version[-1])
            showinfo(title='提示',message='有新版本!请在同级目录下寻找新版本运行')
        else:
            start()
    elif mode == 2:
        mainwindow()
    else:
        print('ERROR!')
    


#start from this
def start():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou
    a=Tk()
    temprery = os.path.isdir(computeruser+'zhugaozigames/userdata')
    if temprery:
        a.destroy()
        denglu()
    else:
        showinfo(title='提示',message='检测到您还未注册，关闭此窗口以注册')
        a.destroy()
        zhuce()


#into the mainwindow
def denglu():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou
    dengluchuangkou.title('登录')
    #label
    Label(dengluchuangkou,text = '账号：',font = font1).grid(row=1,column=1)
    Label(dengluchuangkou,text = '密码：',font = font1).grid(row=2,column=1)
    #entry
    zhanghao = Entry(dengluchuangkou,width=50)
    zhanghao.grid(row=1,column=2,ipady=20)
    password = Entry(dengluchuangkou,width=50)
    password.grid(row=2,column=2,ipady=20)
    Button(dengluchuangkou,text='登录',command=bijiao,font = font1).grid(row=3,column=2)
    dengluchuangkou.mainloop()

def zhuce():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou
    zhucechuangkou = Tk()
    zhucechuangkou.title('注册')
    #label
    Label(zhucechuangkou,text = '注册账号：').grid(row=1,column=1)
    Label(zhucechuangkou,text = '注册密码：').grid(row=2,column=1)
    #entry
    zhanghao = Entry(zhucechuangkou)
    zhanghao.grid(row=1,column=2)
    password = Entry(zhucechuangkou)
    password.grid(row=2,column=2)
    Button(zhucechuangkou,text='注册',command=xieru).grid(row=3,column=2)
    zhucechuangkou.mainloop()



#check the input
def bijiao():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou
    User = open(computeruser+'zhugaozigames/userdata/username.txt')
    word = open(computeruser+'zhugaozigames/userdata/password.txt')
    if (zhanghao.get() == User.read()) and (password.get() == word.read()):
        showinfo(title='登陆成功',message='登陆成功!关闭此窗口以进入主页面')
        dengluchuangkou.destroy()
        mainwindow()
    else:
        showinfo(title='登陆失败',message='登陆失败，请检查您的输入是否正确')
    

def xieru():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou
    os.makedirs(computeruser+'zhugaozigames/userdata')
    os.makedirs(computeruser+'zhugaozigames/newlogs')
    os.makedirs(computeruser+'zhugaozigames/itemrecord')
    User = open(computeruser+'zhugaozigames/userdata/username.txt','w')
    word = open(computeruser+'zhugaozigames/userdata/password.txt','w')
    User.write(zhanghao.get())
    word.write(password.get())
    User.close()
    word.close()
    showinfo(title='即将登陆',message='关闭此窗口以登录')
    zhucechuangkou.destroy()
    mainwindow()



#main_window
def mainwindow():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou,main
    main=Tk()
    main.title('欢迎来到主窗口')
    try:
        maingif = PhotoImage(file = computeruser+'zhugaozigames/image-master/mainwindow.gif')
        Button(main,text='game1',command=game1).grid(row=1,column=2)
        Button(main,text='game2',command=game2).grid(row=1,column=3)
        Label(main,image = maingif).grid(row=1,column=1)
    except TclError:
        res = requests.get("https://github.com/Xiaohanlin1014/image")
        result = requests.get("https://github.com/Xiaohanlin1014/image/archive/master.zip")
        with open(computeruser+"master.zip", "wb") as file:  
            file.write(result.content)
            file.close()
            res.close()
            result.close()
            showinfo(title='DOWNLAND',message='Downloading the file,close this and login again.')
            main.destroy()
        unpackedzip(computeruser+"master.zip",computeruser+"zhugaozigames",2)
    main.mainloop()
#height
def game1():
    global guess,main,game1tk,number
    main.destroy()
    number = random.randint(1,20)
    game1tk = Tk()
    showinfo(title='提示',message='Nice to meet you.I\'m thinking a number between 1 and 20.Enter your guess in \'please enter\'.')
    Label(game1tk,text='please enter your guess:').grid(row=2,column=1)
    guess = Entry(game1tk)
    guess.grid(row=2,column=2)
    Button(game1tk,text='enter',command=belongs_game1tk).grid(row=3,column=3)
    game1tk.mainloop()


def belongs_game1tk():
    global guess,game1tk,number
    try:
        times = 0
        times = times+1
        playerguess = int(guess.get())
        if (playerguess < number):
            Label(game1tk,text='too low!',bg='red',font=font1,fg='white').grid(row=3,column=1)
        elif (number < playerguess):
            Label(game1tk,text='too high',bg='green',font=font1,fg='white').grid(row=3,column=1)
        else:
            showinfo(title='提示',message='你猜中了！即将返回主窗口')
            game1tk.destroy()
            mainwindow()
    except ValueError as err:
        print(str(err)+guess.get()+'   '+str(type(guess)))

def game2():
    global main
    showinfo(title='提示',message='正在开发中！请等待2.0.0版本发布')

require()
