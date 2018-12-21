2.1 Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).
2.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.
2.3. Формирование отчета по практическому заданию и публикация его в портфолио.

# Разработка класса "запись" 
class Record():
  def __init__(self, author, title):
    self.__title = title
    self.__author = author

  def show_comment(self, comment=object):
    print(f"Заголовок коммента: {comment.title}, текст коммента: {comment.text}")

# Разработка класса "комментарий" 
class Comment():
  def __init__(self, title, text):
    self.__title = title
    self.__text = text

# Создание геттеров и сеттеров для классов «запись», «комментарий» поля title
  @property
  def title(self):
    return self.__title
    
  @title.setter
  def title(self, value):
    self.__title = str(value)

  @title.deleter
  def title(self):
    self.__title = None

# Создание геттеров и сеттеров для классов «запись», «комментарий» поля text 
  @property
  def text(self):
    return self.__text
    
  @text.setter
  def text(self, value):
    self.__text = str(value)

  @text.deleter
  def text(self):
    self.__text = None
  
# Функция для вывода на печать информации, хранящийся в объектах.
  def show(self):      
    print("author: " + str(self.author))
    print("title: " + str(self._title))


# Создание объектов класса
myR1 = Record('Andreeva', 'First record')
myC1 = Comment('First comm', 'wow!')
myR1.show_comment(comment=myC1)
