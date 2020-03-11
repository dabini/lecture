# HTML5/JavaScript

## 6. 레이아웃과 고급 CSS 기능

> 용어알기
>
> - 2단 레이아웃
>
>   웹에서 흔히 사용되는 좌우 두 단으로 나눠져 있는 레이아웃
>
> - 롤오버 단추
>
>   마우스가 단추 위로 올라갔을 때 모양이나 색이 변화하여 누를 수 있는 단추라는 것을 사용자에게 알려 주는 기능을 가진 단추
>
> - 트랜지션
>
>   요소의 속성이 변화하는 과정을 보여주는 CSS 기능



# **HTML5/JavaScript**

## **6. 레이아웃과 고급 CSS 기능**

> 용어알기

- 2단 레이아웃

  웹에서 흔히 사용되는 좌우 두 단으로 나눠져 있는 레이아웃

- 롤오버 단추

  마우스가 단추 위로 올라갔을 때 모양이나 색이 변화하여 누를 수 있는 단추라는 것을 사용자에게 알려 주는 기능을 가진 단추

- 트랜지션

  요소의 속성이 변화하는 과정을 보여주는 CSS 기능

### 1) 레이아웃 정렬

#### 1.1) 2단 레이아웃

- float 속성을 사용한 2단 레이아웃

  웹페이지에 많은 내용을 정리하려면 다단 레이아웃을 사용하는 것이 편리

  - 다단 레이아웃: 화면을 세로로 여러 개의 단으로 나눠 콘텐츠를 보여주는 형태

  - HTML 문서는 오로지 위에서 아래로 콘텐츠 제시

    ⇒ 다단 레이아웃 제작 시 플로팅, 포지셔닝 사용

  ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능/Untitled.png)

