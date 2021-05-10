import os, sys
h=os.listdir()
print(h)
path='C:/Users/amazon/Desktop/Trabajo'
z=os.mkdir(path)
print('A new directory was created')
os.rmdir(path)
print('Remove success.')
user=os.getlogin()
print(user)