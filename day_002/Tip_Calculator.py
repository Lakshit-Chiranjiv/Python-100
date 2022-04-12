# Tip Calculator

print("Welcome to the tip calculator!! \n")

billAmount = input("What is the amount of your bill? : $")

tipPercent = input("What percentage of tip you want to pay? : ")

numOfPeople = input("How many people to split the bill? : ")

totalBill = int(billAmount) + (int(tipPercent)/100)*int(billAmount)

billPerPerson = totalBill/int(numOfPeople);

roundedBillPerPerson = round(billPerPerson,2);
print(f"Per person has to pay : ${roundedBillPerPerson}")