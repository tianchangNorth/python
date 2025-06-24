import requests
url = "https://openatom.atomgit.com/explore/journalism/detail/459723510017822720"
count = 0

def main():
  global count 
  r = requests.post(url)
  print(count)
  count += 1

while True:
  main()