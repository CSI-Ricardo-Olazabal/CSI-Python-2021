print("Welcome to David Bisbal Concert.")
clbs = 95
nivp = 85
arnp = 95
print("The price of each seating is as follows; Arena y Nivel Principal: $"+str(arnp)+"; Nivel Principal: $"+str(nivp)+"; Club Seats: $"+str(clbs))
nc = int(input("How many Club Seats? ="))
nn = int(input("How many Nivel Principal? ="))
an = int(input("How many Arena y Nivel Principal? ="))
total = (nc*clbs)+(nn*nivp)+(an*arnp)
def TicketCost(club, nivelprin, arenp):
    print("The cost of total Club Seats: $"+str(club*clbs))
    print("The cost of total Nivel Principal: $"+str(nivelprin*nivp))
    print("The cost of total Arena y Nivel Principal: $"+str(arenp*arnp))
    print("Total Cost: $"+str(total))
TicketCost(nc, nn, an)