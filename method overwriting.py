class ineuron:
    def student(self):
        print("details of all students")
    def achivers(self):
        print("list of achivers")
    def hall_of_fame(self):
        print("everyone from hall of fame")

class ineuron_vision(ineuron):

    def student(self):
        print("filters student")
# func student takes from child class
iv = ineuron_vision()
iv.student()