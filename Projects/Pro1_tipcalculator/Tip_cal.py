print("welcome")
bill = float(input("what is your totall bill?"))
Tip = input("wann give some tip Yes or No")
if Tip == "No":
    print("thanks for your order at XYZ")
if Tip == "yes":
    totaltip =float(input("what % would like to tip 10%,15%,20%"))
    tipamount = totaltip
Bill_with_tip = tipamount/100 *bill + bill
print(Bill_with_tip)