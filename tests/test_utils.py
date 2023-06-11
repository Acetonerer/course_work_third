from utils.func import load_data, form_card_account, form_date

FILE = "info.json"


def test_form_date():
    assert form_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert form_date("2018-03-23T10:45:06.972075") == "23.03.2018"
    assert form_date("2019-03-23") == "23.03.2019"


def test_form_card_account():
    assert form_card_account("Счет 10848359769870775355") == "Счет **5355"
    assert form_card_account("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37 ** **** 3588"
    assert form_card_account("MasterCard 3152479541115065") == "MasterCard 3152 47 ** **** 5065"
    assert form_card_account("Maestro 3806652527413662") == "Maestro 3806 65 ** **** 3662"


