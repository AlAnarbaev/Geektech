# class Human:
#     head=1
#     def __init__(self,name,age,):
#         self.__name=name
#         self._age=age
#     def __run(self):
#         print(f'{self.__name} is running')
#
#
#
# h=Human('Азирет', 20)
# print(h._Human__name)
#
#
#
# class Human2(Human):
#     def get_name(self):
#         return self.__name
#
#     def set_name(self,name):
#         self.__name=name
#
#
# g=Human2('jack',11)
# print(g.set_name('ja'))
# print(g.get_name())
#
#
#
# class Human3:
#     def __init__(self, name, age, ):
#         self.__name = name
#         self._age = age
#
#     def __run(self):
#         print(f'{self.__name} is running')
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name=name
# l=Human3('kelli',29)
# print(l.name)
#
#
#
#
#


class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print(self.name,'run')
    def __str__(self):
        return f'{self.name} {self.age}'
class Run:
    def run(self):
        print('run')
class Name:
    def names(self):
        print(self)

    def run(self):
        print('Name')
class Robot:
    def __init__(self,model):
        self.model=model

    def run(self):
        print(self.model, 'run')
    def __str__(self):
        return self.model


class Human(People,Run,Name,Robot):
    def __init__(self, name, age,model):
        People.__init__(self,name, age)
        Robot.__init__(self,model)

    def __str__(self):
        return f'{self.name} {self.age} {self.model}'

human=Human('Нурислам',45,'A$')
# human.run()
# human.names()
# print(human)
print(human)
human.run()
