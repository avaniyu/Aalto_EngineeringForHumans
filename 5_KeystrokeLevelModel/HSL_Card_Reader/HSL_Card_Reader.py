# ===============================================================
# Author  : Jiayao Yu, User Interfaces Group, Aalto University
# Init    : August, 2017
# Project : ELEC-D7010 Engineering for Humans course materials
# Topic   : Keystoke-level Model (KLM)
# ===============================================================

# ===============================================================
# Usage description
# -------------------
# - Middle HSL GUI: afford buying ticket action performance
# - Modelling panel: record operator sequence, count and calculate 
# total task completion time
# - If report problems on picture loading when running the notebook,
# plase go to menu 'Kernel' -> 'Restart&Clear Output' -> run again
# ===============================================================

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sys, os
import webbrowser
from collections import Counter

root=Tk()
root.title("KLM GUI: HSL Travel Card Reader Example")
root.geometry('990x520')

#KLM on Wikipedia button clicked
def onWikipediaClicked(event):
    webbrowser.open_new(r"en.wikipedia.org/wiki/Keystroke-level_model")

#switch among UIs and record operator sequence
def onButton3Clicked(event):
    ui0.place_forget()
    uiZoneL.place_forget()
    uiZone2.place_forget()
    uiZone1.place_forget()
    uiAddPas.place_forget()
    uiOk.place_forget()
    uiZone3.place(x=190,y=20,width=360,height=480)
    M.set(M.get()+1)
    P.set(P.get()+1)
    K.set(K.get()+1)
    R.set(R.get()+1)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.insert(END,"M P K R (select zone 3)\n\n")
    operatorSequence.see("end")

def onButtonLClicked(event):
    ui0.place_forget()
    uiZone3.place_forget()
    uiZone2.place_forget()
    uiZone1.place_forget()
    uiAddPas.place_forget()
    uiOk.place_forget()
    uiZoneL.place(x=190,y=20,width=360,height=480)
    M.set(M.get()+1)
    P.set(P.get()+1)
    K.set(K.get()+1)
    R.set(R.get()+1)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.insert(END,"M P K R (select zone L)\n\n")
    operatorSequence.see("end")

def onButton2Clicked(event):
    ui0.place_forget()
    uiZone3.place_forget()
    uiZoneL.place_forget()
    uiZone1.place_forget()
    uiAddPas.place_forget()
    uiOk.place_forget()
    uiZone2.place(x=190,y=20,width=360,height=480)
    M.set(M.get()+1)
    P.set(P.get()+1)
    K.set(K.get()+1)
    R.set(R.get()+1)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.insert(END,"M P K R (select zone 2)\n\n")
    operatorSequence.see("end")

def onButton1Clicked(event):
    ui0.place_forget()
    uiZone3.place_forget()
    uiZoneL.place_forget()
    uiZone2.place_forget()
    uiAddPas.place_forget()
    uiOk.place_forget()
    uiZone1.place(x=190,y=20,width=360,height=480)
    M.set(M.get()+1)
    P.set(P.get()+1)
    K.set(K.get()+1)
    R.set(R.get()+1)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.insert(END,"M P K R (select zone 1)\n\n")
    operatorSequence.see("end")

def onAddPasClicked(event):
    uiZone3.place_forget()
    uiZoneL.place_forget()
    uiZone2.place_forget()
    uiZone1.place_forget()
    uiAddPas.place(x=190,y=20,width=360,height=480)
    M.set(M.get()+1)
    P.set(P.get()+1)
    K.set(K.get()+1)
    R.set(R.get()+1)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.insert(END,"M P K R (add passenger)\n\n")
    operatorSequence.see("end")

def onOkClicked(event):
    uiOk.place(x=190,y=20,width=360,height=480)
    M.set(M.get()+1)
    P.set(P.get()+1)
    K.set(K.get()+1)
    R.set(R.get()+1)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.insert(END,"M P K R (click on OK)\n\n")
    operatorSequence.see("end")

