list1 = [1,2,3,4,5]
list2 = [2,3,5]
for x in list1 :
    if x %2 == 1:
        list1.remove (x)
print (list1)

list3 = list2 - list1
print (list3)