import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))
  print('デバッグ:mistake_number = ' + str(4))

def view_question():
  choice_data = random.randint(0, 2)
  question = data[choice_data]
  print(question)
  i = 0
  j = 0
  k=0
  mistake_number=random.randint(0, 8)
  while i < 3:
    question_str = ''
    while j < 3:
      if k==mistake_number:
        question_str+=question[1]
      else:
        question_str += question[0]
      j += 1
      k+=1
    print(question_str)
    i += 1
    j = 0

def play():
  section_message()
  view_question()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)

start_message()
play()