def onCancelClicked(event):
    uiOk.place_forget()
    ui0.place_forget()
    uiZone3.place_forget()
    uiZoneL.place_forget()
    uiZone2.place_forget()
    uiZone1.place_forget()
    uiAddPas.place_forget()
    ui0.place(x=190,y=20,width=360,height=480)
    M.set(M.get()+1)
    P.set(P.get()+1)
    K.set(K.get()+1)
    R.set(R.get()+1)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.insert(END,"M P K R (cancel)\n\n")
    operatorSequence.see("end")

def onResetClicked(event):
    uiOk.place_forget()
    uiZone3.place_forget()
    uiZoneL.place_forget()
    uiZone2.place_forget()
    uiZone1.place_forget()
    uiAddPas.place_forget()
    ui0.place_forget()
    ui0.place(x=190,y=20,width=360,height=480)
    M.set(0)
    P.set(0)
    K.set(0)
    R.set(0)
    time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
    operatorSequence.delete('1.0',END)
    H.set(1)
    operatorSequence.insert(END,"(Reset)\n\nH (homing hand to card reader)\n\n")
    operatorSequence.see("end")

#user task and wikipedia frame
userTaskFrame=ttk.Labelframe(root,text='User Task')
userTask=Message(root,text="To buy maximum 2 value ticket(s) on HSL travel card reader, first select zone, then press <ADD PASSENGER> and <OK>.",anchor=N,justify=LEFT,width=120)
nullFrame=Frame(root)
nullLabel=Label(root,text="placeholder")
wikipediaButton=Button(root,text="KLM on Wikipedia")
userTaskFrame.place(x=20,y=20,width=150,height=200)
userTask.place(x=30,y=45,width=130,height=150)
wikipediaButton.place(x=20,y=450,width=150,height=50)
wikipediaButton.bind('<Button-1>',onWikipediaClicked)

