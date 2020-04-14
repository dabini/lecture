# Django_form 흐름짜기

> 코드 외우지말고, 흐름을 이해하려고 노력하기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



어떠한 로직을 사용하던 Form이나 ModelForm을 사용하는 로직을 사용

1. Form 제공(~.html) = > `Get`방식

   - context에 form이나 modelForm을 넘겨주는 방식

     ```python
     form = ArticleForm()
     
     context = {
         'form' : form
     }
     
     return render(request, '/.html', context)
     ```

2. 데이터를 양식에 맞게 보내주면 => 처리하는 작업 => `POST`방식

   - 양식 데이터(request.POST)를 ModelForm에 넘긴다

     ```python
     form = ArticleForm(request.POST)
     ```

   - 검증
     - 맞을 때: form.save()로 저장
     - 아닐 때: 인덴트를 맞춰주면 처리 가능

### 코드 짜는 방법

get요청 방식 부터 코드 짜기!



### Login

1. login은 ModelForm이 아님을 기억할 것
2. request를 첫번째 인자로 받음
   - 로그인은 쿠키 세션이라는 정보를 받고 있기 때문에!
3. valid 검증
4. login 되어있을때
   - 인자로 request를 먼저 받고, form_get_user() 인자 받기



### @login_required

`decorators`를 사용해서 로그인 되어있을 때 상황 만들어주기

=> `next`파라미터를 이용해서 `/accounts/login`



### Logout



### Articles/Accounts 비교



#### Articles

C : 새로 만들고 `ModelForm` 사용

R: `variable rounting` 사용(어떤 글인지를 판단하기 위해)

D: `variable rounting` 사용

V: `variable rounting` 사용/ `ModelForm` 사용하는 데 `instance` 사용



#### Accounts

C: 

R:

U: 실제 로그인한 유저가 삭제/수정하게 하려면  `request.user` 사용하면 되니까 `variablerouting`이 필요가 없음

D:실제 로그인한 유저가 삭제/수정하게 하려면  `request.user` 사용하면 되니까 `variablerouting`이 필요가 없음