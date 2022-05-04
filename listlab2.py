# listlab
list1 = ['banana','orange','grape']
list2 = ['pear', 'fig', 'apple']

def displist():
    print('List 1 contains: ',list1)
    print('List 2 contains: ',list2)

def compareList(l1,l2):
   l1.sort()
   l2.sort()
   if(l1==l2):
        print('Lists Equal')
        return
   else:
        print('Lists Not Equal')
        return

print(""" You have two lists.  You can 
          1. add an item
          2. delete an item.  
          3. Reverse a list 
          4. Display both lists
          5. Compare lists
          6. Exit
        """)
displist()
answer = ''
while answer != '6':
    answer = input("What would you like to do? 6 to exit: ")
    if answer not in '12345':
        break
    if int(answer) == 1:
        whichlist = input("Which list do you want to add? (1 or 2): ")
        whatitem = input("What do you want to add to this list?: ")
        if int(whichlist) == 1:
            list1.append(whatitem)
            print('New list: ',list1)
        else:
            list2.append(whatitem)
            print('New list: ',list2)
    elif int(answer) == 2:
        whichlist = input("Which list do you want to delete from?(1 or 2): ")
        whatitem = input("How do you want to delete from this list (value or index)?")
        if whatitem == 'value':
            value = input("What value do you want to delte?: ")
            if int(whichlist) == 1:
                list1.remove(value)
                print('New list: ',whichlist)
            else:
                list2.remove(value)
                print('New list: ',whichlist)               
        else:
            indx = input("What index do you want to delte?: ")
            if int(whichlist) == 1:
                del list1[indx]
                print('New list: ',list1)
            else:
                del list2[indx]
                print('New list: ',list2)             
    elif int(answer) == 3:
        rlst = input("Which list do you want to reverse? (list 1 or 2): ")
        if int(rlst) == 1:
            list1.reverse()
            print('New reverse list: ',list1)
        else:
            list2.reverse()
            print('New reverse list: ',list2)            
        
    elif int(answer) == 4:
        displist()

    elif int(answer) == 5:
        compareList(list1, list2)