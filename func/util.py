import random
import string
class Utils:
  def __init__(self):
    pass
  
  def generate_random_string(self,length):
      letters = string.ascii_letters
      return ''.join(random.choice(letters) for i in range(length))
