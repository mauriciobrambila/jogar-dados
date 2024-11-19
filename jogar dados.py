import random       
import sys 
a = input("DESEJA INICIAR O JOGO DIGITE 'sim' e PARA SAIR DIGITE 'nao'\n") 
if a.lower() == "nao":    
    sys.exit()
a = input("7 e 11 somente na 1º rodada voce é campeão,e se você tirar 2,3 ou 12 na 1º rodada, voce perde, ok\n") 
if a.lower() == "ok": 
    #else: 
    print("VAMOS COMEÇAR O JOGO, PRESSIONE ENTER") 
a = input("bem-vindo ao jogo\n") 
def diceNumber(): 
    input("pressione enter para jogar os dados") 
    die1 = random.randint(1, 6) 
    die2 = random.randint(1, 6) 
    return (die1, die2)   
def twoDice(dices): 
    die1, die2 = dices 
    print("jogador: A soma dos nº que você obteve no dado 1 e dado 2 são {} + {} = {}".format(die1, die2, sum(dices))) 
value = diceNumber() 
twoDice(value) 
sum_of_dices = sum(value) 
if sum_of_dices in (2, 3, 12): 
    result = "Você perdeu, tente novamente na próxima vez"
elif sum_of_dices in (7, 11): 
    result = "Parabéns, voce venceu"
else:   
    result = "continue seu jogo por favor"
    currentpoint = sum_of_dices 
    print("bom jogo, seu ponto atual é", currentpoint) 
while result == "continue seu jogo por favor": 
    value = diceNumber() 
    twoDice(value) 
    sum_of_dices = sum(value) 
    if sum_of_dices == currentpoint: 
        result = "Parabéns você ganhou"
    elif sum_of_dices == 6: 
        result = "Parabéns, vc venceu logo no inicio"
if result == "Parabéns você ganhou": 
    print("Parabéns, você ganhou") 
else: 
    print("você perdeu, tente novamente na próxima vez") 