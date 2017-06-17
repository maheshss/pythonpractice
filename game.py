from random import randint
secret=randint(1,10)

print("Welcome!")
guess=0
while guess!=secret:
	g=input("Enter your guess value:")
	guess=int(g)
	if guess!=secret:
		if guess>secret:
			print("Too High")
		else:
			print("Too Low")
	else:
		print("You Win")
print("Game Over!")
