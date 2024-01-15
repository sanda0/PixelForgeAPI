from PIL import Image
from .util import Utils

class Resize:
  def __init__(self, img, w, h):
    self.img = img
    self.w = w
    self.h = h
    
  def execute(self):
    image = Image.open('images/'+self.img)
    util = Utils()
    new_img = image.resize((self.w, self.h))
    new_image_name = util.generate_random_string(8)+self.img
    new_img.save('output/'+new_image_name)
    return new_image_name
    
    
    
    
    