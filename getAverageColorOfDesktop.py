import pyautogui
from PIL import ImageStat

def getAvergeIntColorOfDesktop():
  pic = pyautogui.screenshot() # png
  rgb = ImageStat.Stat(pic)._getmean()
  return rgb2int(rgb) , rgb2brightness(rgb) # _getmedian())

def rgb2int(rgb):
  rgb = list(map(int,rgb))
  return (rgb[0] << 16) + (rgb[1] << 8) + rgb[2]

def rgb2brightness(rgb):
  return int(sum(rgb)/(3*256))

if __name__ == "__main__":
  print("XD")