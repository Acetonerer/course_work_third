from utils.func import load_data, form_card_account, form_date
import unittest
FILE = "oper_test.json"


class TestAll(unittest.TestCase):
    def test_form_date(self):
        self.assertEqual(form_date("2019-08-26T10:50:58.294041"), "26.08.2019")
        self.assertEqual(form_date("2018-03-23T10:45:06.972075"), "23.03.2018")
        self.assertEqual(form_date("2019-03-23"), "23.03.2019")

    def test_form_card_account(self):
        self.assertEqual(form_card_account("Счет 10848359769870775355"), "Счет **5355")
        self.assertEqual(form_card_account("Visa Platinum 1246377376343588"), "Visa Platinum 1246 37 ** **** 3588")
        self.assertEqual(form_card_account("MasterCard 3152479541115065"), "MasterCard 3152 47 ** **** 5065")
        self.assertEqual(form_card_account("Maestro 3806652527413662"), "Maestro 3806 65 ** **** 3662")


class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        file = [
                {
                    "id": 736942989,
                    "state": "EXECUTED",
                    "date": "2019-09-06T00:48:01.081967"
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
                    "id": 921286598,
                    "state": "EXECUTED",
                    "date": "2018-03-09T23:57:37.537412"
                }
        ]
        self.assertCountEqual(load_data(FILE), file)
