class Bank:
    money = 'money'

    def __init__(self, name='q', balance=100):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f'{self._name}' \
               f' {self._balance}'

    def scam(self,obj):
        self._balance += obj._balance
        obj._balance -=obj._balance


a=Bank('вы')
b=Bank('я')
print(a)
print(b)
a.scam(b)
print(a)
print(b)