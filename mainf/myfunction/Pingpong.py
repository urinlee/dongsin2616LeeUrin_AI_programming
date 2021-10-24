import PingPongWr # 메인 모듈
import asyncio # 비동기 실행을 위한 모듈
import uuid
sessionId = uuid.uuid1()

url = f"https://builder.pingpong.us/api/builder/5f0bfffae4b0e31d38cbbba7/integration/v0.2/custom/{sessionId}"  # 핑퐁빌더 Custom API URL
pingpong_token = "Basic a2V5OjI5ZTA1YjBjZmQ0N2EyMGY5OGZiNGE0MjJhYzZiZDcw"  # 핑퐁빌더 Custom API Token

Ping = PingPongWr.Connect(url, pingpong_token)  # 핑퐁 모듈 클래스 선언

class ToPingpong:
    async def send(text): # 비동기식 함수
        
        return_data = await Ping.Pong(session_id ="Example", text = text, topic = True, image = False, dialog = True) # 핑퐁빌더 API에 Post 요청

        return return_data