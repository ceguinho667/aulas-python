import os

#Limpar terminal
os.system("clear");

#Solicitando dados ao usuario
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) 
peso = float(input("Digite seu peso: "))

#Exibindo dados inseridos pelo usuario
print("\n==== Exibindo dados ====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")