import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
change={'A':1,'B':2,'C':3}
level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))

def view_question():
  choice_data = random.randint(0, 2)
  mistake_number = random.randint(0, 8)
  print('デバッグ:mistake_number = ' + str(mistake_number))
  question = data[choice_data]
  print(question)
  i = 0
  j = 0
  print('／｜A B C')
  print('ーーーーー')
  while i < 3:
    question_str = str(i + 1) + '｜'
    while j < 3:
      if (i * 3 + j) == mistake_number:
        question_str += question[1]
      else:
        question_str += question[0]
      j += 1
    print(question_str)
    i += 1
    j = 0

def change_input_number(input_str):
  change_alphabet=change[input_str[0]]
  change_number=int(change[input_str[1]])
  return change_alphabet+change_number
def play():
  section_message()
  view_question()
  choice = input('(例:A1)')
  input_number=change_input_number(choice)
  print('デバッグ:choice = ' + choice)
  print('デバッグ:input_number = ' + input_number)
  
start_message()
play()