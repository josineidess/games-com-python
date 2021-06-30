# variaveis

tab = {'00': '  ', '01': '  ', '02': '  ',
       '10': '  ', '11': '  ', '12': '  ',
       '20': '  ', '21': '  ', '22': '  '}

jogador1 = True

# condições de vitória

cond00 = tab['00'] == tab['01'] == tab['02']
cond11 = tab['10'] == tab['11'] == tab['12']
cond22 = tab['20'] == tab['21'] == tab['22']
condHorizontal = cond00 or cond11 or cond22

cond10 = tab['00'] == tab['10'] == tab['20']
cond12 = tab['01'] == tab['11'] == tab['21']
cond23 = tab['02'] == tab['12'] == tab['22']
condVertical = cond10 or cond12 or cond23

condD1 = tab['00'] == tab['11'] == tab['22']
condD2 = tab['02'] == tab['11'] == tab['20']

condDiagonal = condD1 == condD2


# desenhar tabuleiro

def desenha_tabu():
    print('      |      |    ')
    print('  %s  |  %s  |  %s  ' % (tab['00'], tab['01'], tab['02']))
    print('______|______|____')
    print('      |      |    ')
    print('  %s  |  %s  |  %s  ' % (tab['10'], tab['11'], tab['12']))
    print('______|______|____')
    print('      |      |    ')
    print('  %s  |  %s  |  %s  ' % (tab['20'], tab['21'], tab['22']))
    print('      |      |    ')


desenha_tabu()

'''sistema de jogo'''

# função responsavel por cada jogada


def joga(pos, jogador1):
    if(tab[pos] != 'X ' and tab[pos] != 'O '):
        if(jogador1):
            tab[pos] = 'X '
        else:
            tab[pos] = 'O '
        return True
    else:
        print("Posição ocupada...")
        return False

# função que checa se as condições de vitória foram atendidas


def checa_vitoria():
    if(condHorizontal or condVertical or condDiagonal):
        return True
    else:
        return False
