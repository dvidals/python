from tkinter import *
root=Tk()
myFrame=Frame(root)
myFrame.pack()
operacion=False
res=0
cont=0
contS=0
contM=0
contD=0

theDisplay=StringVar()


display=Entry(myFrame,textvariable=theDisplay,font="Arial 15")
display.grid(row=0,column=0,columnspan=4,pady=10)
display.config(background="black",fg="#00db00",justify="right",width=15)
theDisplay.set("0")

#--------------------------pulsaciones números----------------------
def keys(number):
    global operacion
    
    thenow=theDisplay.get()
    if number=="." and number in thenow and operacion:
            theDisplay.set("0.")
            operacion=False
    elif (number=="." and number in thenow )  or (number=="0"  and thenow=="0" ):
            theDisplay.set(thenow)
    
    elif(number=="." and display.get()=="0"):
            theDisplay.set("0.")

    elif operacion:
            theDisplay.set(number) 
            operacion=False       
    else:
        if(thenow=="0"):
                theDisplay.set(number)
        else:
                theDisplay.set(thenow+number)
        
#--------------------------sumar----------------------


def suma():
        global res,cont,contS,contM,contD,operacion
        operacion=True 
        thenow=float(theDisplay.get())
        if thenow.is_integer():
                thenow=int(thenow)

                
        if cont==0 and contM==0 and contD==0:
                res= res + thenow 
                res=float(res)
                if res.is_integer():
                        res=int(res)
        elif cont!=0:
                res= res - thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                cont=0
        elif contM!=0:
                res=res*thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contM=0
        elif contD!=0:
                res=res/thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contD=0

        contS=contS+1

        
        theDisplay.set(res)   

def multiplica():
        global res,cont,contS,contM,contD,operacion
        operacion=True 
        thenow=float(theDisplay.get())
        if thenow.is_integer():
                thenow=int(thenow)

        if contS==0 and cont==0 and contD==0:
                if contM==0:
                        res=thenow
                        contM=contM+1
                else:
                        res=res*thenow
                        res=float(res)
                        if res.is_integer():
                                res=int(res)
                        
        elif contS!=0:
                res=res+thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contS=0 
                contM=contM+1  
        elif cont!=0:
                res=res-thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                cont=0
                contM=contM+1
        elif contD!=0:
                res=res/thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contD=0
                contM=contM+1
                
        theDisplay.set(res)  
            
        
def divide():
        global res,cont,contS,contM,contD,operacion
        operacion=True
        thenow=float(theDisplay.get())
        if thenow.is_integer():
                thenow=int(thenow)

        if contS==0 and cont==0 and contM==0:
                if contD==0:
                        res=thenow
                        contD=contD+1
                else:
                        res=res/thenow
                        res=float(res)
                        if res.is_integer():
                                res=int(res)

        if contS!=0:
                res=res+thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contS=0 
                contD=contD+1  
        elif cont!=0:
                res=res-thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                cont=0
                contD=contD+1
        elif contM!=0:
                res=res*thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contM=0
                contD=contD+1
        theDisplay.set(res)
                   
        

def resta():
        global res,cont,contS,contM,contD,operacion
        operacion=True
        thenow=float(theDisplay.get())
        res=float(res)
        if thenow.is_integer():
                thenow=int(thenow)
        

        if contS==0 and contM==0 and contD==0:
                if cont==0:
                        res=thenow
                        cont=cont+1                      
                else:
                        res=res-thenow
                        res=float(res)
                        if res.is_integer():
                                res=int(res)
        if contS!=0:
                res=res+thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contS=0 
                cont=cont+1  
        elif contM!=0:
                res=res*thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contM=0
                cont=cont+1
        elif contD!=0:
                res=res/thenow
                res=float(res)
                if res.is_integer():
                        res=int(res)
                contD=0
                cont=cont+1

        
        theDisplay.set(res)   
        
        
        
def resultado():
        global res,cont,contS,contM,contD,resta,operacion
        
        thenow=float(theDisplay.get())

        if thenow.is_integer():
                thenow=int(thenow)
        
        if contS>0:
                resul=res+thenow
                resul=float(resul)
                if resul.is_integer():
                        resul=int(resul)
                theDisplay.set(resul)
        elif cont>0:
                resul=res-thenow
                resul=float(resul)
                if resul.is_integer():
                        resul=int(resul)
                theDisplay.set(resul)
                cont=0
        elif contM>0:
                resul=res*thenow
                resul=float(resul)
                if resul.is_integer():
                        resul=int(resul)
                theDisplay.set(resul)
                contM=0
        elif contD>0:
                resul=res/thenow
                resul=float(resul)
                if resul.is_integer():
                        resul=int(resul)
                theDisplay.set(resul)
                contD=0

        operacion=True
        res=0
        
#-----------------------first row--------------------------
button7=Button(myFrame,text="7",width=5,command=lambda:keys("7"))
button7.grid(row=1,column=0)
button8=Button(myFrame,text="8",width=5,command=lambda:keys("8"))
button8.grid(row=1,column=1)
button9=Button(myFrame,text="9",width=5,command=lambda:keys("9"))
button9.grid(row=1,column=2)
buttonD=Button(myFrame,text="/",width=5,command=lambda:divide())
buttonD.grid(row=1,column=3)

#-----------------------second  row--------------------------
button4=Button(myFrame,text="4",width=5,command=lambda:keys("4"))
button4.grid(row=2,column=0)
button5=Button(myFrame,text="5",width=5,command=lambda:keys("5"))
button5.grid(row=2,column=1)
button6=Button(myFrame,text="6",width=5,command=lambda:keys("6"))
button6.grid(row=2,column=2)
buttonM=Button(myFrame,text="x",width=5,command=lambda:multiplica())
buttonM.grid(row=2,column=3)
#-----------------------third row--------------------------
button1=Button(myFrame,text="1",width=5,command=lambda:keys("1"))
button1.grid(row=3,column=0)
button2=Button(myFrame,text="2",width=5,command=lambda:keys("2"))
button2.grid(row=3,column=1)
button3=Button(myFrame,text="3",width=5,command=lambda:keys("3"))
button3.grid(row=3,column=2)
buttonMin=Button(myFrame,text="-",width=5,command=lambda:resta())
buttonMin.grid(row=3,column=3)

#-----------------------fourth row--------------------------
button0=Button(myFrame,text="0",width=5,command=lambda:keys("0"))
button0.grid(row=4,column=0)
buttonC=Button(myFrame,text=",",width=5,command=lambda:keys("."))
buttonC.grid(row=4,column=1)
buttonSame=Button(myFrame,text="=",width=5,command=lambda:resultado())
buttonSame.grid(row=4,column=2)
buttonPlus=Button(myFrame,text="+",width=5, command=lambda:suma())
buttonPlus.grid(row=4,column=3)


root.mainloop()