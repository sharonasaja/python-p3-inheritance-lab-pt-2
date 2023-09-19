
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        # Inherit the behavior of hello() from the parent class
        super().hello()  
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):
             # Call super() ten times to print "Pick me!" ten times
            super().raise_hand() 

student = Student()
student.hello()  
student.raise_hand() 
chatty_student = ChattyStudent()
chatty_student.hello()

chatty_student.raise_hand()

