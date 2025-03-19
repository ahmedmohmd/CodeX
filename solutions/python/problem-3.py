class Solution:
  def main(self):
    user_input = self.read_number()

    if self.is_odd(user_input):
      print(f"{user_input} is odd.")
    else:
      print(f"{user_input} is even.")

  def is_odd(self, number):
    return number % 2 != 0

  def is_even(self, number):
    return number % 2 == 0
  
  def read_number(self):
    user_input = input("Enter a number: ")

    if not user_input.isdigit():
      print("Invalid input. Please enter a valid number.")
      return self.read_number()

    return int(user_input)
  