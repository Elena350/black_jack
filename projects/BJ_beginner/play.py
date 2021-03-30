import random
def play():
  bet = int(input("Пожалуйста, делайте ставку."))
  cards_values = [[2, "два"], [3, "три"], [4, "четыре"], [5, "пять"], [6, "шесть"], [7, "семь"], [8, "восемь"], [9, "девять"], [10, "десять"], [10, "face"], [10, "face"], [10, "face"], [11, "ace"]] * 4
  random.shuffle(cards_values)
  player_cards = [cards_values.pop(0), cards_values.pop(1)]
  dealer_cards = [cards_values.pop(0), cards_values.pop(1)]
  print(f"Ваши карты: {player_cards[0]}, {player_cards[1]}")
  
  bj_lst = [player_cards[0][1], player_cards[1][1]]
  
  player_value = sum([card[0] for card in player_cards])
  
  if player_value == 22:
      print("У Вас два туза, одному присваивается ценность 1 вместо 11")
      player_cards = [[1, "ace"], [11, "ace"]]
      player_value -= 10
      
     
  if player_value == 21 and "face" in bj_lst:
    print(f"У Вас БлэкДжек! Поздравляем! Ваш выигрыш {int(bet)*2}.")
    result = 2*bet
    return result
  
  print(f"У дилера две карты, первая из них: {dealer_cards[0]}")
  
  while player_value <= 19:    
    hitting_p = input("Будете добирать еще карту? Ответьте 'y' или 'n'")
    if hitting_p == 'n':
      print("Вы сказали нет. 'n'")
      break
    if hitting_p == 'y':
      p = cards_values.pop(0)  
      print(f"Вам выпала карта {p}")
      player_cards.append(p)
      player_value += p[0]
      print(f"У Вас теперь {player_value} очков.")
      if player_value > 21:
        print(f"Вы проиграли, перебор {player_value}, больше 21.")
        result = -bet
        return result
    else:
      print("Error. Ответьте 'y' или 'n' ")     
  print(f"Дилер вскрыл карты: {dealer_cards[0]}, {dealer_cards[1]}") 
  dealer_value = sum([card[0] for card in dealer_cards]) 
  if dealer_value == 22:
      print("У дилера два туза, одному присваивается ценность 1 вместо 11")
      dealer_cards = [[1, "ace"], [11, "ace"]]
      dealer_value -= 10
      
  while dealer_value < 17:
    a = cards_values.pop(0)
    dealer_cards.append(a)
    print(f"Дилер добрал карту, теперь у него: {dealer_cards}")
    dealer_value += a[0]
    print(f"У дилера {dealer_value} очков.")
    if dealer_value > 21:
      print(f"Вы выиграли, тк у дилера перебор. Ваш выигрыш {bet}")
      result = bet  
      return result
    
  if player_value > dealer_value:
    print(f"У Вас {player_value}, у дилера {dealer_value}. Вы выиграли! Ваша ставка: {bet}")
    result = bet
    return result
  if player_value == dealer_value:
    print("Ничья, никто не теряет деньги.") 
    result = 0
    return result
  if player_value < dealer_value:
    print(f"У Вас {player_value},у дилера {dealer_value}.Вы проиграли. -{bet}") 
    result = -bet
    return result