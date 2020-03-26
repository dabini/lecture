# Django



## Web Framework

- 웹페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 통상 데이터 베이스 연동, 템플릿 형태의 표준, 세션과리, 코드 재사용 등의 기능을 포함하고 있다.

- 즉, 프로그래밍 운영체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리의 모임이다.



## Django를 왜 배워야하는가?

1. python 기반이기 때문
2. spotify instagram dropbox 등 다양한 어플리케이션에서 Django를 이용하고 잇음.



### 우리가 알고 있는 웹 프로토콜

요청(request) <-> 응답(response)



## Django는 어떻게 동작하는가

- 모델 뷰 컨트롤러
  - 소프트웨어공학에서 사용되는 소프트웨어 디자인 패턴



![](D://lecture/django/django.png)

|  MVC패턴   |        Django        |
| :--------: | :------------------: |
|   Model    |  Model(데이터 관리)  |
|    View    | Template(인터페이스) |
| Controller |    View(상호동작)    |

=> python



### AWS Cloud9

- 브라우저에서 직접 코드를 작서, 실행 및 디버깅 할 수 있는 클라우드 기반 IDE(통합 개발 환경)
- OS: Ubuntu 18 04 4 LTS
  - python 3.7.6
- 개별 로컬 PC환경에 영향이 없다는 장점이 있다
- 추후에 로컬 개발 환경 설정도 진행할 예정



## 설치

```bash
$ pip install django==2.1.15
```

- 수업에서는 `2.1.15`를 기준으로 진행 예정



### Django 프로젝트 시작

#### 프로젝트 생성

``` bash
$ django-admin startproject {프로젝트명}
```

#### 서버실행

- `django_intro`폴더의 `settings.py` 파일에 아래와 같이 수정한다.

```bash
#28번째 라인의
ALLOWED_HOST = ['*']
```



- 반드시 서버 실행시 명령어가 실행되는 디렉토리를 확인할 것

```bash
~/ $ cd django_intro/
~/django_intro/ $ python manage.py runserver 8080
```

- 실행된 서버는 우측의 url을 클릭한다.
- 서버 종료는 터미널에서 `ctrl + c` 함께 입력한다



#### 리눅스 명령어

- `cd `: change directory

```bash
# django_intro 폴더로 이동
$ cd django_intro/
~/django-intro $
#상위 디렌토리로 이동
$ cd ..
```



- `ls` : 현재 디렉토리 파일 목록

```bash
~/django_intro $ ls

```



### APP생성

- django는 여러개의 앱을 가진 하나의 프로젝트로 구성된다
  - 커뮤니티를 만든다.
    - 회원과 관련된 app - `accounts`
    - 게시물과 관련된 app - `posts`

```bash
$ python manage.py startapp {app이름}
```

- app을 생성하고 반드시 `settings.py`의 `INSTALLED_APPS`에 등록한다.

```BASH
INSTALLED_APPS = [
	...
	'pages',
]
```





## 기본 흐름

### 1. `urls.py`

```python
#django_intro/urls.py
from pages import views

urlpatterns = [
	path('lotto/', views.lotto),
]
```

- path에 url은 항상 `/`로 닫아준다.



### 2. `views.py`

```python
#pages/views.py
import random

def lotto(request):
    pick = random.sample(range(1, 46), 6)
    context = {
        'pick' = pick
    }
    return render(request, 'lotto.html', context)
```

- 함수를 정의할 때, 항상 첫번째 인자는 `request`로 작성해둔다.
  - 내부적으로 요청을 처리할 때, 함수 호출 시 요청정보가 담긴 객체를 넣어준다.

- `render`함수를 통해서 반환한다.
  - 첫번째 인자: `request`
  - 두번째 인자: 템플릿파일(`html`)
  - 세번째인자: dictionary, 템플릿에서 활용하려고 하는 값들을 전달



### 3. `template` 파일 생성

- 반환할 html 파일은 항상 `templates `폴더 안에 생성한다.

```html
<!-- pages/templates/lotto.html -->

<p>{{pick}}</p>
```

- context 딕셔너리의 key값을 적으면 출력된다.

