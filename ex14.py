num=int(input('Digite um número inteiro:'))

u=num // 1 % 10
d=num // 10 % 10
c=num // 100 % 10
m =num // 1000 % 10
dm=num // 10000 % 10
cm=num // 100000 % 10
uml=num // 1000000 % 10
dml=num // 10000000 % 10
cml=num // 100000000 % 10
soma= (u+d+c+m+dm+cm+uml+dml+cml)
print(soma)