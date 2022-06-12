#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from powell import *
from numpy import array
import cmath


# In[4]:


def setox():
    global walk,run,swim,tennis,bike,dance,rope,volly
    walk=tk.Button(frame5,width=7,height=2,text="慢走",command=lambda:[switchButtonState(walk),count("慢走")])
    walk.grid(row=0,column=0)
    run=tk.Button(frame5,width=7,height=2,text="跑步",command=lambda:[switchButtonState(run),count("跑步")])
    run.grid(row=0,column=1)
    swim=tk.Button(frame5,width=7,height=2,text="游泳",command=lambda:[switchButtonState(swim),count("游泳")])
    swim.grid(row=0,column=2)
    tennis=tk.Button(frame5,width=7,height=2,text="羽毛球",command=lambda:[switchButtonState(tennis),count("羽毛球")])
    tennis.grid(row=0,column=3)
    bike=tk.Button(frame5,width=7,height=2,text="腳踏車",command=lambda:[switchButtonState(bike),count("腳踏車")])
    bike.grid(row=1,column=0)
    dance=tk.Button(frame5,width=7,height=2,text="跳舞",command=lambda:[switchButtonState(dance),count("跳舞")])
    dance.grid(row=1,column=1)
    volly=tk.Button(frame5,width=7,height=2,text="排球",command=lambda:[switchButtonState(volly),count("排球")])
    volly.grid(row=1,column=2)
    rope=tk.Button(frame5,width=7,height=2,text="跳繩",command=lambda:[switchButtonState(rope),count("跳繩")])
    rope.grid(row=1,column=3)
    checkupbutton=tk.Button(frame6,width=32,height=2,text="結算運動",command=lambda :check())
    checkupbutton.grid(row=1,column=0)
    clear=tk.Button(frame6,width=32,height=2,text="重選",command=lambda :clearup())
    clear.grid(row=2,column=0)

def clearup():
    global totalw,work,calw
    totalw=0
    work=[]
    calw=[]
    walk['state'] = tk.NORMAL
    run['state'] = tk.NORMAL
    swim['state'] = tk.NORMAL
    tennis['state'] = tk.NORMAL
    bike['state'] = tk.NORMAL
    dance['state'] = tk.NORMAL
    volly['state'] = tk.NORMAL
    rope['state'] = tk.NORMAL
def switchButtonState(self):
    if (self['state'] == tk.NORMAL):
        self['state'] = tk.DISABLED
    else:
        self['state'] = tk.NORMAL
def helper():
    global now,target,time
    now=float(((textnow.get("1.0","end")).replace(" ","")).replace("\n",""))
    height=float(((textheight.get("1.0","end")).replace(" ","")).replace("\n",""))
    target=float(((texttar.get("1.0","end")).replace(" ","")).replace("\n",""))
    time=float(((texttime.get("1.0","end")).replace(" ","")).replace("\n",""))
    calculate(now,target,height,time)
def F(x):
    c =  x[0]/x[1]-1.5 # Constraint function
    return (x[0]-(now-target))**2+(x[1]-time)**2+lam*c**2
def count(self):
    global totalw
    totalw=totalw+1
    work.append(self)
def clear_frame(self):
    for widgets in self.winfo_children():
        widgets.destroy()
def check():
    global cal,calw
    if(totalw==0):
        totalw_0=tk.Label(frame8,text="請先選擇至少一樣運動!",font=("Arial",9))
        totalw_0.grid(row=0,column=0)
        return
    else:
        cal=round(totalcal/(totalw),1)
        for i in range(len(work)):
            if (work[i]=="慢走"):
                calw.append(int(cal/3.1))
            elif(work[i]=="跑步"):
                calw.append(int(cal/9.4))
            elif(work[i]=="游泳"):
                calw.append(int(cal/17.5))
            elif(work[i]=="羽毛球"):
                calw.append(int(cal/6.2))
            elif(work[i]=="腳踏車"):
                calw.append(int(cal/3))
            elif(work[i]=="跳舞"):
                calw.append(int(cal/5))
            elif(work[i]=="排球"):
                calw.append(int(cal/5.02)) 
            elif(work[i]=="跳繩"):
                calw.append(int(cal/9))
    clear_frame(frame8)
    label=tk.Label(frame8,text="你需要每天:",font=("Arial",10))
    label.grid(row=0,column=0)
    for i in range(len(work)):
            label=tk.Label(frame8,text=(work[i],calw[i],"分鐘"))
            label.grid(row=i+1,column=0)
    label=tk.Label(frame9,text=("持續",sugtime,"個月"),font=("Arial",10))
    label.grid(row=0,column=0)
    label=tk.Label(frame9,text=("才能從",now,"減到",now-sugkg),font=("Arial",10))
    label.grid(row=1,column=0)
    


# In[5]:



