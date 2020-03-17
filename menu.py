# learning more

# number=input("enter number:")
# print(type(number))
# new_number = int(number)
#
# print(new_number)
# print(type(new_number))


# ussd
balance=300
print("1.20mb")
print("2.30mb")
print("3.40mb")
choice=int(input("Enter Selection: "))
print(type(choice))

if choice==1:
         # and balance >=20:
    if balance >= 20:
         balance=balance-20
         print("you have purchased 20mb")
         print("your balance is",balance)

    else:
        print("inssuficient balance")

    elif choice==2:
         if balance >= 20:
      balance=balance-30
        print("you have purchased 30mb")
        print("your balance is",balance)

     else:
        print("inssuficient  balance")

     elif choice==3 and balance >=40:
     if balance >= 20:
      balance=balance-40
      print("you have purchased 40mb")
      print("your balance is",balance)

 else:
     print("inssuficient  balance")



# recap
name={"Eunice"}
age={"19"}
# to make changes in a list you may
list.append