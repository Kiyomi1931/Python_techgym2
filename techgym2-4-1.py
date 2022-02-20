import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))

def view_question():
  choice_data = random.randint(0, 2)
  question = data[choice_data]

  count_a=0
  count_b=1
  question_copy=''
  while count_a==3:
    print(question_copy)
    count_v+=1
    while count_b==3:
      question_copy+=question[1]
      count_b+=1

def play():
  section_message()
  view_question()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)

start_message()
play()