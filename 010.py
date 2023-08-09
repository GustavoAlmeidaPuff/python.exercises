#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('quando dinheiro voce tem na sua carteira? R$ '))
dolar = real / 4.90
print ('com {:.2f} reais voce consegue comprar {:.2f} dólares.'.format(real, dolar))