- float 속성을 사용한 2단 레이아웃 설정 방법

  - float 속성을 사용한 2단 레이아웃 설정 방법

    1. HTML 문서 준비하기

       ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능/Untitled (1).png)

       외형에 신경쓰지 않고 정확한 구조로 작성

       - HTML 코드 확인하기

       ```html
       <!DOCTYPE html>
       <html lang="ko">
       <head>
       	<meta charset="utf-8">
       	<title>Title</title>
       	<link rel="stylesheet" href="style.css">
       </head>
       <body>
       	<div id="wrapper">
       		<header><h1>Site Title</h1></header>
       		<section>
       			<nav>
       				<ul>
       					<li><a href="#">About</a></li>
       					<li><a href="#">Products</a></li>
       					<li><a href="#">Portfolio</a></li>
       					<li><a href="#">Custom Service</a></li>
       					<li><a href="#">Contact</a></li>
       				</ul>
       			</nav>
       			<section>
       				<article>
       					<h2>1st Article Title</h2>
       					<p>Lorem ipsum dolor sit amet, consectetuer adipis cing elit, sed diam nonummy nibh euismod tinci dunt ut laorenim ad minim veniam, quis nostrud exerci tation ullam corper suscipit lobortis nisl ut aliq eet dolore magna aliquam erat volut pat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet.</p>
       				</article>
       				<article>
       					<h2>2nd Article Title</h2>
       					<p>Lorem ipsum dolor sit amet, consectetuer adipis cing elit, sed diam nonummy nibh euismod tinci dunt ut laorenim ad minim veniam, quis nostrud exerci tation ullam corper suscipit lobortis nisl ut aliq eet dolore magna aliquam erat volut pat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet.</p>
       				</article>
       			</section>
       		</section>
       		<footer>
       			<p>Lorem ipsum dolor sit amet, consectetuer adipis cing elit</p>
       		</footer>
       	</div>
       </body>
       </html>
       ```

       

    2. 섹션 요소의 넓이 설정하기

       - CSS 이용하여 HTMl 요소의 스타일 지정

         => 다단 레이아웃에서 섹션 요소 넓이 지정이 가장 중요

       - 전체 요소 margin과 padding 0으로 설정

         ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\3.JPG)

         => 요소 간의 여백이 사라짐

       - 섹션 요소 넓이 설정

         - wrapper: HTML 페이지 고정된 크기 설정

         - 최종 요소의 넓이: margin넓이 + padding 넓이 + border의 굵기

           ```css
           #wrapper{
               width: 700px; #전체넓이 700px 설정
           }
           ```

         - header: 680px = 700px -20px (패딩 10px씩)

           ![image-20200311092609137](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\4.JPG)

           ```css
           header{
               width: 680px;
               height:80px;
               padding:10px;
               background-color:lightgray;
           }
           nav {
               width:160px;
               height:380px;
               padding:10px;
               background-color:gray;
           }
           nav+section{
               width: 500px;
               height: 380px;
               padding: 10px;
               background-color:darkgray;
           }
           footer {
               padding: 5px;
               background-color:black;
           }
           ```

           

    3. float 속성 설정하기

       - float 속성: left, right

       - 2단 레이아웃 만들기

         - 방법:

            nav 요소 - 왼쪽으로 floating

           nav + section 요소 - 오른쪽으로 floating

           ```css
           nav {
               width:160px;
               height:380px;
               padding:10px;
               background-color:gray;
               float:left;
           }
           nav+section{
               width: 500px;
               height: 380px;
               padding: 10px;
               background-color:darkgray;
               float:right;
           }
           ```

         - footer 요소에 clear 속성 적용하기

           1. nav 요소와 nav+section 요소 높이 같게 지정

           2. footer 요소에 clear 속성 설정

              => 여러단의 높이 CSS 에서 수치 맞출 시 관리의 어려움

              => footer의 경우: clear:both;로 설정

           ```css
           footer{
               clear:both;
               padding:5px;
               background-color:black;
           }
           ```

         - 디자인 스타일을 적용하여 정리하고 꾸밈

    4. 2단 레이아웃 완성하기

       ```CSS
       * {
       	margin: 0;
       	padding: 0;
       }
       
       #wrapper {
       	width: 700px;
       	background-color: gray;
       }
       
       header {
       	width: 680px;
       	height: 80px;
       	padding: 10px;
       	background-color: lightgray;
       }
       
       nav {
       	width: 160px;
       	padding: 10px;
       	float: left;
       }
       
       nav+section {
       	width: 500px;
       	padding: 10px;
       	background-color: darkgray;
       	float: right;
       }
       
       footer {
       	clear: both;
       	padding: 5px;
       	background-color: black;
       	color: white;
       }
       
       body {
       	font-size: 0.9em;
       	font-family: "Lucida Grande", Tahoma, Verdana, Arial, Helvetica, sans-serif;
       }
       
       p {
       	margin-bottom: 20px;
       }
       
       li {
       	list-style: none;
       	margin-bottom: 10px;
       }
       
       a {
       	text-decoration: none;
       	color: white;
       }
       
       a:hover {
       	color: red;
       }
       ```

       

