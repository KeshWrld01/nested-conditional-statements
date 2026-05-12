computer_science = input("Did you have the course? Y/N ")

if computer_science == "Y":
    fee_balnce = int(input("ENter the fee balance: "))
    if fee_balnce == 0:
        print("The student is eligibale")
    else:
        print("The student is not eligible")
else:
    print("You cannot sit for the exam.")


print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int( input("Enter your choice: ") )

if( choice == 1 ):
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")


  choice2=int(input("Enter you choice2: "))
  if choice2==1: 
    print("you have selected scooty")
  else:
    print("you have selected scooter")


elif( choice == 2 ): 
  print( "what type of car?" )
  print("1.Sedan")
  print("2.SUV")
  choice3=int(input("enter your choice3: "))

  if choice3==1: 
    print("you have selected sedan")
  else:
    print("you have selected XUV")

else: 
  print("Wrong choice!")