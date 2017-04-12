import os
import sys
from random import randint
with open('users.txt') as f:
	for line in f:
		print("INSERT INTO `customer` (`CEmail`, `Age`, `CPassword`) VALUES ('{}', {}, 'password')".format(f.readline().strip()+"@gmail.com", randint(12, 50)))
        