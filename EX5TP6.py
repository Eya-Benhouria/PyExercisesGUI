

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

def minimize(__entier): 
    _entier = list(__entier) 
    for i in range(0, len(_entier) - 1): 
        if(int(_entier[i]) > int(_entier[i+1])): 
            for j in range(i+1, 0, -1): 
                if(int(_entier[j]) < int(_entier[j-1])): 
                    temp = _entier[j] 
                    _entier[j] = _entier[j-1] 
                    _entier[j-1] = temp 
    __entier = "".join(_entier) 
    return __entier 

def suite(_entier): 
    count = 0
    Uo = _entier 
    Un = _entier 
    while(1): 
        print(Un) 
        Un = str(int(maximize(Uo)) - int(minimize(Uo))) 
        count += 1 
        if( Uo == Un ): 
            print("Le nombre des termes de la suite est : ", count) 
            break 
        Uo = Un 

suite("9324")
