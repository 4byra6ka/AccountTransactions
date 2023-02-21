class operation():
    def __init__(self, id, state, date,  description, from_, to):
        self.id = id
        self.state = state
        self.date = date
        self.operationamount = self.operationamount()
        self.description = description
        self.from_ = from_
        self.to = to


    class operationamount():
        def __init__(self, amount, currency):
            self.amount = amount
            self.currency = currency


        class currency():
            def __init__(self, name, code):
                self.name = name
                self.code = code
