
polynomial = "x"

def solution(polynomial):
    num = 0
    x = 0

    arr = polynomial.split(' + ')

    for i in arr:
        if i.isdigit():
            num += int(i)
        else:
            x = x + 1 if i == 'x' else x + int(i[:-1])
        
    if x == 0:
        return str(num)
    elif x == 1:
        return 'x + ' + str(num) if num != 0 else 'x'
    else:
        return str(x) + 'x + ' + str(num) if num != 0 else str(x) + 'x'

    
print(solution(polynomial))