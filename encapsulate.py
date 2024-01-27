# modify
# not allow user to modify available information directly
class ineuron1:
    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)
    def student_change(self,new_value):
#setter function
        self.__students1 = new_value

i = ineuron1()
i.students()
i.__students1= "big data by me"
i.students()
i.student_change("gaurav")
i.students()