def calculate(now,target,height,time=0):
    clear_frame(frame4)
    global bmi,standw
    bmi=now/(height)**2
    standw=round(22*height**2,1)
    if(now<=target and bmi>24):
        text1=tk.Label(frame4,text="快點減肥!",font=("Arial",9))
        text1.grid(row=0,column=0)
        return
    elif(now <=target and bmi<=24 and bmi>=18):
        text1=tk.Label(frame4,text="現在蠻標準的",font=("Arial",9))
        text1.grid(row=0,column=0)
        return
    elif(now<=target and bmi<18):
        text1=tk.Label(frame4,text="多吃點呦~你太瘦了",font=("Arial",9))
        text1.grid(row=0,column=0)
        return
    else:
        xStart = array([1.5,1])
        global lam,sugtime,sugkg,totalcal,bmiafter
        if (bmi>24):
            lam=10000*bmi
        elif(bmi<=24 and bmi>=20):
            lam=0.05*bmi
        elif(bmi<20 and bmi>=18):
            lam=0.01*bmi
        else:
            lam=0
        xMin,nIter = powell(F,xStart)
        c =  xMin[0]/xMin[1]-1.5
        mindis=F(xMin)-lam*c**2
        sugtime=round(xMin[1],1)
        sugkg=round(xMin[0],1)
        totalcal=7700*sugkg/(sugtime*30)
        text2=tk.Label(frame4,text=("依照你的bmi",round(bmi,1),",建議你在",sugtime,"月內，減去",sugkg,"公斤"),font=("Arial",9))
        text2.grid(row=1,column=0)
        bmiafter=round(((now-sugkg)/(height)**2),1)
        text3=tk.Label(frame4,text=("減重後的bmi為",bmiafter),font=("Arial",9))
        text3.grid(row=2,column=0)
        if(bmiafter>=24):
            text4=tk.Label(frame4,text=("減重之後還是太重，建議目標體重設:",standw),font=("Arial",9))
            text4.grid(row=3,column=0)
            setox()
        elif(bmiafter<24 and bmiafter>=18):
            text4=tk.Label(frame4,text=("                    減重後已到達標準區間                  "),font=("Arial",9))
            text4.grid(row=3,column=0)
            setox()
        elif(bmiafter<18 and bmi<18):
            text4=tk.Label(frame4,text=("減重後會變太輕，建議不要減重，並增重至",standw,"公斤"),font=("Arial",9))
            text4.grid(row=3,column=0)
            setox()
        elif(bmiafter<18 and bmi<=24 and bmi>=18):
            text4=tk.Label(frame4,text=("減重後會變太輕，建議不要減重，已經很標準了~"),font=("Arial",9))
            text4.grid(row=3,column=0)
            setox()
            
        elif(bmiafter<18 and bmi>24):
            text4=tk.Label(frame4,text=("減重後會變太輕，建議減重至",standw,"公斤就好~"),font=("Arial",9))
            text4.grid(row=3,column=0)
            setox()
        


# In[7]:


win =tk.Tk()
win.title("期末專題")
win.geometry("350x600")
frame1= tk.Frame(win)
frame1.grid(row=0,column=0,sticky="w")
frame2=tk.Frame(win)
frame2.grid(row=1,column=0,sticky="w")
frame3=tk.Frame(win)
frame3.grid(row=2,column=0,sticky="w")
frame4=tk.Frame(win)
frame4.grid(row=3,column=0,sticky="w")
frame5=tk.Frame(win)
frame5.grid(row=4,column=0,sticky="w")
frame6=tk.Frame(win)
frame6.grid(row=5,column=0,sticky="w")
frame7=tk.Frame(win)
frame7.grid(row=6,column=0,sticky="w")
frame8=tk.Frame(win)
frame8.grid(row=7,column=0,sticky="w")
frame9=tk.Frame(win)
frame9.grid(row=8,column=0,sticky="w")

labelnow=tk.Label(frame1,text="現在體重: ",font=("Arial",9))
labelnow.grid(row=0,column=0)
textnow=tk.Text(frame1,width=30,height=1)
textnow.grid(row=0,column=1)
labeltar=tk.Label(frame1,text="目標體重:",font=("Arial",9))
texttar=tk.Text(frame1,width=30,height=1)
labeltar.grid(row=1,column=0)
texttar.grid(row=1,column=1)
labelheight=tk.Label(frame1,text="身高(公尺):",font=("Arial",9))
labelheight.grid(row=2,column=0)
textheight=tk.Text(frame1,width=30,height=1)
textheight.grid(row=2,column=1)
labeltime=tk.Label(frame1,text="幾個月內:",font=("Arial",9))
texttime=tk.Text(frame1,width=30,height=1)
labeltime.grid(row=3,column=0)
texttime.grid(row=3,column=1)

checkbutton=tk.Button(frame3,width=38,height=2,text="計算",font=("Arial",9),command=lambda:helper())
checkbutton.grid(row=0,column=0)
totalw=0
work=[]
calw=[]
rio=[]
win.mainloop()


# In[ ]:





# In[ ]:




