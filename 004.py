#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
var = input('digite algo: ')

print('o tipo dessa variavel é: ', type(var))
print('só tem espaços? ', var.isspace()) 
print('só tem numeros? ', var.isnumeric()) 
print('É alfabetico? ', var.isalpha()) 
print('é alfanumerico? ', var.isalnum()) 
print('esta em maiusculas? ', var.isupper()) 
print('esta em minusculas? ', var.islower())
print('esta capitalizada? ', var.istitle()) 