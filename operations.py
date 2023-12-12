import datetime
from write import buy_edit_file
from write import sell_edit_file
lst = []
laptops = {}


def display_laptops_table(laptops):
    '''The function displays the content of the txt file in the console in table format.'''
    print("\n")
    print("\n")
    
    
    print("                                         ----------------------------------------------------------------------------------------------------------------------------------")
    print("                                                            {:<8} {:<18} {:<13} {:<13} {:<13} {:<13} {:<13}".format('Sn', 'Name', 'Brand', 'Price', 'Quantity', 'Processor', 'Graphics Card' ))
    print("                                         ----------------------------------------------------------------------------------------------------------------------------------")
    for k, v in laptops.items():
        name, brand, price, quantity, processor, graphics = v
        price = "$"+price
        print("                                                            {:<8} {:<18} {:<13} {:<13} {:<13} {:<13} {:<13}".format(k, name, brand, price, quantity, processor, graphics ))
        print("                                         ----------------------------------------------------------------------------------------------------------------------------------")
    print("                                         ----------------------------------------------------------------------------------------------------------------------------------")



user_bought_products = [] #Declaring an empty list
def user_input_info(user_bought_products, laptops,S,Q):
    '''This function stores user purchases in a separate list and deals regarding product shipping. '''
    product_name = laptops[S][0] 
    user_required_quantity = Q
    user_selected_product_actual_price = ("$"+laptops[S][2])
    amount_to_be_paid = "$"+str(user_required_quantity*int(user_selected_product_actual_price.replace('$','')))
    

    
    shipping = input("Dear user, do you want your product to be shipped?(Y/N)")
    shipping = shipping.upper()
    if shipping =="Y":
        address = input("Dear user, do you live within the valley?(Y/N)")
        address = address.upper()
        if address =="Y":
            shipping_cost = "$"+"50"
            total_amount_including_shippingcost = "$"+str(int(amount_to_be_paid.replace('$',''))+int(shipping_cost.replace('$','')))
            user_bought_products.append([ product_name,  user_required_quantity, user_selected_product_actual_price, amount_to_be_paid, shipping_cost, total_amount_including_shippingcost])
            return(user_bought_products)
        elif address =="N":
            shipping_cost = "$"+"150"
            total_amount_including_shippingcost = "$"+str(int(amount_to_be_paid.replace('$',''))+int(shipping_cost.replace('$','')))
            user_bought_products.append([ product_name,  user_required_quantity, user_selected_product_actual_price, amount_to_be_paid, shipping_cost, total_amount_including_shippingcost])
            return(user_bought_products)

def bought_receipt(user_bought_products, Name, Contact):
    '''The function gives user's purchase receipt in a unique text file each time the function is invoked.'''
    filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    with open("{}.txt".format(filename), "w") as f:
        f.write("\n")
        f.write("\n")
        f.write("Date and Time: {}".format(datetime.datetime.now()))
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t{}".format("Binayak Laptops"))
        f.write("\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{}".format("Kathmandu, New Road, 9856088970"))
        f.write("\n")
        f.write("Name: {}".format(Name))
        f.write("\n")
        f.write("Contact No.: {}".format(Contact))
        f.write("\n")
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("{:<8}\t{:<18}\t{:<13}\t{:<13}\t{:<13}\t{:<13}".format('Laptop Name', 'Quantity Purchased', 'Product Price', 'Amount to be paid', 'Shipping cost', 'Total amount including shipping cost\n'))
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\n")
        total_cost = 0
        for laptop in user_bought_products:
            f.write("{:<8}\t  {:<18}\t{:<13}\t  {:<13}\t\t   {:<13}\t\t{:<13}\n".format(laptop[0],laptop[1],laptop[2],laptop[3],laptop[4],laptop[5]))
            total_cost = total_cost+int((laptop[5].replace('$','')))
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+"Total Cost: {}".format("$"+str(total_cost)))


def sold_receipt(user_bought_products, Name, Contact):
    '''The function gives user's selling receipt in a unique text file each time the function is invoked.'''
    filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    with open("{}.txt".format(filename), "w") as f:
        f.write("\n")
        f.write("\n")
        f.write("Date and Time: {}".format(datetime.datetime.now()))
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t{}".format("Binayak Laptops"))
        f.write("\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{}".format("Kathmandu, New Road, 9856088970"))
        f.write("\n")
        f.write("Name: {}".format(Name))
        f.write("\n")
        f.write("Contact No.: {}".format(Contact))
        f.write("\n")
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("{:<8}\t{:<18}\t{:<13}\t{:<13}\t{:<13}\t{:<13}".format('Laptop Name', 'Quantity Purchased', 'Product Price', 'Amount to be paid', 'Shipping cost', 'Total amount including shipping cost\n'))
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\n")
        total_cost = 0
        for laptop in user_bought_products:
            f.write("{:<8}\t  {:<18}\t{:<13}\t  {:<13}\t\t   {:<13}\t\t{:<13}\n".format(laptop[0],laptop[1],laptop[2],laptop[3],laptop[4],laptop[5]))
            total_cost = total_cost+int((laptop[5].replace('$','')))
            total_cost = 13/100*(total_cost)+total_cost
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+"VAT : 13%\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+"Total Cost: {}".format("$"+str(total_cost)))




