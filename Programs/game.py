from tkinter import *
from random import randint
secret=randint(1,10)

#print("Welcome!")
#guess=0
#while guess!=secret:
#	g=input("Enter your guess value:")
#	guess=int(g)
#	if guess!=secret:
#		if guess>secret:
#			print("Too High")
#		else:
#			print("Too Low")
#	else:
#		print("You Win")
#print("Game Over!")

app=Tk()
app.title("Game")
Label(app,text="Enter Your Guess").pack()
guess=Entry(app)
guess.pack()

ans=IntVar()
ans.set(0)
ans.set(guess)
op=StringVar()
op.set("Click Submit")


def fun():
        if int (guess.get())!=secret:
                if int(guess.get()) > secret:
                        op.set("Too High!")
                else:
                        op.set("Too Low!")
        else :
                op.set("Correct!")

Button(app,text="Submit",command=fun).pack()
Label(app,textvariable=op).pack()

app.mainloop()
