# same person different behaviour
# changing behaviour person to person

class ineuron:
    def students(self):
        print("Students details")

class class_type:
    def students(self):
        print("class type of student")


def ineuron_external(a):
    a.students()
# this function acts as a bridge/common interface btw all the class
i= ineuron()
j= class_type()
ineuron_external(i)
ineuron_external(j)

