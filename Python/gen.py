#
#source = [1, "2", {"count":2, "name": "tiger"}, False]
#target = [str(i) for i in source]
##преврашщает бьект в строку (только эллементарные обьекты)
##reverse = [float(i) for i in target]
##нельзя преобразовать обратно 
#
##print(reversed)
#reverse = []
#for i in source :
#    try:
#        a = float(i)
#    except:
#        a = i 
#    finally:
#        reverse.append(a)
##переводит все возмоные числа в float
#for i in target :
#    try:
#        a = float(i)
#    except:
#        a = i 
#    finally:
#        reverse.append(a)
#
#
#print(source)
#print(target)
#print(reverse)




#for i in range(50):
#
#    a = randint(-100, 100)
#    rndlist.append(a)
from random import *
rndlist = [
    randint(-100, 100) 
    for i in range(49)
    ]
tarlist =[
    i if i > 0 
    else 0 
    for i in rndlist
    ] 
#если i > 0 то пичатоет иначе i = 0

txt = "dasfasfaz"
list1 = list(txt)
text2 = "я броб"
list2 = text2.split('0')
print(list2)
#вписывает текст стринг в колекцию побуквенно
print(list1)

print(rndlist)
print("\n")
print(tarlist)
