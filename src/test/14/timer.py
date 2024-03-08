import sched
import time

from .tti_3 import pipe

def my_function():
    print("Bu fonksiyon her 30 saniyede bir çağrılıyor.")

def schedule_function(sc):
    my_function()
    sc.enter(30, 1, schedule_function, (sc,))

s = sched.scheduler(time.time, time.sleep)

# İlk çalıştırma
s.enter(0, 1, schedule_function, (s,))
s.run()
