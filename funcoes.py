def coracao():
    print('♥' * 30)


def selecao(arguments):
    while not arguments.isnumeric():
        arguments = input('Por favor, digite a númeração de acordo com as referências listadas acima: \n')
    else:
        arguments = int(arguments)
        return arguments


x = False


def verificacao(lista, saida_):
    pergunta = input('Você deseja verificar o que está na lista? [s]im - [n]ao')
    pergunta.lower()
    if pergunta == 's':
        coracao()
        print('Lista: ')
        for i, valor in enumerate(lista):
            print('{} Item: {}'.format(i, valor))
        coracao()
    else:
        saida = input('Deseja sair? [s]im - [n]ao ')
        if saida == 's':
            saida_ = x
            return lista, saida_
        else:
            pass
    return lista, saida_


def qtd(qtd_prod=None):
    value = input('Quantos produtos deseja adicionar? \nMaxímo: 20 - Mínimo: 1\nDigite: ')
    print('')
    while not value.isnumeric():
        value = input('Valor numérico por favor!\n')
    else:
        value = int(value)
    if value < 1 or value > 20:
        coracao()
        print('Por favor, digite um valor entre 1 e 20'.upper())
        coracao()
    else:
        cont = 0
        coracao()
        while cont < value:
            produtos = input('Add item: ')
            produtos = str(produtos)
            qtd_prod.append(produtos)
            cont += 1
        print('')
        laco = False
        return qtd_prod, laco


def escolha(outro_valor, x='Você escolheu!!!\n'):
    print(x)
    while outro_valor:
        return outro_valor, x


def valor_total(lista1, lista2):
    question = input('Deseja saber os itens totais da sua lista?\nIsso resultará no encerramento do programa')
    x = question.upper()
    total = lista1 + lista2
    print('Digite "[S]"im:')
    if x == 'S':
        print('Segue a lista de itens:\n{}'.format(total))
    else:
        print('Valor inválido')
