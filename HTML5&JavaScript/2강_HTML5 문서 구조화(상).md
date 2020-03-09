# HTML5/JavaScript

## 2. HTML5 문서구조화(상)

>용어 알기
>
>표현적 마크업:
>
>콘텐츠의 레이아웃과 디자인을 정의하는 마크업
>
>블록 레벨 요소:
>
>줄바꿈으로 분리되는 하나의 독립된 덩어리 요소
>
>정의 목록:
>
>사전식 정의를 위해 사용되는 목록



### 1) 구조적 마크업의 이해

- 구조적 마크업은 문서의 구조를 정의 

- 표현적 마크업은 문서의 외형을 정의 

- 구조적 마크업과 표현적 마크업의 혼용 

  - 오래된 HTML은 구조적 마크업과 표현적 마크업을 혼용해 사용

    => HTML 표현의 한계

  - 현재 웹 표준에서는 표현적 마크업을 HTML에서 퇴출 

  - 문서의 구조는 HTML을 사용, 문서의 표현은 CSS를 사용 

-  구조적, 표현적 마크업 혼용 사용의 문제점 

  - 표현적 요소의 사용은 접근성을 저해 => 웹 접근성 저해
  - 더 높은 유지비용 발생 
  - 문서 크기 비대화

- 블록 레벨 요소와 인라인 레벨 요소 

  - 블록 레벨 요소: 줄 바꿈이 일어나는 단락 요소 

    - 제목, 문단, 인용문
    - 블록 레벨 요소 안에 인라인 레벨 요소 또는 다른 블록 레벨 요소가 들어갈 수 있음

  - 인라인 레벨 요소: 줄 바꿈이 일어나지 않는 행의 일부 요소

    - 강조, 링크, 이미지
    - 인라인 레벨 요소 안에는 다른 인라인 레벨 요소를 포함할 수 있으나 블록 레벨 요소는 포함 불가

    

### 2) HTML5의 섹션 요소

- 섹션 요소

  - 구역 또는 장
  - 의미가 연결되는 콘텐츠의 집합
  - 자체적으로 제목과 내용을 가질 수 있는 하나의 독립적인 콘텐츠 단위

- HTML5의 섹션 요소

  - div 요소에 아이디, 클래스 속성을 적용하여 섹션 분리
  - HTML5 자주 사용하는 섹션을 추려 새로운 요소로 추가

- 추가된 섹션 요소

  1. section: 범용 섹션 요소

  - 의미
    - 일반적인 문서 또는 프로그램의 섹션
    - 보통 제목을 시작하는 콘텐츠의 의미적 그룹
    - 문서의 영역을 지정하는 레이아웃을 생성
    - 의미 없이 프로그래밍을 위한 분리에는 사용하지 않음

    ![image-20200309131813172](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309131813172.png)

  2. `<nav>`: 네비게이션 요소

  - 의미

    - 네이게이션 링크로 구성되는 섹션
    - 하나의 페이지에 하나 이상의 nav 요소가 사용
    - 블로그 등의 '페이지 삭제', '수정' 등은 네비게이션 요소 아님
    - 목록으로 작성

    ![image-20200309132032424](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132032424.png)

  3. `<article>`

  - 의미

    - 독립적으로 배포 혹은 재사용 가능한 섹션
    - 독립적인 글

    ![image-20200309132115423](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132115423.png)

  4. `<aside>`

  - 의미

    - 문서의 주요 콘텐츠와 별개의 영역 정의
    - 일반적으로 사이드 바 형태로 표현

    ![image-20200309132214733](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132214733.png)

  5. `<header>`

  - 의미

    - 페이지 또는 섹션의 머릿글 그룹
    - 페이지의 제목, 소개, 네비게이션 등의 포함
    - 섹션 요소가 아니므로, 새로운 섹션을 의미하지 않음

    ![image-20200309132316601](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132316601.png)

  6. `<footer>`

  - 의미

    - 가장 가까운 조상 요소의 footer
    - 일반적으로 연관 문서에 대해 정보를 담음(작성자, 링크, 저작권 정보.. 등)
    - 섹션 요소가 아니므로 새로운 섹션이 아님

    ![image-20200309132425765](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132425765.png)

  7. 헤딩과 `<hgroup>`

  - 헤딩

    - 섹션의 제목
    - h1 ~ h6까지 존재(h1 > ... > h6)
    - HTML5에서는 헤딩을 순서대로 사용하지 않아도 됨.

    ![image-20200309132518486](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132518486.png)

  - `<hgroup>`

    - 섹션의 제목 그룹(h1~h6 요소들을 그룹 짓기 위해 사용)
    - <hgroup>은 포함된 헤딩 요소의 가장 높은 등급
    - 서브 타이틀의 범주의 생성을 감추기 위해 사용

    ![image-20200309132618877](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132618877.png)

  8. 제목에 따른 섹션 분리

  - 섹션 요소의 구조 결정

    - 요소를 겹처 상위 요소와 하위 요소를 생성
    - 섹션 내부에서는 타이틀(헤딩)의 등급에 따른 구조화
    - 헤딩 요소: 섹션의 시작은 표기 되지만, 섹션의 끝은 표기 되지 않음.

    ![image-20200309132831282](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132831282.png)

  9. `<address>`

  - 의미

    - 가장 가까운 조상 요소인 article 또는 body 요소의 연락처 정보 의미
    - 영향력: 가장 가까운 조상 요소에 한정
    - 내용: 연락처 정보의 형태라면 어떤 형태라도 허용

    ![image-20200309132955771](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309132955771.png)



