from utils import utils
import pytest


@pytest.fixture
def link_400():
    return "https://raw.githubusercontent.com/typicode/demo/master/"


def test_load_operations_error400(link_400):
    with pytest.raises(NameError) as e_info:
        utils.load_operations(link_400)


@pytest.fixture
def link_200():
    return "https://raw.githubusercontent.com/typicode/demo/master/db.json"


def test_load_operations_200(link_200):
    assert type(utils.load_operations(link_200)) == type(dict())


@pytest.fixture
def link_error():
    return "https://raw.githubuser.ru/"


def test_load_operations_error(link_error):
    with pytest.raises(Exception) as e_info:
        utils.load_operations(link_error)


def test_data_masking():
    assert utils.data_masking(None) is None
    assert utils.data_masking("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'
    assert utils.data_masking("Счет 64686473678894779589") == 'Счет **9589'


@pytest.fixture
def operations_none():
    return [{}]


def test_list_operations_none(operations_none):
    assert utils.list_operations([]) == []
    with pytest.raises(NameError) as e_info:
        assert utils.list_operations(None)
    assert utils.list_operations(operations_none) == []


@pytest.fixture
def operations_canceled():
    return [{'id': 608117766, 'state': 'CANCELED', 'date': '2018-10-08T09:05:05.282282', 'operationAmount':
        {'amount': '77302.31', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на счет',
             'from': 'Visa Gold 6527183396477720', 'to': 'Счет 38573816654581789611'}]


def test_list_operations_canceled(operations_canceled):
    assert utils.list_operations(operations_canceled) == []


@pytest.fixture
def operations_sort():
    return [{'id': 34148726, 'state': 'EXECUTED', 'date': '2018-11-23T23:52:36.999661', 'operationAmount': {'amount':
        '79428.73', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from':
        'Visa Platinum 5355133159258236', 'to': 'Maestro 8045769817179061'}, {'id': 811920303, 'state': 'EXECUTED',
        'date': '2019-06-14T19:37:49.044089', 'operationAmount': {'amount': '63150.74', 'currency': {'name': 'USD',
        'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 73222753239048295679', 'to':
        'Счет 78544755774551298747'}, {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
        'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description':
        'Открытие вклада', 'to': 'Счет 77613226829885488381'}, {'id': 441945886, 'state': 'EXECUTED', 'date':
        '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code':
        'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to':
        'Счет 64686473678894779589'}, {'id': 902831954, 'state': 'EXECUTED', 'date': '2018-04-22T17:01:46.885252',
        'operationAmount': {'amount': '84732.61', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description':
        'Перевод организации', 'from': 'Visa Platinum 3530191547567121', 'to': 'Счет 46878338893256147528'},
        {'id': 86608620, 'state': 'EXECUTED', 'date': '2019-08-16T04:23:41.621065', 'operationAmount': {'amount':
        '6004.00', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from':
        'MasterCard 8826230888662405', 'to': 'Счет 96119739109420349721'}]


def test_list_operations_sort(operations_sort):
    assert [id_operation.get_id() for id_operation in utils.list_operations(operations_sort)] == \
           [801684332, 441945886, 86608620, 811920303, 34148726]
