#James Laroche
#CMP131 
#Week04 
#Lab01 
#Movie Theatre Tickets 
#9/11/2026 
movie=input("enter a movie name") 
ticketa=int(input("how many adult tickets were sold?")) 
ticketc=int(input("how many child tickets were sold?")) 
Gbox=(ticketa * 10) + (ticketc * 6) 
Netbox=Gbox * 0.2 
Amount=Gbox - Netbox 
print("movie name:"movie) 
print(
