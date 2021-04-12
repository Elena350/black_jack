import random
def play():
  bet = int(input("Please make your bet"))
  cards_values = [[2, "two"], [3, "three"], [4, "four"], [5, "five"], [6, "six"], [7, "seven"], [8, "eight"], [9, "nine"], [10, "ten"], [10, "face"], [10, "face"], [10, "face"], [11, "ace"]] * 4
  random.shuffle(cards_values)
  player_cards = [cards_values.pop(0), cards_values.pop(1)]
  dealer_cards = [cards_values.pop(0), cards_values.pop(1)]
  print(f"Your cards: {player_cards[0]}, {player_cards[1]}")
  
  bj_lst = [player_cards[0][1], player_cards[1][1]]
  
  player_value = sum([card[0] for card in player_cards])
  
  if player_value == 22:
      print("You've got two aces, one gets a value of 1 instead of 11")
      player_cards = [[1, "ace"], [11, "ace"]]
      player_value -= 10
      
     
  if player_value == 21 and "face" in bj_lst:
    print(f"You've got BlackJack! Congratulations! Your gain is {int(bet)*2}.")
    result = 2*bet
    return result
  
  print(f"Dealer has got two cards, one of them: {dealer_cards[0]}")
  
  while player_value <= 19:    
    hitting_p = input("Will you pick up a card? Click 'space' for yes or 'n' for no")
    if hitting_p == 'n':
      print("You said No")
      break
    if hitting_p == ' ':
      p = cards_values.pop(0)  
      print(f"You've got a card {p}")
      player_cards.append(p)
      player_value += p[0]
      print(f"You have now {player_value} value.")
      if player_value > 21:
        print(f"You loose {player_value}, is more than 21.")
        result = -bet
        return result
    else:
      print("Error. Print space for 'yes' or 'n' for 'no'")     
  print(f"Dealer opened the cards: {dealer_cards[0]}, {dealer_cards[1]}") 
  dealer_value = sum([card[0] for card in dealer_cards]) 
  if dealer_value == 22:
      print("Dealer has got two aces, one gets a value of 1 instead of 11")
      dealer_cards = [[1, "ace"], [11, "ace"]]
      dealer_value -= 10
      
  while dealer_value < 17:
    a = cards_values.pop(0)
    dealer_cards.append(a)
    print(f"Dealer picked up a card, he has now: {dealer_cards}")
    dealer_value += a[0]
    print(f"Dealer has {dealer_value} value.")
    if dealer_value > 21:
      print(f"You win because dealer busts. Your gain {bet}")
      result = bet  
      return result
    
  if player_value > dealer_value:
    print(f"You have {player_value}, dealer has {dealer_value}. You win! Your bet: {bet}")
    result = bet
    return result
  if player_value == dealer_value:
    print("It's a draw. No one looses money") 
    result = 0
    return result
  if player_value < dealer_value:
    print(f"You have {player_value},dealer has {dealer_value}.You loose. -{bet}") 
    result = -bet
    return result