# 05/12 (화) Javascript

> ❖ 아래의 다양한 실습을 통해 Javascript 기초 문법을 학습한다.



### 1. 타입과 연산자

- Primitive 타입

  - Number

    ```js
    //양의 정수
    const a = 13
    //음의 정수
    const b = -5
    // 실수
    const c = 3.14
    // e의 거듭제곱
    const d = 2.998e8
    //양의 무한대
    const e = Infinity
    // 음의 무한대
    const f = -Infinity
    //Not a Number
    const g = NaN
    
    ```

  - String

    ```js
    // ''와 "" 모두 사용 가능
    const sentence1 = 'hello'
    const sentence2 = "hi"
    ```

    ```js
    // 문자열간 덧셈 가능
    const firstName = 'Tony'
    const lastName = 'Stark'
    const fullName = firstname + lastName
    console.log(fullName)
    ```

    ```js
    //줄바꿈 불가능
    const word = "안녕 
    하세요"
    
    //줄바꿈 하려면 \n 사용
    const word1 = '안녕 \n하세요'
    ```

    - Template Literal

      ```js
      // ``(백틱?)으로 입력할 경우 여러줄의 문자열 입력이 가능.
      const word2 = `안녕들
      하세요`
      console.log(word2)
      ```

      ```js
      const age = 25
      const message = `나는 ${age}살입니다.`
      console.log(message)
      ```

  - Boolean

    ```js
    // 소문자로 표현!
    true
    false
    ```

  - Empty Value

    ```js
    let abc
    console.log(abc)
    //undefined 출력
    
    let def = null
    console.log(def)
    // null 출력
    
    ```

- 연산자 

  - 할당 연산자 

    ```js
    let c = 0
    c += 10
    console.log(c)
    // 10
    c -= 3
    // 7
    c *= 10
    // 70
    c++
    console.log(c)
    // 71
    c--
    console.log(c)
    //70
    ```

  - 비교 연산자 

    ```js
    1<2
    //true
    1>2
    //false
    
    // 문자열도 비교 가능(대문자보다 소문자가 더크고, 문자열 순서대로 더 크게 나타남(ASCII 코드 순서!) )
    'A'<'B'
    //true
    'Z'<'a'
    //true
    '가'<'나'
    //true
    ```

  - 동등 연산자 

    `==` : 가급적 지양할 것!

    ```js
    const a = 1
    const b = '1'
    console.log(a == b)
    //true
    //형변환한 거랑 비슷하다고 생각하면 된다.
    
    console.log(8 * null)
    //0 출력
    
    console.log('5'-1)
    // 4
    
    //항상 그런건 아니다.. => 문자열끼리는 덧셈이 가능하니까!
    console.log('5'+1)
    
    // 문자열은 곱셈이 안되기 때문에 NaN 출력
    console.log('five' * 2)
    //NaN
    ```

  - 일치 연산자

    `===`: type과 값 모두 비교!

    ```js
    const a = 1
    const b = "1"
    console.log(a===b)
    // false
    
    console.log(a === Number(b))
    // true
    ```

  - 논리 연산자

    `&&` : and

    ```js
    true && true
    // true
    
    true && false
    // false
    
    0 && 1
    // 0
    
    1 && 0
    // 0
    
    4 && 7
    // 7
    ```

    `||` : or

    ```js
    false || true
    // true
    
    false || false
    // true
    
    1 || 0
    // 1
    
    0 || 1
    // 1
    
    4 || 7
    // 4
    ```

    `!`: Not

    ```js
    !true
    // false
    
    !false
    // true
    ```

  - 삼항 연산자

    `condition ? exprIfTrue : exprIfFalse`

    ```js
    true? 1:2
    // 1
    
    false? 1:2
    // 2
    
    const result = Math.PI > 4? 'Yep' : 'Nope'
    console.log(result)
    // Nope
    
    const result2 = Math.PI < 4? 'Yep' : 'Nope'
    console.log(result2)
    // Yep
    ```



### 2. 조건문과 반복문

- 조건문

  - if, else if, else

    ```js
    let day = 7
    if (day === 1){
        console.log('월요일')
    } else if (day === 2){
        console.log('화요일')
    } else if (day === 3){
        console.log('수요일')
    } else if (day === 4){
        console.log('목요일')
    } else if (day === 5){
        console.log('금요일')
    } else if (day === 6){
        console.log('토요일')
    } else {
        console.log('일요일')
    }
    ```

  - switch

    ```js
    switch(day){
        case 1:{
            console.log('월요일')
            break
        }
        case 2:{
            console.log('화요일')
            break
        }
        case 3:{
            console.log('수요일')
            break
        }
        case 4:{
            console.log('목요일')
            break
        }
        case 5:{
            console.log('금요일')
            break
        }
        case 6:{
            console.log('토요일')
            break
        }
        default:{
            console.log('일요일')
        }
    }
    ```

    중간에 break를 넣지 않으면 이후 모든 케이스가 출력된다.

    

