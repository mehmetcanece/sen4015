from threading import *
import time

def eat_breakfast():
  time.sleep(3) 
  print("you eat breakfast")


def drink_coffe():
  time.sleep(4)
  print("you drinked coffe")

def study():
  time.sleep(5)
  print("you finished studying")

x=Thread(target=eat_breakfast, args=())
x.start()
y=Thread(target=drink_coffe, args=())
y.start()
z=Thread(target=study, args=())
z.start()

x.join()
y.join() #bunu yapınca main threadin içine giriyor ve sadece 1 threadde çalışıp bitiriyor
z.join()

"""
eat_breakfast()
drink_coffe() böyle yaptiginda hepsi tek tek sırayla oluyor ama sen gidip start ve join kullanırsan aynı anda oluyorlar biri digerini beklemiyor.
study() """



print(active_count())
print(enumerate)
print(time.perf_counter())

print("executing thread name : " , current_thread().getName())