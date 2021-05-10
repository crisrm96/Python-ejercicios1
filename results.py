import os
for i in range(2,256):
    for n in range (2,256):
        y = (n % i)
        if y != 0:
            result= open("/AWSPy/results.txt","w")
            result.write(y)
            result.close()
            break
