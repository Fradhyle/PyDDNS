# PyDDNS
## Contents(목차)
- [English](#English)
    - [Introduction](#Introduction)
    - [Requirements to Collaborate](#Requirements to Collaborate)
    - [Development References](#Development References)
    - [Questions](#Questions)
    - [To-Do](#To-Do)
- [한국어](#한국어)
    - [소개](#소개)
    - [협업 준비물](#협업 준비물)
    - [개발 참고 문헌](#개발 참고 문헌)
    - [질문](#질문)
    - [할 일](#할 일)
### English
#### Introduction
- Purpose: I need DDNS Client for my domain in Cloudflare
- Language: Python
#### Requirements to Collaborate
- **Contact me in advance. (Very important)**
- Python 3.8.8
    - I'm using Anaconda Individual Edition 2020-11
- Requests 2.25.1
---
TL;DR : Perform ```conda update --all``` after install Anaconda Individual Edition 2020-11
#### Development References
Following references are in alphabetical order, case insensitive.
- [Cloudflare API v4 Documentation](https://api.cloudflare.com)
- [cloudflare-python : Official Cloudflare Python Wrapper](https://github.com/cloudflare/python-cloudflare)
- [cURL Converter](https://github.com/NickCarneiro/curlconverter)
- [DnsTube](https://github.com/drittich/DnsTube)
- [Requests](https://requests.readthedocs.io)
#### Questions
1. **Is it okay to save API token/key in plain text?**
    - I also considered about this for a long time.\
      In conclusion, I decided to save it as plain text because it's already safe method.
#### To-Do
- [ ] Stay in background and run regularly.
- [ ] GUI
- [ ] Python-included Excutable
### 한국어
#### 소개
- 개발 목적: CloudFlare를 통해 관리중인 도메인에 대한 DDNS 클라이언트 필요
- 개발 언어: Python
#### 협업 준비물
- **저에게 미리 연락주세요. (매우 중요)**
- Python 3.8.8
    - 저는 Anaconda Individual Edition 2020-11 버전을 사용합니다.
- Requests 2.25.1
---
요약: Anaconda Individual Edition 2020-11 설치 후 ```conda update --all``` 하세요.
#### 개발 참고 문헌
아래의 참고 문헌은 대소문자 구분 없이 알파벳순입니다.
- [Cloudflare API v4 Documentation](https://api.cloudflare.com)
- [cloudflare-python : Official Cloudflare Python Wrapper](https://github.com/cloudflare/python-cloudflare)
- [cURL Converter](https://github.com/NickCarneiro/curlconverter)
- [DnsTube](https://github.com/drittich/DnsTube)
- [Requests](https://requests.readthedocs.io)
#### 질문
1. **API 토큰/키를 평문으로 저장해도 괜찮은가요?**
    - 저 또한 이 문제로 오랫동안 고민을 했습니다.\
      결론적으로, 이미 이 방식은 안전한 방식이기 때문에 평문으로 저장하기로 결정했습니다.
#### 할 일
- [ ] 백그라운드에서 정기적으로 동작하게 만들기.
- [ ] GUI
- [ ] 파이썬이 포함된 실행 파일
