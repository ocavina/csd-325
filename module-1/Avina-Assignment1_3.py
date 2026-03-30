# Oscar Avina
# 03/29/2026
# Module 1.3 Assignment
# This program counts down bottles of beer on the wall using a while loop function.

def bottles_of_beer_countdown(num_of_bottles):
  while num_of_bottles > 1: # while loop will continue the countdown until there is only 1 bottle left.
    print(f"{num_of_bottles} bottles of beer on the wall, {num_of_bottles} bottles of beer.")
    num_of_bottles -= 1 # decreases the number of bottles by 1 for each iteration of the loop.
    if num_of_bottles == 1: # if statement to check when there is only 1 bottle left to manually change the wording
      print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
    else:
      print(f"Take one down and pass it around, {num_of_bottles} bottles of beer on the wall.\n")
  # when there is only 1 bottle left, the while loop will end and the following lines will be printed to complete the song.
  print("1 bottle of beer on the wall, 1 bottle of beer.")
  print("Take one down and pass it around, 0 bottles of beer on the wall.\n")
  print("Time to buy more bottles of beer.")

def main(): # main function that gets user input to start the countdown.
  user_input = int(input("Enter the number of bottles of beer on the wall: "))
  while user_input < 1: # while loop to check if the user input is valid
    print("Please enter a number greater than 0.")
    user_input = int(input("Enter the number of bottles of beer on the wall: "))
  bottles_of_beer_countdown(user_input)

if __name__ == "__main__":
  main()