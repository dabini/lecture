# HTML5/JavaScript

## 1. HTML5의 이해



> 용어알기
>
> W3C 
>
>  World Wide Web Consortium의 약자로 웹 표준을 개발하고 논의하며 제정하는 조직
>
> DOCTYPE
>
> HTML의 문서형식 선언으로 HTML 및 마크업언어의 DTD 또는 버전을 명시한다.
>
> metadata
>
> 문서 또는 파일에 관한 정보를 제공하는 내부 데이터



### 1) HTML5의 탄생과 의미

- HTML이란

  -  **Hyper Text Markup Language** 의 약자

  - **웹용 콘텐츠(글 또는 그림 등)의 구조를 지정하는** 컴퓨터 언어

  - HTML은 **웹서버에 저장**되며 클라이언트 웹 브라우저의 요구에 따라 불려지는 문서

  - 웹 브라우저에 불려진 HTML은 웹브러우저에 의해 읽혀지고 해석되어 화면에 보여진다.

    

- HTML의 탄생과 발전 

  - 1990년 월드 와이드 웹과 함께 탄생 

  - 웹의 발전으로 웹 브라우저의 중요성 확대

  - ‘넷스케이프 네비게이터’와 ‘마이크로소프트 인터넷 익스플로러’의 시장 점유율 전쟁으로 **HTML과 CSS의 비표준 심화 **

    - 웹 브라우저 전쟁

      ![image-20200309101235541](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309101235541.png)

      

  - 새로운 웹 브라우저가 등장하면서 웹의 표준화 논의 

  - 웹 표준을 개발하고 논의하며 제정하는 W3C(World Wide Web Consortium) 

  - 1997년 W3C HTML3.2 권고 – 시장 요구에 의해 비표준 HTML 포함 

  - 1999년 HTML 4.01 권고 – 시장 요구에 의해 다양한 버전 등장 

  - 2000년 XHTML 권고 – XML의 엄격함을 주요 내용으로 한 웹 표준 

  - W3C는 XHTML2 개발 추진 하다 돌연 HTML5로 방향 전환

    ![image-20200309101406205](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309101406205.png)

