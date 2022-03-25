# PyDDNS
## 목차(Contents)
- [한국어](#한국어)
    - [소개](#소개)
    - [개발 참고 문헌](#개발-참고-문헌)
    - [질문](#질문)
    - [할 일](#할-일)

- [English](#English)
    - [Introduction](#Introduction)
    - [Development References](#Development-References)
    - [Questions](#Questions)
    - [To-Do](#To-Do)
---
<!-- [ko-KR] -->
## 한국어
### 소개
- 개발 목적: [Cloudflare](https://www.cloudflare.com/)를 통해 관리중인 도메인에 대한 DDNS 클라이언트 필요
- 개발 언어: [Python](https://python.org)
### 개발 참고 문헌
아래의 참고 문헌은 대소문자 구분 없이 알파벳순입니다.
- [Cloudflare API v4 Documentation](https://api.cloudflare.com)
- [cloudflare-python : Official Cloudflare Python Wrapper](https://github.com/cloudflare/python-cloudflare)
- [cURL Converter](https://github.com/NickCarneiro/curlconverter)
- [DnsTube](https://github.com/drittich/DnsTube)
- [Requests](https://requests.readthedocs.io)
### 질문
1. **API 토큰/키를 평문으로 저장해도 괜찮은가요?**
    - 저 또한 이 문제로 오랫동안 고민을 했습니다.  
      결론적으로, 이미 이 방식은 안전한 방식이기 때문에 평문으로 저장하기로 결정했습니다.  
      하지만 Cloudflare의 권고 사항에 따라 나중에 API 키 방식은 없앨 예정입니다.
### 할 일
- [ ] 백그라운드에서 정기적으로 동작하게 만들기.
- [ ] GUI
- [ ] 파이썬이 포함된 실행 파일
<!-- [en-US] -->
## English
### Introduction
- 개발 목적: I need DDNS Client for my domain in [Cloudflare](https://www.cloudflare.com/)
- 개발 언어: [Python](https://python.org)
### Development References
Following references are in alphabetical order, case insensitive.
- [Cloudflare API v4 Documentation](https://api.cloudflare.com)
- [cloudflare-python : Official Cloudflare Python Wrapper](https://github.com/cloudflare/python-cloudflare)
- [cURL Converter](https://github.com/NickCarneiro/curlconverter)
- [DnsTube](https://github.com/drittich/DnsTube)
- [Requests](https://requests.readthedocs.io)
### Questions
1. **Is it okay to save API token/key in plain text?**
    - I also considered about this for a long time. 
      In conclusion, I decided to save it as plain text because it's already safe method. 
      But I will remove API Key method later because of Cloudflare's recommendation
### To-Do
- [ ] Stay in background and run regularly.
- [ ] GUI
- [ ] Python-included Excutable