- position 속성을 이용한 2단 레이아웃 설정 방법

  - float 속성 설정보다 position 속성 사용 시 몇 가지 더 신경써야함

  - 상대 위치와 절대 위치

    - 상대 위치: 요소 위치 설정 시, 초기 위치에 자신의 볼륨을 그대로 유지

      => 좌표의 원점을 파악하기 어려움

    - 절대 위치: 요소들의 원점 - 부모 요소의 왼쪽 상단으로 통일

      => 요소의 볼륨에 따른 레이아웃 변화에 적용되지 않음

    제작하고자 하는 레이아웃에 어떤 포지셔닝이 필요한지 고려 후, 적용할 것

  - 절대 위치 포지셔닝을 통한 2단 레이아웃 설정하기

    - 절대 위치 포지셔닝을 통한 2단 레이아웃 설정하기

      - 절대위치 포지셔닝 사용시, 본문 article 길이에 따라 footer의 위치 결정되지 않음.
      - footer가 header 요소 아래에 위치

      ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\5.JPG)

    - 절대 위치로 포지션 설정 시 주의 사항

      자유로운 레이아웃이 가능

      절대 요소로 설정한 요소의 형제와 자식 요소 대부분 절대 요소로 지정하여 수치로 위치를 조정해야 함

  - 절대 위치에서 2단 레이아웃 구현

    ```CSS
    * {
    	margin: 0;
    	padding: 0;
    }
    
    #wrapper {
    	width: 700px;
    }
    
    body {
    	font-family: "Lucida Grande", Tahoma, Verdana, Arial, Helvetica, sans-serif;
    	font-size: 0.8em;
    	
    }
    
    header {
    	width: 680px;
    	height: 80px;
    	padding: 10px;
    	background-color: lightgray;
    	font-size: small;
    }
    
    nav {
    	width: 160px;
    	height: 420px;
    	padding: 10px;	
    	background-color: gray;
    	position: absolute;
    }
    
    nav+section {
    	width: 500px;
    	height: 420px;
    	padding: 10px;
    	background-color: darkgray;
    	position: absolute;
    	left: 180px;
    }
    
    footer {
    	width: 690px;
    	padding: 5px;
    	background-color: black;
    	color: white;
    	position: absolute;
    	top: 540px;
    }
    
    p {
    	margin-bottom: 20px;
    }
    
    li {
    	list-style: none;
    	margin-bottom: 10px;
    }
    
    a {
    	text-decoration: none;
    	color: white;
    }
    
    a:hover {
    	color: red;
    }
    ```

  - 상대 위치 포지셔닝을 통한 2단 레이아웃 설정하기

    - 상대 위치 포지셔닝 설정: 원래 자신의 위치 원점으로 선정

    - left, top 등의 속성 사용하지 않을 시, 일반적인 문서 흐름대로 제시

    - 상대 위치에서 2단 레이아웃 만들기

      - 마이너스 좌표로 세밀하게 좌표 설정
      - nav 요소, nav+section요소, footer요소 모두 조정 필요

      ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\6.JPG)

- display 속성을 이용한 2단 레이아웃 설정하기

  블록 레벨 요소들을 inline-block 형태로 줄바꿈 없이 나란히 놓을 수 있음

  ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\7.JPG)

  - display: inline-block; 설정시, 블록이 글자와 같이 취급

    => 각 블록 사이에 기본 자간 표시

    => 요소 사이 여백 발생

    "white-space-collapse" 속성 사용하면 되나 현재 구현되지 않음

  ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\8.JPG)



### 2) CSS 네비게이션

#### 2.1) 인터렉티브 이미지 버튼

- HTML 이미지 버튼

  - HTML 이용시 이미지 버튼을 만들 수 있음

- CSS 인터렉티브 이미지 버튼

  - 버튼 이미지 제작

    ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\9.JPG)

    [CSS코드]

    ```css
    a.button {
    	display: block;
    	width: 160px;
    	height: 19px;
    	background-image: url(images/button.png);
    	background-position: 0 0;
    	font-family: "Lucida Grande", Tahoma, Verdana, Arial, Helvetica, sans-serif;
    	color: #333;
    	text-align: center;
    	padding: 8px 0;
    	text-decoration: none;
    }
    
    a.button:hover {
    	background-position: 0 -35px;
    }
    
    a.button:active {
    	background-position: 0 -70px;
    }
    ```

    - a요소: inline- label 요소

      width, height 속성 이용하여 크기 조절 불가

      display: blcok; 설정

    - a요소의 크기: 디자인한 이미지 크기에 맞춤(위, 아래 패딩 크기 제외)

    - 버튼 이미지: 배경 이미지로 설정

    - 버튼 텍스트 설정: 텍스트 정렬 - 가운데/적절한 패딩 설정

    - 롤오버, 클릭시 버튼 이미지 바꾸는 효과 주기

      a.button:hover: 버튼에 마우스 오버 시 스타일 적용

      a.button:active: 버튼 클릭시 스타일 적용

  - 완료 이미지

    ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\10.JPG)



