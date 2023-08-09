#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

#jeito um: criando variaveis pro caso de eu precisar usar o aantecessor e sucessor mais pra frente no meu codigo
n = int(input('digite um número: '))
a = n - 1
s = n + 1
print ("o antecessor de ", n ," é ", a ," e o sucessor é ", s , ".")

#jeito dois: com o .format
n = int(input('digite um número: '))
print ("o antecessor de {} é {} e o sucessor é {}.".format(n, (n-1), (n+1)))