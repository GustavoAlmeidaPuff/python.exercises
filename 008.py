#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m= float(input('uma distancia em metros: '))
cm= m *100
mm = m*1000

print('a medida de {} metros corresponde a {:.0f}cm e {:.0f}mm'.format(m,cm,mm))