def main():
  
  #set this to any double
  doubleValue = 10.5
  
  #set this to any int
  intValue = 20
  
  #print out addition, subtraction, multiplication, and division of these two values
  print (doubleValue- intValue)
  print(doubleValue + intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)

  
  #populate this list
  myFriends = ["Nick", "Sebastian", "Alex", "Chalupa Arca", "Paul", "Noah", "Justin", "Kate"]
  
  #print out your friends at index 2 and index 3
  print (myFriends[2])
  print (myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [21,22,18,23,17]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0] - fiveNumbers[2])
  print(fiveNumbers[1] + fiveNumbers[3])
  print(fiveNumbers[4] * fiveNumbers[2])
  print(fiveNumbers[1] / fiveNumbers[4])

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[1]=35
  fiveNumbers[0] = 19
  #print out the list
  print(fiveNumbers)
  
main()
