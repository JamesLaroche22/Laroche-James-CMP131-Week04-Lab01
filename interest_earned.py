#James Laroche
#CMP131 
#Week04 
#Lab01 
#Interest Earned 
#9/16/2026  
principal=float(input("Enter principal amount deposited: "))
rate=float(input("Enter interest rate: "))
time=int(input("Enter times compunded: ")) 
decimal_rate=(rate/100)
amount=principal *(1 + decimal_rate/time)**time
interest=amount-principal 
savings=interest+principal 
print("Interest Rate:",rate, "%") 
print("Times Compounded:", time) 
print("Principal:", f"${principal:,.2f}") 
print("Interest:" , f"${interest:,.2f}") 
print("Amount in savings:" , f"${savings:,.2f}") 