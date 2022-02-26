import random
from re import A

data = [['見','貝'], ['土','士'], ['眠','眼']]
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
  return mistake_number

def change_input_number(input_str):
  str_data = { 'A':0, 'B':1, 'C':2 }
  input_str_split = list(input_str)
  col_number = str_data[input_str_split[0]]
  row_number = int(input_str_split[1]) - 1
  input_number = row_number * 3 + col_number
  return input_number

def is_correct_number(mistake_number, input_number):
  if mistake_number == input_number:
    return True
  else:
    return False

def change_string(number):
  a=number//3
  b=number%3

  if a==0:
    number_a=1
  elif a==1:
    number_a=2
  else:
    number_a=3

  if b==0:
    number_b='A'
  elif b==1:
    number_b='B'

  else:
    number_b='C'
  
  print(number_b+str(number_a))


def view_result(is_correct,mistake_number):
  if is_correct:
    print('正解！')
  else:
    print('不正解')
    change_string(mistake_number)

def play():
  section_message()
  mistake_number = view_question()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)
  input_number = change_input_number(choice)
  print('デバッグ:input_number = ' + str(input_number))
  is_correct = is_correct_number(mistake_number, input_number)
  view_result(is_correct,mistake_number)

start_message()
play()