#### 2.2) 네비게이션 만들기

- 텍스트 네비게이션

  - 네이게이션: 웹사이트에서 분류된 영역으로 쉽게 갈 수 있는 링크의 모음

    - 초창기: 텍스트 네비게이션 => 현재: 그래픽 네비게이션으로 발전
    - 웹 초창기: 텍스트 네비게이션 => 제작하기 쉽고 로딩이 빨라 현재도 많이 사용

  - HTML으로 텍스트 네비게이션 구조 작성하기

    - nav 요소 안에서 작성

    - 네비게이션 HTML 작성 방법: 목록 형태 => 링크의 목록으로 작성

    - 목록 작성 시 순서는 상관 없음: 

      <ol>순서있는 목록/ <ul> 순서없는목록

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  	<head>
  		<meta charset="utf-8">
  		<title>Title</title>
  		<link rel="stylesheet" href="style.css">
  	</head>
  	<body>
  		<nav>
  			<ol>
  				<li><a href="https://plus.google.com/">+누구?</a></li>
  				<li><a id="current" href="http://www.google.co.kr/webhp">검색</a></li>
  				<li><a href="http://www.google.co.kr/imghp">이미지</a></li>
  				<li><a href="http://maps.google.co.kr">지도</a></li>
  				<li><a href="https://play.google.com">Play</a></li>
  			</ol>
  		</nav>
  	</body>
  </html>
  ```

  ![](D:\lecture\HTML5&JavaScript\6강 레이아웃과 고급 CSS 기능\11.JPG)

- CSS로 텍스트 네비게이션 스타일 적용하기

  - display: inline 설정

    ```css
    nav li{
        display: inline;
    }
    ```

    - 목록마다 줄바꿈 없이 한 줄로 보여짐
    - 목록의 블릿이 사라짐

  1. 링크에 설정되어 있는 기본 스타일 초기화

     ```CSS
     nav {
         font-family: "Lucida Grande", Tahoma, Verdana, Arial, Helvetica, sans-serif;
         font-size: 0.8em;
         font-weight: bold;
     }
     
     nav li{
         display: inline;
     }
     
     nav a {
         color: #bbb;
         text-decoration: none;
     }
     ```

     - nav 요소 내

       - 서체: 산세리프체(고딕 계열)
       - 크기: 약간 작게, 볼드

     - a 요소 내

       - 서체 색: 회색

       - 텍스트 데코레이션:none

         

  2. 목록 요소에 배경색을 검정으로 설정

     ```css
     nav {...}
     nav ol {
         background-color: #2d2d2d;
         padding: 6px;
     }
     
     nav li{
         display: inline;
         margin: 0 10px;
     }
     nav a{..}
     ```

     - ol요소

       - 배경색: 검정색(#2d2d2d)으로 설정
       - 상하좌우 padding: 6px

       width와 height을 설정하지 않는 이유:display: inline;

  3. 웹 브라우저 marging, padding 0으로 설정

     ```css
     *{
         margin: 0;
         padding: 0;
     }
     ```

  4. 마우스 롤 오버 설정하기: a:hover 선택자

     ```css
     nav a:hover{ #마우스 롤오버 시 선택자
         color: #fff;
     }
     nav #current {# 현재 페이지 메뉴 선택
         color: #fff;
     }
     ```

  전체코드

  ```css
  * {
  	margin: 0;
  	padding: 0;
  }
  
  nav {
  	font-family: "Lucida Grande", Tahoma, Verdana, Arial, Helvetica, sans-serif;
  	font-size: 0.8em;
  	font-weight: bold;
  }
  
  nav ol {
  	background-color: #2d2d2d;
  	padding: 6px;
  }
  
  nav li {
  	display: inline;
  	margin: 0 10px;
  }
  
  nav a {
  	color: #bbb;
  	text-decoration: none;
  }
  
  nav a:hover {
  	color: #fff;
  }
  
  nav #current {
  	color: #fff;
  }
  ```

  

### 3) CSS 변형과 트랜지션