- HTML5의 탄생 

  - 기존 HTML의 한계
    - 웹 기반 사업과 기술의 발전을 못 따라간 XHTML 
    - 동적인 웹을 위한 표준화 된 기술을 요구
    - W3C의 XHTML2로의 발전 예고 

  ![image-20200309101628501](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309101628501.png)

  ![image-20200309101749354](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309101749354.png)

  ![image-20200309101854350](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309101854350.png)

  

  - WHATWG((Web Hypertext Application Technology Working Group) 탄생 

    - 시장 요구에 부응하지 못하는 W3C에 실망한 웹 관련 업체와 단체가 자체적으로 만든 워킹 그룹 
    - 웹 기술과 시장의 요구를 분석하여HTML5 명세서 작업 착수

  -  W3C의 HTML5 수용 

    - 2008년 W3C HTML5 초안 발표 
    - 2009년 XHTML2 개발 중단 
    - 2014년 XHTML5 권고 예정 

  - HTML5의 특징 

    - 기존 HTML과의 호환성 유지 

    - 실용적 설계: 느슨한 문법, 기존 HTML의 효율적인 추가 요소, 안전한 보안 

    - 표현과 내용의 완벽한 분리

    - 플러그인 없이 각종 미디어 처리 및 동적인 작동: 캔버스

      자체적으로 2D, 3D 처리 가능

      웹 브라우저가 다양한 미디어 처리

      다양한 이벤트 제공

    - 최신 웹 기술 수용: 지오로케이션, 웹소켓, 웹스토리지, 웹워커 등

  ![image-20200309102123160](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309102123160.png)

### 2) HTML5 시작하기

- 텍스트 에디터

  - HTML은 텍스트 파일
  - 단순 텍스트 파일을 생성하는 어떠한 텍스트 에디터에서도 작성 가능
    - 메모장, 워드패드, 워드프로세서
  - 전문적인 텍스트 에디터: 각종 컴퓨터 언어 프로그래밍에 최적화-
  - 장점
    1. 코드 인식률을 높이기 위한 텍스트 컬러링
    2. 에러 확인을 편하게 해주는 라인 넘버링
    3. 코드 정리를 도와주는 인덴트 기능
    4. 편리한 텍스트 이동
    5. 코드 제안과 자동 완성
    6. 향상된 검색과 치환 기능
    7. 기타 프로그래밍 관련 기능들
  - 무료로 사용할 수 있는 전문적인 텍스트 에디터
    - notepadd++
    - komodo Edit
    - Apatana Studio 3

- Doctype 지정하기

  - Doctype 지정이유:

    HTML은 여러 버전이 존재하므로Doctype을 명시해야 한다. 

  - 기존 Doctype 은 매우 길고 복잡한 DTD를 명시해야 했었다.

  -  HTML5의 실용성 원칙으로 인해 짧아졌다. 

  -  <!DOCTYPE html>

  - ![image-20200309103148936](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309103148936.png)

- HTML 작성 규칙 

  -  HTML의 마크업 명령은 **요소**라 부른다. 

    - HTML은 마크업 언어이므로 콘텐츠와 함께 사용
    -  HTML은 대소문자를 구분하지 않는다.

  - HTML 요소의 표현

    - 요소는 콘텐츠와 구분을 위해서 꺽쇠로 둘러싼다. 

      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309103329061.png" alt="image-20200309103329061" style="zoom:80%;" />

      - 태그 <p>, <a>, <div>

  - 요소의 범위

    - 시작태그와 마침태그로 요소의 범위를 지정한다. 

      <p>이것은 단락 입니다.</p> 

      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309103419107.png" alt="image-20200309103419107" style="zoom:80%;" />

      

    - 마침태그가 없이 단독으로 사용되는 요소도 있다.
      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309103457381.png" alt="image-20200309103457381" style="zoom:80%;" />

       <br>,  <img>, <meta> 등 

  - 요소의 속성 기술

    <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309103527246.png" alt="image-20200309103527246" style="zoom:80%;" />

    - 요소의 속성은 속성명 = “속성값” 형식으로 기술한다.

       <img src=”img/logo.jpg” alt=”Company Logo”>

    

- HTML의 구조

<!Doctype html> <html> <head> </head> <body> </body> </html>
§ <html>은 HTML 코드 전체를 감싼다. § HTML은 <head>와 <body> 부분으로 나뉜다. § <head>는 메타데이터와 스크립, CSS등이 위치한다. § <body>부분은 콘텐츠가 담기는 곳으로 웹 브라우저에 표시된다.

```html
<!DOCTYPE html>
<html>
	<head>
        
    </head>
    <body>
        
       
    </body>
</html>
```

![image-20200309103655930](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309103655930.png)



### 3) HEAD 설정하기

- 타이틀 지정 

  -  HTML 파일의 제목으로 웹 브라우저 타이틀에 나타난다. 

  - 즐겨찾기나 북마크를 저장할 때도 사용되므로 적절한 제목을 선택해야 함.

  - 타이틀 지정 예

    ```html
    <title>웹 페이지 제목</title>
    ```

    

- 문자 인코딩 

  - 사용하는 텍스트 에디터의 문자 인코딩과HTML의 문자 인코딩과 동일해야 웹 브라우저에서 옳바르 게 표시된다. 

  - 유니코드인 UTF-8로 지정한다.

    ```html
    <meta charset='UTF-8'>
    ```

    

- 메타데이터 

  파일에 관한 정보를 가지고 있는 데이터

  - 메타데이터를 기술 하면 웹 검색에 유리하다. 
  -  HTML에 대한 정보를 기록할 수 있다.
  - 

  - 메타데이터 기술 방법 

    ```html
    <head>
        
    	<meta name="description"content="HTML5와 Javascript 학습콘텐츠">
        #description: HTML 파일의 간략한 설명 기술
    	<meta name="keywords" content="HTML5, CSS, JavaScript"> 
        #keywords: HTML 파일의 키워드
        <meta name="author"content="Lee HaeBum"> 
        #author: HTML 파일의 작성자
    	<meta name=”copyright” content=”©2012 Lee HaeBum”> 
        #copyright: 저작권 정보
    	<meta name="reply-to" content=gomtomi@imacca.com> 
        #reply-to: 연락처 메일 입력
    	<meta name="date" content="2012-05-30T12:35:20+09:00">
        #date: HTML 파일의 작성일
    </head>
    ```



- 외부 파일 연결

  - 웹페이지는 HTML, CSS, JavaScript 3가지로 이루어짐

    - HTML: 콘텐츠의 구조 정의
    - CSS: 콘텐츠의 레이아웃과 표현 등 외향을 정의
    - JavaScript: 콘텐츠의 작동을 정의

    HTML과 함께 사용되는 CSS와 자바스크립트는 다른 파일로 분리함이 원칙이다.

  - 외부 CSS 파일 연결

     <link rel="stylesheet" href="css/style.css">

  - 외부 자바스크립트 파일 연결 

    <script src="js/script.js"></script>

  ![image-20200309105101007](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309105101007.png)

  ```html
  <!DOCTYPE html>
  <html lang='en'>
      <head>
          <meta charset = "utf-8">
          <title></title>
      </head>
  </html>
  ```

  