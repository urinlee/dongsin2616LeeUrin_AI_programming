import re


class cal:    #cal 클래스 생성
    text = ""   #변수 생성
    sum = ""

    def __init__(self, text):   #생성자
        for i in range(0, len(text)):
            if text[i].isdigit() or text[i] in ["+", "-", "*", "/", " "]:
                self.text += text[i]
            else:
                break


    def calculate(self):    #변수
        sum = eval(self.text)   #이건...뭐랄까 약간 파이썬코드를 입력하는 느낌 이랄까?
        return sum  #결과 리턴
            




        