import requests

def Is_Yankees_Site_online(url):
  try:
    datas = requests.get(url)
    datas.raise_for_status
  except requests.exceptions.HTTPError as err:
    print(err)
  return datas.status_code


def PRINT_MY_NAME_NOOB(name):
  print('Hi, %s.' % name)

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

  if Is_Yankees_Site_online('https://www.mlb.com/yankees') == 200:
    print("Yea yankees site is online")


if __name__ == '__main__':
  main()

  