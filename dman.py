# JSON 모듈이 빈 파일을 불러올 때 발생하는 오류 처리 import
from json.decoder import JSONDecodeError
import json
import sqlite3
import pathlib


class JSONMan:
    def __init__(self, file):
        self.file = pathlib.Path(file)
    
    def load(self):
        # JSON 파일 불러오기
        try:
            fp = open(self.file, 'r', encoding='utf-8')
        # JSON 파일이 발견되지 않을 경우 파일 생성 후 읽기 모드로 불러오기
        except FileNotFoundError:
            open(self.file, 'w', encoding='utf-8')
            fp = open(self.file, 'r', encoding='utf-8')

        # 파일에서 JSON 데이터 읽기
        try:
            data = json.load(fp)
        # JSON 데이터를 불러올 때 발생할 수 있는 오류 처리
        # 예: 빈 파일
        except JSONDecodeError:
            pass
        # 불러온 설정값 반환
        finally:
            return data

    def save(self, data):
        # 데이터 파일을 새로 쓰기 모드로 불러온 후 JSON 저장
        with open(self.file, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4, separators=(',', ':'))

class SQLMan:
    def __init__(self, file):
        self.file = pathlib.Path(file)

    def connect(self):
        try:
            conn = sqlite3.connect(self.file)
        except sqlite3.Error as e:
            print(e)
        else:
            return conn