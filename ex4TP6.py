

def anti_palindrome(_list, _entier):
        count = 0 
        for i in range(0, int(len(_entier)//2) ): 
            if(_entier[i] != _entier[-i-1]): 
                count = count + 1 

        if(count == int(len(_entier)//2)): 
            _list.append(_entier) 

def maximize(__entier):
    _entier = list(__entier) 
    for i in range(0, len(_entier) - 1): 
        if(int(_entier[i]) < int(_entier[i+1])): 
            for j in range(i+1, 0, -1): 
                if(int(_entier[j]) > int(_entier[j-1])): 
                    temp = _entier[j] 
                    _entier[j] = _entier[j-1] 
                    _entier[j-1] = temp 
    __entier = "".join(_entier) 
    return __entier 

def verification(__entier): 
    _entier = list(__entier) 
    list_variable = [] 
    for i in _entier: 
        if i not in list_variable: 
            list_variable.append(i)
    __entier = "".join(list_variable) 
    return __entier 

def sizing(): 
    _size = 0 
    while(_size<5 or _size>50): 
        _size = int(input("Donner le nombre d entiers :\n >_"))
    return _size 

def appending(_list, _size): 
    for i in range(0, _size): 
        x = input(">_") 
    anti_palindrome(_list, x) 

L = [] 
size = sizing() 
appending(L, size) 
for i in range(0, len(L)): 
    extra_variable = maximize(L[i]) 
    extra_variable = verification(extra_variable) 
L[i] = extra_variable 
print(L[:]) 
