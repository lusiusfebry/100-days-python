print("Welcome to the Tip Calculator")
totalBill = int(input ("What was the total bill ? $"))
totalTip = float(input("How much tip would you like to give? 10, 12 or 15? "))
totalPeopleToSplit = int(input("How many people to split the bill? "))

tip = ((totalTip / 100) * totalBill) + totalBill
totalSplitToEachPerson = round(tip / totalPeopleToSplit,2)

print (f"Each person should pay : ${totalSplitToEachPerson}")
