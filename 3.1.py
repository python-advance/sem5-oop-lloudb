# 3.1 Разработка прототипа приложения “Регистрация на конференцию” на основе фрагмента технического задания с использованием ООП.
import re 

class Person():
  logger = []
  
  def __init__(self, user):

    self.f_name = user["f_name"] 
    self.s_name = user["s_name"]
    self.birthyear = user["birthyear"] 
    self.email = user["email"] 
    self.country = user["country"]
    self.city = user["city"]   

  @property
  def birthyear(self):
      return self._birthyear
    
  @birthyear.setter
  def birthyear(self, value):
    pattern1 =  r"^[1-2][0-9][0-9][0-9]"
    prov1 = re.compile(pattern1)
    self.logger.append("Cоздан паттерн для года рождения")

    if (not (prov1.findall(str(value)))):
      raise ValueError('Неверный формат года рождения')
    else:
      self.logger.append("Год прошел проверку")
      self._birthyear = int(value)

  @birthyear.deleter
  def birthyear(self):
      print('Year delete')
      self._birthyear = None

  @property
  def email(self):
      return self._email
    
  @email.setter
  def email(self, value):
    pattern2 = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    prov2 = re.compile(pattern2)
    self.logger.append("Cоздан паттерн для email")

    if (not (prov2.findall(str(value)))):
      raise ValueError('Неверный формат email')
    else:
      self.logger.append("Email прошел проверку")
      self._email = value

  @email.deleter
  def email(self):
      print('Email delete')
      self._email = None

  def info(self):
    self.participant_info = {
      "f_name": self.f_name,
      "s_name": self.s_name,
      "email": self.email,
      "birthyear": self.birthyear,
      "country": self.country,
      "city": self.city
    }

    return self.participant_info

name = input("Введите имя:")
surName = input("Введите фамилию:")
year = input("Введите год рождения:")
mail = input("Введите почту:")
country = input("Введите страну:")
town = input("Введите город:")

new_dict={"f_name":name,"s_name":surName,"email":mail, "birthyear":year, "country":country, "city":town}

new_user=Person(new_dict)

with open('fileLog.txt', 'a') as file:
  file.write(str(new_user.logger))

with open('fileInfo.txt', 'a') as resultfile:
  resultfile.write(str(new_dict.values())+"\n")
