from epics import caget
from threading import Timer
import numpy as np
import smtplib
#import keyboard 

def keyboard_stop():
    keyboard.unhook_all()
def func_call(type_of_limit):
    type = input('Choose the type of'+type_of_limit)
    type_of_PV = ('Choose the type of "y" variable (P2/P3):')

    a = np.loadtxt(type+"boundcoefB2_IR:paraffin:"+type_of_PV+".txt")[0] 
    b = np.loadtxt(type+"boundcoefB2_IR:paraffin:"+type_of_PV+".txt")[1]
    c = np.loadtxt(type+"boundcoefB2_IR:paraffin:"+type_of_PV+".txt")[2]
    d = np.loadtxt(type+"boundcoefB2_IR:paraffin:"+type_of_PV+".txt")[3]
    e = np.loadtxt(type+"boundcoefB2_IR:paraffin:"+type_of_PV+".txt")[4]
    return([type, a, b, c, d, e])

def exp(x,a):
    return(exp(x*a))
def sqrt(x):
    return(sqrt(x*a))         
def pol1(x, a, b):
    return(a*x + b)
def pol2(x, a, b, c):
    return(a*(x**2) + b*x + c)   
def pol3(x, a, b, c, d):
    return(a*(x**3) + b*(x**2) + c*x + d)
  

num_x = int(input('Choose which PV is "x"-variable (insert its number) (IR:paraffin:flow is 11, IR:paraffin:P2 is 7 and IR:paraffin:P3 is 8) '))
num_y = int(input('Choose which PV is "y"-variable (insert its number) (IR:paraffin:flow is 11, IR:paraffin:P2 is 7 and IR:paraffin:P3 is 8) '))          

whatwascalledforup = func_call('bound (up/down)')   
whatwascalledfordown = func_call('bound (up/down)')

#define the function for upper boundary
def bound_up(whatwascalledforup, x):
    return(whatwascalledforup[1]*(x**4) + whatwascalledforup[2]*(x**3) + whatwascalledforup[3]*(x**2) + whatwascalledforup[4]*x + whatwascalledforup[5])
#define the function for lower boundary
def bound_down(whatwascalledfordown, x):
    return(whatwascalledfordown[1]*(x**4) + whatwascalledfordown[2]*(x**3) + whatwascalledfordown[3]*(x**2) + whatwascalledfordown[4]*x + whatwascalledfordown[5])
   
def algorythm(whatwascalledforup, whatwascalledfordown, num_x, num_y):
    
    PVarray = []
    for i in range(1, 10,1):
        PVarray.append(caget('IR:paraffin:GM10:channels.CH0'+str(i)))
    for i in range(10, int(caget('IR:paraffin:GM10:channels.NELM')) + 1,1):
        PVarray.append(caget('IR:paraffin:GM10:channels.CH'+str(i)))
    x = PVarray[num_x - 1]
    y = PVarray[num_y - 1]
    if (bound_up(whatwascalledforup, x) < y) or (bound_down(whatwascalledfordown, x) > y):
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('example@gmail.com','example')
        smtpObj.sendmail('example@gmail.com","example@gmail.com","OUT OF RANGE!")
    #else: continue
    #keyboard.add_hotkey('ctrl+alt', keyboard_stop)
    #keyboard.wait()
    Timer(600, algorythm, [whatwascalledforup,whatwascalledfordown, num_x, num_y], {} ).start()
    

algorythm(whatwascalledforup, whatwascalledfordown, num_x, num_y)  

    
