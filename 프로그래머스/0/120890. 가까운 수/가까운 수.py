def solution(array, n):
    return array[list(map(lambda x: abs(x-n)+0.5 if x>n else abs(x-n) ,array)).index(min(list(map(lambda x: abs(x-n)+0.5 if x>n else abs(x-n) ,array))))]