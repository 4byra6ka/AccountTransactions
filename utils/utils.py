import requests
from dto.operation import *
def load_operations(url):
    """
    Загрузка операций по транзакциям в формате JSON
    :param url: Ссылка str
    :return: JSON
    """
    load = requests.get(url=url)
    if load.status_code != 200:
        return NameError(f"Удаленный сервер не отвечает {load.status_code}")
    return load.json()

def list_operations(json_transactions):
    """
    Загрузка в опараций в класс и предоставления списка
    :param json_transactions: JSON всех транзакций
    :return: List транзакций
    """
    list_transactions = []
    for transaction in json_transactions:
        if transaction == {}:
            continue
        if transaction.setdefault('state') in [None, "CANCELED"]:
            continue
        list_transactions.append(
            operation(id=transaction.setdefault('id'),
                      state=transaction.setdefault('state'),
                      date=transaction.setdefault('date'),
                      amount=transaction['operationAmount'].setdefault('amount'),
                      name=transaction['operationAmount']['currency'].setdefault('name'),
                      code=transaction['operationAmount']['currency'].setdefault('code'),
                      description=transaction.setdefault('description'),
                      from_=transaction.setdefault('from'),
                      to=transaction.setdefault('to'))
        )
    return list_transactions

