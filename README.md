# 음성명령 제어 '따라와'


 # 프로젝트 구조

- Aserver
  - app.py
  - templates
  - css
- Bserver
  - app.py
  - csss
- img
- raspToSerial
- serialToArduino
- Assistant
  - assistant.py

**Aserver**

> A라즈베리파이의 서버 폴더입니다.



**Bserver**

> B라즈베리파이의 서버 폴더입니다.



**Assistant**
> 구글 어시스턴트 폴더입니다.



**raspToSerial**
> 시리얼 파트 폴더입니다.



**serialToArduino**
> 아두이노 파트 폴더입니다.
> 아두이노 자체에 업로드하지만, 명시적으로 모두가 볼 수 있게하고자,
> 이 폴더에 업로드하면 됩니다.



**img**

> 설계디자인을 저장해둔 폴더입니다.
>
> 프로젝트 개발에 사용되는 폴더는 아닙니다.





----

### Assistant

**environment**

* Python
* Google Assistant SDK
* Linux based on Debian

> 프로젝트 운영체제로 Debian 계열 raspbian 기준에서 설치하였으나,
>
> 운영체제 상관없이 동작 가능합니다.

```bash
sudo apt-get install portaudio19-dev libffi-dev libssl-dev libmpg123-dev
```

```bash
python -m pip install --upgrade google-assistant-library
```

```bash
python -m pip install --upgrade google-assistant-sdk[samples]
```



`credentials` 생성위한 환경 설치 및 `client*.json` 발급

```bash
python -m pip install --upgrade google-auth-oauthlib[tool]
```

```bash
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --scope https://www.googleapis.com/auth/gcm --save --headless --client-secrets /path/to/client_secret_client-id.json
```

[구글 어시스턴트 SDK 문서 참고](https://developers.google.com/assistant/sdk/guides/library/python/embed/install-sample)



-----







공부하면서 참고하기 좋은 문서들

* [Flask](https://mooneegee.blogspot.com/2017/10/python-flask.html)
* [Python3](https://wikidocs.net/book/1)
* [requests 와 BeautifulSoup4](https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/)
* [PyMySQL](https://parkminkyu.github.io/python/flask/05-python-flask.html)



* [BootStrap](http://getbootstrap.com/docs/4.1/getting-started/introduction/)
* jinja2   [문서1](http://jinja.pocoo.org/docs/2.10/templates/) [문서2](http://flask.pocoo.org/docs/1.0/templating/)
* [Rachet](http://goratchet.com/components/)





> 이외의 라이브러리들은 본인이 필요하다고 생각하면 자유롭게 써보도록 해요. 
>
> 좋은 라이브러리가 있다면 공유해주세요







| 이름   | 담당                        | 비고 |
| ------ | --------------------------- | ---- |
| 노아론 | 어시스턴트                  |      |
| 장수경 | 서버 - A파트                |      |
| 허승은 | 서버 - B파트                |      |
| 이새하 | 아두이노                    |      |
| 전승현 | 서버-아두이노 간 시리얼통신 |      |

