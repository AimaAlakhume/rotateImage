def solution(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
            
    for lst in a:
        lst.reverse()
            
    return a
