# -*- coding: utf-8 -*-
"""Correção_exercícios_while.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FRyFj5mgrh8kUY9Gqc6GtP8cZILaxRYW

# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
"""

while True:
    nota = float(input("Digite uma nota entre zero e dez: "))

    if nota >= 0 and nota <=10:
        print("Nota válida:", nota)
        break
    else:
        print("Valor inválido! A nota deve estar entre zero e dez. Tente novamente.")

"""# 2. Faça um programa que calcule o mostre a média aritmética de N notas."""

notas = 0
contador = 0
continuar = "S"
while continuar == "S":
    nota = float(input("Digite uma nota: "))
    notas += nota
    contador += 1
    continuar = input("Deseja continuar? (S/N): ").upper()


print(f"A média das notas é {notas/contador:.2f}.")

"""# 3. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

# Solicite ao usuário a quantidade de turmas.
# Para cada turma, peça que o usuário informe a quantidade de alunos.
# Certifique-se de que o número de alunos por turma não ultrapasse 40.
# Ao final, exiba a média de alunos por turma.

"""

turmas = int(input('Digite quantas turmas tem: '))
soma = 0
contador = 0

while contador < turmas:
  alunos = int(input(f'Digite a quantidade de alunos {contador+1}ª turma: '))
  if alunos <= 40:
    contador += 1
    soma += alunos
  else:
    print('O número de alunos deve ser no máximo 40')
print(f'A média é {soma/contador:.0f}')

"""# 4 Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado. Por exemplo, se o número é 201 , então a saída deve ser 3."""

print('Contagem de digitos')

digitos = int(input('Digite um número: '))
contador = 0

while digitos != 0:
  digitos = digitos // 10
  contador += 1
print(f'Total de digitos = {contador}')

"""# 5 Crie um programa em Linguagem Python que solicite a senha de um usuário e depois, peça pra digitar novamente até que as duas senhas sejam correspondentes."""

print('Confirmação de senha')
senha1 = input('Digite a senha ')
senha2 = input('Digite sua senha novamente ')

while senha1 != senha2:
  print('Senha errada, digite novamente ')
  senha1 = input('Digite a senha: ')
  senha2 = input('Digite sua senha novamente ')
print('Senha confirmada')

"""# 6 Faça um programa em Python que leia 'n' números inteiros a partir do teclado, até que o usuário digite 0. Ao final, mostre a soma de todos os números digitados."""

soma = 0

while True:
  numero = int(input('Digite um número (0 para sair): '))
  if numero == 0:
    break
  else:
    soma += numero
print(f'A soma dos números digitados é {soma}')