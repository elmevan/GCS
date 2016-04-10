def tabuada(num, num1):
    mutiplica = num * num1
    print("{} x {} = {}".format(num, num1, mutiplica))

def contaLetra(opcao, frase):
    soma = 0
    for letra in frase:
        if letra == opcao:
            soma = soma + 1
    print("Quantidade de {} {}".format(opcao, soma))

for num in range (1,11):
    for num1 in range (1,11):
        tabuada(num, num1)
    num = num + 1
    num = 1
    print("------")
print("fim")

contaLetra(input("Opção de escolha: "),input("Qual a Frase: "))
teste
