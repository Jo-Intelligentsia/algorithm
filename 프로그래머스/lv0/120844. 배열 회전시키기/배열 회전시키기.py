def solution(numbers, direction):
    ls = []
    if direction == 'right':
        ls.append(numbers[-1])
        for i in range(len(numbers)-1):
            ls.append(numbers[i])
    elif direction == 'left':
        for i in range(1,len(numbers)):
            ls.append(numbers[i])    
        ls.append(numbers[0])
        
    return ls