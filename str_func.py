
def sts_titles(st):
    """Функция для преоброзования каждой буквы в слове с заглавной буквы"""
    print(st.upper())

sts_titles("hey")


def word_titles(st):
   """Функция для преоброзования каждого слова с заглавной буквы"""
   s = st
   s = s.title()
   print(s)

word_titles('hello world')
