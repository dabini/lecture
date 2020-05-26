# Vue-app

### 1. Lifecycle Diagram

![img](Vue-instance-lifecycle-Page-1.png)

#### 1) created

- created 시점에 도착할시 method에 정의된 함수가 자연스럽게 실행됨
- 초기화 이후 AJAX 모듈을 보내기 좋은 hook /시점
- Data, Methods에 접근 가능



#### 2) mounted

- DOM과 Vue 인스턴스가 연동이 완료되고 난 이후에 실행할 일들

- `mounted ` 과정을 넘겨야 DOM과 연동되어 활동이 됨!



#### JS 에서 볼 수 있는 비동기 요청

- Axios

- setTimeout

  서버 과부하를 막기 위한 안전장치

  ```html
  setTimeout(() => {}, 500)
  ```

  

