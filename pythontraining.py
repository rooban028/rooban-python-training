order_amount=int(input("Enter Amount:"))
cust_type=input("Enter Customer type:").lower()
deli_dist=int(input("Enter Distance:"))
pay_method=input("Enter payment Method:").lower()

dis=0
if order_amount>=1000:
    dis=order_amount-(order_amount*0.1)
elif 500<=order_amount<1000:
    dis=order_amount-(order_amount*0.05)

if order_amount>=500 and cust_type=="prime":
    dis=dis-(dis*0.05)

if deli_dist<=5:
    dis+=40
else:
    dis+=70

if pay_method=="cash on delivery" and order_amount<=500:
    dis+=25

print("Price=",dis)