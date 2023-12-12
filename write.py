def buy_edit_file(laptops, S, Q):
    '''This function edits the quantity of the products in the txt file after user has finished buying.'''
    added = int(laptops[S][3]) + int(Q)
    laptops[S][3] = str(added)
    with open("Available_Laptops.txt", "w") as f:
        for i in laptops.values():
            f.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")


def sell_edit_file(laptops, S, Q):
    '''This function edits the quantity of the products in the txt file after user has finished selling.'''
    subtracted = int(laptops[S][3]) - int(Q)
    laptops[S][3] = str(subtracted)
    with open("Available_Laptops.txt", "w") as f:
        for i in laptops.values():
            f.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")

