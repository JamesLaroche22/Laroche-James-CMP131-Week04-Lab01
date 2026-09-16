#James Laroche
#CMP131 
#Week04 
#Lab01 
#Interest Earned 
#9/16/2026  
principal=float(input("Enter principal amount deposited"))
rate=float(input("Enter interest rate"))
time=int(input("Enter times compunded")) 
decimal_rate=(rate/100)
amount=principal *(1 + decimal_rate/time)**time
intrest=amount-principal 
savings=intrest+principal 
print("Interest Rate:", f"%{decimal_rate}") 
print("Times Compounded:", time) 
print("Principal:", f"${principal}") 
print("Intrest:" , f"${intrest}") 
print("Amount in savings:" , f"${savings}") 