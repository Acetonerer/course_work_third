from utils.func import load_data, form_card_account, form_date
import unittest

FILE = "oper_test.json"


class TestAll(unittest.TestCase):
    def test_form_date(self):
        """
        Тесты на работу функции форматирования даты
        """
        self.assertEqual(form_date("2019-08-26T10:50:58.294041"), "26.08.2019")
        self.assertEqual(form_date("2018-03-23T10:45:06.972075"), "23.03.2018")
        self.assertEqual(form_date("2019-03-23"), "23.03.2019")

    def test_form_card_account(self):
        """
        Тесты на работу функции форматирования номера карты или счета
        """
        self.assertEqual(form_card_account("Счет 10848359769870775355"), "Счет **5355")
        self.assertEqual(form_card_account("Visa Platinum 1246377376343588"), "Visa Platinum 1246 37 ** **** 3588")
        self.assertEqual(form_card_account("MasterCard 3152479541115065"), "MasterCard 3152 47 ** **** 5065")
        self.assertEqual(form_card_account("Maestro 3806652527413662"), "Maestro 3806 65 ** **** 3662")


class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        """
        Тест на работу функции работы с данными
        """
        file = [
            {
                "id": 104807525,
                "state": "EXECUTED",
                "date": "2019-06-01T06:46:16.803326"
            },
            {
                "id": 580054042,
                "state": "EXECUTED",
                "date": "2018-06-20T03:59:34.851630"
            },
            {
                "id": 619287771,
                "state": "EXECUTED",
                "date": "2019-08-19T16:30:41.967497"
            },
            {
                "id": 179194306,
                "state": "EXECUTED",
                "date": "2019-05-19T12:51:49.023880"
            },
            {
                "id": 484201274,
                "state": "EXECUTED",
                "date": "2019-04-11T23:10:21.514616"
            }
        ]
        self.assertCountEqual(load_data(FILE), file)
