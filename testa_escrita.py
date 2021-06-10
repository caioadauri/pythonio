arquivo_contatos = open('dados/contatos-escrita.csv', mode='w')

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '12,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()

input('Pressione <Enter> pra encerrar o programa')
