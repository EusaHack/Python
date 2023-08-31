def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1 # (-1) se agrego ya que una lista empieza desde 0
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # (2) se modifico el 1 porque ya se habia utilizado la posicion n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # (-) se cambio el signo ya que iba a ser la misma posicion con st 

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)