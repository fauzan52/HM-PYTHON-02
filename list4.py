list1 = [1,2,3,4,5]
x = input ("Masukkan angka = ")
y = int (x)
if y not in list1 :
    list1.append(y)
else :
    print ("Angka sudah ada")
print (list1)