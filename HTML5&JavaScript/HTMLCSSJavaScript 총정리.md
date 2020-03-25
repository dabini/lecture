# HTML/CSS/JavaScript 총정리



- First class function
  - 자바 스크립트 함수는 아래와 같은 특징을 가진다.
    - 함수를 인자로 전달 가능함
    - 함수를 반환할 수 있음
    - 변수에 함수를 할당 가능함
  - 위의 조건은 프로그래밍 언어에서 일급 객체(fist class object/ first class citizen)의 조건이다.

- Closure
  - 크로저는 함수와 함수가 선언된 어휘적 환경(Lexical scoping, environment)의 조합이다.

### 1. HTML

- Html 기본 개념(정의, 기본구조 등)
- 태그
  - 그룹 컨텐츠, 텍스트 관련 요소, table, form, input
- 시맨틱태그
- 일반적으로 HTML 요소들은 문서의 위에서부터 아래로 순차적으로 나열한다.



### 2. CSS

- CSS 기본 개념(정의 활용법 등)

- 선택자 관련 개념들(우선 순위)

- 단위(px, rem, em)

- Box model

- Block, inline 요소 및 display

- position, float

  - CSS position(위치 자체를 변경)
    - static: 디폴트값(기준 위치)
      - 기본적인 요소의 배치 순서에 따름(좌측 상단)
      - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로  배치된다.
    - 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동이 가능하다(음수값도 가능)
      - relative: static 위치를 기준으로 이동
      - absolute: static이 아닌 가장 가까이 있는 부모/조상 요소 중 static이 아닌 것! (부모가 relative여야함!)를 기준으로 이동
      - fixed: 부모 요소와 관계 없이 브라우저를 기준으로 이동
        - 스크롤시에도 항상 같은 곳에 위치
  - CSS float의 속성(둥둥 떠 있도록)
    - float은 요소를 일반적 흐름에서 벗어나도록 하는 속성 중 하나
      - 반드시 clear 속성을 통해 초기화가 필요하며, 예상치 못한 상황이 발생할 수 있음
    - float를 사용하는 경우 block 사용을 뜻하며, display  값이 inline인 경우 block으로 계산
  - float의 문제점
    - 자식 요소의 float 속성으로 인해 부모 영역의 높이가 사라지는 문제
    - clear 한 요소의 margin이 제대로 표현 되지 않은 문제

  - 해결방안
    - 다야한 해결 방안들이 있으나, 가장 많이 활용되고 문제가 없는 의사요소 선택자를 활용한 방법을 소개
    - clearfix::after{}

- HTML/CSS의 기본 특징

  - 일반적으로 HTML 요소들은 문서의 위에서부터 아래로 순차적으로 나열된다.
  - 아래의 방법들을 통해 변경될 수 있다.
    - display 속성을 통해 요소가 보여지는 방식 변경
      - block, inlin, inline-block
      - table, flexible box, grid 등의 레이아웃을 활용
    - position 속성을 통해 위치 자체를 변경
    - float 속성을 통해 떠 있도록 만듬

### 3. JS

- JS 기초 개념

  - 데이터 타입(원시 타입, 객체 타입), 연산자
  - 원시타임(primitive) - 변경 불가능 값
    - boolean - true, false
    - null
    - undefined
    - number
    - string
    - symbol(ES6)
  - 객체 타입(object)
    - object:일반객체, function, array, date, RegExp

  - null vs undefined
    - null
      - 의도적으로 변수에 값이 없다는 것을 명시
      - typeof 출력시 object로 출력되는 것은 설계상의 실수
    - undefined
      - 선언 이후 할당하지 않은 변수에 지정된 값
      - 자바스크립트 엔진이 할당 이전에 초기화된 값
      - 직접 값으로 할당해서 사용하는 것 금지
  - 변수 유효 범위(scope)
    - 자바스크립트는 함수 레벨 스코프를 가진다.
    - 따라서 함수 내에서 선언된 변수는 지역 변수이며,
    - 나머지는 전역 변수로 활용 된다.
    - 변수 선언시 키워드를 쓰지 않으면, 암묵적 전역으로 설정된다.
  - 호이스팅과 let, const(ES6)
    - 자바스크립트에서는 모든 선언을 호이스팅한다.
    - ES6에서 새롭게 등장한 let과 const 키워드는 이러한 내용을 방지할 수 있다.
      - 호이스팅 자체가 이뤄지지 않는 것은 아니고, var는 선언과 동시에 초기화(undefined)를 하고, let, const는 선언과 초기화 단계까 분리되어 진행된다
      - 뿐만 아니라, 블록 레벨 스코프를 가지고 있다ㅣ.

