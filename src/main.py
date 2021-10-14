basket = []
print ("Welcome to your shopping basket!")
while True:
  if len(basket) == 0:
    print ("Your basket is currently empty.")
  elif len(basket) == 1:
    print ("You have 1 item in your basket. Here is your basket: " + str(basket))
  else:
    print ("You have " + str(len(basket)) + " items in your basket. Here is your basket: " + str(basket))
    
  choose = input("Would you like to add/remove/swap/save any items to your basket?: ")
  if choose == "Add" or choose == "add":
    add = input("What item would you like added to your basket?: ")
    basket.append(add)
    print ("I have added " + add + " to your shopping basket.")
  elif choose == "Remove" or choose == "remove":
    while True:
      remove = input("What item would you like to remove from your basket?")
      if remove in basket:
        basket.remove(remove)
        print ("I have removed the item " + remove + " from your basket.")
        break
      else:
        print ("The item you entered does not exist in your current basket. Please try again.")
  elif choose == "Swap" or choose == "swap":
    while True:
      swap_out = input("What item do you want to swap out?: ")
      if swap_out in basket:
        swap_in = input ("What item do you want to swap in?: ")
        place = basket.index(swap_out)
        basket[place] = swap_in
        print ("I have swapped " + swap_out + " for " + swap_in + ".")
        break
      else:
        print ("The item you entered does not exist in your current basket. Please try again.")
  elif choose == "Save" or choose == "save":
    print ("I have saved your basket.")
    break
  else:
    print ("I did not understand what you told me. Please try again.")
    
print ("Thank you for shopping with us today! Here is your checkout basket: " +str(basket))
  
  
    
  

  
    
  
  

