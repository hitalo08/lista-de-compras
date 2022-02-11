from funcoes import selecao, coracao, verificacao,qtd, escolha, valor_total

laco = bool
lista_salada = []
lista_frutas = []
lista_cereais = []
lista_carneseovos = []
laco_itens = True
saida = False

valor_usuario = 0
laco_selecao = bool
coracao()
print('Seja bem vindo a lista de compras')

#Programa principal
while laco_selecao:
    print('O que você irá comprar no supermercado?\n')
    print('[1] Salada\n[2] Frutas\n[3] Cereais\n[4] Carnes e Ovos\n')
    value = input('Por favor, digite um valor!')


    #SALADA
    if selecao(value) == 1:
        escolha(laco_itens, x='\nVocê escolheu SALADA!\n')
        qtd(lista_salada)
        verificacao(lista_salada, saida)
    #FRUTAS
    elif selecao(value) == 2:
        escolha(laco_itens, x='\nVocê escolheu FRUTAS!\n')
        qtd(lista_frutas)
        verificacao(lista_salada, saida)
    #CEREAIS
    elif selecao(value) == 3:
        escolha(laco_itens, x='\nVocê escolheu CEREAIS!\n')
        qtd(lista_cereais)
        verificacao(lista_salada, saida)
    #CARNES E OVOS
    elif selecao(value) == 4:
        escolha(laco_itens, x='\nVocê escolheu CARNES E OVOS!\n')
        qtd(lista_carneseovos)
        verificacao(lista_salada, saida)

print(valor_total(lista_salada, lista_frutas))
