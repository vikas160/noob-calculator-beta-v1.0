from tkinter import *
import os
import pygame

#Noob Calculator made by vikas

pygame.mixer.init()


def get(number):
    pygame.mixer.music.load('cork.mp3')
    pygame.mixer.music.play()
    global Value
    Value=Value+str(number)
    data.set(Value)


def clr():
    global Value
    Value=""
    data.set(" ")
    os.system("cls")



def prime():
 n=data.get()
 if n<=2:
     data.set("Not a prime number")
 else :
  for i in range(2,n):
   if(n%i==0):
        data.set("Not a prime number")
        break

   else :
      data.set("Given number is prime")

def odd():
  even=data.get()

  if(even%2==0):
   data.set("Number is even ")
  else:
   data.set("Number is odd")


def tabel():
  pygame.mixer.music.load('tabv2.mp3')
  pygame.mixer.music.play()
  tab=data.get()

  for i in range (1,11):
     tot=tab*i
     print(tab,"X",i,"=",tot)
     data.set("Table generated in terminal")

def eq():
  pygame.mixer.music.load('shoot.mp3')
  pygame.mixer.music.play()
  global Value
  result=str(eval(Value))
  data.set(result)


def rev():
    num=data.get()
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print("--------------------------------------")
    print("Reversed Number: " + str(reversed_num))
    print("--------------------------------------")
    data.set("Reverse number printed in terminal")

root=Tk()
root.config(bg="pink")
root.title("Adv Cal Made By Vikas")
root.geometry("270x360")
root.maxsize(270,360)
root.minsize(270,360)

Value=""
data=IntVar()
disp=Entry(root,textvariable=data,justify="right",bd=5,bg="light green",width=28,font=("Bold,20"))
disp.grid(row=0,columnspan=50,ipady=15)




btn7=Button(root,text=7,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(7))
btn7.grid(row=1,column=0,pady=4)
btn8=Button(root,text=8,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(8))
btn8.grid(row=1,column=1,pady=4)

btn9=Button(root,text=9,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(9))
btn9.grid(row=1,column=2,pady=4)

btnad=Button(root,text="+",height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get("+"))
btnad.grid(row=1,column=3,pady=4)

btn4=Button(root,text=4,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(4))
btn4.grid(row=2,column=0,pady=3)
btn5=Button(root,text=5,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(5))
btn5.grid(row=2,column=1,pady=3)

btn6=Button(root,text=6,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(6))
btn6.grid(row=2,column=2,pady=3)

btnmul=Button(root,text="x",height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get("*"))
btnmul.grid(row=2,column=3,pady=4)

btn1=Button(root,text=1,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(1))
btn1.grid(row=3,column=0,pady=3)
btn2=Button(root,text=2,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(2))
btn2.grid(row=3,column=1,pady=3)
btn3=Button(root,text=3,height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(3))
btn3.grid(row=3,column=2,pady=3)
btndev=Button(root,text="÷",height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda : get("/"))
btndev.grid(row=3,column=3,pady=4)

btn0=Button(root,text="0",height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get(0))
btn0.grid(row=4,column=1,pady=4)
btnmin=Button(root,text="-",height=2,width=6,bd=3,font=("ariel,12,bold"),command=lambda:get('-'))
btnmin.grid(row=4,column=3,pady=4)

btneq=Button(root,text="=",height=2,width=6,bd=3,font=("ariel,12,bold"),command=eq)
btneq.grid(row=4,column=2,pady=4)

btneq=Button(root,text="Clr",height=2,width=6,bd=3,font=("ariel,12,bold"),command=clr)
btneq.grid(row=4,column=0,pady=4)


btnprim=Button(root,text="Prime",height=2,width=6,bd=3,font=("ariel,10,bold"),command=prime)
btnprim.grid(row=5,column=0,pady=4)


btnodd=Button(root,text="O/E",height=2,width=6,bd=3,font=("ariel,10,bold"),command=odd)
btnodd.grid(row=5,column=1,pady=4)

btntabel=Button(root,text="TG",height=2,width=6,bd=3,font=("ariel,10,bold"),command=tabel)
btntabel.grid(row=5,column=2,pady=4)

btnrev=Button(root,text="RNUM",height=2,width=6,bd=3,font=("ariel,10,bold"),command=rev)
btnrev.grid(row=5,column=3,pady=4)



root.mainloop()



