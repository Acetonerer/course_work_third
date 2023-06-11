import json
from datetime import datetime

"""Функция загрузки данных из json файла,
отделения выполненных опеаций и сортировки по дате 
последних 5 операций"""
def load_data(FILE):
    with open(FILE, "r", encoding="UTF -8") as file:
        operation = json.load(file)
        operations_exe = []
        for oper in operation:
            try:
                if oper["state"] == "EXECUTED":
                    operations_exe.append(oper)
            except LookupError:
                operation_error = "Операция не выполнена"
        opers_last = operations_exe[-5:]
        opers_sort = sorted(opers_last, key=lambda x: x["date"], reverse=True)
        return opers_sort

"""Функция, получающая на входе номер счета или карты. 
Она также определяет, что именно она получила, 
а после маскирует номер звездочками и выводит в требуемом формате"""
def form_card_account(str_):
    str_list = str_.split(' ')
    numb = str_list[-1]
    if len(str_list) == 2:
        if str_list[0] == "Счет":
            return "Счет" + " " + "**" + numb[-4:]
        else:
            return f"{str_list[0]} {numb[:4]} {numb[4:6]} ** **** {numb[-4:]}"
    else:
        return f"{str_list[0]} {str_list[1]} {numb[:4]} {numb[4:6]} ** **** {numb[-4:]}"

"""Функция, приводящая дату в заявке к требуемому формату"""
def form_date(data):
    date = datetime.fromisoformat(data)
    date_form = date.strftime("%d.%m.%Y")
    return date_form
