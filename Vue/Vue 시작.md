# Vue 시작

- VS CODE

  - Vetur extension install

- Chrome

  - Vue.js devtools install
  - 설정에서 '파일 URL에 대한 액세스 허용'

- CDN

  https://kr.vuejs.org/v2/guide/installation.html

  ```html
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  ```

  

- code

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJS</title>
  </head>
  <body>
    <div id="app">
        
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el : "#app", //어디에 마운팅할 것인지를 지정 (element)
        data : {
          
        }
      })
    </script>
  </body>
  </html>
  ```

  

- v-bind

  `:`으로도 쓰임

- v-on

  `@`으로도 쓰임

- v-model

  v-model => input, select, textarea

- v-show

  > https://kr.vuejs.org/v2/guide/conditional.html (if와 비교)

  