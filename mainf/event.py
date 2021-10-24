import mainf.myfunction.Math as changeMath
import mainf.myfunction.Search as Msearch
import mainf.myfunction.Pingpong as MP
import asyncio
import json
import warnings
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


warnings.filterwarnings('ignore')


plus = [" + ", "+", "더하기", "플러스", "plus"]
minus = [" - ", "-", "빼기", "뺴기", "마이너스", "minus"]
multi = [" * ", "*", "곱하기", "고파기"]
divi = [" / ", "/", "나누기", "분의"]

class AI:

    def MATHC(text):
        retext = text   #MATH 인식
        
        
        for i in plus:
            if retext.find(i) > 0:
                retext = retext.replace(i, plus[0])

        
        for i in minus:
            if retext.find(i) > 0:
                retext = retext.replace(i, minus[0])

        
        for i in multi:
            if retext.find(i) > 0:
                retext = retext.replace(i, multi[0])


        for i in divi:
            if retext.find(i) > 0:
                retext = retext.replace(i, divi[0])
        return changeMath.cal(retext).calculate()

    def MATHS(text):
        for i in plus:
            if text.find(i) > 0:
                print("ok")
                return True
        for i in minus:
            if text.find(i) > 0:
                return True
        for i in multi:
            if text.find(i) > 0:
                return True
        for i in divi:
            if text.find(i) > 0:
                return True

        return False

        

    def SEARCHC(text):
        if text.find("찾아") > 0 or text.find("검색") > 0:
            return Msearch.search(text).search()
        else:
            return None

    async def answer(text):
        send = ""
        if AI.MATHS(text) == True:
            send = f"놀랍게도 {AI.MATHC(text=text)}예요!^^"
        else:
            ans = await MP.ToPingpong.send(text)
            print(ans)
            print("topic: " + str(ans['topic']))
            if ans['text'] == None:
                send = ans['topic']
            else:
                send = ans['text']

        print(send) 
        return send
    
    def asyanswer(text):
        return str(asyncio.get_event_loop().run_until_complete(AI.answer(text)))







