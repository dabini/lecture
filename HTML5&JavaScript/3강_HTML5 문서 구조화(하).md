# HTML5/JavaScript

## 3. HTML5 문서구조화(하)

> 용어알기
>
> 루비주석
>
> 중국어나 일본어 등에서 발음이나 기타 내용을 텍스트 위에 작은 글씨로 넣는 방식의 주석
>
> get 방식 전송
>
> 서식 내용을 이름과 데이터의 스트링 형태로 만들어 URL 뒤에 덧붙여 전달하는 방식
>
> post 방식 전송
>
> 서식의 내용을 클라이언트(웹 브라우저)와 서버 간의 약속된 형식으로 인코딩을 하여 서버로 전송하는 방식



### 1) HTML 표(Table)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <title>sample</title>
        <link rel='stylesheet'href='style.css'>
    </head>
    <body>
        <figure>
        <table>
            <caption><h2>
                커뮤니케이션수단으로서의인터넷</h2></caption>
            <colgroup class='index'><col span='2'></colgroup>
            <colgroup class='value'><col id='internet'><col id='messenger'></colgroup>
            <thead id='all'>
                <tr><th colspan='2'>구분</th><th>인터넷커뮤니티가입률(%)</th><th>인스턴스메신저이용률(%)</th></tr>
            </thead>
            <tbody id="perAge">
                <tr><td colspan='2'>전체</td><td>45.2</td><td>37.1</td>
                </tr>
            </tbody>
            <tbody>
            	<tr><td rowspan='6'>연령</td><td>6 ~ 19세</td><td>43.0</td><td>38.1</td></tr>
                <tr><td>20대</td><td>67.8</td><td>61.1</td></tr>
                <tr><td>30대</td><td>41.2</td><td>30.2</td></tr>
                <tr><td>40대</td><td>28.9</td><td>17.1</td></tr>
                <tr><td>50대</td><td>22.2</td><td>14.2</td></tr>
                <tr><td>60대이상</td><td>13.0</td><td>5.0</td></tr>
            </tbody>
            </table>
            <figcaption>
                출처:2004년 6월<cite><a href="http://www.kisa.or.kr/">한국인터넷진흥원</a></cite>
            </figcaption>
        </figure>
    </body>
