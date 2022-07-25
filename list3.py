text1 = input ("Masukkan bilangan : ")
text2 = int (text1)
list1 = [1,2,3,4,5]

for i in list1 :
    if text2 == i :
        print ("Angka yang anda masukkan sudah ada")
        break
    else :    
        list1.append(text2)
        break
print (list1)