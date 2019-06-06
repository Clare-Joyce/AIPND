from time import time, sleep

start_time = time()
sleep(120)
end_time  = time()
tot_time = end_time - start_time
print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" +
      str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + 
      str( int(  ( (tot_time % 3600) % 60 ) ) ) ) 