#Função
def f(num, x, exp):
    return (num*x**(exp+1))/(exp+1)

#Definir inicio e fim do intervalo e o tanto de subdivisões
inicioIntervalo=int(input('Digite onde o intervalo se inicia: '))
fimIntervalo=int(input('digite onde o número termina: '))


if(fimIntervalo>inicioIntervalo):
    integraInicio=0
    integraFim=0

    mais=True
    while(mais):
        num=(int(input('Digite um numero: ')))
        exp=(int(input('Qual expoente de X: ')))

        integraInicio+=f(num, inicioIntervalo, exp)
        integraFim+=f(num, fimIntervalo, exp)

        resposta=str(input('Colocar mais dados? s/n: '))
        while(resposta!='s' and resposta != 'n'):
            resposta=str(input('Digite Novamente. s/n: '))
        if(resposta=='n'):
            mais=False



    integral=integraFim-integraInicio

    print(integral)



else:
    print('Valores inválidos')

