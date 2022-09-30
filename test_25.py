


class CanNotJump():
    h = 'blabla'
    def do(self):
        print('not ka ka ka')
        print(self.h)

a = CanNotJump()
a.do()
b = CanNotJump()
b.h = '678'
b.do()



class CanJump():
    def do(self):
        print('ka ka ka')

class Animal():
    color = 'red'
    
    jump = CanJump()
    def do_jump(self):
        self.jump.do()
        

    def sound(self):
        print('vauuuuuuuuuu')

    def say_color(self):
        print(self.color)

class Dog(Animal):

    def sound(self):
        print('gav gav')

class Cat(Animal):
    def sound(self):
        print('may may')

class Turtle(Animal):
    jump = CanNotJump()

#---------------------------------------------
dog = Dog()
dog.do_jump()
turtle = Turtle()
turtle.do_jump()
# cat = Cat()
# cat.sound()
# dog.jump()
# cat.jump()





# turtle = Turtle()
# turtle.jump()
