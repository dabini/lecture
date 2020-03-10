# HTML5/JavaScript

## 5. CSS 문서표현(하)

> 용어 알기
>
> - Box model
>
>   웹의 모든 요소가 적용되는 모델로 모든요소가 상자와 같은 사각형 영역으로 표현되는 모델
>
> - positioning
>
>   position 속성으로 요소의 위치 속성을 상대 위치 또는 절대 위치 등으로 나타내는 것
>
> - 마진겹침 현상
>
>   상하 마진이 연속될 때 큰 수치의 마진으로 겹쳐 마진이 의도와 다르게 넓게 적용되는 것을 막아주는 현상

### 1) CSS에서 텍스트 표현

#### 1.1) 서체의 지정과 텍스트 설정

- 서체의 지정과 크기 설정

  - 웹 서체의 이해

    - 서체 사용의 이유 : 문서 외형 꾸미기, 문서의 특성 제시, 구조 이해 쉽게 하기 위함

    - 웹은 다양한 서체를 사용

      -> 웹 이용자 간의 서체 공유가 원활히 이루어지지 않음

      -> 운영체제 간에도 다른 서체들을 제시

      다른 사용자, 다른 운영 체제로 인하여 본래 서체 지정된 서체가 아니라 다른 서체로 대체 되어 제시되는 경우가 많음

  - 폰트 패밀리(font-family)

    - font-family: 비슷한 모양의 서체를 묶어서 제시

    - 형식: top-family:( 사용할 서체), (대안 서체1), (대안 서체2);

      ![image-20200310102155504](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102155504.png)

      "font-family에서 지정한 마지막 서체도 없다면 웹 브라우저 기본 서체 사용"

  - 일반 폰트 패밀리

    ![image-20200310102424058](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102424058.png)

    ![image-20200310102444500](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102444500.png)

    

- 서체 크기 조절

  - font-size: 속성 : 서체 크기 조절

    ![image-20200310102559927](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102559927.png)

  - 서체 크기 단위

    ![image-20200310102634326](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102634326.png)

    ![image-20200310102656468](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102656468.png)

- 다양한 변형 서체(Italic, Bold, Small cap)

  - Italic: 약간 비스듬한 모양의 서체

    - 설정 방법: font-style 속성 사용

      ![image-20200310102908345](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102908345.png)

      ![image-20200310102921301](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102921301.png)

    - Bold: 일반 텍스트보다 굵은 서체

      ![image-20200310102952504](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310102952504.png)

    - Small cap: 알파벳을 사용하는 문자에 해당하는 서체 스타일, 텍스트의 크기로 대소문자 표기

      ![image-20200310103025261](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103025261.png)

- 텍스트 스타일 설정

  - 텍스트 간격 설정
    - 텍스트 간격: 글자와 글자 간의 간격 또는 단어와 단어간의 간격의미

  - 자간 설정

    - 자간: 글자와 글자 간의 간격

    - 자간 설정:letter-spacing 속성 사용

      ![image-20200310103143473](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103143473.png)

  - 단어 간격 설정

    - 단어 간격 설정: word-spacing 속성 사용

      ![image-20200310103213216](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103213216.png)

  - 행간 설정

    - 행간 설정: line-height 속성 사용

      ![image-20200310103239675](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103239675.png)

- 텍스트 스타일 설정

  - 텍스트 정렬

    ![image-20200310103414936](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103414936.png)

  - 세로 정렬의 예

    ![image-20200310103439707](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103439707.png)

    ![image-20200310103505479](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103505479.png)

  - vertical-align 속성 값

    - vertical-align: 세로 정렬의 속성 값

    - vertical-align 속성 값

      top: 위

      middle: 중간

      bottom: 아래

      baseline: 서체의 기본 정렬선 정렬 의미

      super: 위첨차

      sub: 아래 첨자

      text-top: 텍스트 상단

      text-bottom: 텍스트 하단

    - 수치와 %도 가능하다 하지만 아직까지 대부분의 웹 브라우저에서는 설정이 잘 되지 않음

  - 텍스트 인덴트

    - 단락의 들여쓰기

      ![image-20200310103743366](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310103743366.png)

