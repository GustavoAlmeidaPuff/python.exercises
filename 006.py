#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
num = int(input('digite um numero: '))

print ('o dobro de {} é {}'.format(num,(num * 2)))
print ('o triplo de {} é {}'.format(num,(num * 3)))
print ('a raiz quadrada de {} é {}'.format(num,math.sqrt(num)))