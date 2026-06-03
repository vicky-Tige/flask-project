class student:
    def __init__(self,name,age,student_no,course):
        self.name=name
        self.age=age
        self.student_no=student_no
        self.course=course

        def study(self,unit):
            print(f"{self.name} studies {unit}")
        
        def sleeps(self,time):
            print(f"{self.name} sleep at {time}")
        def eats(self,food):
            print(f"{self.name} eats {food}")
        def get_details(self):
            print("user details")
            print(f"Name:{self.name} - student_No:{self.student_no} - Course:{self.course}")
            print("------------------------------------------------")

        student1=student("jack",28,"S101","cs")
        print(type(student1))
        print(student1)
        student1.get_details()
        student1.study("web development")
    
        student1.sleep("10pm")
        student1.eats("apples")
        
        student2=student("jane",28,"S102","Data Science")
        print(type(student2))
        print(student2)
        student1.get_details()
        student1.study("oop")
    
        student1.sleep("11pm")
        student1.eats("cake")

        
        






