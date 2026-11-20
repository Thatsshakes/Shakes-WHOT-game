seed = id(object()) & 0xffffffff

def irand():
  global seed
  seed ^= (seed<<13)&0xffffffff
  seed ^= (seed>>17)
  seed ^= (seed<<5)&0xffffffff
  return float(seed)/((2**32)-1)

print(irand())


def shuffle(data):
    for index in range(len(data) - 1, 0, -1):
      j = int(irand() * (index+1)) 

      data[index], data[j] = data[j], data[index]

    arr1 = []
    arr2 = []
    market = []

    mid = len(items)//2
    quarter = len(items)//4

    for result_index in range(len(items)):
       if result_index < quarter:
          arr1.append(data[result_index])
       elif result_index < mid:
          arr2.append(data[result_index])
       else:
          market.append(data[result_index])

    played_container = []

    print(f"Player1 cards: {arr1}\nPlayer2 cards: {arr2}\nMarket: {market}")
    print("=" * 65)
    print("\n")


    print("==========  Start WHOT Game  ==========")
    
def take_turn(player_name, player_cards, played_container, market):
    
   #  for arr1_items, arr2_items in zip(arr1, arr2):
   #     mode = input("Enter your mode: Player1 turn or Player2 turn: ")

   #     if mode == "Player1 turn":
   #      p1 = int(input(f"Player 1 (your card is {arr1_items}), Enter your card number: "))
   #      played_container.append(p1)

   #      mode == "Player2 turn"

   #     if mode == "Player2 turn":
   #      p2 = int(input(f"Player 2 (your card is {arr2_items}), Enter your card number: "))
   #      played_container.append(p2)


   #      if p1 != p2:
   #        played_container.pop()  
   #        if len(market) > 0:
   #           market.pop()
   # 


   top_card = played_container[-1]
   print(f"\n--- {player_name} Turn ---")
   print("Card to match:", top_card)


   for idx, card in enumerate(player_cards):
    print(f"{idx}: {card}")

   choice = input(f"{player_name}, Enter card index (or 'm' for market): ")

   if choice == 'm':
      if len(market) > 0:
         player_cards.append(market.pop())
         print("Drew a card from market.")
   else:
      card_idx = int(choice)
      chosen_card = player_cards[card_idx]


      #Match number (index 0) OR shape (index 1)
      if chosen_card[0] == top_card[0] or chosen_card[1] == top_card[1]:
         played_container.append(player_cards.pop(card_idx))
         print(f"{player_name} played {chosen_card}")
      else:
         print("No match! Drawing 1 card from market.")
         if len(market) > 0:
            player_cards.append(market.pop())

    
       

items = [((n%7)+1, ['B', 'O', '+', '*','T'][n%5]) for n in range(20)]


print(shuffle(items))


