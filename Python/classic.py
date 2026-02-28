import array
tuple1 = (1, 2, 3)
#mutable = ([1, 2],[3, 4])
a = [1, 2]
b = [3, 4]
mutable = (a, b)
a[1] = 5
#это кортедж неизменяеммый список
print(mutable)
print(tuple1)
print("______________________")
#set - это набор, каждое значение уникально
a = set()
b = {}
a.add(1)
a.add(2)
print(a)
a = {4, 3, 2, 1}
set1 = {'А', 'Б', 'С' ,'Д' }
#set1.remove('А')
list1 = [10, 20, 30, 40]
list1.append(10)
print(list1)
arr = array.array('i', [1,2,3,4,5])
print(arr)
list3 = list(arr)
print(list3)
set2 =set(arr)
print(set2)
set1 = set(list1)
tuple1 = tuple(set1)
print(tuple1)
print(set1)
print(a)