### 2) 그룹 콘텐츠 요소

- 그룹 콘텐츠 요소

  - 그룹으로 내용을 분리하는 역할을 하는 요소
  - 기존 HTML의 요소가 대부분
  - 콘텐츠의 역할을 정의

- 문단과 인용

  1. `<p>` : 콘텐츠의 문단 의미

  - 의미
    - 마지막에 P요소 하나만 사용해 문단을 분리하는 방법으로 잘못 사용
    - 정확한 사용법: 문단의 시작과 끝에 P요소 정확히 지정

  ![image-20200309133442479](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309133442479.png)

  - 콘텐츠 중 문단이긴 하나 더 적합한 요소가 존재하는 경우:

    - p요소보다 더 적합한 요소 사용 => 좀 더 구조적

      ![image-20200309133523288](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309133523288.png)

  2. `<blockquote>` :인용을 의미

  - 의미

    - 인용된 소스의 cite 속성으로 URL 주소 표시
    - blockquote 안에 p요소를 넣어도 되고 안 넣어도 됨.

    ![image-20200309133708870](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309133708870.png)

    

  3. `<pre>` : 형식화된 텍스트 블록 표현

  - 의미

    - 공백을 포함한 입력한 텍스트가 그대로 웹 브라우저에 출력
    - pre 요소는 웹 브라우저에 고정폭 서체로 표현
    - 컴퓨터 코드나 문자 그림을 표현하는데 적합

    ![image-20200309133814460](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309133814460.png)

  4. `<hr>` : 문단 레벨에서 주제의 분리

  - 의미

    - 문단 레벨에서 주제의 분리를 나타냄
    - 씬 전환 또는 참고서의 섹션 내에서 다른 화제로의 전환 등
    - 시각적으로는 분리를 위한 선이 하나 보이지만 표현적 마크업으로 사용하면 안 됨.

    ![image-20200309133947048](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309133947048.png)

    ![image-20200309133955954](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309133955954.png)

- 목록

  - 텍스트 콘텐츠를 설명하기 위해 자주 사용되는 구조
  - 순서 있는 목록, 순서 없는 목록, 정의 목록

  1. 순서 있는 목록: 순서가 바뀌면 의미가 바뀌는 목록

     - `<ol>`요소: 순서가 있는 목록 정의
     - `<li>`요소: `<ol>`의 자식 요소로 목록의 아이템 역할

     ![image-20200309134147190](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309134147190.png)

     ![image-20200309134251564](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309134251564.png)

     

  2. 순서 없는 목록

     - `<ul>`요소: 순서 없는 목록 정의
     - `<li>`요소: 목록 아이템 표현
     - 목록 앞에 숫자 대신 말머리 기호 나타남

     ![image-20200309134328361](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309134328361.png)

     

  3. 정의 목록

     - 사전식 정의를 위해 사용
     - 하나 이상의 '정의 제목'과 '정의 내용'의 쌍으로 이루어짐

     ![image-20200309134358522](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309134358522.png)

     ![image-20200309134422218](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309134422218.png)

