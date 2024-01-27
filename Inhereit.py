#Multilevel Inhereit
class bank:
    def transaction(self):
        print("total transaction value ")
    def account_opening(self):
        print("account opening status ")
    def deposit(self):
        print("deposited amount ")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("transaction through hdfc to icici ")

class icici(HDFC_bank):
    pass


i = icici()
i.hdfc_to_icici()
i.deposit()
i.account_opening()
i.transaction()




# Multiple
class banks:
    def trans(self):
        print("total transaction value ")
    def account(self):
        print("account opening status ")
    def dep(self):
        print("deposited amount ")
    def test(self):
        print("bank class")

class HDFC:
    def hdfc_icici(self):
        print("transaction through hdfc to icici ")
    def test(self):
         print("hdfc class")
# function test will consider according to first class or seond class in child class
class Icici(HDFC,banks):
    pass

i=Icici()
i.hdfc_icici()
i.dep()
i.account()
i.trans()
i.test()