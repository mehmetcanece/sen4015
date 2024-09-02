import threading

def display(msg):
  for i in range(5):
    print(msg)

t1 = threading.Thread(target=display,args=("Mehmetcan",))
t2 = threading.Thread(target=display,args=("Ece",))

t1.start()

t2.start()

t1.join()

t2.join()

print("Done!")


# output rastgele şekilde 5 tane mehmetcan 5 tane ece çıktısı çıkarır, en son ise Done! yazar.