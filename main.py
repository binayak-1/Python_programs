import sys
from operations import *
from read import *
from write import *

def start_program():
    '''This function is executed at the start of the program and it displays the content table and store details.'''
    print("")
    print("")
    print("")
    print("")
    print("")
    print("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"Binayak Electronics")
    print("\n")
    print("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"Kathmandu,Pepsicola|9800108001")

    extract_laptops(lst,laptops)
    display_laptops_table(laptops)

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")


    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Enter 1 to buy.")
    print("Enter 2 to sell.")
    print("Enter 3 to exit.")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
start_program() #calling or invoking the function.

#Using try except block to handle exceptions while asking user for input.
try:
    A = int(input("Enter your option:")) 
    while (A)<0 or (A)>3:
        print("Error!, the given option does not exist. Please enter a valid number.")
        A = int(input("Enter your option:"))
except:
    correct = False
    while correct == False:
        print("Something went wrong when accessing the value of A. Please enter a valid value.")
        A = (input("Enter your option:"))
        if A=="1" or A=="2" or A=="3":
            correct = True
        else:
            correct = False
A = int(A)
if A ==3:
    sys.exit("Thanks for visiting our shop!") #using the sys command to end the program early.

Name = input("Enter your full name: ")
Contact = input("Enter your contact number/info: ")
#if else block to be executed according to user input.
if A==1:
    buying_process(user_bought_products, Name, Contact)
   
elif A == 2:
   selling_process(user_bought_products, Name, Contact)
