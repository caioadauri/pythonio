arquivo_contatos = open('dados/contatos.csv')

conteudo = arquivo_contatos.readlines()

print(conteudo)

for linha in conteudo:
    print(linha, end='')
