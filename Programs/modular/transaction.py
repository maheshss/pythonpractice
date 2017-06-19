#This file contains transaction module that will save all POS transactions for coffee

def save_transaction(price,credit_card,description):
	file =open("transactions.txt","a")
	file.write("%16%07%16\n" %(credit_card,price*100,description)
	

