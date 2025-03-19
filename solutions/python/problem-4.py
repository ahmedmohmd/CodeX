class Solution:
  max_age = 21
  
  def main(self):
    user_age = self.read_number()
    has_license = self.read_license()

    if(user_age >= Solution.max_age and has_license):
      print("Hired")
    else:
      print("Rejected!")

  def read_number(self):
    user_input = input("Enter your Age: ")

    if not user_input.isdigit():
      print("Invalid input. Please enter a valid age.")
      return self.read_number()

    return int(user_input)
  
  def read_license(self):
    has_license_answers = ["yes", "y"]
    not_has_license_answers = ["no", "n"]

    user_input = input("Do you have a driver license? (yes/no): ")

    if(user_input.lower() in has_license_answers):
      return True
    elif (user_input.lower() in not_has_license_answers):
      return False
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")
      return self.read_license()
