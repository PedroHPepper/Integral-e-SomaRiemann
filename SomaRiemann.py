#Função
def f(x):
    return (4*x**2)+x+1

#Definir inicio e fim do intervalo e o tanto de subdivisões
inicioIntervalo=int(input('Digite onde o intervalo se inicia'))
fimIntervalo=int(input('digite onde o número termina'))
n=int(input('Quantas subdivisões'))

if(fimIntervalo>inicioIntervalo):
    h=(fimIntervalo-inicioIntervalo)/n
    somaMédia=0
    somaInf=0
    somaSup=0
    for n in range(n):
        X0=inicioIntervalo+(n*h)
        X1=X0+h
        X_média=(X1+X0)/2
        somaMédia+=f(X_média)*h
        somaInf+=f(X0)*h
        somaSup+=f(X1)*h



    print('A soma Superior é', somaSup)
    print('A Soma da média é', somaMédia)
    print('A soma inferior é', somaInf)
else:
    print('Valores inválidos')

