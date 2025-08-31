def solution(i, j, k):
    answer = 0
    k_str = str(k)
    for number in range(i,j+1):
        for parts in str(number):
            if k_str == parts:
                answer +=1
    return answer