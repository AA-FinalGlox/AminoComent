import amino
import os
import time
import getpass
os.system("clear")
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;93m"
none = "\033[0m"
color2="\033[1;36m"
print(" ")
print(' ')
print(red+' _____   _____       ___  ___   _____   __   _   _____  ')
print(red+'/  ___| /  _  \     /   |/   | | ____| |  \ | | |_   _| ')
print(red+'| |     | | | |    / /|   /| | | |__   |   \| |   | |   ')
print(red+'| |     | | | |   / / |__/ | | |  __|  | |\   |   | |   ')
print(red+'| |___  | |_| |  / /       | | | |___  | | \  |   | |   ')
print(red+'\_____| \_____/ /_/        |_| |_____| |_|  \_|   |_|   ')
print(' ')
print(green+' _____   _____   _____  ')
print(green+'|  _  \ /  _  \ |_   _| ')
print(green+'| |_| | | | | |   | |   ')
print(green+'|  _  { | | | |   | |   ')
print(green+'| |_| | | |_| |   | |   ')
print(green+'|_____/ \_____/   |_|                '+color2+"by: AA-Glox")
print(' ')
print(' ')
def Tass2(data):
	listusers=[]
	for userId ,status in zip(data.userId,data.status):
		if status !=9 and status !=10:
			listusers.append(userId)
def Tass(data):
	listusers=[]
	for userId ,status in zip(data.profile.userId,data.profile.status):
		if status !=9 and status !=10:
			listusers.append(userId)
client=amino.Client()
zero=False
while zero==False:
    try:
        e=input(yellow+"your email : "+none)
        a=getpass.getpass(yellow+"password : "+none)
        client.login(email=e,password=a)
        zero=True
    except:
    	zero=False
    	print(yellow+'verify email or password'+none)
    	one=input(yellow+'continue?'+green+' y/n : '+none)
    	if one=="N" or one=="n" or one=="no":
    		os._exit(1)
zero=False
infoos = input (yellow+"your profile Link : "+none)
infoo=amino.Client().get_from_code(infoos)
chatId=infoo.objectId
comId=infoo.path[1:infoo.path.index("/")]

print(" ")
print(yellow+'—'*30)
print(yellow+"Choose number..")
print("—"*30)
print(yellow+"1 - online memebers")
print(yellow+"2 - New members")
q=input(yellow+"===> ")


subclient = amino.SubClient(comId=comId, profile=client.profile)

size = input(green+'Maximum? : '+none)
o = input(green+'comment : '+none)

if q==1:
        oldComments = []
        listusers = subclient.    get_online_users(start=0,size=size)
        for nickname, id in zip(listusers.        profile.nickname,     listusers.    profile.userId):
            wallComments = subclient.        get_wall_comments(str(id), sorting='top').content

        if o not in wallComments:
            oldComments.append(listusers)
            subclient.comment(o,userId=id)
            print(green+"Commented on",none+nickname,id)

if q==2:
        oldComments = []
        listusers = subclient.    get_all_users(start=0,size=size)
        for nickname, id in zip(listusers.        profile.nickname,     listusers.    profile.userId):
            wallComments = subclient.        get_wall_comments(str(id), sorting='top').content

        if o not in wallComments:
            oldComments.append(listusers)
            subclient.comment(o,userId=id)
            print(green+"Commented on",none+nickname,id)