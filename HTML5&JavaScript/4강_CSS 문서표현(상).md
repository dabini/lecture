# HTML5/JavaScript

## 4. CSS 문서표현(상)

> 용어알기
>
> - CSS
>
>   Cascading Style Sheets의 약자로 HTML 문서에 외형을 정의하기 위한 스타일 언어
>
> - 선택자
>
>   CSS 스타일 적용을 위해 HTML 문서 내의 단일 요소 또는 요소들을 선택하는 구문 규칙
>
> - 의사 클래스
>
>   의사 클래스는 요소의 기본 상태와는 무관하게 링크, 동적, 구조적 상태를 이용하는 선택자의 일부



### 1) CSS의 이해

- CSS란?

  - CSS: Cascading Style Sheets의 약자

  - CSS의 특징

    1. HTML 요소에 스타일 적용하기 위해 사용

       - HTML 외형을 정의
       - 스타일 시트 파일이라고 함
       - HTML 요소의 시각적 특성을 원하는 대로 변경 가능

    2. CSS의 장점

       - 디자인을 정의, 관리, 재활용하는데 용이
       -  하나의 CSS 파일은 다수의 HTML에서 사용할 수 있어 체계적이고 경제적

       ![image-20200310073737797](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310073737797.png)

    3. HTML과 함께 사용되지만 HTML은 아님
       - CSS는 스타일 언어
       - HTML 이외에 다른 프로그래밍 언어와 사용 가능

- CSS 작동 방법

  - HTML (문서 구조 정의) + CSS (문서 외형 정의) => 짝을 이뤄 사용

  - CSS 작성방법

    1. HTML 요소에 직접 CSS 정의: HTML요소에 스타일 속성 이용
    2. CSS 모아서 정의: HTML 헤더 부분에 style 요소 사용
    3. **CSS 파일을 만들어 HTML에 연결**
       - HTML이 서버에서 웹브라우저로 로드될 때 같이 로드
       - HTML 내용 화면에 나타낼 때 외형 디스플레이에 CSS파일 참고 됨

  - CSS 화면 정의 내용

    - 텍스트의 크기 및 스타일
    - 요소들의 레이아웃
    - 그림, 섹션 요소들의 크기와 테두리, 배경 색 또는 이미지
    - 화면 전환이나 요소들의 움직임

    

- CSS 기술방식

  - 기본 기술방식

    - 형태: 성택자 {속성 선언}

    - 예

      ```css
      h1{font-size: 1.5em;}
      ```

  - 선택자

    - 정의 : HTML의 어떤 요소, 요소들에 속성들이 적용되는지 정의하는 곳
    - 형태: 단순한 요소명, 클래스 , ID 또는 복잡한 논리형 등으로 가양

  - 속성 선언

    - 정의: 선택자를 통해 선택된 HTML 요소에 적용할 스타일 속성 내용
    - 구성: 속성과 값
    - 속성: 정의하는 스타일의 내용
    - 속성 값: 속성의 내용(키워드, 단위가 있는 수치)
    - 특징
      1. 하나의 선택지는 하나의 속성 선언을 가짐
      2. 각각의 속성 선언은 ;(세미 콜론)으로 분리
      3. 속성 선언은 { } 사용

  - 예

    ```css
    h1{
        width: 300px;
        height: 50px;
        font-size: 1.5em; #em은 비율단위!
        color: red;
        font-weight: bold;
    }
    ```

    <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310074611004.png" alt="image-20200310074611004" style="zoom:80%;" />

    

