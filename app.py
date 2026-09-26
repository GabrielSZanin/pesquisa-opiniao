# Pesquisa de opinião - TudoWeb
# Autor: Gabriel Zanin

# Quantidade de entrevistados para pesquisa
quantidade_entrevistados = 50

# Contadores das respostas
total_excelente = 0
total_ruim = 0

# Coleta das respostas
for entrevistado in range(1, quantidade_entrevistados + 1):
    print(f"\n--- Entrevistado {entrevistado} ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opinião sobre o atendimento: "))

    # Validação da opinião
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida! Digite 1, 2 ou 3.")
        opiniao = int(input("Digite novamente a opinião sobre o atendimento: "))

    # Verificação da opinião
    if opiniao == 1:
        total_excelente += 1
        classificacao = "EXCELENTE"

    elif opiniao == 2:
        classificacao = "BOM"

    else:
        total_ruim += 1
        classificacao = "RUIM"

    print(f"Resposta registrada: {classificacao}")

# Resultado final da pesquisa
print("\n=== Resultado final da pesquisa ===")
print(f"Total de entrevistados: {quantidade_entrevistados}")
print(f"Quantidade de respostas EXCELENTE: {total_excelente}")
print(f"Quantidade de respostas RUIM: {total_ruim}")