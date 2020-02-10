import glob
import os

github_path = 'https://raw.githubusercontent.com/kamyu1201/useful-slack-emoji/master/common/'
file_path = os.path.abspath(__file__ + '/../common/*')

print(file_path)

files = glob.glob(file_path)
for f in files:
  filename = os.path.split(f)[1]
  print('!['+filename+']('+github_path+filename+')')