- HTML 문서에 CSS 적용과 연결

  - HTML 요소 속성으로 CSS 적용

    - 선택자를 통하여 직접 요소에 CSS 스타일 추가

    - 방법: 스타일 속성을 통해 CSS 스타일 적용

    - CSS 속성 언언: ;(세미콜론)으로 분리

    - 예

      ```css
      <h1 style="width:350px; height:50px; font-size: 1.5em; color:red; font-weight:bold">이것은 첫번째 제목입니다.</h1>
      ```

      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310074926668.png" alt="image-20200310074926668" style="zoom:80%;" />

    - 단점
      1. 동일 요소 공통으로 적용 불가
      2. 수정 및 변경 시 모든 HTML 코드 검토
      3. 체계적인 관리와 변경 불가능
      4. 스타일 속성은 테스트 용으로만 사용

    

  - Style 요소를 사용한 CSS 적용

    - 방법: <head> 부분에 선택자를 이용하여 style 요소 정의

    - CSS 코드가 위치한 HTML 파일에만 적용

    - 단점: 전체 수정 시 모든 HTML 파일을 수정해야함.

       => 테스트 용으로만 사용

    - style 요소의 속성

      1. type

         style 언어가 어떤 MIME 타입인지 지정

         CSS 파일의 경우: text/css 지정

         HTML5의 경우: 생략 가능(생략하면 css로 지정됨)

      2. media

         현재 CSS 코드가 어떤 매체일 경우 지정되는지 지정

         "all"지정: 모든 매체에서 현재 CSS 적용, 미디어쿼리

    - 예

      ```html
      <!DOCTYPE html>
      <html>
          <head>
              <meta charset="utf-8">
              <title>Title</title>
              <style type="text/css" media="all">
                  h1 {
                      width: 300px;
                      height: 50px;
                      font-size: 1.5em;
                      color: red;
                      font-weight: bold;
                  }
              </style>
          </head>
          <body>
              <h1>이것은 첫 번째 제목입니다.</h1>
              <h2>이것은 두 번째 제목입니다.</h2>
              <h1>이것도 첫 번째 제목입니다.</h1>
          </body>
      </html>
      ```

      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310075859154.png" alt="image-20200310075859154" style="zoom:80%;" />

- 외부 CSS 파일 HTML 문서에 연결

  - 장점

    1. 여러 HTML 파일에서 공통으로 사용 가능
    2. 수정 시 HTML 파일을 전체 수정할 필요 없음
    3. 체계적이고 구조적인 스타일 관리 가능
    4. 전체 전송량이 줄어듬

  - 외부 스타일 시트 파일: .css를 가지는 파일, 텍스트로 이루어짐

  - HTML에서 외부 CSS 파일의 연결

    1. HTML 코드 작성

    2. 비어있는 파일을 작성하고 확장자 .css로 저장

    3. CSS 파일 경로 지정

       (HTML 코드 <head>부분에 link 요소 사용)

    4. CSS 파일 열어 CSS 스타일 지정

  

  - link 요소 : HTML문서와 외부 리소스 연결을 위해 사용, 대부분 CSS 파일 연결

  - link 요소의 속성

    - rel

      생략 불가능한 속성

      현재 HTML과 연결할 파일간의 관계를 나타냄

      다양한 값을 가짐

      CSS 파일 연결: rel="stylesheet"

    - href

      연결하고자 하는 리소스 파일 경로 지정

    하나의 HTML파일에 여러 개의 link 요소 사용하여 각기 다른 여러 CSS 파일 링크 가능

    예)

    <link rel="stylesheet" href="css/style.css">

    <link rel="stylesheet" href="css/style.css" type="text/css" media="all">

    

- CSS 코드 내에서 외부 CSS 파일 불러오기

  - 왜 CSS 코드 내에서 외부 css 파일을 불러올 필요가 있는가?

    => 구조적으로 잘 설계된 css는 css 파일 내부에서 다른 css 파일을 불러오기도 함

    - 예

      1. 가장 기본이 되는 스타일을 정의한 default.css 파일을 만들었다.

      2. 제작하는 사이트의 메인 페이지들은 공통적으로 default.css와 함께 main.css 파일 그리고 navi.css 파일을 불러올 필요가 있다.

         서브페이지 HTML 파일은 main.css를 link 요소로 불러온다.

      3. 모든 서브 페이지들은 dafault.css와 sub.css, navisub.css 파일이 필요하다면 sub.css 파일에서 default.css와 navisub.css 파일을 불러들인다.

  - @import 구문

    - 형태: @import url('불러들일 css파일이름');

    - 사용: style 요소 및 css 파일 내부에서 사용

    - 예

      ```html
      <!DOCTYPE html>
      <html>
          <head>
              <meta charset="utf-8">
              <title>Title</title>
              <style type="text/css" media="all">
                  @import url('default.css');
                  h1 {
                      weight: 300px;
                      height: 50px;
                      font-size: 1.5em;
                      color: red;
                      font-weight: bold;
                  }
              </style>
          </head>
          <body>
              <h1>이것은 첫 번째 제목입니다.</h1>
              <h2>이것은 두 번째 제목입니다.</h2>
              <h1>이것도 첫 번째 제목입니다.</h1>
          </body>
      </html>
      ```

      

  

### 2) CSS의 선택자 1

#### 2.1) 타입선택자

