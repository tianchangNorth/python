import requests
url = "https://vcs.zijieapi.com/vc/setting?aid=2608&repoId=56081"
count = 0

def main():
  global count 
  r = requests.post(url)
  print(r.text)
  count += 1

if __name__ == "__main__":
  main()