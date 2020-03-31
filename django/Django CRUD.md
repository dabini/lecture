# Django CRUD

## 프로젝트 및 app 설정

### 1. 프로젝트 생성

```bash
$ django-admin startproject {{}}
```



### 2. 프로젝트 설정(settings.py)

```python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+wq8wgwvswyzp!p8be8&l&u2^l%k1ns_&3f*v+&_=yr1(9m1g^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_crud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

```



### 3. app 설정(articles)



## Model 활용

### 1. model 정의

```python
#models.py
class Article(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- `models.Model`을 상속받은 클래스를 생성한다.
- 속성은 내가 구성하고 싶은 테이블의 컬럼 이름을 지정하고, 데이터 타입에 맞춰서 필드를 정의한다.

### 2. Migration

- 정의된 모델을 데이터베이스에 반영하기 위해서는 항상 마이그레이션 명령어를 통해 마이그레이션 파일을 생성한다.

  ```bash
  $ python manange.py makemigrations
  ```

  

- 마이그레이션 파일은 모델의 변경사항을 관리한다.

- 생성된 마이그레이션 파일을 데이터베이스에 반영하기 위해서는 아래의 명령어를 입력한다.

  ```bash
  $ python manage.py migrate
  ```



- 관리자 만들기

  ```bash
  $ python manage.py createsuperuser
  ```

  - 이메일은 안 써도 됨!



## Django ORM

>  기본적인 데이터베이스 조작은 CRUD(Create Read Update Delete)



### 1. 생성

```python
article = Article()
article.title = '제목'
article.content = '내용'
article.save()
```



### 2. 조회

```python
Article.objects.all()

Article.objects.get(id=1)
```



### 3. 수정

```python
a1 = Article.objects.get(id=1)
a1.title = '제목수정'
a1.save()
```



### 4. 삭제

```python
a1 = Article.objects.get(id=1)
a1.delete()
```



## ORM

Model

- MTV 패턴에서 데이터를 관리

Migration

- Model로 정의된 데이터베이스 스키마를 반영

ORM(Query method, QuerySet APIs)

- 데이터베이스를 조작