- 선택자: HTML 요소를 선택하기 위해 사용되는 CSS 구문

- 타입선택자(Type Selector)

  - HTML 요소명, 요소의 클래스 속성 값, ID 값
  - 가장 쉽고 선택의 기본이 되는 기초적인 선택자

  1. HTML 선택자

     - 타입 서택자 중에서 HTML 요소가 선택자인 선택자

     - 선택자 형식: HTML 요소명

     - 예

       ```css
       h1 {color: pink;}
       p {padding-lef: 10px} #HTML 선택자
       ```

  2. 클래스 선택자

     - CSS를 적용할 대상: HTML의 클래스 속성 값

     - 클래스 선택자 속성: 요소들을 원하는 그룹으로 묶을 수 있음

     - HTML 문서 내의 동일한 클래스 값을 가지는 모든 요소에 적용

     - 선택자 형식: .(점)으로 시작하는 클래스 속성 값

     - 예

       <html코드>

       ```html
       <p class="mycomment">개인적인코멘트입니다.</p>
       <div class="mycomment">
           <img src="img/fugi.jpg">
           <p class="fignumber">그림 13</p>
       </div>
       ```

       <CSS코드>

       ```css
       .mycomment {color: gray;
       font-weight: bold;}
       .fignumber {font-size:0.8em;
       float:right;}
       ```

       

  3. ID 선택자

     - CSS를 적용할 대상: HTML ID 속성 값

     - HTML ID 속성: HTML 문서 내의 유일한 값으로 고유의 요소 식별

     - HTML 문서 내의 같은 ID를 가진 유일한 요소에 적용

     - 선택자 형식: #(샾)으로 시작하는 ID 속성 값

     - 예

       <HTML코드>

       ```HTML
       <div id="pinkbox">이것은 핑크 상자입니다.</div>
       <div id="greenbox">이것은 그린 상자입니다.</div>
       ```

       <CSS 코드>

       ``` css
       #pinkbox {width:200px;
       height:50px;
       background-color: pink;}
       #greenbox {width:200px;
       height: 50px;
       background-color: green;}
       ```

       <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310082547615.png" alt="image-20200310082547615" style="zoom:80%;" />

   4. 그룹 지정

      - 여러 요소에 동일한 CSS 스타일 적용: 클래스 속성 이용

        => but, 이미 클래스 속성을 적용한 경우 스타일 그룹 위해 클래스 속성 지정 불가

      - 두 개 이상의 요소에 동일한 스타일을 적용하고 싶을 때

      - 그룹 지정 형식: ,(쉼표)로 동일한 스타일 적용할 선택자들 분리해 나열

      - 예

        <CSS 코드>

        ```css
        h1, h2, h3, #sectionTitle {color: brown;}
        ```

        선택자들의 ,(쉼표)분리해 나열한 후 동일한 CSS 적용 방법

        고급 선택자, 의사 클래스에도 동일하게 사용 가능



#### 2.2) 고급 선택자

- 고급 선택자(계층 위치 선택자)

  - 고습 선택자: HTML 문서의 요소들의 계층 관계를 이용하여 선택하는 선택자
  - HTML 요소들의 계층 관계: 자손 요소, 직계 자손 요소, 형제 요소, 인접 형제 요소

  ```html
  <article>
      <section>
          <h1>섹션 제목</h1>
          <p>이것은 <strong>단란</strong>입니다.</p>
          <ol>
              <li>첫 번째 목록</li>
          </ol>
      </section>
  </article>
  ```

  ![image-20200310083316512](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310083316512.png)

  ![image-20200310083346630](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310083346630.png)

  ![image-20200310083412585](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310083412585.png)

- 하위 선택자

  - 하위 선택자: 어떤 요소 하위에 있는 특정 자손 요소 선택 시 사용

  - 표현: (부모 요소)(자손 요소)

    - 예) a b {.....} : a 요소 하위에 있는 b요소를 선택
    - 예) a b c{.....} : a 요소 하위에 있는 b요소의 하위에 있는 c요소 선택

    ![image-20200310090854101](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310090854101.png)

- 직계자손 선택자

  - 직계자손선택자: 바로 하위에 있는 요소 선택 시 사용

    => 여러 단계가 아래 있는 자손을 모두 선택하는 하위 선택자와는 다름

  - 표현: (부모 요소) > (직계 자손 요소)

    - 예) a > b : a 요소 바로 하위(직계 자손 관계)에 있는 모든 b요소 선택

    ![image-20200310091633358](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310091633358.png)

    

