
corredor = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre',
            'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre',
            'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
janela = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre',
          'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre',
          'Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']


def controle_de_passageiros(corredor, janela):
    num_menu = input('Escolha o número de uma das opções: \n'
                     '1 - Vender passagem. \n'
                     '2 - Mostrar mapa de ocupação do ônibus. \n'
                     '3 - Encerrar. \n')
    for i in range(24):
        if corredor[i] == 'Livre':
            break
        elif janela[i] == 'Livre':
            break
        else:
            print('Ônibus lotado. ')
            num_menu = '3'
    return num_menu


def ocupacao_de_assentos(num):
    if num == '1':
        posicao = input('Deseja se sentar na janela (j) ou corredor (c)? ')
        if posicao == 'j' or posicao == 'J':
            controle = input('Qual o número da poltrona? ')
            controle = int(controle)
            if janela[controle] == 'Livre':
                print('Venda efetivada')
                janela.insert(controle-1, 'Ocupada')
            else:
                print('Poltrona ocupada. \n')
        elif posicao == 'c' or posicao == 'C':
            controle = input('Qual o número da poltrona? ')
            controle = int(controle)
            if corredor[controle] == 'Livre':
                print('Venda efetivada.')
                corredor.insert(controle-1, 'Ocupada')
            else:
                print('Poltrona ocupada. \n')


def controle_de_assentos(janela, corredor):
    for i in range(24):
        print(f'Janela {i+1}: {janela[i]}. '
              f'Corredor {i+1}: {corredor[i]}.')


j = True
while j is True:
    num = controle_de_passageiros(janela, corredor)
    if num == '1':
        ocupacao_de_assentos(num)
    elif num == '2':
        controle_de_assentos(janela, corredor)
    elif num == '3':
        j = False
    else:
        print('Dígito inválido... ')
