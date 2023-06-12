from utils.func import load_data, form_card_account, form_date

FILE = "operations.json"


def main():
    """
    Основной код
    Выводит информацию о 5 последних
    отформатированных операциях
    """
    operations = load_data(FILE)
    for operation in operations:
        operation["date"] = form_date(operation["date"])
        try:
            operation["from"] = form_card_account(operation["from"])
        except LookupError:
            operation["from"] = "Неизвестный источник"
        operation["to"] = form_card_account(operation["to"])
        print(operation["date"] + " " + operation["description"])
        print(operation["from"] + " -> " + operation["to"])
        print(operation["operationAmount"]["amount"] + " "
              + operation["operationAmount"]["currency"]["name"], end="\n\n")


if __name__ == "__main__":
    main()
