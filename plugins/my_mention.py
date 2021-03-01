# coding: utf-8
import time
import random
import re
import json
import codecs
import sys
import schedule
from bs4 import BeautifulSoup
from time import sleep 
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
@respond_to('')
def dice_normal(message):
    text=message.body['text']
    if "d" in text :
        text1=text.split(' ')
        if "o" in text1[0] :
            dicetype="ijo"
            text2=text1[0].split("o")
            text1[0]=text2[0]
        elif "u" in text1[0] :
            dicetype="ika"
            text2=text1[0].split("u")
            text1[0]=text2[0]
        else:
            dicetype="normal"
        print(text1[0])
        dice=text1[0].split('d')
    else:
        print("でーた")
        exit()
    if dice[0].isdigit() and dice[1].isdigit():
        dicelist=[]
        dicevalue=0
    else:
        print("data")
        exit()
    for i in range(int(dice[0])):
        nowdice=random.randint(1,int(dice[1]))
        dicelist.append(nowdice)
        dicevalue+=nowdice
    if dicetype=="normal" and int(dice[0]) == 1:
        message.send(text1[0] +" -> " + str(dicevalue))
    elif dicetype=="normal" and int(dice[0]) != 1:
        dicelist  = [str(i) for i in dicelist]
        dicelist="["+','.join(dicelist)+"]"
        message.send(text1[0] + " -> " + str(dicevalue)+str(dicelist))
    elif dicetype=="ijo":
        if(dicevalue>=int(text2[1])):
            message.send(text1[0] +" ( "+text2[1]+"  <=  " + str(dicevalue) +" ) 成功")
        else:
            message.send(text1[0] +" ( "+text2[1]+"  <=  " + str(dicevalue) +" ) 失敗")
    elif dicetype=="ika":
        if(dicevalue<=int(text2[1])):
            message.send(text1[0] +" ( "+text2[1]+"  >=  " + str(dicevalue) +" ) 成功")
        else:
            message.send(text1[0] +" ( "+text2[1]+"  >=  " + str(dicevalue) +" ) 失敗")
    

        