- 기타 텍스트 꾸미기

  - 텍스트 밑줄 긋기

    - 설정: text-decoration 속성 사용

    - text-decoration 속성값

      underline: 밑줄 생성

      overline: 텍스트 위에 줄그어줌

      line-throught: 텍스트 중간에 줄을 그어줌( 텍스트 삭제 의미)

      non: 밑줄 없앰

    - 텍스트 밑줄 긋기 예

      ![image-20200310104102200](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310104102200.png)

      

  - 대소문자 변경

    - 설정: text-transform 속성 사용

    - text-transform 속성 값

      capitalize: 각 단어의 첫 글자 대문자 만드는 속성

      uppercase: 모든 텍스트 대문자 변환

      lowercase: 모든 텍스트 소문자 변환

      none: 대소문자 변경 기능 없앰

  - 텍스트 그림자 설정

    - 설정: text-shadow 속성 사용

    - text-shadow 속성 값

      x-offset(x축 거리): 그림자가 x축으로 얼마나 비껴 나타나는지 의미

      y-offset(y축 거리): 그림자가 y축으로 얼마나 비껴 나타나는지 의미

      blur: 그림자 테두리의 흐림 정도 설정

      color: 그림자 색

      none: 그림자 속성 해제

    ![image-20200310104858444](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310104858444.png)

    ![image-20200310104919464](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310104919464.png)

    ![image-20200310104934830](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310104934830.png)

    

#### 1.2) 컬러와 배경 설정

- 컬러

  - 웹 색상 코드

    ![image-20200310105208206](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310105208206.png)

  - 투명도 표현

    - 컬러에 투명도 설정 가능

    - 투명도 설정 방법: 10진수 색상 코드로만 가능

      ![image-20200310105249389](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310105249389.png)

  - 텍스트 색 지정

    - color 속성 사용

      ![image-20200310105325397](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310105325397.png)

- 배경 설정

  - 배경

    - HTML의 블록 요소에 사각형 형태의 영역
    - 크기, 배경 색, 이미지 설정 가능

  - 배경 색 설정

    - background-color 속성

      ![image-20200310105527037](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310105527037.png)

  - 배경 이미지

    - background-image 속성사용

    - 웹 페이지 전체에 지정 이미지(flower.png) 배경 적용 예시

      ![image-20200310105636728](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310105636728.png)

  - 배경 이미지 반복 설정

    - background-repeat 속성 사용

    - 배경 설정의 기본 스타일은 배경 이미지의 반복

      ```css
      body{
          background-image: url("images/flower.png");
          background-repeat: no-repeat; 배경의이미지가 반복해서 나타나지 않도록 설정
      }
      ```

    - background-repeat 속성

      ![image-20200310105820050](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310105820050.png)

  - 배경 이미지 고정 설정

    - background-attachment 속성 사용

      ```css
      body{
          background-image: url("images/flower.png");
          background-repeat: no-repeat;
          background-attachment: fixed; 배경 이미지 고정
      }
      ```

    - background-attachment 속성

      ![image-20200310105951024](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310105951024.png)

  - 배경 이미지 위치 설정

    - background-position 속성 사용

    - 웹 브라우저의 왼쪽 상단을 기준으로 x,y 좌표 지정

      ```css
      body{
          background-image: url("images/flower.png");
          background-repeat: no-repeat;
          background-attachment: fixed;
          background-position: 30px, 30px; 배경 이미지 왼쪽 아래로 30px 이동
      }
      ```

  - 배경 이미지 크기 설정

    - background-size 속성 사용

    - 배경 이미지의 가로 세로 크기 속성 값으로 지정

      ```css
      body{
          background-image: url("images/flower.png");
          background-repeat: no-repeat;
          background-attachment: fixed;
          background-position: 30px, 30px;
          background-size: 50% 50%;
      }
      ```

      => 배경이미지의 크기는 상대적인 크기

- 그라디언트 설정하기

  ![image-20200310151221048](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310151221048.png)

  - 설정

    ```css
    body {
        background: filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffff', endColorstr='#ff0000', GrandientType = 1);
    }
    ```

  - 그라디언트 CSS 코드를 생성해 주는 웹 어플리케이션 사용

    https://www.colorzilla.com/gradient-editor/



### 2) 목록, 표 꾸미기

#### 2.1) 목록 꾸미기

- 블릿 꾸미기

  - 블릿 스타일 설정

    - 블릿: 목록을 정리하며 예쁘게 보이도록 목록 아이템 앞에 붙는 숫자 또는 특수 문자
    - 웹 브라우저는 순서가 있는 목록(아라비아 숫자, 알파벳 등), 순서가 없는 목록(동그라미, 사각형 블릿)에 따라 알맞은 블릿 제공
    - 블릿 설정: list-style-type 속성 사용

    ![image-20200310151727784](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310151727784.png)

  - list-style-type 속성 값

    - 순서가 있는 목록 형태

      ![image-20200310151820895](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310151820895.png)

      ![image-20200310151830028](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310151830028.png)

      ![image-20200310151840871](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310151840871.png)

    - 순서가 없는 목록 블릿 표시

      ![image-20200310151901506](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310151901506.png)

  - 블릿이 없는 목록: none

    ``` css
    li {
        list-style-type: none;
    }
    ```

