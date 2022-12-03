import requests
from lib.config import SERVER_GOIP, USERNAME, PASSWORD

class Req():    
    def __init__(self):
        self._SERVER_GOIP = SERVER_GOIP
        self._USERNAME = USERNAME
        self._PASSWORD = PASSWORD
        
    
    def send_sms(self, SMS_PROVIDER, GOIP_NAME, SMS_NUMBER, SMS_TEXT):
        try:
            url = f"http://{self._SERVER_GOIP}/goip/en/dosend.php?USERNAME={self._USERNAME}&PASSWORD={self._PASSWORD}&smsprovider={SMS_PROVIDER}&goipname={GOIP_NAME}&smsnum={SMS_NUMBER}&method=2&Memo={SMS_TEXT}"
            r = requests.get(url=url)     
            
            if int(r.status_code) != 200:
                print("Ошибка запроса на удаленный сервер")
                return False
            
        except Exception as err:
            print(err)
            return False
        
        print(r.text)
        return r.text