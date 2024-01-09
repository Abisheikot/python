salary=int(input("enter your salary: "))
age=int(input("enter your age: "))
if(salary>=20000 and age<=25):
    loan_amount=int(input("enter the loan amount: "))
    if(loan_amount>50000):
        print("maximu loan amount is:50000")
    print("you are eligible for loan")

else:
    print("you are not eligible for loan")
