n_testes = int(input())

for j in range(n_testes):

    x = int(input())

    n1 = 0
    n2 = 1
    resp = "0 1 "

    for i in range(x):
        n3 = n1+n2

        
        n1=n2
        n2=n3
    print(f"Fib({x}) = {n1}")