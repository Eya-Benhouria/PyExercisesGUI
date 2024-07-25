def seperating(_list, _entier): 
    if( len(_entier)%3 == 0 ): 
        for i in range(1, int(len(_entier)/3)*3, 3): 
            _list.append(_entier[-i-2] + _entier[-i-1] + _entier[-i]) 

    elif( len(_entier)%3 == 1 ): 
        for i in range(1, int(len(_entier)//3)*3, 3): 
            _list.append(_entier[-i-2] + _entier[-i-1] + _entier[-i]) 
        _list.append(_entier[0]) 


    elif( len(_entier)%3 == 2 ): 
        for i in range(1, int(len(_entier)//3)*3, 3): 
            _list.append(_entier[-i-2] + _entier[-i-1] + _entier[-i]) 
        _list.append(_entier[0] + _entier[1]) 

    else: 
            print("Something wrong !") 

def list_sum(_list): 
    sum = 0 
    for i in range(0, len(_list)): 
        if(i%2 == 0): 
            sum -= int(_list[i]) 
        elif(i%2 == 1): 
            sum += int(_list[i]) 
        else: 
            print("Something wrong !") 
    return sum 

L = [] 
variable = input(">_") 
seperating(L, variable) 
print(L[:]) 
sum_result = abs(list_sum(L)) 
print(sum_result) 
if(sum_result%13 == 0): 
    print(f"{sum_result} est divisible par 13 donc {variable} est divisible par 13") 
else: 
    print("N'est par divisible") 
