# инкапсуляция
# git clone


# инкапсуляция заключечние в одно место (класс) для работы с ними
# предастовление пользователя публичного интерфейса

# публичный
# защищенный
# скрытый
class Human:
    head=1
    def __init__(self,name,age,):
        self.__name=name
        self._age=age
    def __run(self):
        print(f'{self.__name} is running')

    @property
    def prin(self):
        return self.__name
    @prin.setter
    def prin(self,name):
        self.__name=name


h=Human('Азирет', 20)
print(h.prin)
h.prin='j'
print(h.prin)



# def run(a):
#     print(f'{a} is running')
#

# run(h)