- 형제 선택자

  - 형제 선택자: 특정 요소 다음에 나오는 형제 관계 요소들 선택

  - 표현: (요소1) ~ (요소 1의 형제 요소)

    - 예) a ~ b: a 요소 뒤에 있는 모든 b 요소 선택

    ![image-20200310091753930](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310091753930.png)

- 인접 형태 선택자

  - 인접 형태 선택자: 특정 요소 바로 다음에 오는 형제 요소를 선택

  - 표현: (요소1) + (요소 1의 인접 형제 요소)

    - 예) a + b: a 요소 바로 뒤에 있는 b 요소 선택

    ![image-20200310091918579](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310091918579.png)

- 전체 선택자
  - 전체 선택자: 모든 요소를 선택하기 위해 사용

  - 표현:*

    - 예) a *: a 요소 아래 모든 요소를 선택
    - 예) a b~*: a 요소 아래 있는 b 요소 다음 형제 관계의 모든 요소를 선택

    ![image-20200310092102817](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310092102817.png)

    

### 3) CSS의 선택자 2

#### 3.1) 의사클래스

-  의사 클래스(pseudo class)

  - 가짜 또는 모조 클래스, 클래스의 특징을 가짐

  - 형식: :(콜론) 의사 클래스 명

    - 선택자 뒤에 붙어 선택자의 상태를 기준으로 선택

    - :link 의사 클래스: 한번도 클릭하지 않은 링크

      => 히스토리에 없는 링크 상태 의미

  - 예) a:link{...} : 한 번도 방문하지 않은 링크 선택

    ![image-20200310092727111](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310092727111.png)

- 링크 의사 클래스(:link, :visited)

  - 링크 의사 클래스: 링크의 상태 선택자로 이용

  - :link 의사 클래스: 한 번도 방문하지 않은 링크

  - :visited 의사 클래스: 방문한 링크에 CSS 스타일 적용 시 사용

    ![image-20200310092824358](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310092824358.png)

  - 예)

    ![image-20200310092916646](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310092916646.png)

    ![image-20200310092935775](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310092935775.png)

- 동적 의사 클래스

  - 마우스와 커서에 관한 상태를 의사 클래스로 나타냄

  - :active 의사 클래스: 마우스로 클릭했을 때 상태 의미

  - :hover 의사 클래스: 마우스 커서가 올라간 상태 의미

    - 링크 뿐만 아니라 대부분의 요소에 적용 가능
    - HTML과 CSS 만으로 상당히 동적인 페이지 제작 가능

  - :focus 의사 클래스: 서식 폼과 같은 요소에 마우스 위치하여 입력 또는 선택 상황의미

    => 요소가 포커스를 가짐

  - 예제

    ![image-20200310093132791](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093132791.png)

    ![image-20200310093146200](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093146200.png)

    ​	![image-20200310093217316](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093217316.png)

#### 3.2) 구조적 의사 클래스, 의사 엘리먼트

- 구조적 의사 클래스

  - 구조적 의사 클래스

    - HTML 구조에 따른 의사 클래스
    - 형제와 자손 그리고 몇 번째 요소인지로 상태 구분
    - CSS3에서 추가된 내용

  - :root 의사 클래스: 문서의 최상위 요소 의미

    - 단독으로 사용

      ![image-20200310093411163](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093411163.png)

      

  - :empty 의사 클래스: 비어있는 요소 의미

    - HTML 구조에 따른 의사 클래스

    - 형제와 자손 그리고 몇 번째 요소인지로 상태 구분

      ![image-20200310093453492](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093453492.png)

  - :only-child 의사 클래스: 형제가 없는 요소

    자신이 속한 부모 오쇼의 유일한 자손 요소

    ![image-20200310093543813](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093543813.png)

  - :only-of-type 의사 클래스: 같은 타입의 형제가 없을 때 사용

    ![image-20200310093641772](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093641772.png)

    ![image-20200310093656833](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093656833.png)

  - :first-child, :last-child 의사 클래스

    ![image-20200310093734843](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093734843.png)

    ![image-20200310093751492](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093751492.png)

  - :nth-of-type(n), :nth-last-of-type(n) 의사 클래스

    ![image-20200310093835014](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093835014.png)

    ![image-20200310093923219](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310093923219.png)

  - :first-of-type, :last-of-type 의사 클래스

    ![image-20200310094015931](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310094015931.png)

    ![image-20200310094247123](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310094247123.png)

    