- 기타 그룹핑

  1. `<figure>`, `<figcaption>`

  - figure 요소
    - 일반적으로 사진, 일러스트, 비디오 등을 표시하고 주석을 다는 용도
    - 제거하거나 위치를 옮기더라도 문서의 주된 흐름에는 영향을 미치지 않음
    - figcaption 요소를 포함

  - figcaption 요소: figure 요소 내용에 대한 캡션

  ![image-20200309134601999](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309134601999.png)

  2. `<div>`

  - 구조적으로 특별한 의미가 전혀 없음
  - 스타일 또는 스크립트 목적으로 콘텐츠를 분리하기 위해 사용
  - 단순목적의 분리로만 사용해야 함

- id, class, title

  - 전역 속성으로 모든 요소에서 속성으로 사용 가능

  ![image-20200309134933056](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309134933056.png)



### 3) 텍스트 관련 요소

- 텍스트 관련 요소

  - 텍스트 구조를 나타내는 온라인 레벨요소

  1. `<a>`

  - 하이퍼링크를 나타냄
  - href 속성으로 링크 경로 저장

  ![image-20200309141730631](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309141730631.png)

  ​	=>target 속성은 href 속성이 있을 때만 사용 가능

  2. `<em>`, `<strong>`

  - em 요소: 내용을 강조하기 위해 사용
  - strong 요소: 내용이 중요함을 표시
  - 요소를 중첩해 강조와 중요함의 정도를 표현 가능

  ![image-20200309141848466](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309141848466.png)

  3. `<q>`, `<cite>`

  - q 요소: 인용을 나타내는 인라인 요소
  - `<blockquote>`를 사용하여 인용된 단락 표현
  - `<q>` 요소로 인용 구두점을 사용하면 안 됨
  - `<cite>` 요소: 인용 문구의 원본 주소, 즉 작품의 제목 언급이나 참조했을 때 사용

  ![image-20200309142102994](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309142102994.png)

  4. `<abbr>`

  - 약어 및 두문자어 나타냄
  - title 속성 : <abbr>에서 사용할 때만 원형 표시 가능
  - 특정 약어 스타일을 적용하고자 할 때 span 대신 사용 가능

  ![image-20200309142225628](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309142225628.png)

  5. `<i>`, `<b>`

  - i와 b 요소는 예전 버전의 HTML에서 표현적 마크업 요소

  - HTML5에서 자주 사용하는 표현적 마크업에 구조적 의미를 부여

  - `<i>`요소: 가장 주된 사용은 다른 언어 표현

    (영문에서 이텔릭체로 표현하는 숙어 인용, 분류학 등에 사용)

  - `<b>`요소: 의미있는 중요성을 부가하지 않고 눈에 띄게 하기 위해 사용

    ![image-20200309142437931](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309142437931.png)

  6. `<sup>`, `<sub>`

  - `<sup>`요소: 위첨자

  - `<sub>`요소: 아래 첨자

    ![image-20200309142542887](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309142542887.png)

  7. `<span>`, `<br>`, `<img>`

  - `<span>`요소

    - 아무 의미도 가지고 있지 않음
    - 단지 인라인 레벨에서 스타일을 적용하거나 스크립트에서 사용하고자 콘텐츠를 분리하는 역할

  - `<br>`요소

    - 마침 요소 없이 사용되면 문단 분리가 아닌 단순 줄바꿈을 표시

    - 단락 분리의 의미로 사용해서는 안되며 시 또는 주소 작성 등에 사용

      ```html
      <p>
          P.sherman<br>
          42 Wallaby Way<br>
          Sydney
      </p>
      ```

      

  - `<img>`요소

    - 이미지를 의미

    - 마침 요소가 없이 단독으로 사용

    - 디자인을 위한 이미지를 지정에 사용하면 안됨

    - src 속성에 이미지의 경로를 지정

    - alt 속성은 이미지를 대체하기 위한 텍스트

      ```html
      <img src="images/tim.jpg" alt="웹의 창시자 팀 버너스리경"
      ```

      