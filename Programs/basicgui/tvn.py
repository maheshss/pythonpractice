from tkinter import *
import pygame.mixer

sounds=pygame.mixer
sounds.init()

correct_s=sounds.Sound("alarm.wav")
wrong_s=sounds.Sound("bee.wav")



def play_correct():
	numcorrect.set((numcorrect.get()+1))
	correct_s.play()
def play_wrong():
	numwrong.set((numwrong.get()+1))
	wrong_s.play()

app=Tk()
app.title("TVN")


numcorrect=IntVar()
numcorrect.set(0)
numwrong=IntVar()
numwrong.set(0)


b1=Button(app,text="Correct!",width=10,comman=play_correct)
b1.pack(side='left',padx=10,pady=10)

b2=Button(app,text="Wrong!",width=10,comman=play_wrong)
b2.pack(side='right',padx=10,pady=10)

lab=Label(app,text='Ready, click!',height=3)
lab.pack()

lab1=Label(app,textvariable=numcorrect)
lab1.pack(side='left')

lab2=Label(app,textvariable=numwrong)
lab2.pack(side='right')

app.mainloop()


