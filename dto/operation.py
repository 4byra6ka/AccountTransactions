from datetime import datetime as dt


class Operation:
    def __init__(self, id, state, date, amount, name, code, description, from_, to):
        self.id = id
        self.state = state
        self.date = date
        self.operationamount = self.OperationAmount(amount, name, code)
        self.description = description
        self.from_ = from_
        self.to = to

    def __repr__(self):
        return f'id = {self.id}, state = {self.state}, date = {self.date}, description = {self.description}, ' \
               f'from_ = {self.from_}, to = {self.to}'

    def get_id(self):
        return self.id
    def get_date(self):
        return self.date

    def get_print_operation(self):
        return f"{dt.strftime(self.date, '%d.%m.%Y')} {self.description}\n" \
               f"{'' if self.from_ is None else str(self.from_) + ' -> '}{self.to}\n" \
               f"{self.operationamount.amount} {self.operationamount.currency.name}"

    class OperationAmount:
        def __init__(self, amount, name, code):
            self.amount = amount
            self.currency = self.Currency(name, code)

        def __repr__(self):
            return f'amount = {self.amount}'

        class Currency:
            def __init__(self, name, code):
                self.name = name
                self.code = code

            def __repr__(self):
                return f'name = {self.name}, code = {self.code}'
