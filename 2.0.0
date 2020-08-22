#-*- coding: UTF-8 -*-


#import and make global items 
from tkinter import *
from tkinter.messagebox import *
from bs4 import BeautifulSoup
import tkinter.font as f
import getpass,os,requests,zipfile,shutil,random,send2trash,ctypes
from tkinter import filedialog


#global main and game1 items
computeruser = "C:\\Users\\"+getpass.getuser()+"\\Desktop\\"
zhanghao,password,dengluchuangkou,zhucechuangkou,main,guess,game1tk,number=None,None,Tk(),None,None,None,None,None
font1 = f.Font(size=30)
version = ['1.0.0.py','1.1.1.py']
#global game2 items
x,f1,theheight,thespeed=1,f.Font(size=45),[],[]
s=700

#require from this
def require():
    global computeruser,zhanghao,password,dengluchuangkou,zhucechuangkou
    try:
        res = requests.get("https://github.com/Xiaohanlin1014/zhugaozi")
        result = requests.get("https://github.com/Xiaohanlin1014/zhugaozi/archive/master.zip")
        with open(computeruser+"master.zip", "wb") as file:  
            file.write(result.content)
            file.close()
            res.close()
            result.close()
            print(computeruser+"zhugaozigames")
            unpackedzip(computeruser+"master.zip",computeruser+"\\zhugaozigames",1)
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
            #shutil.move(computeruser+'/zhugaozigames/zhugaozi-master',computeruser+'/zhugaozigames')
            send2trash.send2trash(computeruser+'/zhugaozigames/'+version[-1])
            showinfo(title='提示',message='有新版本!请在./zhugaozi-master(或./)目录下寻找新版本运行')
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
    os.makedirs(computeruser+'zhugaozigames/itemzhugaozi')
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



def k(HZ):
    global theheight
    p=ctypes.windll.kernel32
    p.Beep(HZ,500)
    theheight.append(HZ)
    thespeed.append(s)
    print(theheight)
    print(thespeed)


def height(h):
    global x
    x = h

def speed(speed):
    global s
    s=speed

def save():
    '''
    Save your play to a .zhugaozi file and back to mainwindow.
    '''
    global a
    F=open(filedialog.asksaveasfilename(title='保存猪羔子文件', filetypes=[('猪羔子', '*.zhugaozi'), ('All Files', '*')]),'w')
    for x in range(len(thespeed)):
        F.write(str(theheight[x])+','+str(thespeed[x])+'\n')
    F.close()
    #a.destroy()
def delete():
    '''
    Delete your last play.
    '''
    global theheight,thespeed
    del thespeed[-1]
    del theheight[-1]

def game2():
    '''
    The main code for Zhugaozi Piano Player.
    '''
    global a,main#,f1
    #f1=f.Font(size=45)
    main.destroy()
    a=Tk()
    #a.geometry('1920x1080')
    a.title('Zhugaozi Piano Player')
    Button(a,text='C',command=lambda: k(131*x),fg='red',font=f.Font(size=45)).grid(row=1,column=1)
    Button(a,text='D',command=lambda: k(147*x),fg='orange',font=f.Font(size=45)).grid(row=1,column=2)
    Button(a,text='E',command=lambda: k(165*x),fg='yellow',font=f.Font(size=45)).grid(row=1,column=3)
    Button(a,text='F',command=lambda: k(175*x),fg='green',font=f.Font(size=45)).grid(row=1,column=4)
    Button(a,text='G',command=lambda: k(196*x),fg='pink',font=f.Font(size=45)).grid(row=1,column=5)
    Button(a,text='A',command=lambda: k(220*x),fg='blue',font=f.Font(size=45)).grid(row=1,column=6)
    Button(a,text='B',command=lambda: k(247*x),fg='purple',font=f.Font(size=45)).grid(row=1,column=7)
    Button(a,text='低音',command=lambda: height(1),fg='purple',font=f.Font(size=45)).grid(row=2,column=1)
    Button(a,text='中音',command=lambda: height(2),fg='purple',font=f.Font(size=45)).grid(row=2,column=2)
    Button(a,text='高音',command=lambda: height(4),fg='purple',font=f.Font(size=45)).grid(row=2,column=3)
    Button(a,text='1/8',command=lambda: speed(500),fg='purple',font=f.Font(size=45)).grid(row=2,column=4)
    Button(a,text='1/4',command=lambda: speed(1000),fg='purple',font=f.Font(size=45)).grid(row=2,column=5)
    Button(a,text='1/2',command=lambda: speed(2000),fg='purple',font=f.Font(size=45)).grid(row=2,column=6)
    Button(a,text='保存并退出',command=save,fg='purple',font=f.Font(size=45)).grid(row=3,column=5)
    Button(a,text='<--',command=delete,fg='red',font=f.Font(size=45)).grid(row=3,column=3)
    menuBar = Menu(a) 
    sonMenu = Menu(menuBar)
    sonMenu.add_command(label='播放并继续编辑文件',command=play)
    sonMenu.add_command(label='',command=play)
    print(f1)#test
    menuBar.add_cascade(label = "文件", menu = sonMenu)
    a["menu"] = menuBar
    a.mainloop()

def play():
    '''
    Play your file.
    '''
    F=open(filedialog.askopenfilename(title='选择猪羔子文件', filetypes=[('猪羔子', '*.zhugaozi'), ('All Files', '*')]),'r')
    read=F.readlines()
    print(read)
    for x in read:
        print('in play')
        music=x.split(',')
        print(x)
        p=ctypes.windll.kernel32
        p.Beep(int(music[0]),int(music[1]))
        print(x)
require()