- 다단계목록

  - 각 단계마다 새로운 블릿을 적용하고 싶을 때 직계자식 선택자를 이용하여 블릿 표시

    [HTML코드]

    ```html
    <h1>성공한 사람의 7가지 습관</h1>
    <ul>
        <li>개인의 승리
            <ol>
                <li>자신의 삶을 주도하라</li>
                <li>목표를 확립하고 시작하라</li>
                <li>중요한 것부터 먼저하라</li>
            </ol>
        </li>
        <li>대인관계의 승리
            <ol>
                <li>상호이익을 모색하라</li>
                <li>이해시키려 하기 전에 먼저 상대를 이해하려 하라.</li>
                <li>시너지를 창출하라.</li>
            </ol>
        </li>
        <li>자기 쇄신
            <ol>
                <li>심신을 단련하라.</li>
            </ol>
        </li>
    </ul>
    ```

    [CSS코드]

    ```css
    ul>li{
        list-style-type:square;
    }
    ul>li>ol{
        list-style-type:lower-alpha;
    }
    ```

  

  - 이미지 블릿 설정

    - list-style-image 속성 사용

    - 속성값: 이미지 URL을 설정

      ![image-20200310152444617](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310152444617.png)

  - 블릿 위치 설정

    - 목록 아이템이 한 줄 이상일 때 블릿의 위치 설정 가능

    - list-style-position 속성 사용

    - 속성 값

      ![image-20200310152526201](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310152526201.png)

  - 배경 이미지를 이용한 이미지 블릿 생성 방법

    1. 그래픽 어플리케이션을 이용하여 블릿 이미지 제작

       dot.png 설정

    2. 목록 요소의 margin과 padding 설정

       - 목록 요소의 marging과 padding: '0'으로 설정

       - list-style-type 속성: none 설정(목록의 블릿 제거)

         ![image-20200310152650727](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310152650727.png)

    3. 제작한 블릿 이미지 목록 요소의 백그라운드 이미지로 설정

       - background-image 속성값 dot.png 이미지 URL로 설정

         ![image-20200310152732146](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310152732146.png)

         

- Margin, Padding

  - HTML의 대부분의 요소에 적용 가능

  - 모든 블록 레벨 요소들은 박스 형태의 영역을 가지고 있음

    ![image-20200310152915484](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310152915484.png)

    둘 다 0으로 설정하면 모든 공간이 여유공간 없이 바짝 붙어있는 형태

  - marging과 padding 설정

    ![image-20200310153002329](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153002329.png)

  - margin과 padding 설정예

    ![image-20200310153030025](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153030025.png)

    ![image-20200310153046821](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153046821.png)

- Border 설정(테두리 선 설정)

  ![image-20200310153125809](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153125809.png)

  - 표 border의 설정

    - border 생성 속성: border-width, border-style, border-color

      ![image-20200310153326323](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153326323.png)

    - 일반적인 속성 값

      ![image-20200310153404948](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153404948.png)

    - 명암을 설정하는 속성 값

      ![image-20200310153424214](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153424214.png)

  - 웹 브라우저 표시예

    ![image-20200310153445445](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153445445.png)

  - 각 셀마다 모두 border 설정: <th>, <td> 요소에 적용

    ![image-20200310153518985](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153518985.png)

  - 셀 간격 설정

    ![image-20200310153614443](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153614443.png)

    

  - border의 선택적 적용

    - border는 top, bottom, left, right 선택적 적용 가능

    - 셀의 아랫 부분만 선택적으로 border 적용 예

      ![image-20200310153700607](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153700607.png)

