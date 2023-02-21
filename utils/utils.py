import requests

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

