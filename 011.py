# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l= float(input('largura da parede: '))

a= float(input('altura da parede: '))

area= l*a

Ltinta= area/2

print('sua parede tem a dimesão de {:.2f}x{:.2f} e sua área é de {:.3f}metros quadrados\n e a quantidade necessária de tinta é de {} litros de tinta'.format(l, a, area, Ltinta))
#yooo