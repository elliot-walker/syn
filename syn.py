import sys
import base64
import os
import socket
from modules import helper as h

h.clear()
port = 9000
print(h.GREEN+h.banner_text+"\nVersion 1.0\nCreated by мишапов (@Mikhail Semenov)")
while 1 > 0:
	choice = input(h.RED+'S'+h.GREEN+'Y'+h.RED+'N'+h.YELLOW+':'+h.WHITE)

	if choice == 'help':#In helper class def help() and return all this
		print('Help Menu\n_______________________________')
		print('quit : quit out of program')
		print('clear : clear console screen')
		print('ip : get your local ip address')
		print('cp : create payload')
		print('listen: listen to a port')
	elif choice == 'ip':
		print(h.getip())
	elif choice == 'clear':
		h.clearB()
	elif choice == 'quit':
		h.clear()
		sys.exit()
	elif choice == 'listen':
		h.listen(port)
	elif choice == 'cp':
		while 1 > 0:
			try:
				port = input('Enter a port please or nothing to keep at default of 9000: ')
				if(port == ''):
					port = int(9000)
					break
				port = int(port)
			except ValueError:
				print('invalid port!')
				continue
			break
		h.createsimplepayload(port)
	elif choice == 'about':
		h.about()
	else:
		print('Invalid input')
