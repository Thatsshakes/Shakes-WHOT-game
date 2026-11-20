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


    for arr1_items, arr2_items in zip(arr1, arr2):
       mode = input("Enter your mode: Player1 turn or Player2 turn: ")

       if mode == "Player1 turn":
        p1 = int(input(f"Player 1 (your card is {arr1_items}), Enter your card number: "))
        played_container.append(p1)

        mode == "Player2 turn"

       if mode == "Player2 turn":
        p2 = int(input(f"Player 2 (your card is {arr2_items}), Enter your card number: "))
        played_container.append(p2)


        if p1 != p2:
          played_container.pop()  
          if len(market) > 0:
             market.pop()        

    return played_container
       

items = [((n%7)+1, ['B', 'O', '+', '*','T'][n%5]) for n in range(20)]


print(shuffle(items))


