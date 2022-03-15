import datetime
from colorama import Fore
now = datetime.datetime.now()
def main():
  print(Fore.BLUE+now.strftime("%Y-%m-%d %H:%M:%S"))
