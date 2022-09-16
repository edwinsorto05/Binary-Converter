#Procedure 1 - Decimal to Binary
def dec_to_bin(choice):
  value = 0 #sets to 0
  place_value_list = [1] #sets to list with 1
  binary_num_list = [] #sets to empty list
  print("Enter a decimal number.") #asks user for a decimal number
  decimal_num = int(input()) #user int. input is stored
  decimal_num_2 = decimal_num #second variable decimal_num_2 will equal decimal_num
  x = 0 # sets to zero
  place_value = 0 #sets to zero
            
  while place_value < decimal_num: #does everything underneath while place_value is less than decimal_num
    x = x + 1 #x equals itself plus 1
    place_value = 2 ** x #place_balue equals 2 to the power of the value of x
    if place_value <= decimal_num: #if place_value is less than or equal to decimal_num
      place_value_list.append(place_value) #appends place_value to place_value list
  place_value_list.reverse() #reverses place_value list
  for value in range(len(place_value_list)): #for value in range of length of place_value_list
    if place_value_list[value] <= decimal_num_2: #if value of element of value is less than or equal to decimal_num_2
      binary_num_list.append('1') #appends '1' to binary_num_list
      decimal_num_2 = decimal_num_2 - place_value_list[value] #decimal_num_2 equals itself subtracted by the value of element of value in place_value_list
      value = value + 1 #value equals itself plus 1
    else: #if place_value[value] isn't less than or equal to decimal_2
      binary_num_list.append('0') #appends '0' to binary_num_list
      value = value + 1 #value equals itself plus 1

  binary_num = "".join(binary_num_list) #binary_num equals binary_num_list elements joined by ""
  print()
  print('(', decimal_num, "=", binary_num, ')') #prints decimal_num from user and binary number it equals

#Procedure 2 - Binary to Decimal
def bin_to_dec(choice):
  value = 0 #sets to 0
  place_value_list = [1] #sets to list with 1
  decimal_num_list = [] #sets to empty list
  print("Enter a binary number.") #asks user to enter a binary number
  binary_num = str(input()) #stores user input
  binary_num_2 = ''.join(reversed(binary_num)) #equals binary_num reversed and joined by ''
  bit = 0 #sets to 0
  index = 0 #sets to 0
  x = 0 #sets to 0
  place_value = 0 #sets to 0
  while index <= len(binary_num_2): #while value of index is less than or equal to length of binary_num_2
    x = x + 1 #x equals itself plus
    place_value = 2 ** x #equals 2 to the power of x
    place_value_list.append(place_value) #appends place_value to place_value_list
    index = index + 1 #index equals itself plus 1
  for bit in range(len(binary_num_2)): #for bit in range of length of binary_num_2
    if binary_num_2[bit] == '1': #if value of element of bit in binary_num_2 equals '1'
      decimal_num_list.append(place_value_list[bit]) #appends place_value_list[bit] to decimal_num_list
    bit = bit + 1 #bit equals itself plus 1
  decimal_num = sum(decimal_num_list) #equals total sum of decimal_num_list
  print()
  print('(', binary_num, '=', decimal_num, ')') #prints binary number from user and decimal number it equals

#Procedure 3 - Compare Binary Numbers
def comp_bin(choice):
  value = 0 #sets to 0
  place_value_list = [1] #sets to list with 1
  decimal_num = [0, 0] #sets to list with 0 and 0
  decimal_num_list = [] #sets to empty list
  binary_num_list = [0, 0] #sets to list with 0 and 0
  binary_num_list_2 = [0, 0] #sets to list with 0 and 0
  binary_order_list = [] #sets to empty list
  binary_comp_list = [] #sets to empty list

  print("Enter a binary number.") #asks user to enter a binary number
  binary_num_list[0] = str(input()) #element 0 of binary_num_list equals user input
  print("Enter another binary number.") #asks user to enter anothery binary number
  binary_num_list[1] = str(input()) #stores user input into element 1
  binary_num_list_2[0] = ''.join(reversed(binary_num_list[0])) #equals element 0 of binary_num_list reversed and joined by ''
  binary_num_list_2[1] = ''.join(reversed(binary_num_list[1])) #equals element 1 of binary_num_list reveresed and joined by ''
  num = 0 #sets to 0
  for num in range(len(binary_num_list_2)): #for number in range in range of length of binary_num_list_2
    #Sets values below to 0
    bit = 0
    index = 0
    x = 0
    place_value = 0
    while index < len(binary_num_list[num]) - 1: #while index is less than length of element of num in binary_num_list subtracted by 1
      x = x + 1 #x equals itself plus 1
      place_value = 2 ** x #equals 2 to the power of x
      place_value_list.append(place_value) #appends place_value to place_value_list
      index = index + 1 #index equals itself plus 1
    for bit in range(len(binary_num_list_2[num])): #for bit in range of length of element num of binary_num_list
      if binary_num_list_2[num][bit] == '1': #if sublist num and bit of binary_num_list_2 equals 1
        decimal_num_list.append(place_value_list[bit]) #appends element of bit in place_value_list to decimal_num_list
      bit = bit + 1 #bit equals itself plus 1
    decimal_num[num] = sum(decimal_num_list) #element of num in decimal_num equals the sum of decimal_num_list
    decimal_num_list = [] #sets to empty list
    num = num + 1 #num equals itself plus 1
  print()      
  print('(', decimal_num[0], ',', decimal_num[1], ')') #prints element 0 of decimal_num and element 1 of decimal_num
  if decimal_num[0] < decimal_num[1]: #if element 0 of decimal_num is less than element 1 of decimal_num
    #Prints elements 0 and 1 of binary_num_list to binary_comp_list and prints them
    binary_comp_list.append(binary_num_list[0]) 
    binary_comp_list.append(binary_num_list[1])
    print('(', binary_comp_list[0], ',', binary_comp_list[1], ')')
  else:#if decimal_num[0] isn't less than decimal_num[1]
    #appends elements 1 and 0 of binary_num_list to binary_order_list
    binary_order_list.append(binary_num_list[1])
    binary_order_list.append(binary_num_list[0])
  if decimal_num[0] > decimal_num[1]: #if element 0 of decimal_num is greater than element 1 of decimal_num
    print('(', binary_order_list[0], ',', binary_order_list[1], ')') #prints element 0 and 1 of binary_order_list

#Asks user to enter 1, 2, or 3
print('Choose an action:')
print('Press 1 to convert decimal to binary.')
print('Press 2 to convert binary to decimal.')
print('Press 3 to compare binary numbers.')
answer = str(input()) #stores user input
value = 0

#Convert Decimal to Binary
if answer == '1':
  dec_to_bin(answer)
#Convert Binary to Decimal
elif answer == '2':
  bin_to_dec(answer)
#Compare Binary Numbers
elif answer == '3':
  comp_bin(answer)
else:
  #tells user to restart program if they input anything other than '1', '2', or '3'
  print('That is not an option. Please restart program.')