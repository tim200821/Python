import json;

user_data = {
    "name":input("Введите имя : "),
    "age":int(input("Введите ваш возраст : ")),
    "email":input("Введите ваш Электронная почта : "),
    "adres":input("Введите ваш адрес : ")
}

print(f"Имя : {user_data['name']}")
print(f"Возраст : {user_data['age']}")
print(f"Email : {user_data['email']}")
print(f"Адрес : {user_data['adres']}")