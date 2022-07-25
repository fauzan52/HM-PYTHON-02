# Menggabungkan teks

# text = "saya lapar sekali pengen makan banyak"
# print (text.replace(" ", ""))
# text1 = text.split()
# print (text1)
# text1.insert(5, 'nasi')

# text2 = text.split()
# print (''. join(text2))

# del text1[0]
# print (text1)

text1 = "saya lapar sekali pengen makan banyak"
text2 = text1.split()
print (text2)
text3 = ""

for x in text2 :
    text3 += x
print (text3)