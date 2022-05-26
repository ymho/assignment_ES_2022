from re import I


for num in range(1, 101):
    string = ''

    # ここから記述
    
    # 3の倍数ならstringの末尾に文字列Fizzを加える
    if num % 3 == 0:
        string += 'Fizz'
    
    # 5の倍数ならstringの末尾に文字列Buzzを加える
    if num % 5 == 0:
        string += 'Buzz'
    
    # stringが空ならば、3の倍数でも5の倍数でもないため
    # stringをnumとする
    if string == '':
        string = num
         
    # ここまで記述

    print(string)
