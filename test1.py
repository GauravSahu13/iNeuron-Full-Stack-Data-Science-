class Person:
# to create generic code
#constructor is a init method ---> entity or function or inbuilt func by which you will able to pass data/information to class
# self --> pointer(pointing to class)
# always take last constructor
    def __init__(self,name,surname,yob):
        self.name = name
        self.surname = surname
        self.yob = yob

    def age(self, current_year):
        return current_year - self.yob

# anuj_var == class variable ---> object
anuj_var = Person('anuj','shaw',1999)
print(anuj_var.name)
print(anuj_var.age(2023))


# self._name ---> protected variable
# self.__surname ---> private variable ---> calling:(anuj._Person__surname)
# from test2.py import person  where test2 ---> file & person --> class