#hsl card reader UIs
uiPic0=ImageTk.PhotoImage(Image.open("hsl_ui_0.PNG").resize((352,472)))
uiPicZone3=ImageTk.PhotoImage(Image.open("hsl_ui_1_zone3_selected.PNG").resize((352,472)))
uiPicZoneL=ImageTk.PhotoImage(Image.open("hsl_ui_1_zoneL_selected.PNG").resize((352,472)))
uiPicZone2=ImageTk.PhotoImage(Image.open("hsl_ui_1_zone2_selected.PNG").resize((352,472)))
uiPicZone1=ImageTk.PhotoImage(Image.open("hsl_ui_1_zone1_selected.PNG").resize((352,472)))
uiPicAddPas=ImageTk.PhotoImage(Image.open("hsl_ui_addPas2.PNG").resize((352,472)))
uiPicOk=ImageTk.PhotoImage(Image.open("hsl_ui_showCard.PNG").resize((352,472)))
zone3=ImageTk.PhotoImage(Image.open("zone3.PNG").resize((129,43)))
zoneL=ImageTk.PhotoImage(Image.open("zoneL.PNG").resize((129,43)))
zone2=ImageTk.PhotoImage(Image.open("zone2.PNG").resize((130,45)))
zone1=ImageTk.PhotoImage(Image.open("zone1.PNG").resize((130,40)))
okPic=ImageTk.PhotoImage(Image.open("ok.PNG").resize((90,55)))
addPasPic=ImageTk.PhotoImage(Image.open("addPas.PNG").resize((80,45)))
cancelPic=ImageTk.PhotoImage(Image.open("cancel.PNG").resize((45,40)))
ui0=Canvas(root,borderwidth=2,relief=GROOVE)
uiBackground0=ui0.create_image(180,240,image=uiPic0)
button3Ui0=ui0.create_image(102,172,image=zone3)
buttonLUi0=ui0.create_image(100,257,image=zoneL)
button2Ui0=ui0.create_image(98,342,image=zone2)
button1Ui0=ui0.create_image(99,423,image=zone1)
ui0.place(x=190,y=20,width=360,height=480)
#UI after zone 3 selected
uiZone3=Canvas(root,borderwidth=2,relief=GROOVE)
uiBackground3=uiZone3.create_image(180,240,image=uiPicZone3)
buttonLUi3=uiZone3.create_image(100,257,image=zoneL)
button2Ui3=uiZone3.create_image(98,342,image=zone2)
button1Ui3=uiZone3.create_image(99,423,image=zone1)
okUi3=uiZone3.create_image(270,400,image=okPic)
addPasUi3=uiZone3.create_image(285,260,image=addPasPic)
cancelUi3=uiZone3.create_image(314,98,image=cancelPic)
#UI after zone L selected
uiZoneL=Canvas(root,borderwidth=2,relief=GROOVE)
uiBackgroundL=uiZoneL.create_image(180,240,image=uiPicZoneL)
button3UiL=uiZoneL.create_image(102,172,image=zone3)
button2UiL=uiZoneL.create_image(98,342,image=zone2)
button1UiL=uiZoneL.create_image(99,423,image=zone1)
okUiL=uiZoneL.create_image(270,400,image=okPic)
addPasUiL=uiZoneL.create_image(285,260,image=addPasPic)
cancelUiL=uiZoneL.create_image(314,98,image=cancelPic)
#UI after zone 2 selected
uiZone2=Canvas(root,borderwidth=2,relief=GROOVE)
uiBackground2=uiZone2.create_image(180,240,image=uiPicZone2)
button3Ui2=uiZone2.create_image(102,172,image=zone3)
buttonLUi2=uiZone2.create_image(100,257,image=zoneL)
button1Ui2=uiZone2.create_image(99,423,image=zone1)
okUi2=uiZone2.create_image(270,400,image=okPic)
addPasUi2=uiZone2.create_image(285,260,image=addPasPic)
cancelUi2=uiZone2.create_image(314,98,image=cancelPic)
#UI after zone 1 selected
uiZone1=Canvas(root,borderwidth=2,relief=GROOVE)
uiBackground1=uiZone1.create_image(180,240,image=uiPicZone1)
button3Ui1=uiZone1.create_image(102,172,image=zone3)
buttonLUi1=uiZone1.create_image(100,257,image=zoneL)
button2Ui1=uiZone1.create_image(100,342,image=zone2)
okUi1=uiZone1.create_image(270,400,image=okPic)
addPasUi1=uiZone1.create_image(285,260,image=addPasPic)
cancelUi1=uiZone1.create_image(314,98,image=cancelPic)
#UI add passenger
uiAddPas=Canvas(root,borderwidth=2,relief=GROOVE)
uiBackgroundAddPas=uiAddPas.create_image(180,240,image=uiPicAddPas)
okUiAddPas=uiAddPas.create_image(264,433,image=okPic)
cancelUiAddPas=uiAddPas.create_image(312,100,image=cancelPic)
#UI show card after pressing <OK>
uiOk=Canvas(root,borderwidth=2,relief=GROOVE)
uiBackgroundOk=uiOk.create_image(180,240,image=uiPicOk)
cancelUiOk=uiOk.create_image(312,98,image=cancelPic)

