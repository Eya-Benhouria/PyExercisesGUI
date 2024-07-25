def sizing():
        _list = 0
        while(_list<5 or _list>50):
            print("The list size : ")
            _list = int(input(">_"))
        return _list
def sum_entier(_entier):
    sum = 0
    _entier = int(_entier)
    while(_entier >= 1):
        sum += _entier%10
        _entier = _entier//10
    return sum

def facteurs(_list, _entier):
    _entier = int(_entier)
    i = 2
    while(_entier%i == 0):
        _list.append(i)
        _entier = int(_entier/i)
    i = 3
    while(i <= _entier):
        while(_entier%i == 0):
            _list.append(i)
            _entier = int(_entier/i)
            i = i + 2

def sum_facteurs(_list):
    sum = 0
    for i in range(0, len(_list)):
        if(_list[i]<10):
            sum += int(_list[i])
        else:
            sum += sum_entier(_list[i])
    return sum

def smith(_list):
    for i in range(0, len(_list)):
        list_variable = []
        facteurs(list_variable, _list[i])
        if(sum_entier(_list[i]) == sum_facteurs(list_variable) and len(list_variable) > 1):
            print(_list[i])
size = sizing()
L = [7, 23, 2000, 29, 100, 13, 70, 27, 636]
