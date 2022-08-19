def soma(x,y):
    print("O resultado é: ", x + y) 

def sub(x,y):
    print("O resultado é: ", x - y)

def mult(x,y):
    print("O resultado é:", x * y)

def div(x,y):
    if y == 0:
        print("Divisão por zero não existe!")
        exit()
    print("O resultado é: ", x / y)

print('**********************Calculadora Python**********************\n')

print("Selecione o número da operação desejada: ")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

oper = int(input('Digite sua opção (1/2/3/4): '))
if oper < 1 or oper > 4:
    print("Escolha uma opção válida!")
    exit()

x = int(input('Insira o primeiro número: '))
y = int(input('Insira o segundo número: '))

if oper == 1:
    soma(x,y)
elif oper == 2:
    sub(x,y)
elif oper == 3:
    mult(x,y)
else:
    div(x,y) 