</html>
```

- 표(Table)의 역할: 자료나 정보를 일목요연하게 보여주는 역할

- 표 작성시 유의 점

  - 웹 접근성이 떨어짐
  - 표 이외에 더 좋은 표현 방법이 있다면 표를 사용하지 않음
  - 표를 페이지 레이아웃에 사용하지 않음
  - 웹페이지 레이아웃 시 절대 사용하지 않음!!

- HTML 표 작성 방법

  - 표 용어의 통일

    - 명확한 행과 열에 대한 표현이 없음

      | 가로열 | row    |
      | ------ | ------ |
      | 세로열 | column |

- 표 만들기 예시

1. table 요소: <table>,</table>

   - 표를 의미, 표의 시작과 끝에 입력

   - row와 column 같이 다양한 요소 포함

   - XHTML 이전: <table border='1'> ->테두리 선의 두께 지정

   - HTML5 :표현적 마크업 존재하지 않음

     => CSS를 통하여 테두리 두께 지정

     CSS 미설정시 기본 설정 테두리 두께: 0(테두리가 보이지 않음)

     ![image-20200309153128802](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309153128802.png)

2. tr 요소

   - table 요소 내부에 정의, 표의 row

   - 사용방법 : <tr>로 시작하여 </tr>로 마침

   - 요소는 테이블 셀(th 또는 td 요소)포함
     ![image-20200309153237538](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309153237538.png)

     ![image-20200309153259867](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309153259867.png)

3. td요소, th 요소

   - td요소: 테이블 셀(칸)을 의미

   - th요소: 헤더 셀을 의미, 제목 셀에 사용

   - 셀을 정하기 전에 테이블에 몇 개의 column으로 구성되어 있는 지 파악

     ![image-20200309153406990](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309153406990.png)

- 셀 병합: 테이블 셀을 하나로 만들 필요가 있음

  - 가로 셀 병합

    - colspan 속성 사용

      예)<th colspan='2'>구분</th>: 가로 두 개의 셀을 합침

      ![image-20200309153712263](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309153712263.png)

  - 세로 셀 병합

    - rowspan 속성 사용

      예) <td rowspan='6'>연령</td>: 세로 6개의 셀을 합침

      ![image-20200309153723594](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309153723594.png)

  - 셀 병합 후 필요 없어진 셀을 지움

    ![image-20200309153800779](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309153800779.png)

    

- 마침 태그는 반드시 사용해야 하는가?

  - 대부분의 요소는 시작 태그와 마침 태그로 구성된다.

  - XHTML에서는 마침 태그가 있는 요소들은 반드시 마침 태그를 사용해야 했었다.

  - HTML5에서는 요소의 영역 끝을 인지할 수 있으면 마침 태그를 생략해도 된다.

  - 예) 아래 코드는 <tr>과 <th>,<td>의 마침 태그가 없지만 웹 브라우저에서 정확히 해석됩니다.

    ```html
    <table>
        <tr><th>국어</th><th>영어</th><th>수학</th>
        <tr><th>90점</th><th>85점</th><th>70점</th>
    </table>
    ```

- 표의 구조화

  - 컴퓨터가 표를 이해 가능하도록 함
    1. 표를 이해하면 검색자의 요구를 정확히 연결
    2. 분석을 통한 데이터 활용도 높임
    3. 시각 장애가 있는 사람들에게 컴퓨터가 표를 읽어줄 수 있음

  - 표의 어떤 셀이 어떤 의미를 가지고 어떤 셀에 영향을 주는지에 대한 설정

  

- thead, tbody, tfoot

  - 표의 가장 큰 구조적 분리
  - thead: 표 머리 부분으로 제목으로 구성된 row 집합
    - 하나 이상의 row로 구성
    - 표 마다 하나의 thead 요소만 사용 가능

  - tbody: 일반적인 row의 집합
    - 하나 이상의 row로 구성
    - 하나의 표에 여러 개의 tbody 사용 가능
    - 표의 내용 분리가 있을 때 사용
  - tfoot: row의 요약(footer)들로 구성된 row 집합
    - 하나 이상의 row로 구성
    - 표마다 하나의 tfoot요소만 사용 가능
    - table 요소 내 위치와 상관없이 tfoot 요소는 표 마지막에 표시

  - 예

    ```html
    <thead>
        <tr><th>성명</th><th>국어</th><th>영어</th><th>수학</th></tr>
    </thead>
    
    <tfoot>
        <tr><td>과목별 합계</td><td>240</td><td>215</td><td>260</td></tr>
        <tr><td>과목별 평균</td><td>80</td><td>72</td><td>87</td></tr>
    </tfoot>
    
    <tbody>
        <tr><td>김철수</td><td>85</td><td>60</td><td>75</td></tr>
        <tr><td>이영희</td><td>90</td><td>95</td><td>85</td></tr>
        <tr><td>박민순</td><td>65</td><td>60</td><td>100</td></tr>
    </tbody>
    ```



- col, colgroup 요소: cloumn의 구조화를 위하여 사용

  - col 요소: 하나의 column을 의미
    - span 속성을 이용하여 하나 이상의 column을 가리킬 수 있음
  - colgroup 요소: col요소의 그룹
    - table 요소 내부에 위치
    - caption 요소보다 뒤에 있어야 하며 thead, tbody, tfoot요소 보다는 앞에 있어야 함

  - 예

    ```html
    <table>
        <colgroup id='students'><col></colgroup>
        <colgroup id='subject'><col id='korean'><col id='english'><col id='math'></colgroup>
        
        <thead>
        	<tr><th>성명</th><th>국어</th><th>영어</th><th>수학</th></tr>
    	</thead>
    
        <tfoot>
            <tr><td>과목별 합계</td><td>240</td><td>215</td><td>260</td></tr>
            <tr><td>과목별 평균</td><td>80</td><td>72</td><td>87</td></tr>
        </tfoot>
    
        <tbody>
            <tr><td>김철수</td><td>85</td><td>60</td><td>75</td></tr>
            <tr><td>이영희</td><td>90</td><td>95</td><td>85</td></tr>
            <tr><td>박민순</td><td>65</td><td>60</td><td>100</td></tr>
        </tbody>
    </table>
    
    ```



- scope 속성

  - 정의: th 요소에 사용되는 속성, th의 영향력이 어느쪽으로 향햐는 지 지정

  - scope 속성 미 설정시 **scope="auto"**로 설정

    ​								문맥으로 헤더 셀의 영향이 row 또는 column을 결정

  - 예

    - scope = 'row', scope = 'col'
    - 헤더 셀이 row 또는 column에 영향을 줌

    ```html
    <table>
        <tr><th scope='col'>업체</th><th scope='col'>주요내용</th></tr>
        <tr><th scope='row'>Dell, HP</th><td>데이터스토리지업체미 3PAR인수 경쟁(11 ~ 16억 달러)</td></tr>
        <tr><th scope='row'>Apple</th><td>10억달러를투자하여노스캐롤라이나주에초대형데이터센터구축</td></tr>
        <tr><th scope='row'>Intel</th><td>보안업체맥아피 76억 8,000만 달러에 인수</td></tr>
        <tr><th scope='row'>IBM</th><td>소프트웨어기업스텔링커머스 14억 달러에 인수</td></tr>
        <tr><th scope='row'>Google</th><td>데이터센터에40억달러(2007~2008년> 및 6~7억달러(2010년)투자</td></tr>
    </table>
    ```

  - 예

    - scope ='rowgroup', scope='colgroup'
    - row 집합 또는 column의 집합에 헤드셀이 영향을 미치도록함

    ```html
    <table>
        <thead>
            <tr><th>ID</th><th>Measurement</th><th>Average</th></tr></thead>
        <tbody>
            <tr><td></td><th scope=rowgroup></th><td></td><td></td></tr>
            <tr><td>93</td><th>Legs</th><td>3.5</td><td>4</td></tr>
            <tr><td>10</td><th>Tails</th><td>1</td><td>1</td></tr>
        </tbody>
        <tbody>
            <tr><td></td><th scope=rowgroup>English speakers</th><td></td><td></td></tr>
            <tr><td>32</td><th>Legs</th><td>2.67</td><td>4</td></tr>
            <tr><td>35</td><th>Tails</th><td>0.33</td><td>1</td></tr>
        </tbody>
    </table>
    ```

- caption 요소

  - 정의: table의 제목을 나타냄, table 요소의 첫번째 자식 요소로 가장 먼저 설정
  - 예)

  ![image-20200309160731722](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309160731722.png)

  

### 2) HTML 서식(form)

- HTML5 서식

  - 사용자의 상호작용
  - 서버에서 처리될 데이터를 제공하는 역할을 하는 웹 페이지 콤퍼넌트
  - HTML5는 고급 폼 콘트롤러를 제안하지만 아직 모든 웹브라우저에서 지원하지는 않음

- form 요소

  - 정의 : HTML 서식을 정의하는 요소

  - 예 (고객 이름 입력 서식)

    ```html
    <form>
        <p><label>고객이름: <input></label></p>
    </form>
    ```

    => form 요소 내부의 서식요소는 대부분 <p>,</p>요소 안에 정의

    ![image-20200309162259450](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309162259450.png)

  - form 요소의 속성: 서식의 내용을 어느 곳으로 어떤 방식으로 전송할 것인지 속성 지정

    action 

    - 서식에서 전송단추를 눌렀을 때 내용이 전송 되는 서버 파일의 URL

    method

    - 폼이 전송되는 방식을 결정
    - get과 post 중 선택

  - method = 'get' (GET 방식)

    - 클라이언트(웹 브라우저)는 서버에 폼 데이터를 이름과 값이 결합된 스트링 형태로 전달
    - 데이터의 이름과 값: "&"문자를 이용하여 연결
    - action 속성의 인터넷 주소(URL)값 뒤에 붙어 URL 생성
    - 웹 브라우저에서 직접 입력해서 접근 가능, 북마크도 가능
    - 예(이름과 나이를 서버에 전송하는 폼 코드)

    ```html
    <form action="customReg.html" method='get'>
        <p><label>고객이름: <input name="custom_name"></label></p>
        <p><label>고객나이: <input name="custom_age"></label></p>
    </form>
    ```

    ![image-20200309162649418](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309162649418.png)

    => get 방식은 전송 내용이 그대로 노출 됨

  - method="post"

    - 클라이언트(웹 브라우저)와 서버간의 약속된 형식으로 인코딩을 하여 서버로 전송
    - 인터넷 주소(URL)에 전송 값이 나타나지 않음
    - 전송 내용은 가려지지만 북마크나 링크로 접근 불가

- input 요소

  - 정의: 다양한 타입을 가지는 입력 데이터 필드

  - input 요소의 type 속성:

    input 요소를 통해 받아들이는 데이터의 속성 정의로 type 속성에 따라 input 요소를 다르게 표현

    예) text, password, hide, radio, submit, reset 등

  - HTML5에서 input요소의 type 속성 값

     url, tel, email과 같은 구체적인 타입추가

- label 요소

  - 정의: 서식 입력 요소의 캡션

  - label 요소의 사용

    - for 속성의 사용

      ```html
      <label for='name'>이름</label><input id='name'type='text'>
      ```

    - label 요소 내부에 서식 요소 넣기

      ```html
      <label>이름:<input type='text'></label>
      #label 요소 내부에 서식 요소를 넣을 때는 두 개 이상의 서식 요소를 넣지 않음
      ```



- input 요소들

  - 텍스트와 패스워드 입력 서식

    - <input type='text'>

      - 일반적인 줄바꿈이 없는 텍스트 입력
      - type을 지정하지 않으면 text 타입으로 인식

    - <input type='password'>

      - 패스워드 입력
      - 화면에 입력된 텍스트가 보이지 않음

    - 예

      ```html
      <p><label>이름:<input type='text'></label></p>
      <p><label>아이디:<input type='text'></label></p>
      <p><label>암호:<input type='password'></label></p>
      ```

      

    <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309163446007.png" alt="image-20200309163446007" style="zoom:80%;" />

  - 입력 서식의 중요 공통 서식들

    - name 속성

      - 서버에 전달될 서식 값의 이름
      - 반드시 필요한 속성

    - 예

      ```html
      <p><label>이름:<input type='text' name='name'></label></p>
      <p><label>아이디:<input type='text' name='id'></label></p>
      <p><label>암호:<input type='password' name='pw'></label></p>
      ```

    - required 속성

      - 서식 값이 반드시 입력되어야 함을 의미
      - 회원가입 시 회원 이름과 아이디 등과 같은 필수적인 서식 필드에 필요
      - 서식이 제출되기 전에 **유효성 검사**에서 처리

    - 예

      ```html
      <p><label>이름:<input type='text' name='name' required></label></p>
      <p><label>아이디:<input type='text' name='id' required></label></p>
      <p><label>암호:<input type='password' name='pw' required></label></p>
      ```

    - placeholder 속성

      - 입력 폼에 짧은 힌트

    - 예

      ```html
      <p><label>이름:<input type='text' name='name' placeholder='홍길동' required></label></p>
      <p><label>아이디:<input type='text' name='id' placeholder="ID를 반드시 입력하세요."required></label></p>
      ```

      ![image-20200309164011496](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309164011496.png)

    - maxlength 속성

      - 서식 요소에 입력되는 값의 최대 길이 설정
      - maxlength 속성이 설정된 입력 폼은 maxlength 값 이상 입력이 안됨

    - 예

      ```html
      <p>주민등록번호: <input maxlength='6' name='IDcode1'>,<input maxlength='7' 'name'="IDcode2"</p>
      ```

    - autofocuse 속성

      - 폼이 로딩되면 커서가 autofocus 속성이 있는 폼 요소로 이동
      - 첫 번째 입력 폼 지정에 사용

    - 예

      ```html
      <p><label>이름:<input name='name' placeholder='홍길동' required autofocus></label></p>
      <p><label>아이디:<input name='id' placeholder='ID를 반드시 입력하세요.' required autofocus></label></p>
      <p><label>이름:<input name='pw' type='password' required></label></p>
      ```

      

    - fieldset 요소
      - 정의: 폼 요소들의 공통된 이름으로 그룹화 할 때 사용

    - 예

      ```html
      <fieldset>
          <legend>필수 입력</legend>
          <p><label>이름:<input name='name' placeholder='홍길동' required autofocus></label></p>
      	<p><label>아이디:<input name='id' placeholder='ID를 반드시 입력하세요.' required autofocus></label></p>
      	<p><label>이름:<input name='pw' type='password' required></label></p>
      </fieldset>
      ```

      #<legend>,</legend>요소를 이용하여 fieldset 그룹에 이름 지정

      "<fieldset>,</fieldset>으로 이름, 아이디, 암호를 필수 입력이란 이름으로 그룹화"

      ![image-20200309164636214](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309164636214.png)

  - 라디오 단추

    - 정의: 나열된 여러 보기 중 하나만 선택하게 할 때 사용하는 폼 콘트롤러
    - 사용법: <input type='radio'>
    - 예

    ```html
    <label>성별:</label>
    <input type='radio' id='male'name='sex'value='male'><label for='male'>남성</label>
    <input type='radio' id='female'name='sex'value='female'><label for='female'>여성</label>
    ```

    같은 보기 그룹의 라이도 단추들은 name 속성 값이 같아야 함

    value 속성: 이용하여 버튼이 선택 되었을 때 서버에 전달될 값을 입력

    ![image-20200309164900789](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309164900789.png)

    - checked 속성: 라이도 버튼과 체크 박스에서 미리 선택되어야 하는 버튼이 있다면 checked 속성 설정

    - checked 속성 사용 예시

      ```html
      <label>성별:</label>
      <input type='radio' id='male'name='sex'value='male'checked><label for='male'>남성</label>
      <input type='radio' id='female'name='sex'value='female'><label for='female'>여성</label>
      ```

      ![image-20200309164959823](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309164959823.png)

  - 체크 박스

    - 정의: 여러 보기 중 복수 선택이 가능한 입력 타입
    - 사용 법: <input type='checkbox'>
    - 예

    ```html
    <fieldset>
        <legend>관심분야</legend>
        <p>
            <label><input type='checkbox'name="interesting"value='html5'>HTML5</label>
            <label><input type='checkbox'name='interesting'value='css'>CSS3</label>
            <label><input type='checkbox'name='interesting'value='javascript'>JavaScript</label>
            <label><input type='checkbox'name='interesting'value='ajax'>Ajax</label>
        </p>
        <p>
            <label><input type='checkbox'name='interesting'value='webapp'>Web Apps</label>
            <label><input type='checkbox'name='interesting'value='jquery'>jQuery</label>
            <label><input type='checkbox'name='interesting'value='nodejs'>nodeJS</label>
        </p>
    </fieldset>
    ```

    같은 보기 그룹의 라디오 단추들은 name 속성 값이 같아야함

    value 속성: 이용하여 버튼이 선택되었을 때 서버에 전달될 값을 입력

  ![image-20200309165446499](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309165446499.png)

  ​		=> 복수선택이 가능한 것을 확인할 수 있음

  

  - 선택 메뉴 select 요소

    - select 요소

       메뉴로 선택할 내용을 제시하고 하나를 선택하게 함

      자식 요소로 option요소를 가짐

    - option 요소

      메뉴 내용과 선택했을 때 값을 설정

      value: 메뉴가 선택되었을  때 서버로 전달되는 내용

      selected 속성 사용시 미리 선택 가능

    - 예

      ```html
      <p><label>휴대전화</label>
      <select name="telCode">
          <option value='010'>010</option>
          <option value='011'>011</option>
          <option value='016'>016</option>
          <option value='017'>017</option>
          <option value='019'>019</option>
          </select>
      <input type='tel'name='telNum'placeholder='1234-5678'></p>
      ```

      ![image-20200309165941322](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309165941322.png)

    - selected 속성 사용 예

      ```html
      <p><label>휴대전화</label>
      <select name="telCode">
          <option value='010'>010</option>
          <option value='011'selected>011</option>
          <option value='016'>016</option>
          <option value='017'>017</option>
          <option value='019'>019</option>
          </select>
      <input type='tel'name='telNum'placeholder='1234-5678'></p>
      ```

      ![image-20200309170121488](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309170121488.png)

  - textarea 요소

    - 정의: 여러 줄의 평범한 텍스트를 편집할 수 있는 폼 요소

    - textarea 속성들

      - cols: 한 줄당 입력할 수 있는 글자 수를 제한

      - rows: textarea가 몇 개의 줄로 보여질지 결정

        디자인적 요소는 CSS 통해 설정

      - wrap: soft  또는 hard의 값을 가짐
        1. soft: 텍스트가 제출될 때 줄바꿈이 되지 않음
        2. hard: 텍스트가 제출될 때 줄바꿈이 되도록 줄바꿈 문자를 삽입함

    - 예

      ```html
      <p><label for='comment'>하고싶은말: </label><br><textarea id='comment' cols='50' rows='5'></textarea></p>
      ```

      ![image-20200309170422240](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309170422240.png)

  - button 요소

    - 정의: 단추를 만드는 요소

    - type 속성에 따른 button 요소

      - type='summit' 

        서식을 제출하는 단추를 만듬

      - type='reset'

        서식을 초기화 하는 단추를 만듬

      "type 속성이 정의되지 않을 시 일반적인 단추를 만듦"

    - 예

      ```html
      <p><button type='submit'>가입하기</button><button type='reset'>재작성</button></p>
      ```

      ![image-20200309170621831](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309170621831.png)

### 3) HTML5 기타 요소들

- 새로운 텍스트 요소들

  - HTML5의 새로운 요소들
    - 웹 사이트를 분석하고 웹 제작자의 다양한 요구를 수집하여 많은 요소 추가
    - 많은 요소가 아직 대부분의 웹 브라우저에서 구현되지 않음
    - 서식 관련 요소의 추가가 많음

  - mark 요소

    - 정의: 문서 내에서 다른 문맥과 관련성을 표시하기 위해 참조 목적으로 표시하거나 하이라이팅한 텍스트

      1. 검색 된 내용을 표시하기 위해
      2. 틀린 곳을 표시하기 위해

    - 기본 스타일: 텍스트가 하이라이트 되어 보임

      문서 상황에 따라 CSS로 적절한 스타일 정의해 사용

    - 강조나 중요한 내용의 경우

      문서 내에서 다른 내용과 분리, 강조, 부각을 위해 em, strong, b, i, mark 요소 사용

    - 예

      ```html
      <p>아래 표시된 곳은 맞춤법이 틀린 곳입니다.</p>
      <p>나는 돌아오는 길에 친구 집에<mark>들려서</mark> 어제 놀다 두고 온 책을 가지고 왔다.</p>
      ```

      ![image-20200309171444235](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309171444235.png)

  - ruby, rt, rp

    - ruby

      - 주석: 중국어나 일본어 등의 발음이나 기타 주석 목적으로 사용
      - 요소: 구문에 루비 주석을 달기 위해 사용

    - rt

      - 루비 주석을 나타냄

      - 루비 주석을 지원하지 않는 웹 브라우저에서 루비 주석을 괄호로 표시하기 위해 사용

        ![image-20200309171541869](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309171541869.png)

  - time

    - time 요소 : 시간과 날짜를 표시하는데 사용

      정확한 24시간, 그레고리력 이외의 시간과 날짜는 표시하지 않음

      예) 기원전 250년 겨울, 80년대 중반, 주라기 중반 등은 time요소로 표시하지 않음

    - 예

      ```html
      <p>나는 보통 <time>16:00</time>에 간식을 먹습니다.</p>
      ```

    - datetime 속성: 정확한 날짜와 시간 명시

      ```html
      <div class='vevent'>
          <a class='url' href="https://www.web2con.com/">http://www.web2con.com/</a>
          <span class='summary'>Web 2.0 컨퍼런스</span>:
          <time class='dtstart'datetime="2007-10-05">10월 5일</time> -
          <time class='dtend'datetime='2007-10-20'>19</time>,
          at the <span class='location'>샌프란시스코 Argent 호텔</span>
      </div>
      ```

    - pubdate 속성: 부모 요소, 만약 부모 요소가 없다면 문서의 작성된 날짜와 시간 표시

      ```html
      <article>
          <h1>소소한 일</h1>
          <footer>작성일자 <time pubdate>2009-08-30></time></footer>
          <p>그 남자의 오토바이에 경적을 달았다.</p>
      </article>
      ```

  - 그 외의 텍스트 요소

    - S

      - 더 이상 정확하지 않거나, 관련없는 내용
      - 문서에서 삭제 되었음을 표시하는 del요소와는 구분해 사용

    - 예

      ```html
      <p>특판! 아이스 티와 레모네이드!</p>
      <p><s>권장 소비자 가격: 1병$3.99</s></p>
      <p><strong>1병에 겨우 $2.99 입니다.</strong></p>
      ```

    - command/menu

      - command 요소: 사용자가 실행할 수 있는 명령
      - menu 요소: command 목록
      - 현재까지 IE9에서만 유일히 구현
      - 사용법: 실행할 명령 스크립트와 연결되어야 하고 type속성을 이용하여 command type 지정

    - 예

      ```html
      <menu type="toolbar">
          <command type="radio"radiogroup="alignment" checked="checked" label="Left"icon="icons/alL.png" onclick="setAlign('left')">
          <command type="radio"radiogroup="alignment" label="Center"icon="icons/alC.png" onclick="setAlign('center')">
          <command type="radio"radiogroup="alignment" label="Right"icon="icons/alR.png" onclick="setAlign('right')">
          <hr>
          <command type="command"disabled label="Center"icon="icons/pub.png" onclick="publish()">
      </menu>
      ```

    - details/summary

      - details 요소

        추가적인 정보를 제공하기 위한 기능 요소

        보통 가려져 있다가 사용자 요구에 의해 퍼짐

        현재 IE9에서만 유일히 구현

      - summary 요소

        details 요소 내부에 요약이나 범례를 나타냄

      - 예

        ```html
        <section class='progress window'>
            <h1>Copying "Realyy Achieving Your Childhood Dreams"</h1>
            <details>
            <summary>Copying... <progress max='375505392' value='97543282'></progress>25%</summary>
            	<dl>
                    <dt>Transfer rate:</dt><dd>452KB/s</dd>
                    <dt>Local filename:</dt><dd>/home/rpausch/raycd.m4v</dd>
                    <dt>Remote filename:</dt><dd>/var/www/lectures/raycd.m4v/dd>
                    <dt>Duration</dt><dd>01:16:27</dd>
                    <dt>Color profile:</dt><dd>SD (6-1-6)</dd>
                    <dt>Dimensions:</dt><dd>302X240</dd>
                </dl>
            </details>
        </section>
        ```

  - datalist

    - 정의: 다른 입력 요소에서 사용하도록 미리 정의 된 option 집합
    - datalist 요소가 사용되는 요소 타입에 따라 다르게 구현

  - 새로운 input 타입

    - search
      - 검색을 위한 텍스트 입력 타입
      - 검색 목적을 제외하면 text 타입과 같은
    - tel
      - 전화번호 입력을 위한 타입
      - 줄바꿈을 할 수 없으나 입력 형태를 제한하지 않음
    - url
      - 인터넷 주소 입력을 위한 타입
      - 입력 값이 URL 형식인지 내용 검사를 함

    ![image-20200309173844555](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309173844555.png)

    - email
      - 이메일 입력을 위한 타입
      - 입력 값이 이메일 형식인지 내용 검사
    - datetime, date, month, week, time, datetime-local
      - datetime: 국제적 날짜와 시간 입력을 위한 타입
      - data, month, week: 날짜, 달, 주 입력을 위한 타입
      - time: 시간 입력을 위한 타입
      - datetime-local: 지역 날짜와 시간 입력을 위한 타입

    - 예

      ![image-20200309174111146](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309174111146.png)

    - number

      - 숫자 입력을 위한 타입

      - 직접 입력과 단추를 이용한 입력 모두 가능

      - 입력의 최소 수치와 최대 수치를 제한하기 위해 min, max 속성 사용 가능

      - step 속성: 단추를 이용해 입력 시 단추 입력 수치 제한을 위한 속성

        ![image-20200309174247416](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309174247416.png)

    - range
      - 정밀한 숫자 입력이 필요하지 않는 숫자 입력 타입
      - 슬라이드 형태로 표현
    - color
      - #으로 시작하는 7글자 색상코드 입력을 위한 타입

  - progress 요소

    - 정의: 작업의 진척도를 나타내는 요소

    - value 속성으로 얼마나 진척되었는지를 설정

    - max 속성으로 완료 수치 설정

    - 지원하지 않는 웹 브라우저를 위해 내부에서 텍스트로 입력

    - 예

      ```html
      <p>Progress: <progress value="50" max="100">50%</progress></p>
      ```

      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309174451421.png" alt="image-20200309174451421" style="zoom:80%;" />

  - meter 요소

    - 정의: 알려진 범위 내에서 수치 정도를 나타냄

      예) 투표율, 디스크 사용현황, 검색 빈도 등

    - 진척도 표시는 progress 요소를 사용

    - min, max, value 속성을 이용하여 나타냄

    - 지원하지 않는 웹 브라우저를 위해 내부에서 텍스트로 입력

    - 예

      ```html
      <dl>
          <dt>Radius: <dd><meter min=0 max=20 value=12 title="centimeters">12cm</meter></dd></dt>
      	<dt>Height: <dd><meter min=0 max=10 value=2 title="centimeters">2cm</meter></dd></dt>
      </dl>
      ```

      <img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309174700502.png" alt="image-20200309174700502" style="zoom:80%;" />

  - HTML5에서 사라진 요소들

    ![image-20200309174903634](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200309174903634.png)

    

