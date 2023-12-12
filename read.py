def extract_laptops(lst,laptops):
    '''This function extracts information on laptops from the txt file and stores it in a dictionary which inturn is stored in a list.'''
    with open("D:\Python\Available_Laptops.txt","r") as file:
        id = 1
        for line in file:
            line = line.replace('\n', ' ')
            laptops.update({id:line.split(",")})
            id +=1    
        lst.append(laptops)
        
    return(lst,laptops)

