# testing
from sys import stdout
from time import sleep

word =''
for i in [i for i in 'hello world!']:
	word += i
	stdout.write(word)
	stdout.flush()
	sleep(0.5)
	stdout.write('\r')