ui0.tag_bind(button3Ui0,'<Button-1>',onButton3Clicked)
ui0.tag_bind(buttonLUi0,'<Button-1>',onButtonLClicked)
ui0.tag_bind(button2Ui0,'<Button-1>',onButton2Clicked)
ui0.tag_bind(button1Ui0,'<Button-1>',onButton1Clicked)
uiZone3.tag_bind(buttonLUi3,'<Button-1>',onButtonLClicked)
uiZone3.tag_bind(button2Ui3,'<Button-1>',onButton2Clicked)
uiZone3.tag_bind(button1Ui3,'<Button-1>',onButton1Clicked)
uiZone3.tag_bind(addPasUi3,'<Button-1>',onAddPasClicked)
uiZone3.tag_bind(okUi3,'<Button-1>',onOkClicked)
uiZone3.tag_bind(cancelUi3,'<Button-1>',onCancelClicked)
uiZoneL.tag_bind(button3UiL,'<Button-1>',onButton3Clicked)
uiZoneL.tag_bind(button2UiL,'<Button-1>',onButton2Clicked)
uiZoneL.tag_bind(button1UiL,'<Button-1>',onButton1Clicked)
uiZoneL.tag_bind(addPasUiL,'<Button-1>',onAddPasClicked)
uiZoneL.tag_bind(okUiL,'<Button-1>',onOkClicked)
uiZoneL.tag_bind(cancelUiL,'<Button-1>',onCancelClicked)
uiZone2.tag_bind(button3Ui2,'<Button-1>',onButton3Clicked)
uiZone2.tag_bind(buttonLUi2,'<Button-1>',onButtonLClicked)
uiZone2.tag_bind(button1Ui2,'<Button-1>',onButton1Clicked)
uiZone2.tag_bind(addPasUi2,'<Button-1>',onAddPasClicked)
uiZone2.tag_bind(okUi2,'<Button-1>',onOkClicked)
uiZone2.tag_bind(cancelUi2,'<Button-1>',onCancelClicked)
uiZone1.tag_bind(button3Ui1,'<Button-1>',onButton3Clicked)
uiZone1.tag_bind(buttonLUi1,'<Button-1>',onButtonLClicked)
uiZone1.tag_bind(button2Ui1,'<Button-1>',onButton2Clicked)
uiZone1.tag_bind(addPasUi1,'<Button-1>',onAddPasClicked)
uiZone1.tag_bind(okUi1,'<Button-1>',onOkClicked)
uiZone1.tag_bind(cancelUi1,'<Button-1>',onCancelClicked)
uiAddPas.tag_bind(okUiAddPas,'<Button-1>',onOkClicked)
uiAddPas.tag_bind(cancelUiAddPas,'<Button-1>',onCancelClicked)
uiOk.tag_bind(cancelUiOk,'<Button-1>',onCancelClicked)

#modelling UI
modelFrame=ttk.Labelframe(root,text='Modelling')
#operator sequence display
scrollbar=Scrollbar(root,width=10)
operatorSequenceTitle=Label(root,text="Operator Sequence:",anchor=W,justify=LEFT)
operatorSequence=Text(root,yscrollcommand=scrollbar.set,padx=10,pady=10)
scrollbar.config(command=operatorSequence.yview)
#operator count display
operatorCountTitle=Label(root,text="Operator Count:",anchor=W,justify=LEFT)
operatorK=Label(root,text="K =",justify=LEFT)
operatorP=Label(root,text="P =",justify=LEFT)
operatorH=Label(root,text="H =",justify=LEFT)
operatorD=Label(root,text="D =",justify=LEFT)
operatorM=Label(root,text="M =",justify=LEFT)
operatorR=Label(root,text="R =",justify=LEFT)
K=IntVar()
K.set(0)
operatorKCount=Label(root,textvariable=K,justify=LEFT)
P=IntVar()
P.set(0)
operatorPCount=Label(root,textvariable=P,justify=LEFT)
H=IntVar()
H.set(0)
operatorHCount=Label(root,textvariable=H,justify=LEFT)
D=IntVar()
D.set(0)
operatorDCount=Label(root,textvariable=D,justify=LEFT)
M=IntVar()
M.set(0)
operatorMCount=Label(root,textvariable=M,justify=LEFT)
R=IntVar()
R.set(0)
operatorRCount=Label(root,textvariable=R,justify=LEFT)
operatorRCount2=Label(root,textvariable=R,anchor=W,justify=LEFT)
#operator values display
operatorValuesTitle=Label(root,text="Operator Values (second):",anchor=W,justify=LEFT)
operatorValuesK=Label(root,text="Keystroke\t= 0.10",underline=(0),anchor=W,justify=LEFT)
operatorValuesP=Label(root,text="Pointing\t\t= 1.10",underline=(0),anchor=W,justify=LEFT)
operatorValuesH=Label(root,text="Homing\t\t= 0.40",underline=(0),anchor=W,justify=LEFT)
operatorValuesD=Label(root,text="Drawing\t\t= .9n+.16l",underline=(0),anchor=W,justify=LEFT)
operatorValuesM=Label(root,text="Mentally preparing = 1.35",underline=(0),anchor=W,justify=LEFT)
operatorValuesR=Label(root,text="Response from system = depends",underline=(0),anchor=W,justify=LEFT)

