import requests
import pirate_nintendo_roms
from yes_or_no import yes_or_no

def Is_Yankees_Site_online(url):
  try:
    datas = requests.get(url)
    datas.raise_for_status
  except requests.exceptions.HTTPError as err:
    print(err)
  return datas.status_code


def PRINT_MY_NAME_NOOB(name):
  #print('Hi, %s.' % name)

  # fstrings are better in 2022 than what?
  # Better than % .format() style strings(See
  ## other print statement)
  #better than green eggs and ham
  #click on the little purple chat icon on the bottom right
  #looks like we can edit code at the same Time
  
  print(f"Hi, {name}.")

def main():
  name = input('What is your name?\n')
  PRINT_MY_NAME_NOOB(name)

  # using + will result in undefined behavior
  # better off with an fString aka print(f"text {var}")
  # Especially sus in python 3
  #open the chat
  #I updated it
  #Ok, im actually going to go find socks and go outside now
  if Is_Yankees_Site_online('https://www.mlb.com/yankees') == 200:
    print(f"Yea {name}, the yankees site is online")

  if yes_or_no(f'Hey {name}, do you wanna pirate some roms?'):
    print('yarrr, here be links')
    for link in pirate_nintendo_roms.parse_rom_urls():
      print(link)
  else:
    print('nay? shiver me timbers are you the FBI?')

if __name__ == '__main__':
  main()  