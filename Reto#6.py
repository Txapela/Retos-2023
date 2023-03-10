#!/usr/bin/env python

'''
 Crea un programa que calcule quien gana m谩s partidas al piedra,
 papel, tijera, lagarto, spock.
 - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 - La funci贸n recibe un listado que contiene pares, representando cada jugada.
 - El par puede contener combinaciones de "馃椏" (piedra), "馃搫" (papel),
   "鉁傦笍" (tijera), "馃" (lagarto) o "馃枛" (spock).
 - Ejemplo. Entrada: [("馃椏","鉁傦笍"), ("鉁傦笍","馃椏"), ("馃搫","鉁傦笍")]. Resultado: "Player 2".
 - Debes buscar informaci贸n sobre c贸mo se juega con estas 5 posibilidades.
'''
# Inicio de la funci贸n
def round(game):

  modelwins = {"馃椏":["鉁傦笍","馃"] , "馃搫":["馃椏","馃枛"] , "鉁傦笍":["馃搫","馃"] , "馃":["馃搫","馃枛"] , "馃枛":["鉁傦笍","馃椏"]}
  player_1 = 0
  player_2 = 0
  tie = 0

#Inicio del bucle "for" para recorrer posiciones y comparar valores
  for i in game:
    
    if i[0] == i[1]:
      tie += 1
    elif i[0] in modelwins[i[1]]:
      player_2 += 1
    else:
      player_1 += 1
  
# Impresi贸n de resultados
  if player_1 > player_2:
    print ("PLAYER-1 WINS.")
  elif player_1 < player_2:
    print ("PLAYER-2 WINS.")
  else:
    print ("TIED GAME")

# Games
round([("馃椏","鉁傦笍"), ("鉁傦笍","馃"), ("馃搫","鉁傦笍")])   #Player-1 wins
round([("馃椏","鉁傦笍"), ("鉁傦笍","馃椏"), ("馃椏","馃椏")])   #Tie
round([("馃椏","馃枛"), ("馃","馃枛"), ("馃","馃椏")])   #Player-2 wins
round([("鉁傦笍","鉁傦笍"), ("馃","馃枛"), ("馃","鉁傦笍"), ("馃","馃")])   #Tie
round([("馃椏","鉁傦笍"), ("鉁傦笍","馃"), ("馃搫","鉁傦笍"), ("馃椏","鉁傦笍"), ("鉁傦笍","馃"), ("馃搫","鉁傦笍")])   #Player-1 wins
