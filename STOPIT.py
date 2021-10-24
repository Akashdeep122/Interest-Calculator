import sqlite3
import csv
from tkinter import *


def Calculate():
    Gui.t1.delete('1.0', END)
    try:
      value = int(Gui.e1_value.get())
      interest = float(Gui.e2_value.get())
      term = int(Gui.e3_value.get())
      name = Gui.e4_value.get()
    except Exception as e:
        Gui.t1.insert(END,"Error: Please")
        Gui.t2.insert(END,"Give me a")
        Gui.t3.insert(END,"valid number")
        
        return

    Answer1=value+(value*interest/100*term)
    Answer2=value*interest/100*term
    csv_file = open('calculator.csv', 'a', newline="")
    writer = csv.writer(csv_file)
    row = [name,value,interest,Answer1]
    writer.writerow(row)

    Gui.t1.delete('1.0', END)
    Gui.t2.delete('1.0', END)
    Gui.t3.delete('1.0', END)
    

    insert(name,value,interest,Answer1)
    Gui.t1.insert(END,Answer1)
    Gui.t2.insert(END,Answer1/12)
    Gui.t3.insert(END,Answer2)
    return
    
window = Tk()

def Gui():
  l1 = Label(window,text="Base Amount",height=1,width=15)
  l1.grid(row=0,column=0)

  l2 = Label(window,text="Interest")
  l2.grid(row = 0,column=2)

  l3 = Label(window,text="Number of Years")
  l3.grid(row=1,column=0)

  l4 = Label(window,text="Your Name")
  l4.grid(row=1,column=2)

  Gui.e1_value=StringVar()
  Gui.e1 = Entry(window,textvariable=Gui.e1_value)
  Gui.e1.grid(row=0,column=1)


  Gui.e2_value=StringVar()
  Gui.e2 = Entry(window,textvariable=Gui.e2_value)
  Gui.e2.grid(row=0,column=3)

  Gui.e3_value=StringVar()
  Gui.e3 = Entry(window,textvariable=Gui.e3_value)
  Gui.e3.grid(row=1,column=1)

  Gui.e4_value=StringVar()
  Gui.e4 = Entry(window,textvariable=Gui.e4_value)
  Gui.e4.grid(row=1,column=3)

  b1 = Button(window,text="Calculate",width=12,command=Calculate)
  b1.grid(row=2,column=1,columnspan=2)

  Gui.t1=Text(window,height=1,width=20)
  Gui.t1.grid(row=3,column=1,columnspan=2)

  l5 = Label(window,text="Final Value")
  l5.grid(row=3,column=0)

  Gui.t2=Text(window,height=1,width=20)
  Gui.t2.grid(row=4,column=1,columnspan=2)

  l6 = Label(window,text="Per Month")
  l6.grid(row=4,column=0)

  Gui.t3=Text(window,height=1,width=20)
  Gui.t3.grid(row=5,column=1,columnspan=2)

  l7 = Label(window,text="Extra Interest To Pay")
  l7.grid(row=5,column=0)

 


        
def insert(name,amount,interest,Answer1):
    name = str(name)
    conn = sqlite3.connect("warnings.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO warns VALUES(?,?,?,?)",(name,amount,interest,Answer1))
    conn.commit()
    conn.close()

#we DONT NEED THIS NOW THO    
def AskandCalc():
  try:
    value = int(input("Please tell the pricipal amount of the interest ,Write amount in integer "))
    if value<0:
        print("I NEED A REAL VALUE Please")
        AskandCalc()
    interest = float(input("Please Tell the interest rate, Decimals Also Allowed "))
    if interest<0.0:
        print("I NEED A REAL VALUE Please")
        AskandCalc()
    term = int(input("How much time is the term, Please Write Value in Years, Write Amount in Number "))
    if term<0:
        print("I NEED A REAL VALUE Please")
        AskandCalc()
    name = input("Could i Have Your name Please?")
  except:
    print("Please write the value Correctly as defined")
    AskandCalc()
  Answer1=value+(value*interest/100*term)
  Answer2=value*interest/100*term
  csv_file = open('calculator.csv', 'a', newline="")
  writer = csv.writer(csv_file)
  row = [name,value,interest,Answer1]
  writer.writerow(row)

  insert(name,value,interest,Answer1)

  print(f"{Answer1}Rs is the Amount to be paid in total \n{Answer2}Rs is the value to be paid extra as Interest \nYou have to Pay {Answer1/(12*term)}Rs each Month")

Gui()


