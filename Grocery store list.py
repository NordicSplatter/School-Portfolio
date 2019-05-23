grocery_history = []
#controls loop
stop = 'go'

while stop !='q':
  
  grocery_item = {}
  #collects user input
  item_name = input('Item name:\n')    
  quantity = input('Quantity purchased:\n')
  cost = input('Price per item:\n')  
 
  grocery_item['name'] = (item_name)
  grocery_item['number'] = int(quantity)
  grocery_item['price'] = float(cost)
  
   #adds the input items into the dictionary
  grocery_history.append(grocery_item)
  
  #asks user if they would like to continue  
  stop = input("Would you like to enter another item?\n Type 'c' for continue or 'q' to quit:\n")


grand_total = 0

 #loop
for i in grocery_history:
  
  
  item_total = i['number'] * i['price']
  
  grand_total = item_total + grand_total
  
  print(str(i['number']) + ' ' + i['name'] + '@ $' + str(i['price']) + 'ea $' + str(item_total))
  
  
 
item_total = 0
#prints the final product total
print('\n')
print('Grand Total: $%.2f\n' %(grand_total))
