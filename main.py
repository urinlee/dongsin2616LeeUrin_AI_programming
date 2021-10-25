import pyautogui
import mainf.event as Answer
import mainf.myfunction
import asyncio
import base64
import re

#기본 텍스트
answer = "입력되어있지 않음"


while True:
    
    #---------대화 입력칸---------
    question = pyautogui.prompt(f"____________________AI대답____________________\n    {answer}\n_____________________________________________", "질문을 입력하세요.")
    print(question)
    if question == None:
        break
    else:
        answer = Answer.AI.asyanswer(question)

    #---------pyautgui상 이모티콘 출력 불가---------
    # 이모티콘 제거
    emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                    "]+", flags=re.UNICODE)

    answer = emoji_pattern.sub(r"", answer)
    #---------몇몇 범위 밖에 있는 이모티콘---------
    answer = answer.replace("🤗", "")
    answer = answer.replace("🤫", "")
    answer = answer.replace("🤣", "")
    answer = answer.replace("🤐", "")
    answer = answer.replace("🤔", "")
    answer = answer.replace("핑퐁", "우린")
    


    #---------너무 길면---------


#동신중 2616이우린



