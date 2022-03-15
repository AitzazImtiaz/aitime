import datetime
import colorama
now = datetime.datetime.now()
def main():
  print(Fore.BLUE+now.strftime("%Y-%m-%d %H:%M:%S"))
