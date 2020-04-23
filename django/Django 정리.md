# Django 정리

### 프로젝트 및 APP 초기 설정

```bash
#프로젝트 생성
$ django-admin startproject {프로젝트명}
```

- settings.py 
  -  `ALLOWED_HOST = ['*']` 로 지정 
    - 모든 호스트에서 접근이 가능하게 해줌.
  - `LANGUAGE_CODE = 'ko-kr'`
  - `TIME_ZONE = 'Asia/Seoul'`



```bash
#앱 생성
$ python manage.py startapp {앱이름}

#앱이름은 복수형으로 만들어주기
```

- settings.py 

  - `INSTALLED_APPS`에 앱등록

- urls.py

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ]
  ```

  



### Model 정의

```python
#models.py

# 내가 그릴 테이블을 상상하기 => 이를 위한 모델링을 진행!!

class 모델명(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    ...
    user = models.ForeignKey()
```



### ModelForm 정의

> Model에 정의한 필드를 <form></form> 와 같이 HTML에 만들어야하는데 이를 자동으로 만들어주는 기능
>
> 모델이 변경되면 컬럼들도 자동으로 변경될 수 있게 해줌
>
> valid 검증 역시 효율적으로 할 수 있음 => HTML

```python
#forms.py

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
```



### 코드 작성 흐름

> Url
>
> View 
>
> Template

#### 1. urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('create/', views.create, name='create'),
]
```

- path를 정의하면 어떠한 패턴의 url이 들어오면 이 url을 실행한 view함수를 만들어줘야함.

- namespace를 만들어줌으로써 url을 변수화시킴!



#### 2. views.py

> MTV 패턴 중 중간관리자 역할
>
> M - Query&Method
>
> T - Context

```python
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

def create(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)
```

- 함수(인자 => 반환(return))

  - 인자: HTTP Request of object(request, pk 등)

  - 반환: HTTP Response of  object(render/redirect)



#### 3. Templates

- DTL을 통해서 HTML 파일 만들어주기

- context에 넘어온 딕셔너리를 사용

- request/ user에 대한 정보도 사용할 수 있음

  - `settings.py` 안에 `context-processors`에 포함이 되어있기 때문에

- 확장(상속) 기능: `{% extends 'base.html' %}`을 통해 `base.html` 을 상속받음

- `settings.py`에서`DIR` , `APP_DIRS`  순으로 탐색을 함

  - `articles/templates/articles/create.html` 하는 이유: 

    => namespace 처럼 경로를 편하게 찾게 하려고!

  - `os.path.join(BASE_DIR,'templates')` 로 templates 경로 패턴 저장



#### 4. 정적파일(Static files)

`APP/static`

- `{% load static %}` 을 통해 정적 파일 사용





## Django 기본

> OOP: 객체 지향 프로그래밍

### 클래스

- 클래스 : 전체적인 패턴
  - 동작(메서드)
  - 상태(멤버변수(인스턴스.. 같은 것들))



### Name import

- https://github.com/django/django

- 폴더 구조라고 생각하고 외우기

- 가장 많이 쓰는 거!

  `from django.contrib.auth import ...`

  ```python
  #urls.py
  from django.urls import path
  form django.urls import path,include
  
  #forms.py
  from django import forms
  
  #models.py
  from django.db import models
  
  #auth
  from django.conf import settings
  from django.contrib import admin
  from django.contrib.auth import get_user_model
  from django.contrib.auth import login 
  from django.contrib.auth import logout
  from django.contrib.auth.forms import UserCreationFrom, AuthenticationForm
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth.decorators import login_required
  
  #views.py
  from django.shortcuts import render, redirect, get_object_or_404
  from django.views.decorators.http import require_POST
  ```

  

#### 케이스 네이밍  컨벤션

##### lower 카멜 케이스 (lowerCamelCase)

- camel**C**ase, background**C**olor, class**N**ame
- 단봉낙타 표기법이라고도 한다.
- 보통 카멜 케이스라고 하면 lower 카멜 케이스를 의미한다.
- 각 단어의 첫 문자를 대문자로 표시하되, 이름의 첫 문자는 소문자로 적는다.

##### Upper 카멜 케이스 (UpperCamelCase)

###### 파스칼 케이스 (PascalCase)

- **C**amel**C**ase, **B**ackground**C**olor, **C**lass**N**ame
- 쌍봉낙타 표기법이라고도 한다.
- 전체 이름의 첫 문자를 포함한 각 단어의 첫 문자를 대문자로 표시한다.

##### 스네이크 케이스 (snake_case)

- camel***\**case, background\**\***color, class**_**name
- 각 단어의 사이를 언더바`_`로 구분해주는 표기법이다.

##### 헝가리안 표기법 (Hungarian notation)

- **b**CamelCase, **sz**BackgrounColor, **str**ClassName
- 이름 앞에 변수의 타입을 접두어로 넣어주는 표기법이다.
- 접두어의 종류에는 ch - `char`, db - `double`, str - `string`, b - `boolean` 등이 있다.





### Auth

- 모델(내부 유저 모델 사용)
- 폼(UserCreationForm, AuthenticationForm)

- 커스텀하고 싶으면 각각 `Models.py`, `Forms.py` 에서 가져와서 커스텀해서 상속



- 회원가입

  - User 모델을 만들어야 하니까 `UserCreationForm` (`ModelForm`의 일종)사용

  - `UserCreationForm`은 `ArticleForm`쓰는 것 처럼 사용

    

- 로그인

  - 지정된 폼은 없지만, `AuthenticationForm`을 가져와서 사용

  - `AuthenticationForm`의 경우, **`request`** 객체에 담겨있기 때문에 주의할것...!!

    ```python
    def login(request):
        if request.method=='POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return ... 
    ```

  - `@login_required`: 로그인 되어 있을 때 로그인 창 못오게 하는것

  - `@required_POST`: 로그아웃은 POST 요청만 보내...

  - `get_object_or_404`: 오류나면 404 오류 내보내...



- Request 응답 로직 순서

  1. Get => 모델폼html

  2. POST( 저장로직) => redirect
     1. 값을 받아오고
     2. 검증하고
     3. 저장한다