- 반복문

  - while

    ```js
    let i = 0
    while (i < 6){
        console.log(i)
        i++
    }
    ```

    ```js
    let i = 0
    while (i < 6){
        console.log(i++)
    }
    ```

  - For

    ``` js
    for (let i=0; i < 6; i++){
        console.log(i)
    }
    ```

  - for ... of

    ```js
    const numbers = [0, 1, 2, 3, 4, 5]
    for (const number of numbers){
        console.log(number)
    }
    ```

  - for ... in

    ```js
    const fruits = {
        'apple' : 2,
        'banana' : 10,
        'tomato' : 10,
        'watermelon' : 2,
    }
    
    for (const key in fruits){
        console.log(key)
    }
    //apple
    //banana
    //tomato
    // watermelon
    
    for (const key in fruits){
        console.log(fruits[key])
    }
    //2
    //10
    //10
    //2
    
    Object.entries(fruits)
    ```

  - continue

    ```js
    for (let i = 0; i < 10; i++){
        if (i === 3) {
            continue
        }
        console.log(i)
    }
    ```

    

### 3. 함수

- 선언식 & 표현식

  ```js
  // 선언식
  function add(num1, num2){
      return num1 + num2
  }
  add(3, 9)
  
  
  // 표현식
  const sub = function(num1, num2){
      return num1 - num2
  }
  sub(77, 21)
  ```

- 기본값 인자

  ```js
  square = num => num**2
  ```

  ```js
  let noArg = () => 'No args'
  let noArg2 = _ => 'No args'
  ```

- 화살표 함수

  ```js
  const arrow = function(name){
      return `hello ${name}`
  }
  ```

  ```js
  const arrow2 = (name) => {return `hello ${name}`}
  ```

  ```js
  const arrow3 = name => {return `hello ${name}`}
  ```

  ```js
  const arrow4 = name => return `hello ${name}`
  ```





### 4. 자료구조

- 배열 (Array) 

  - 배열의 인덱스 접근 

    ```js
    var colorArr = ['red', 'orange', 'yellow', 'green']; console.log(colorArr[0]);
    console.log(colorArr[1]);
    console.log(colorArr[2]);
    console.log(colorArr[3]);
    ```

    ```js
    var score = [50,90,30,70], sum = 0;
    for (var i = 0; i < score.length; i++) {
        sum += score[i];
    }
    console.log(sum);
    ```

    

  - 자주 쓰이는 배열 매서드 

    `concat`, `join`,   `indexOf`,  `slice`, `plice`,  `sort`, `push`, `pop`, `shift`, `unshift`

    ```js
    var li = ['a', 'b', 'c', 'd', 'e'];
    li.push('f'); //배열 맨 뒤에 추가
    console.log(li);
    
    li = li.concat(['f', 'g']); //배열 맨 뒤에 여러개 추가
    console.log(li);
    
    li.unshift('z'); //배열 맨 앞에 추가
    console.log(li);
    
    li.splice(1, 0, 'a2', 'a3') //위치, 삭제할 개수, 추가할 내용
    console.log(li);
    
    ```

    ```js
    var li = ['a', 'b', 'c', 'd', 'e'];
    
    li.shift(); //맨 앞의 원소 삭제
    console.log(li);
    
    li.pop(); //맨 뒤의 원소 삭제
    console.log(li);
    ```

    ```js
    var li = ['c', 'e', 'a', 'b', 'd']
    li.sort();
    console.log(li);
    
    li.reverse();
    console.log(li);
    ```

    

- 오브젝트 (Object) 

  JavaScript는 객체기반의 스크립트 언어이며 JavaScript를 이루고 있는 거의 모든 것은 객체이다. 객체란 **여러 속성을 하나의 변수에 저장할 수 있도록 해주는 데이터 타입**으로 Key / Value Pair를 저장할 수 있는 구조이다.

  -  오브젝트 내 요소의 접근 

    ```js
    var user = new Object(); // "object constructor" syntax
    var user = {}; 
    
    var user = {
      name: "dabin",
      age: 25
    };
    console.log(user.name)
    ```

    

  - 오브젝트 → 배열 반환 메서드 

    ```js
    const object1 = {
      a: 'somestring',
      b: 42,
      c: false
    };
    
    console.log(Object.values(object1));
    ```

    

  - 오브젝트 리터럴 

    ```js
    var 인스턴스 = {
        프로퍼티 : 초기값,
            . . .
            메서드 : function(){
        . . .
        }
    }
    ```

    

-  JSON <-> Object

  - JSON → Object 

    `JSON.parse(jsonString)`

  - Object → JSON

    `JSON.stringify(object)`