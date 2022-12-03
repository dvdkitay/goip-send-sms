import logging
import os
import sys
import argparse

from lib.req import Req


logging.basicConfig(
    format='[SCRIPT-DEBUG] %(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt='%d-%b-%y %H:%M:%S'
)

req = Req()

def args_filter():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '--provider', dest='provider', type=str, default=''
    )
    
    parser.add_argument(
        '--goip', dest='goip', type=str, default=''
    )
    
    parser.add_argument(
        '--file', dest='file', type=str, default=''
    )
    
    parser.add_argument(
        '--text', dest='text', type=str, default=''
    )
    
    
    args = parser.parse_args()
    
    return {
        "provider": args.text, 
        "goip": args.file,
        "file": args.file, 
        "text": args.text
    }
    
def run():
    
    args = args_filter()
    
    configs = {
            "SMS_PROVIDER": args.get("provider"),
            "GOIP_NAME": args.get("goip"),
            "FILE": args.get("file"),
            "SMS_TEXT": args.get("text"),
        }
    
    if not configs["SMS_PROVIDER"] or not configs["GOIP_NAME"] or not configs["FILE"] or not configs["SMS_TEXT"]:
        logging.error("Обязательны для передачи скрипту: Смс провайдер, Имя GOIP, Файл, Текст")
        return False
        
    
    with open(configs["FILE"], 'r') as f:
        line = f.read().splitlines()
        
        for SMS_NUMBER in line:
            
            if not SMS_NUMBER:
                pass
            
            logging.info(f"Отправляем смс на номер: {SMS_NUMBER}")
            
            sms = req.send_sms(
                configs["SMS_PROVIDER"], configs["GOIP_NAME"], 
                configs["FILE"], configs["SMS_TEXT"]
            )
    
            if not sms:
                logging.error(f"Ошибка отправки смс на номер: {SMS_NUMBER}")
            else:
                logging.info(f"Успешная отправка смс на номер: {SMS_NUMBER}")
    
    return True
    
if __name__ == '__main__':
    
    if not run():
        logging.error("Программа завершилась с ошибкой")
    else:
        logging.info("Успешное завершение программы")
