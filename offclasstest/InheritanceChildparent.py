'''Multiple inheritance'''

class bird:
    def intro(self):
        print("There are different types of birds.")
    def fly(self):
        print("Most of the birds can fly but some cannot.")
        

class animal:
    def intro(self):
        print("There are different types of animals.")
    def walk(self):
        print("Most of the animals can walk.")

class hybrid(bird, animal):
    def intro(self):
        bird.intro(self)
        animal.intro(self)
        print("This is a hybrid of bird and animal.")
    def fly(self):
        bird.fly(self)
    def walk(self):
        animal.walk(self)

h = hybrid()
h.intro()
h.fly()
h.walk()




