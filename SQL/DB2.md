# DB

### 데이터베이스의 특징

- 데이터 베이스 장점

  - 데이터 중복 최소화
  - 데이터 공유
  - 일관성, 무결성, 보안성 유지
  - 데이터의 표준화 가능
  - 용이한 데이터 접근

- 데이터 베이스 단점

  - 전문가 필요
  - 비용 부담
  - 백업과 복구가 어려움
  - 시스템 복잡함
  - 과부화 발생

  

  

### 데이터 무결성(Date Integrity)

> 컴퓨팅 분야에서 데이터의 정확성과 일관성을 유지하고 보증하는 것

- 개체 무결성

  모든 테이블이 기본키를 가져야 하며, 고유하고 빈 값은 허용되지 않는다.

- 참조 무결성

  모든 외래키 값은 참조 릴레이션의 기본키거나 NULL

- 도메인 무결성

  정의된 도메인에서 모든 열(속성)이 선언되도록 규정



### 

## 일대다관계

```python
#models.py
class Reporter(models.Model):
    username = models.CharField(max_length=10)

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
```

- `aritlces_article` 테이블에 `reporter_id `컬럼이 추가 된다.

- `reporter`의 경우 `article_set` 으로 N개(QuerySet)를 가져올 수 있다.

- `article` 의 경우 `reporter로` 1에 해당하는 오브젝트를 가져올 수 있다.
- `on_delete`:  참조 대상이 삭제되는 경우:
  - `CASCADE`: 해당 객체(`'reporter'`)가 삭제되었을 때 참조하는 객체(`'article'`)도 모두 삭제 
  - `PROTECT`: 참조하는객체(`'article'`)가 존재하면, 삭제 금지
  - `SET_NULL`: NULL 값으로 치환, `NOT NULL`옵션이 있는 경우 활용 불가
  - `SET_DEFAULT`: 디폴트 값(`'article'`)을 참조하게끔 한다.



```sql
-- sql
CREATE TABLE "articles_article" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "title" varchar(10) NOT NULL, 
    "content" text NOT NULL, 
    "reporter_id" integer NOT NULL REFERENCES "articles_reporter" ("id") DEFERRABLE INITIALLY DEFERRED
);
```



### 기본쿼리

#### 준비

```bash
Reporter.objects.create(username='요트맨')
Reporter.objects.create(username='john')
Reporter.objects.create(username='justin')
Reporter.objects.create(username='neo')

r1 = Reporter.objects.get(pk=1) 
```

#### article 생성(N)

```bash
a1 = Article()
a1.title = '제목1'
a1.content = '내용1'
# reporter는 리포터 오브젝트를 저장
a1.reporter = r1
# reporter_id는 숫자(INTEGER)를 저장
# a1.reporter_id = 1 
a1.save()
```

```bash
a2 = Article.objects.create(title='제목2', content='내용2', reporter=r1)

```



### 1:N 관계 활용

```bash
# 1. 글의 작성자
a2 = Article.objects.get(pk=2)
a2.reporter

# 2. 글의 작성자의 username
a2.reporter.username

# 3. 글의 작성자의 id
a2.reporter.id
a2.reporter_id

#4. 작성자(1)의 글
r1 = Reporter.objects.get(pk=1)
r1.article_set.all()


#5. 1번글의 작성자가 쓴 모든 글
a1 = Article.objects.get(pk=1)
a1.reporter.article_set.all()
```

