import urllib
from urllib.request import urlopen

#이건 아직 덜 만들었지만 시간 없는 관계로 패스
class search:
    text = ""
    sengine="https://www.google.co.kr/search?q=" #구글 검색엔진

    def __init__(self, text):   #생성자
        self.text = text

    def search(self):   #url 연결
        text = self.text
        cegine = self.sengine
        cegine += urllib.parse.quote(text)
        return cegine