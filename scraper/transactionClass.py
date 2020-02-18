# this file contains the transaction object class

class Transaction:
    def __init__(self, Date, Amount, Balance, Location, Tender, Transaction):
        self.date = Date
        self.amount = Amount
        self.balance = Balance
        self.location = Location
        self.tender = Tender
        self.transaction = Transaction

    # getter methods

    def getDate(self):
        return self.date

    def getAmount(self):
        return self.date

    def getBalance(self):
        return self.balance

    def getLocation(self):
        return self.location

    def getPaymentAccount(self):
        return self.tender

    def getTransaction(self):
        return self.transaction
