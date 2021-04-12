#!/bin/python


#import module yang di butuhkan
import os
import random
import sys
import time
import getpass
from time import sleep
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.4)


print ('loading..')
sleep(0.1)
mengetik('> > > > > > > > > > > > > > >] 100%')
def lagi():
    f = raw_input(" Do you Want To Continued [y/n]: ")
    if f == "y":
       os.system("python2 belajar.py")
    elif n == "n":
         sys.exit()

def menu():
    os.system("clear")
    os.system("figlet               Welcome ")
    print "                     \033[1;91mAUTHOR \033[1;97m: \033[1;94mARSKUY "
    print "                 ----------------------"
    print "                   \033[1;97m[\033[1;91m!\033[1;97m] \033[1;95mPRIVASI TOOLS "
    print
    print "\033[1;97m1). \033[1;93mSpam Wa "
    print "\033[1;97m2). \033[1;94mBaca Alquran \033[1;97m(\033[1;93mSpecial Ramadhan\033[1;97m)"
    print "\033[1;97m3). \033[1;96mCara Pakai Tools Ini"
    print "\033[1;97m4). \033[1;92mSpam Sms"
    print "\033[1;97m5). install metasploit"
    print "\033[1;97m6). \033[1;94mSpam All"
    print "\033[1;97m7). \033[1;96mStabilkan Jaringan"
    print "\033[1;97m0). \033[1;91mexit\033[1;93m/\033[1;91mkeluar\033[1;97m"
    pilih = raw_input("pilih slur ==> ")
    # out put
    if pilih =="1":
        os.system("clear")
        print ('loading')
        mengetik ('> > > > > > > > > > > > > >] 100%')
        print ('installing data')
        os.system("figlet proses")
        os.system("pkg install git")
        os.system("git clone https://github.com/Sxp-ID/Brutal-Wa")

    elif pilih =="2":
        os.system('clear')
        print ('loading..')
        mengetik('> > > > > > > > > > > > > > >] 100%')
        os.system("figlet Ayo Baca")
        os.system("pip install bs4")
        os.system("git clone https://github.com/hekelpro/Al-Quran")
    elif pilih =="3":
        os.system('clear')
        print ('loading..')
        mengetik('> > > > > > > > > > > > > > >] 100%')
        os.system("figlet fahami")
    elif pilih =="4":
        os.system("clear")
        print ('loading..')
        mengetik('> > > > > > > > > > > > > > >] 100%')
        os.system("git clone https://github.com/ziyanfranz/spamcall")
    elif pilih =="5":
        os.system("clear")
        print ('loading..')
        mengetik('> > > > > > > > > > > > > > >] 100%')
        os.system("pkg install wget")
        os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
        os.system("chmod +x metasploit.sh")
        os.system("./metasploit.sh")
    elif pilih =="6":
        os.system("clear")
        print ('loading..')
        mengetik('> > > > > > > > > > > > > > >] 100%')
        os.system("git clone https://github.com/Sxp-ID/Brutal-SCW")
    elif pilih =="7":
        os.system("clear")
        print ('loading..')
        mengetik('> > > > > > > > > > > > > > >] 100%')
        os.system("figlet stabil Jaringan")
        os.system("ping -s 1000 8.8.8.8")
    elif pilih =="0":
        sys.exit()

menu()
