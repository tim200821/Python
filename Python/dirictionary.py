#Словарь (dictionary) в языке Python хранит коллекцию элементов, где каждый элемент имеет уникальный ключ и ассоциированое с ним некоторое значение.
# dictionary = { ключ1:значение1, ключ2:значение2, ....}
users = {1: "Tom", 2: "Bob", 3: "Bill"}
#В словаре users в качестве ключей используются числа, а в качестве значений - строки. То есть элемент с ключом 1 имеет значение "Tom", элемент с ключом 2 - значение "Bob" и т.д

#другой пример
emails = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}
#Но необязательно ключи и строки должны быть однотипными. Они могу представлять разные типы:


objects = {1: "Tom", "2": True, 3: 100.6}
#Мы можем также вообще определить пустой словарь без элементов:
objects = {}
#или так:
objects = dict()

users_list = [
    ["+11112345", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
print(users_dict) 
users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)
print(users_dict["+111123455"])

key = "+958758767"
if key in users_dict:
    user = users_dict[key]
    print(user)
else:
    print("Элемент не найден")

user2 = users_dict.get("+384767557", "Unknown phone number")
print(user2)

del users_dict["+111123455"]
print(users_dict)

user2 = users_dict.pop("+384767557", "Unknown phone number")
print(user2)
print(users_dict)

users_dict.clear()
print(users_dict)

users_dict["+111123455"] = "sam"
users_dict["+111123456"] = "kik"
users_dict["+111123457"] = "tom"
users_dict["+111123458"] = "lola"

lijk = users_dict.copy()
print(lijk)

fulr = {
    "+123": "kot",
    "+345": "kit"
}
print(fulr)

fulr.update(lijk)
print(fulr)

user3 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in user3:
    print(f"Phone: {key}  User: {user3[key]} ")
for key, value in user3.items():
    print(f"Phone: {key}  User: {value} ")
for key in user3.keys():
    print(key)
for value in user3.values():
    print(value)

users5 = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

print(users5)
old_email = users5["Tom"]["email"]
users5["Tom"]["email"] = "supertom@gmail.com"
print(users5["Tom"])     # { phone": "+971478745", "email": "supertom@gmail.com }

key = "email"
if key in users5["Tom"]:
    print(users5["Tom"]["email"])
else:
    print("skype is not found")
#проверка наличие значения

tom_skype = users5["Tom"].get("email", "Undefined")
print(tom_skype)    # Undefined
#проверка наличия значения только через get() более опциональная