- 기타 의사 클래스

  - :lang() 의사 클래스: 지정한 언어 속성을 가지는 요소

    - 예) HTML 문서 전체가 한국어

      <html lang='ko'>

    - 하나의 HTML 문서에 다양한 국가의 언어 사용할 경우 해당 언어가 사용된 요소 적용

      ![image-20200310094501896](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310094501896.png)

  - :not()의사 클래스: 부정을 읨

    - () 안에 선택에서 제외될 선택자 삽입

      ![image-20200310094559850](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310094559850.png)

      ​	=> :not() 의사 클래스는 진정한 논리 의사 클래스라고 할 수 있음

      

- 의사 엘리먼트

  - 가짜 요소, 선택자에 따라 기존 요소에 추가로 새로운 요소 정의

    => 독립된 스타일 적용 가능

  - :first-letter 의사 엘리먼트: 선택자에서 선택한 요소의 첫 번째 글자를 새 요소로 만듦

    - 첫 번째 글자에 새로운 스타일 적용 가능
    - 문단의 첫 글자 확대, 들여쓰기 가능

  - :fist-line 의사 엘리먼트: 선택자에서 선택한 요소의 첫 번째 줄을 새 요소로 만듦

    ![image-20200310094819534](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310094819534.png)

  - :after, :befor 의사 엘리먼트: 선택자에 의해 선택된 요소 앞 뒤에 요소를 만듦

    ![image-20200310094857636](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310094857636.png)

#### 3.3) 속성 선택자

- 속성을 이용한 선택

  - 속성 선택자: HTML 요소들의 다양한 속성 적용

  - 형태: a[title]{color: pink;}

    => title 속성이 있는 <a> 요소 선택

    ![image-20200310095011176](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095011176.png)

- 속성과 속성값 선택자

  - 속성과 속성값을 모두 이용하는 속성 선택자

    - 형태: 선택자[속성='속성값']

    ![image-20200310095213959](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095213959.png)

- 속성 선택자 등식 연산

  - 속성과 속성값 선택자는 속성 값이 정확히 일치하는 요소 선택

    => 하이퍼링크 속성이 외부 URL의 형태를 가진 요소를 선택하기 위해서는 어려움 존재

    ![image-20200310095311941](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095311941.png)

  - 다양한 등식을 통하여 원하는 선택 가능

    - 예) a[href^="http://"]{color : pink;}

      => 하이퍼링크 속성 값이 "http://" 로 시작하는 a요소 선택

      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095537574.png" alt="image-20200310095537574" style="zoom:120%;" />

      

- 미디어 쿼리

  - 현재 HTML문서가 보여지는 화면이 어떤 것인지를 파악

    => 각종 기기에 따라 다른 CSS 스타일 지정 가능

  ![image-20200310095621237](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095621237.png)
  - 미디어쿼리 구문: link 요소에 속성으로 적용

    - 미디어쿼리값 + 미디어쿼리 속성

    - 예) 외부 CSS 파일 연결을 위해 링크 요소 사용, media 속성으로 미디어쿼리 적용

      ![image-20200310095743288](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095743288.png)

    - 미디어쿼리 값

      - 현재 CSS3에서 지원하는 미디어쿼리

        ![image-20200310095823998](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095823998.png)

      - 디바이스의 최소 넓이나 최대 넓이 등을 제한하는 미디어쿼리 속성값

        ![image-20200310095853473](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310095853473.png)

      - 전체 미디어쿼리 속성값: https://www.w3.org/TR/css3-mediaqueries/

- 상속과 캐스케이딩

  - HTML 요소에 적용된 CSS 스타일도 하위 자식에게 상속

  - 예) 계층 구조로 작성된 HTML

    ![image-20200310100003673](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310100003673.png)

    ![image-20200310100010257](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310100010257.png)

    - CSS 단계적 순서로 스타일 적용

    - 적용 우선 순위: 부모로부터 상속된 스타일이 사용자 정의보다 적용 우선순위 낮음

    - h2(사용자 직접 정의)가 header에서 상속되어 먼저 적용 -> 빨간색

      ![image-20200310112336018](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310112336018.png)

      

  - 적용 우선 순위 단계

    ![image-20200310100231205](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310100231205.png)

  - Css 적용 우선 순위(cascading order)

    1. 중요도(!important)
    2. 우선 순위
       - 인라인/id 선택자/class 선택자/요소 선택자
    3. 소스 순서