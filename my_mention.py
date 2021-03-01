# coding: utf-8
import random
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
@respond_to('')
def dice_normal(message):
    text=message.body['text']
    if "help" in text:
        message.send("基本:○d○の形式でサイコロを振れます。後ろにu〇もしくはo〇をつけると以上以下の判定ができます。")
        message.send("応用:san○ ○ ○の形式でSAN値チェックができます。１番目にSAN値、2番目に成功時、3番目に失敗時の値を入れます。")
        return
    elif "san" in text :
        sancheck=text.split(' ')
        if '@' in sancheck[0]:
            del sancheck[0]
        sancheck[0]=sancheck[0].replace("san","")
        print(sancheck[0])
        if sancheck[0].isdigit():
            dicevalue=random.randint(1,100)
        else:
            return
        if(dicevalue<=int(sancheck[0])):
            message.send("SAN-1d100 ( "+sancheck[0]+"  >=  " + str(dicevalue) +" ) 成功")
            if 'd' in sancheck[1]:
                tdice=sancheck[1].split('d')
                if tdice[0].isdigit() and tdice[1].isdigit():
                    ddicelist=[]
                    ddicevalue=0
                else:
                    return
                for i in range(int(tdice[0])):
                    nowddice=random.randint(1,int(tdice[1]))
                    ddicelist.append(nowddice)
                    ddicevalue+=nowddice
            else:
                    ddicevalue=int(sancheck[1])
        else:
            message.send("SAN-1d100 ( "+sancheck[0]+"  >=  " + str(dicevalue) +" ) 失敗")
            if 'd' in sancheck[2]:
                fdice=sancheck[2].split('d')
                if fdice[0].isdigit() and fdice[1].isdigit():
                    ddicelist=[]
                    ddicevalue=0
                else:
                    return
                for i in range(int(fdice[0])):
                    nowddice=random.randint(1,int(fdice[1]))
                    ddicelist.append(nowddice)
                    ddicevalue+=nowddice
            else:
                ddicevalue=int(sancheck[2])
        nowsan=int(sancheck[0])-ddicevalue
        message.send("SAN値減少:"+str(ddicevalue)+"("+sancheck[0]+" -> "+str(nowsan)+")")
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
        return
    if dice[0].isdigit() and dice[1].isdigit():
        dicelist=[]
        dicevalue=0
    else:
        print("data")
        return
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
    

        