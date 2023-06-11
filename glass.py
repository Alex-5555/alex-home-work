'''
class Animal:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print(self.name)
    
dog = Animal('gav gav')
dog.sound()
cat = Animal('may may')
cat.sound()


class Animal:
    def sound(self):
        print(self.name)

class Dog(Animal):
    name = 'gav gav'

class Cat(Animal):
    name = 'may may'

dog = Dog()
dog.sound()
cat = Cat()
cat.sound()

# Создайте класс Soda (для определения типа газированной воды), 
# принимающий 1 аргумент при инициализации (отвечающий за добавку 
# к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать 
«Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе 
отобразится следующая фраза: «Обычная газировка».
class Soda():
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    
    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка + {self.ingredient}')
        else:
            print('Обычная газировка')

Wather_1 = Soda("Малина")
Wather_2 = Soda(10)
Wather_1.show_my_drink()
Wather_2.show_my_drink()

# Николаю требуется проверить, возможно ли из представленных 
# отрезков условной длины сформировать треугольник. 
# Для этого он решил создать класс TriangleChecker, принимающий 
# только положительные числа. 
# С помощью метода is_triangle() возвращаются следующие значения 
# (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.
class TriangleCheker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sides_sort = sorted(self.sides)
                if sides_sort[0] + sides_sort[1] > sides_sort[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'

triangle_1 = TriangleCheker([2, 3, 4])
print(triangle_1.is_triangle())
triangle_2 = TriangleCheker([-7, 10, 'resset'])
print(triangle_2.is_triangle())                 


# Евгения создала класс KgToPounds с параметром kg, куда 
# передается определенное количество килограмм, а с помощью 
# метода to_pounds() они переводятся в фунты. Чтобы закрыть 
# доступ к переменной “kg” она реализовала методы set_kg() - 
# для задания нового значения килограммов, get_kg()  - для 
# вывода текущего значения кг. Из-за этого возникло неудобство: 
# нам нужно теперь использовать эти 2 метода для задания и вывода 
# значений. Помогите ей переделать класс с использованием функции 
# property() и свойств-декораторов. Код приведен ниже.
class KgToPounds():
    def __init__(self, kg):
        if isinstance(kg, (int, float)):
            self.kg = kg
        else:
            self.kg = None
       
    def to_pounds(self):
        if self.kg:
            return self.kg * 2.205
        else:
            return 'Килограммы задаются только числами'

to_points1 = KgToPounds(3)
print(to_points1.to_pounds())
to_points2 = KgToPounds('tresch')
print(to_points2.to_pounds())        

class KgToPounds():
    def __init__(self, kg):
        self.__kg = kg
        # self.__set_kg(kg)
    
    def to_pounds(self):
        return self.__kg * 2.205
    
    def set_kg(self, kg_new):
        if isinstance(kg_new, (int, float)):
            self.__kg = kg_new
        else:
            raise ValueError ("Килограммы задаются только числами")
    
    def get_kg(self):
        return self.__kg

    kg = property(get_kg, set_kg)

to_pounds1 = KgToPounds(3)
to_pounds1.kg = 4
print(to_pounds1.kg, to_pounds1.__dict__)
print(to_pounds1.to_pounds())

class KgToPounds():
    def __init__(self, kg):
        self.__kg = kg
    
    def to_pounds(self):
        return self.__kg * 2.205
    
    def set_kg(self, kg_new):
        if isinstance(kg_new, (int, float)):
            self.__kg = kg_new
        else:
            raise ValueError ("Килограммы задаются только числами")

    def get_kg(self):
        return self.__kg       
    
    kg = property()
    kg = kg.getter(get_kg)
    kg = kg.setter(set_kg)

p = KgToPounds(3)
print(p.to_pounds())
p.kg = 5
print(p.kg, p.__dict__)   

class KgToPounds():
    def __init__(self, kg):
        self.www(kg)
        # if isinstance(kg, (int, float)):
        # self.__kg = kg
        # else:
            # raise ValueError ("Килограммы задаются только числами")
            
    def to_pounds(self):
        return self.__kg * 2.205
    
    @property  
    def kg(self):
        return self.__kg 

    def www(self, h):
        if isinstance(h, (int, float)):
            self.__kg = h
        else:
            raise ValueError ("Килограммы задаются только числами")
      
    @kg.setter
    def kg(self, kg_new):
       self.www(kg_new)

    @kg.deleter
    def kg(self):
        del self.__kg

p = KgToPounds(3)
# print(p.to_pounds(), p.__dict__)
p.kg = 5
# del p.kg
# p.set_kg(7)
print(p.kg, p.__dict__)  

class KgToPounds():
    def __init__(self, kg):
        self.__kg = kg
                   
    def to_pounds(self):
        return self.__kg * 2.205
     
    @property  
    def kg(self):
        return self.__kg 

    @kg.setter
    def kg(self, kg_new):
        if isinstance(kg_new, (int, float)):
            self.__kg = kg_new
        else:
            raise ValueError ("Килограммы задаются только числами")
   
    @kg.deleter
    def kg(self):
        del self.__kg

p = KgToPounds(3)
print(p.to_pounds(), p.__dict__)
p.kg = 5
# del p.kg
# p.set_kg(7)
print(p.kg, p.__dict__)  


# Николай – оригинальный человек. 
# Он решил создать класс Nikola, принимающий при инициализации 
# 2 параметра: имя и возраст. Но на этом он не успокоился. 
# Не важно, какое имя передаст пользователь при создании экземпляра,
# оно всегда будет содержать “Николая”. 
# В частности - если пользователя на самом деле зовут Николаем, то
# с именем ничего не произойдет, а если его зовут, например, Максим,
# то оно преобразуется в “Я не Максим, а Николай”.
# Более того, никаких других атрибутов и методов у экземпляра не 
# может быть добавлено, даже если кто-то и вздумает так поступить 
# (т.е. если некий пользователь решит прибавить к экземпляру 
# свойство «отчество» или метод «приветствие», то ничего у такого 
# хитреца не получится).

class Nikola:

    __slots__ = ['name', 'old']

    def __init__(self, name, old):
        if name == 'Николай':
            self.name = name
        else:
            self.name = f'Я не {name}, а Николай'
        self.old = old


    #     self.exam_name(name)
    #     self.exam_old(old)

    #     # self.name = name
    #     # self.old  = old
    
    # def exam_name(self, name):
    #     if name == 'Николай':
    #         self.name = name
    #     else:
    #         self.name = f'Я не {name}, а Николай'
        
    # def exam_old(self, old):
    #     if type(old) == int or old < 18 or old > 65:
    #         self.old = old

    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self, name):
    #     self.exam_name(name)
    #     self.__name = name 

    # @property
    # def old(self):
    #     return self.__old

    # @old.setter
    # def old(self, old):
    #     self.exam_old(old)
    #     self.__old = old 

person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)
print(person1.name)
print(person2.name)
print(person1.__dict__)
person2.surname = 'Петров'
'''
# Cтроки в Питоне сравниваются на основании значений символов. 
# Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», 
# – то «Яблоко» окажется бОльшим. 
# А все потому, что английская буква «A» имеет значение 65 
# (берется из таблицы кодировки), а русская буква «Я» – 1071 
# (с помощью функции ord() это можно выяснить). 
# Такое положение дел не устроило Анну. 
# Она считает, что строки нужно сравнивать по количеству входящих 
# в них символов.
# Для этого девушка создала класс RealString и реализовала 
# озвученный инструментарий. Сравнивать между собой можно как 
# объекты класса, так и обычные строки с экземплярами класса 
# RealString. 
# К слову, Анне понадобилось только 3 метода внутри класса 
# (включая __init__()) для воплощения задуманного.            

