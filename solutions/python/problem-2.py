class Solution:
  def main(self):
    user_name = self.get_user_name()

    print(f"Hello, {user_name}!")
  
  def get_user_name(self):
    user_name = input("Enter your name: ")

    return user_name