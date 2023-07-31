# Variáveis de contagem
maiores_dezoito = 0
homens = 0
mulheres_menos_vinte = 0

while True:
    # Leitura dos dados
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [M/F]: ").upper()

    # Verificações das condições
    if idade > 18:
        maiores_dezoito += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_vinte += 1

    # Pergunta se deseja continuar
    opcao = input("Deseja continuar? [S/N]: ").upper()
    print('-'*30)
    if opcao == "N":
        break

# Exibição dos resultados
print(f"\nTotal de pessoas com mais de 18 anos: {maiores_dezoito}")
print(f"Total de homens cadastrados: {homens}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_vinte}")