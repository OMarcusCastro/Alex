nome = input()
salario = float(input())
vendas = float(input())
bonus = vendas * 0.15
total = bonus + salario
print(f"TOTAL = R$ {total:.2f}")