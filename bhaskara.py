import math
a=float(input('Digite o valor do coeficiente a:',))
b=float(input('Digite o valor do coeficiente b:',))
c=float(input('Digite o valor do coeficiente c:',))
print('A=',a,'B=',b,'C=',c)
delta=b**2-4*a*c
print(delta)
## Se Δ = 0, a equação do segundo grau possui uma raiz real;
if delta==0:
    raiz1=(-b+math.sqrt(delta))/(2*a)
    print('A única raiz é=',raiz1)
else:
    ## Se Δ < 0, a equação do segundo grau não possui raízes reais;
    if delta<0:
        print('Esta equação não prossui raizes reais.')
    else:
    ## Se Δ > 0, a equação do segundo grau possui duas raízes reais.    
        raiz1=(-b+math.sqrt(delta))/(2*a)
        raiz2=(-b-math.sqrt(delta))/(2*a)
        print('A primeira rais é:',raiz1)
        print('A segunda rais é:',raiz2)