def buy_laptops(laptops):
    ''' This function asks user if he/she wants to keep on buying.'''
    S = int(input("Enter the serial code of the product you wish to buy:"))
    while  S<0 or S>len(laptops):
        print("Sorry we don't have any product with such serial code. Please enter a valid code")
        S = int(input("Enter the serial number of the product you wish to buy:"))
    Q = int(input("How many of such laptop do you wish to buy?:"))
    user_input_info(user_bought_products, laptops,S,Q)
    buy_edit_file(laptops,S,Q)

def sell_laptops(laptops):
    '''This function asks the user if he/she wants to keep on selling.'''
    S = int(input("Enter the serial code of the product you wish to sell:"))
    while  S<0 or S>len(laptops):
        print("Sorry we don't have any product with such serial code. Please enter a valid code")
        S = int(input("Enter the serial number of the product you wish to sell:"))
    Q = int(input("How many of such laptop do you wish to sell?:"))
    while Q>int(laptops[S][3]):
        print("Sorry, We do not have the mentioned quantity available currently. Please take reference of the provided table.")
        Q = int(input("How many of such laptop do you wish to sell?:"))
    user_input_info(user_bought_products, laptops,S,Q)
    sell_edit_file(laptops,S,Q)


def display_bought_receipt(user_bought_products, Name, Contact):
    '''This function displays user purchase receipt on the console.'''
    print("\n")
    print("\n")
    print("Date and Time: {}".format(datetime.datetime.now()))
    print("\t\t\t\t\t\t\t\t\t\t\t\t{}".format("Binayak Laptops"))
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t{}".format("Kathmandu, New Road, 9856088970"))
    print("\n")
    print("Name: {}".format(Name))
    print("\n")
    print("Contact No.: {}".format(Contact))
    print("\n")
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                      {:<8}\t{:<18}\t{:<13}\t{:<13}\t{:<13}\t{:<13}".format('Laptop Name', 'Quantity Purchased', 'Product Price', 'Amount to be paid', 'Shipping cost', 'Total amount including shipping cost'))
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    total_cost = 0
    for laptop in user_bought_products:
        print("                  \t{:<8}\t  {:<18}\t{:<13}\t  {:<13}\t\t   {:<13}\t\t{:<13}\n".format(laptop[0],laptop[1],laptop[2],laptop[3],laptop[4],laptop[5]))
        total_cost = total_cost+int((laptop[5].replace('$','')))
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+"Total Cost: {}".format("$"+str(total_cost)))





def display_sold_receipt(user_bought_products, Name, Contact):
    '''This function displays user sold receipt on the console.'''
    print("\n")
    print("\n")
    print("Date and Time: {}".format(datetime.datetime.now()))
    print("\t\t\t\t\t\t\t\t\t\t\t\t{}".format("Binayak Laptops"))
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t{}".format("Kathmandu, New Road, 9856088970"))
    print("\n")
    print("Name: {}".format(Name))
    print("\n")
    print("Contact No.: {}".format(Contact))
    print("\n")
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                      {:<8}\t{:<18}\t{:<13}\t{:<13}\t{:<13}\t{:<13}".format('Laptop Name', 'Quantity Purchased', 'Product Price', 'Amount to be paid', 'Shipping cost', 'Total amount including shipping cost'))
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    total_cost = 0
    for laptop in user_bought_products:
        print("                  \t{:<8}\t  {:<18}\t{:<13}\t  {:<13}\t\t   {:<13}\t\t{:<13}\n".format(laptop[0],laptop[1],laptop[2],laptop[3],laptop[4],laptop[5]))
        total_cost = total_cost+int((laptop[5].replace('$','')))
        total_cost = 13/100*(total_cost)+total_cost
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                  ----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+"VAT: 13%")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+"Total Cost: {}".format("$"+str(total_cost)))

def buying_process(user_bought_products, Name, Contact):
    '''This function oversees all the factors regarding buying.'''
    buy_laptops(laptops)
    q = input("Do you wish to keep on buying?(Y/N)")

    while q.upper()=="Y":
        buy_laptops(laptops)
        q = input("Do you wish to keep on buying?(Y/N)")
        if q.upper()=="N":
            break 
    display_bought_receipt(user_bought_products, Name, Contact)
    bought_receipt(user_bought_products, Name, Contact)    
   
def selling_process(user_bought_products, Name, Contact):
    '''This function oversees all the process regarding selling functions.'''
    sell_laptops(laptops)
    q = input("Do you have more to sell?(Y/N)")

    while q.upper()=="Y":
        sell_laptops(laptops)
        q = input("Do you have more to sell?(Y/N)")
        if q.upper()=="N":
            break 
    display_sold_receipt(user_bought_products, Name, Contact)
    sold_receipt(user_bought_products, Name, Contact)
