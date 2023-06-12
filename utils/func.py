import json
from datetime import datetime


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
        opers_sort = sorted(operations_exe, key=lambda x: x["date"], reverse=True)
        opers_last = opers_sort[:5]
        return opers_last


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


def form_date(data):
    date = datetime.fromisoformat(data)
    date_form = date.strftime("%d.%m.%Y")
    return date_form