- 셀 Padding 과 셀 배경 색 설정

  - 셀 padding 설정: 셀의 여백 조절

    ![image-20200310153739496](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310153739496.png)

  - 셀 배경 색 설정

    - background-color 속성 사용

  - 셀에 각기 다른 색 적용하기

    [HTML코드]

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Title</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <table>
                <caption>2011년 한국영화흥행순위</caption>
                <colgroup><col id="order"><col><col><col></colgroup>
                <thead>
                    <tr><th>순위</th><th>작품명</th><th>감독</th><th>관객수</th></tr>
                </thead>
                <tbody>
                    <tr><td>1위</td><td>최종병기 활</td><td>김한민</td><td>7,459,974명</td></tr>
                    <tr><td>2위</td><td>써니</td><td>강형철</td><td>7,375,110명</td></tr>
                    <tr><td>3위</td><td>완득이</td><td>이한</td><td>5,315,682명</td></tr>
                    <tr><td>4위</td><td>조성명탐점:각시투구꽃의 비밀</td><td>김석윤</td><td>4,759,460명</td></tr>
                    <tr><td>5위</td><td>도가니</td><td>황동혁</td><td>4,673,409명</td></tr>
                </tbody>
            </table>
        </body>
    </html>
    ```

    

    [CSS 코드]

    ```css
    thead {
        background-color: #ddd;
    }
    tbody {
        background-color: greenyellow;
    }
    td:first-of-type {
        background-color: yellow;
    }
    ```

    

    ![image-20200310154658067](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310154658067.png)

    

- 기타 설정

  - 빈 셀 감추기

    - empty-cells 속성 <table>에 적용

      ![image-20200310155248318](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310155248318.png)

  - caption 위치와 정렬

    - caption-side 속성 적용

      ![image-20200310155321313](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310155321313.png)

  

### 3) CSS 박스 모델

#### 3.1) CSS 박스 모델 기초

- CSS 박스 모델

  - 박스모델

    - HTML문서 body 부분의 모든 요소가 사각형 영역을 가지고 있음

    - 요소를 박스로 구성, 박스들의 위치와 상관관계를 지정하는 방식 정의

    - 박스 모델의 margin과 padding

      - 박스 모델의 margin과 padding: 요소 콘텐츠를 둘러싼 여백 의미

        ![image-20200310155806048](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310155806048.png)

        => 요소에 border를 정의하지 않았더라고 border를 설정하면 나타나는 곳에 가상의 border 기준으로 함

      ![image-20200310155856834](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310155856834.png)

- 블록레벨요소와 인라인레벨요소의 margin과 padding

  - 블록 레벨 요소와 인라인 레벨 요소의 margin과 padding의 차이점

    ![image-20200310155943834](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310155943834.png)

  - 웹브라우저 기본 margin과 padding 초기화

    - HTML 요소마다 웹 브라우저들에 따른 기본 margin과 padding 설정 존재

      - CSS 설정 없이 최소한의 문서 구조 이해, 가독성을 높여 줌

    - 새로운 스타일 적용 시 기본 margin과 padding으로 혼란 야기

      - CSS 작성 시작과 함께 margin과 padding '0'으로 설정

    - margin과 padding 초기화 설정예

      ![image-20200310160117205](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310160117205.png)

  - width, height 속성: 블록 레벨 요소의 크기 설정

    => 인라인 레벨 요소에는 적용 안됨

    - width 속성: 요소의 넓이 설정

    - height 속성: 요소의 높이 설정

    - 문단 요소: width, height: 150px 설정예시

      ![image-20200310160432694](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310160432694.png)

    ![image-20200310160501875](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310160501875.png)

    - 정확한 요소의 크기: width와 height로 정한 값 + padding 값 + border의 굵기 값 + margin 값

      => p 요소의 크기: 150px + padding left 20 px + padding right 20 px = 190 

- margin 겹침

  - 연속되는 블록 레벨 요소에 모두 margin 요소 적용시

    => 두 개의 margin이 연속 적용으로 margin이 겹치는 현상 발생

    ![image-20200310160741848](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310160741848.png)

  - margin 겹칩

    ![image-20200310160908875](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310160908875.png)

- Position

  - position 속성: 특정 요소가 다른 요소들과 어떠한 관계 속에서 위치를 결정하는 지 설정

  - 속성 값: 상대 위치, 절대 위치, 고정 위치

  - 상대 위치(relative): 자신의 원래 위치에서 설정한 위치 만큼 이동

    ![image-20200310163324479](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310163324479.png)

  - 상대 위치 속성 적용하여 위치 이동

    - 요소 위치 설정 속성: top, left, bottom, right 속성

      => 요소의 위치 수정 시 반드시 position 속성 설정

    ![image-20200310163512652](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310163512652.png)

    

  - 절대 위치(absolute): 기본 흐름에서 벗어나 요소를 띄워 줌

    - 설정 방법: position: absolute;

      ![image-20200310163559613](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310163559613.png)

    - z-index 속성: 어떤 요소가 다른 요소 위에 나타나는지 설정

      - z-index 속성 값: 정수

      - 속성 값이 높게 설정될 수록 앞에 배치

      - 미 설정시 HTML 문서에서 요소가 나타난 순서대로 위에 제시 됨

        ![image-20200310163801662](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310163801662.png)

  - 고정 위치(fixed): 부모 좌표를 넘어서 브라우저 원점에서 좌표를 정하게 되는 고정 위치

    - 부모 요소 위치 및 문서 스크롤 등에 영향을 받지 않음
    - 설정 방법: position: fixed;

    ![image-20200310163922113](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310163922113.png)

  - 이 외의 위치 속성

    ![image-20200310163945677](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200310163945677.png)





