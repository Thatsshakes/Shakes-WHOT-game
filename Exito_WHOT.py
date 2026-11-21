seed = id(object()) & 0xffffffff

def irand():
  global seed
  seed ^= (seed<<13)&0xffffffff
  seed ^= (seed>>17)
  seed ^= (seed<<5)&0xffffffff
  return float(seed)/((2**32)-1)

print(irand())


def shuffled(data):
    for index in range(len(items)-1, 0, -1):     #steady looper backwards
        random_pointer = int(irand() * (index+1)) 

        data[index], data[random_pointer] = data[random_pointer], data[index]

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

    print(f"Player 1 cards: {arr1}\nPlayer 2 cards: {arr2}\nMarket: {market}") 
    print("\n")

    print("==========  Starting WHOT Game  ==========")
    played_container = []
    top = market.pop(-1)
    played_container.append(top)
    print(f"Compared card: {played_container}")

    mode = input("Player 1 or Player 2: ")

    if mode == "Player 1":
        print(f"These are your cards Player 1: {arr1}")
        p1_input = int(input("Enter your desired card index from player 1 cards: "))

        played_container_number, played_container_shape = played_container[-1]

        for card_index, (arr1_card_number, arr1_card_shape) in enumerate(arr1):
            if p1_input == card_index:
                if arr1_card_number == played_container_number or arr1_card_shape == played_container_shape:
                    played_card = arr1.pop(card_index)
                    played_container.append(played_card)
                    print(f"Remaining cards for Player 1 are: {arr1}")
                    print(f"Played pile: {played_container[-1]}")
                else:
                    print("Card doesn't match! Go to market.")
                    mode = input("Type Market: ")
                    if mode == "Market":
                        arr1.append(market.pop(-1))
                        print(f"Remaining cards for Player 1 are: {arr1}")
                        print(f"Played pile: {played_container[-1]}") 
                    else:
                        print("Invalid Input, type 'Market'")
                break

        mode = input("Type 'Player 2': ")

    if mode == "Player 2":
        print(f"These are your cards Player 2: {arr2}")

        p2_input = int(input("Enter your desired card index from player 2 cards: "))

        played_container_number, played_container_shape = played_container[-1]

        for card_index, (arr2_card_number, arr2_card_shape) in enumerate(arr2):
            if p2_input == card_index:
                if arr2_card_number == played_container_number or arr2_card_shape == played_container_shape:
                    played_card = arr2.pop(card_index)
                    played_container.append(played_card)
                    print(f"Remaining cards for Player 2 are: {arr2}")
                    print(f"Played pile: {played_container[-1]}")
                else:
                    print("Card doesn't match! Go to market.")
                    market_input = input("Type Market: ")
                    if market_input == "Market":
                        arr2.append(market.pop(-1))
                        print(f"Remaining cards for Player 2 are: {arr2}")
                        print(f"Played pile: {played_container[-1]}")
                    else:
                        print("Invalid Input, type 'Market'")
                break

   #  print(f"Played pile: {played_container}")

items = [((n%7)+1, ['B', 'O', '+', '*','T'][n%5]) for n in range(20)]


print(shuffled(items))