# when manually change operator sequence via text box
def onOpSeqFocused(event):
    global operatorSequenceTmp
    operatorSequenceTmp = operatorSequence.get("1.0", 'end-1c')

def updateOpSeq():
    global operatorSequenceTmp
    if (operatorSequence.get("1.0",'end-1c')!=operatorSequenceTmp):
        operatorSequenceTmp = operatorSequence.get("1.0",'end-1c')
        countOp = Counter(operatorSequenceTmp)
        K.set(countOp['K'])
        P.set(countOp['P'])
        H.set(countOp['H'])
        D.set(countOp['D'])
        M.set(countOp['M'])
        R.set(countOp['R'])
        operatorSequence.see(END)
        time.set(round(K.get()*0.10+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))

def onOpSeqManuallyChanged(event):
    operatorSequence.after(5,updateOpSeq)

operatorSequence.bind('<Button-1>', onOpSeqFocused)
operatorSequence.bind('<Key>', onOpSeqManuallyChanged)

#reset button to restart modelling
resetButton=Button(root,text="Reset",bg='#007ac9',fg="white")
resetButton.bind('<Button-1>',onResetClicked)
#homing operator: homing hand to card reader
H.set(1)
operatorSequence.insert(END,"H (homing hand to card reader)\n\n")
#total time display
totalTimeTitle=Label(root,text="Total Time (second):",anchor=W,justify=LEFT)
time=DoubleVar()
time.set(0)
totalTime=Label(root,textvariable=time,anchor=E)
time.set(round(K.get()*0.20+P.get()*1.10+H.get()*0.40+M.get()*1.35,2))
totalTimePlus=Label(root,text="+")
totalTimeR=Label(root,text="R")
#modelling UI layout
modelFrame.place(x=570,y=20,width=390,height=480)
operatorSequenceTitle.place(x=590,y=40,width=340,height=20)
operatorSequence.place(x=590,y=65,width=335,height=150)
scrollbar.place(x=925,y=65,width=10,height=150)
yPos=245
operatorCountTitle.place(x=590,y=yPos,width=120,height=20)
operatorValuesTitle.place(x=730,y=yPos,width=210,height=20)
operatorK.place(x=600,y=yPos+25,width=30,height=20)
operatorKCount.place(x=630,y=yPos+25,width=20,height=20)
operatorValuesK.place(x=740,y=yPos+25,width=210,height=20)
operatorP.place(x=600,y=yPos+45,width=30,height=20)
operatorPCount.place(x=630,y=yPos+45,width=20,height=20)
operatorValuesP.place(x=740,y=yPos+45,width=210,height=20)
operatorH.place(x=600,y=yPos+65,width=30,height=20)
operatorHCount.place(x=630,y=yPos+65,width=20,height=20)
operatorValuesH.place(x=740,y=yPos+65,width=210,height=20)
operatorD.place(x=600,y=yPos+85,width=30,height=20)
operatorDCount.place(x=630,y=yPos+85,width=20,height=20)
operatorValuesD.place(x=740,y=yPos+85,width=210,height=20)
operatorM.place(x=600,y=yPos+105,width=30,height=20)
operatorMCount.place(x=630,y=yPos+105,width=20,height=20)
operatorValuesM.place(x=740,y=yPos+105,width=210,height=20)
operatorR.place(x=600,y=yPos+125,width=30,height=20)
operatorRCount.place(x=630,y=yPos+125,width=20,height=20)
operatorValuesR.place(x=740,y=yPos+125,width=210,height=20)
resetButton.place(x=590,y=430,width=100,height=50)
totalTimeTitle.place(x=740,y=430,width=170,height=20)
totalTime.place(x=740,y=455,width=80,height=20)
totalTimePlus.place(x=820,y=455,width=30,height=20)
operatorRCount2.place(x=850,y=455,width=20,height=20)
totalTimeR.place(x=870,y=455,width=40,height=20)

root.mainloop()
