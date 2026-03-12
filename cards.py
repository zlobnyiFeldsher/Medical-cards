patients = []
def add_patient():
    name = input("Введите имя:
    age = input("Введите возраст: ") 
    diagnosis = input("Введите диагноз: ")
    patient = {"name": name, "age": age, "diagnosis": diagnosis}
    patients.append(patient)
    print("Карта добавлена")

def personal_data_edit():
    name = input("Введите имя для редактирования: ")
    for patient in patients:
        if patient["name"] == name:
            patient["name"] = input("Введите новое имя: ")
            patient["age"] = input("Введите новый возраст: ")
            patient["diagnosis"] = input("Введите новый диагноз: ")
            print("Редактирование завершено" 
    return

def find patient():
    name = input("Введите имя для поиска: ")
    for patient in patients:
        if patient["name"] == name:
            print("Пациент найден")
        else:
            print("Пациент не найден")
    return
    
def delete_card():
    name = input("Введите имя: ")
    for patient in patients:
        if patient["name"] == name: 
            patients.remove(patient)
            print("Карта удалена")
        else:
            print("Пациент не найден")
    return

def patients_list():
    for patient in patients:
        print(patient)

while True:
    print("1 - Добавить пациента") 
    print("2 - Изменить данные") 
    print("3 - Найти пациента") 
    print("4 - Удалить карту") 
    print("5 - Показать все карты") 
    print("0 - Выйти из программы")
    
choice = input("Выберите действие: ")
if choice == "1": 
    add_patient()
elif choice == "2":
    personal_data_edit()
elif choice == "3": 
    find_patient()
elif choice == "4":
    delete_card()
elif choice == "5":
    patients_list()
elif choice == "0":
    break
