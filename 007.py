# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input("qual foi a primeira nota do aluno?"))
nota2 = float(input("qual foi a segunda nota do aluno?"))

media = (nota1 + nota2) / 2

print("a media entre {:.1f} e {:.1f} é igual á {:.1f}".format(nota1,nota2,media))