class RealString:
    def __init__(self, str1, str2):
        # self.verify_str1(str1)
        # self.verify_str2(str2)
        self.str1 = str1 
        self.str2 = str2
       
    def exam_str(self):   
        if len(self.__str1) > len(self.__str2):
            return 'Строка 1 длиннее, чем Строка 2'
        if len(self.__str1) < len(self.__str2):
            return 'Строка 1 короче, чем Строка 2'
        else:
            return 'Строка 1 равна Строке2'

    @classmethod
    def verify_str1(cls, str1):
        if type(str1) != str:
            raise TypeError('Данные должны быть строкой')
        if len(str1) < 1:
            raise ArithmeticError('Cтрока должна иметь хотя бы один символ')

    @classmethod
    def verify_str2(cls, str2):
        if type(str2) != str:
            raise TypeError('Данные должны быть строкой')
        if len(str2) < 1:
            raise ArithmeticError('Cтрока должна иметь хотя бы один символ')
    
    @property
    def str1(self):
        return self.__str1
    @str1.setter
    def str1(self, str1):
        self.verify_str1(str1)
        self.__str1 = str1
        
    @property
    def str2(self):
        return self.__str2
    @str2.setter
    def str2(self, str2):
        self.verify_str2(str2)
        self.__str2 = str2    

s = RealString('Alex', 'Dima')
print(s.__dict__)
s.str1 = 'Grisha'
print(s.__dict__)
print(s.exam_str())
