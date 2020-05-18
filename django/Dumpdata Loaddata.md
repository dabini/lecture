# Dumpdata/ Loaddata

> 장고에서 DB 데이터를 옮기는 방법!



- 기본 명령어

  ```shell
  $ python manage.py dumpdata > xxx.json
  ```

  장고가 사용하고 있는 모든 DB의 데이터를 json 형식으로 저장!

  수정 전에 dumpdata 해줄 것!

  

  

  ```shell
  $ python manage.py loaddata xxx.json
  ```

  기존에 dump해온 json 파일을 장고 DB에 넣어주는 작업!

  - 특정 주소 요구 시!

    > templates 폴더와 비슷하다

    ```shell
    $ mkdir board/fixtures
    $ mkdir board/fixtures/board
    
    $ python manage.py loaddata board/data.json
    UNIQUE 제약조건에 걸림!
    ```

    

