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

![](D:\lecture\django\django_work.png)

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



## Variable routing

> url의 특정 위치의 값을 변수로 활용

### 1. urls.py

```python
path('hi/<str:name>/', views.hi),
path('add/<int:a>/<int:b>', views.add),
```



### 2. views.py

```python
def hi(request, name):
    context = {
        'name': name
    }
    return render(request, 'hi.html', context)
```



### 3. template

```html
<h1>
    안녕, {{name}}
</h1>
```



## DTL

> 템플릿파일(html)은 django template language를 통해 구성할 수 있다.



1. 출력

   ```bash
   {{ menu }}
   {{ menu.0 }} #인덱스 접근 방법
   ```

2. 문법 `{%%}`

   ```html
   {%for menu in menupan %}
   
   {% endfor %}
   ```

   

3. 주석 `{# #}`

   ```html
   {# 주석입니다. #}
   ```



### 반복문

```html
{% for reply in replies %}
	<li>{{ reply }}</li>
{% endfor %}
```

- `{{ forloop.counter }}`

  1부터 수 세기

- `{{ forloop.counter0 }}`

  0부터 수 세기

- `{% empty %}`



### 조건문

```html
{% if user == 'admin' %}
	<p>관리자 입니다.</p>
{% else %}
	<p>권한이 없습니다.</p>
{% endif %}
```



#### built-in tag, filter

- 공식문서 확인

  https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/

```html
{{ content|length }}
{{ content|truncatechars:10 }}
```



## Template 확장

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Django 기초 - pages</title>
    {% block css %}
    {% endblock %}
</head>
<body>
    <h1>Django 기초 문법 학습</h1>
    {% block body %}
    {% endblock %}
</body>
</html>
```



```html
{% extends 'base.html' %}
{% block css %}
<style>
    h1{
        color : blue;
    }
</style>
{% endblock %}
    {% block body %}
    <h1>{{id}}번째 글입니다. </h1>
    <p>{{content}}</p>
    <p>{{content|length}}글자</p>
    <p>{{content|truncatechars:10}}</p>
    <hr>
    <!-- 댓글 출력 반복 -->
    <ul>
    {% for reply in replies %}
        <li>{{reply}}</li>
    {% endfor %}
    </ul>
    <ul>
    {% for reply in replies %}
        <li>댓글{{forloop.counter}}: {{reply}}</li>
    {% endfor %}
    </ul>
    <ul>
    {% for reply in replies %}
        <li>댓글{{forloop.counter}}: {{reply}}</li>
        { % empty %}
        <p>댓글이 없어요! 작성해주세요.. ㅠㅠ</p>
    {% endfor %}
    </ul>

    <ul>
        {%if user == 'admin'%}
            <p>수정, 삭제</p>
        {% else %}
            <p>관리자 권한이 없습니다.</p>
        {% endif %}
    </ul>
{% endblock %}
```





## Template 설정

```python
#django_intro/settings.py Line#55
TEMPLATES = [
    {
        #DTL 엔진을 활용, jinja2 등으로 변경 가능함.
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #APP 내에 있는 폴더가 아닌 
        'DIRS': [],
        # APP_DIRS: True 인경우, 등록된 app(INSTALLED_APP)의 디렉토리에 있는 templates 폴더를 템플릿 폴더로 활용하겠다라는 의미!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



#### Form을 통한 요청 처리

#### 개요

1. 사용자들로부터 값을 받아서(`boards/new/`)
2. 이를 단순 출력하는 페이지 구성(`boards/complete`)



##### 1. 사용자에게 form 양식 제공

1. url 지정

```python
path('new', views.new)
```



2. view 함수 생성

   ```python
   def new(request):
       return render(request, 'boards/new.html')
   ```

3. template

   ```html
   <form action="/boards/complete/">
       제목: <input type="text" name="title"
   </form>
   ```

   - form 태그에는 `action` 속성을 정의한다.
     - 사용자로부터 내용을 받아서 처리하는 url
   - input 태그에는 `name`속성을 통해 사용자가 입력한 내용을 담을 변수 이름을 지정한다.
   - url 예시: `/boards/complete/?title=제목제목`



##### 2. 사용자 요청 처리

1. urls.py 정의

   ```python
   path('/boards/complete/', views.complete)
   ```

2. views.py

   ```python
   def complete(request):
       title = request.GET.get('title')
       context = {
           'title' : title,
       }
       return render(request, 'boards/complete.html', context)
   ```

   - request에는 요청과 관련된 정보들이 담긴 객체가 저장되어 있다.

3. template

   ```html
   {{ title }}
   ```

   