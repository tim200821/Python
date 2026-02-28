import array as arr

numbers = arr.array( 'i',[1,2,3,4,5])

for number in numbers:
    print(number)


print("________________")
numbers.append(6)
# append добавляет одно значение в конец массива


for number in numbers:
    print(number)

print("________________")

numbers.extend([7,8,10])

for number in numbers:
    print(number)

print("________________")

numbers.insert(8 , 9)
#insert добавляет в любое место нужное значение
for number in numbers:
    print(number)

print("________________")

numbers.remove(5)

for number in numbers:
    print(number)

print("________________")

target1 = numbers.pop(4)
target2 = numbers.pop(4)
# находит цель по индексу и удоляет ее из массива
print(numbers)
print(target1)
print(target2)