- 객체 선언 및 활용

  - 객체 생성 방법
    - 객체는 key와 value로 구성된 속성들의 모임
    - 기본 객체 생성법
      - 객체 리터럴
      - object 생성자 함수
    - 객체 리터럴로 생성을 하는 경우 키가 문자열로 표기될 수 있으면, 암묵적 형변환 발생
    - 만약 생성자 함수를 만들어 사용하면 마치 클래스처럼 속성이 동일한 객체를 생성
    - 속성 접근은 . 혹은 []로 접근

- 배열, 순회

  - JS에서 배열은 값만 존재한다
    - 배열 리터럴
    - Array  생성자 함수
  - 배열 순회
    - for
    - for ... of
    - forEach => 메소드
    - for ... in 은 배열의 요소만 접근하는 것이 아니라 속성까지 출력될 수 있다.
      - 자바스크립트에서 배열도 object라서 속성 설정이 가능하지만, 리스트의 요소가 아니라, 객체의 속성이 된다.
  - 배열 메소드
    - sort 메소드에 비교함수(인자)가 없으면 문자열 기준으로 정렬한다.
    - 비교함수가 잇따면, 해당 함수의 리턴값이 0보다 크거나 작음으로 정렬한다.
    - 문자열 관련: join, toString
    - 배열합치기: concat
    - 원소 삽입 삭제:push, pop, unshift, shift
    - 인덱스 탐색: indexOf 
    - 배열조작: splice => 자르고 저장
    - 배열자르기: slice => return까지

- 함수(함수 정의(화살표 함수까지) ~ 클로저)

  - 함수 선언

    - 함수 호이스팅

      - 자바스크립트에서는 모든 선언이 호이스팅 된다.

      - 앞서 설명한 함수 선언 방식의 가장 큰 차이점은 아래와 같다

        - 함수 선언문의 경우 선언, 초기화, 할당이 모두 이루어져 실행이 가능
        - 함수 표현식은 변수 호이스팅이 발생하여, undefined 즉 실행 불가

        

        

        

  - 화살표 함수(ES6)

    ```javascript
    var sum = (a,b) => a+b
    ```

  - 함수 인자

    - 자바스크립트에서 함수는 매개변수 전달에 대한 제한이 없음
      - ARGUMENTS 객체는 매개변수로 넘겨지느 모든 정보를 가지고 있음.

- 이벤트, DOM 조작(querySelector/querySelectorAll)

  - DOM	
    - 문서의 구조화된 표현을 제공하여, dom 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 변경할 수 있도록 도우며, 구조화된 노드와 오브젝트 문서르 표현
    - 주요 객체
      - window: DOM 문서를 표현하는 창, 가장 최상위 객체
      - document: 페이지 콘테츠의 진입점 역할을 하며, <body> 등 다른 요소들을 포함
      - navigator, location, history, screen
  - window
    - window 객체는 전역 객체
    - 다양한 함수, 이름공간, 객체 등이 포함

  - DOM 접근
    - 단일 Node
      - document.querySelector(selector)
    - NodeList(non-live)
      - document.querySelectorAll(selector)
  - Dom 조작
    - InnerHTML, insertAdjacentHTML
      - Dom 조작시 아래와 같은 메서드를 통해서도 가능하나 ,XSS 공격에 취약점이 있으므로 사용시 주의
      - element.innerHTML(text)
      - element.insertAdjacentHTML(position, test)
    - Node Attribute
      - element.style
        - element.style.color
        - element.style.backgroundColor
      - element.setAttribute(attributeName, value)
      - element.getAttribute(attributeName)

- 이벤트

  - 브라우저에서 특정한 이벤트가 발생하면 이에 대한 이후 행위를 정의할 수 잇다.
  - 이벤트를 정의하는 경우, 인라인으로도 작성 가능하나 분리하여 작성하는 것이 좋다
  - 이벤트 예시
    - load, copy, mouseover, click, submit 등
  - addEventListener
    - EventTarget.addEventListener(type, listener, [, useCapture]);
      - type: 이벤트 유형
      - listener: 이벤트가 발생했을 때 실행할 콜백 함수(핸들러)
      - useCapture: 기본값(false), 상위 노드로 전파(버블링), 만약 true인 경우 하위노드로 전파(캡쳐링)
  - 이벤트 전파
    - event는 해당 요소에서 전파되며, 캡처링과 버블링으로 구분
    - 항상 캡처링으로 시작하여 버블링으로 종료되며, addEventListene 메소드의 useCapture를 통해 특정 상황에 대해 이벤트 관리가 가능
  - 이벤트 객체와 this
    - 이벤트 리스너의 콜백함수에서 this를 활용하는 경우, 이벤트 리스너에 바인딩 되어 있는 요소가 지정된다. 아래와 같이 인벤트를 등록하는 경우, 버블링에 의해 this값은 계속 변경된다.

- Closure
  - First class function
    - 자바스크립트 함수는 아래와 같은 특징을 갖는다
      - 함수를 인자로 전달 가능함
      - 함수를 반환할 수 있음
      - 변수에 함수를 할당함
    - 위의 조건은 프로그래밍 언어에서의 일급객체의 조건이다.

