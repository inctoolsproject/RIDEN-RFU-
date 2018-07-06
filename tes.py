from GENERATOR import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("WELCOME TO RFU SEKAWAN\n\n")

#cl = RIDEN()
cl = RIDEN(authTokenRFU="EupBoQXqFuwMd3HSCoM4.1EmqU+/dVpG0MFQ7n3YXHa.l2ePvhfUlo+vMwnBH37S83USbbhujOcHZ+xijfynr2A=")
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = RIDENChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
#cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

print ("LOGIN SUCCESS RFU")

clProfile = cl.getProfile()
clSettings = cl.getSettings()
RIDEN = RIDENPoll(cl)

Rfu = [cl]
mid = cl.profile.mid
RfuBot=[mid]

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RIDEN_FAST_USER(fast):
    global time
    global ast
    global groupParam
    try:
        if fast.type == 0:
            return

        if fast.type == 25:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
              if msg.contentType == 0:
                if rfuText is None:
                    return
                else:               
                    if rfuText.lower() == 'PROSES TRANSISI':
                        cl.sendMessage(0, user)

                    elif 'profile ' in rfuText.lower():
                        try:
                            key = eval(msg.contentMetadata["MENTION"])
                            u = key["MENTIONEES"][0]["M"]
                            cname = cl.getContact(u).displayName
                            cmid = cl.getContact(u).mid
                            cstatus = cl.getContact(u).statusMessage
                            cpic = cl.getContact(u).picturePath
                            a = cl.getProfileCoverURL(mid=u)
                            cl.sendText(kirim, 'Nama : '+cname+'\nMid : '+cmid+'\nBio : '+cstatus+'\nURL Picture : http://dl.profile.line.naver.jp'+cpic)
                            cl.sendMessage(kirim, None, contentMetadata={'mid': cmid}, contentType=13)
                            cl.sendImageWithURL(kirim, a)
                            if "videoProfile='{" in str(cl.getContact(u)):
                                cl.sendVideoWithURL(kirim, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                            else:
                                cl.sendImageWithURL(kirim, 'http://dl.profile.line.naver.jp'+cpic)
                        except Exception as e:
                            cl.sendText(kirim, str(e))

                    elif rfuText in ["Me","me"]:
                        cl.sendMessage(kirim, None, contentMetadata={'mid': user}, contentType=13)

                    elif rfuText.lower() == 'res':
                        cl.sendText(kirim, 'Restarting Server Prosses..')
                        print ("Restarting Server")
                        restart_program()

                    elif rfuText in ["Sp","sp","Speed","speed"]:
                        start = time.time()
                        cl.sendText("u2fd9d66d7006f6dac03dc94950fa83c8", ' ')
                        elapsed_time = time.time() - start
                        cl.sendText(kirim, "%s" % (elapsed_time))
                        start2 = time.time()
                        cl.sendText("u2fd9d66d7006f6dac03dc94950fa83c8", ' ')
                        elapsed_time = time.time() - start2
                        cl.sendText(kirim, "%s" % (elapsed_time))
                        start3 = time.time()
                        cl.sendText("u2fd9d66d7006f6dac03dc94950fa83c8", ' ')
                        elapsed_time = time.time() - start3
                        cl.sendText(kirim, "%s" % (elapsed_time))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#


while True:
    try:
        Operation = RIDEN.singleTrace(count=50)
        if Operation is not None:
            for fast in Operation:
                RIDEN.setRevision(fast.revision)
                thread1 = threading.Thread(target=RIDEN_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as RIDEN:
        logError(RIDEN)
