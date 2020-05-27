# Vue 프로젝트 시작

### 1. node.js 버전 확인

- VSCode terminal에서 `node -v`를 쳐서 버전이 v12.16.3 나오는지 확인



### 2. npm 설치

- `npm install -g @vue/cli` 로 npm 설치
- 이후로 `vue`로 시작하는 명령어가 가능해짐



### 3. 프로젝트 시작

- `vue create { 프로젝트 명 }`
- `Enter`키 로 default로 시작하기

- `cd { 프로젝트 명}` : 프로젝트 폴더로 이동
- `npm run serve` 



### 4. 컴포넌트 사용하기

- `component`폴더 안에 vue 파일 만들기

  - 기본 형식 만들어주기 `<` + `tab`

  ```vue
  <template>
      <h1>나의 첫 컴포넌트</h1>
  </template>
  
  <script>
  export default {
      name : 'MyComponent',
  
  }
  </script>
  
  <style>
  
  </style>
  ```

- `App.vue`파일

  - script에서 import 하기

    ```vue
    import MyComponent from './components/MyComponent.vue'
    ```

  - script 컴포넌트 등록하기

    ```vue
    export default {
      name: 'App',
      components: {
        HelloWorld,
        MyComponent,
    ```

  - template에서 사용

    ```vue
      <div id="app">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
        <MyComponent />
      </div>
    ```

- component내 template 안에서는 하나의 요소만 사용 가능!

  => 여러개 사용할 때는 `div`와 같은 태그로 묶어주기

- 컴포넌트 내 `data`는 return 값이 있는 **function**이어야 한다



### 5. 라이브러리 사용

- 터미널에서 라이브러리 설치하기 

  ```bash
  $ npm install axios
  
  # 줄임말 사용가능!
  $ npm i axios
  ```

  