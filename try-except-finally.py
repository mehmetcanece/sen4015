""" try except finally bloğu ile tryın içindekileri deniyorsun, errorların name ine göre except diyip bu olursa bunu yap gibi komut veriyorsun. finally konulmak zorunda değil ama koyarsan en sona koyuyorsun!! """

try:
  number1 = int(input("a/b for a: "))
  number2 = int(input("a/b for b: "))

  result = number1 / number2
  print(result)
except ZeroDivisionError:
  print("You can not divide to zero!")
except ValueError:
  print("You have to give numbers")
finally:
  print("aa")

