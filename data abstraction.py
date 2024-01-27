# access
# hiding actual data behind class
# hiding implementation
class ineuron:
    __students = "data science"

    def student(self):
        print("class of students is ",ineuron.__students)

i = ineuron()
i.student()
