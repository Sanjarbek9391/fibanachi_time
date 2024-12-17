from turtledemo.penrose import start

import time
a=list(range(1,100000))
start_time = time.time()
for i in a:
    pass
end_time=time.time()
n=end_time-start_time
print("n=",n)
    