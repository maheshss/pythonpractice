
import promotion
import starbuzz

items=["Hot Coffee","Cold Coffee","Latte"]
prices=[1.2,2.2,1.5]
running=1

def save_transaction(price,credit_card,description):
        file = open("transactions.txt","a")
        file.write("%s%07d%s\n" %(credit_card,price*100,description))
	
while running:
	option = 1
	for choice in items:
		print(str(option)+". "+choice)
		option=option+1
	print(str(option)+". Quit ")
	choice = int(input("Choose your option:" ))
	if choice == option:
		running = 0
	else:
		credit_card = input("Credit card number: ")
		price = promotion.discount(prices[choice-1])
		sbpc = input("Starbuzz Card: ")
		if sbpc=="Y":
			price = starbuzz.discount(price)
		save_transaction(price,credit_card,items[choice-1])

