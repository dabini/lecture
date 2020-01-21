# git & github

개발자 세계에서 살아남기

- '프로젝트' 

  프로젝트 중심의 자기소개

- Git,

  - 오픈소스 프로젝트
  - 개발자의 이력서
  - 분산 버전 관리 시스템
  - 파일들의 로그를 남겨서 파일 간 차이를 알 수 있음

- git의 작업 흐름

  - `add` 커밋할 목록에 추가
  - `commit` 커밋(create a snapshot) 만들기
  - `push` 현재까지의 역사가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

- git의 기본

  - $ git`add` `helloworld.py`

  - $git `commit` `-m`   -로 시작하면  short name 옵션

  - $git congif `--global` `user.name "John"`  --로 시작하면  short name 옵션

    

## CLI

- CLI 종류
  - 유닉스  shell(sh, zsh, bash 등)
  -  CP/M
  -  DOS의 command.com
  -  cmd(window 전용)

- bash 명령어 기초
  - ls 현재 디렉토리의 내용들을 나열
  - cd 현재 작업하는 디렉토리를 변경
  - mkdir  새로운 디렉토리 생성
  - echo 문자열 출력
  - rm 파일 지우기
  - exit 터미널 종료
- CLI는 항상 자신이 어디있는지를 주의하자



## gitbash 다운로드

1. google 검색창에 git bash 검색후 git for windows에서 다운로드
2. 



### 집에서 불러올 때

1. git clone "clone or download링크 복사"
2. ls 로 폴더 구조 확인 가능
3. 파일 만들기 `touch a.txt`
4. 파일 경로 추가 `git add .`  add뒤에 한 칸 뛰고 . 하면 폴더 안 모든 파일 커맨드됨
5. 내용 입력(?) `git commit -m "b.txt 파일 추가"`
6. git에 올리기 `git push origin master`



### git 파일 수정하기

1.  `git pull origin master`으로 파일 모두 다운 받은 후 수정하기



### git  파일 만들기

1. 새로운 폴더 만든 후, 마우스 우클릭에서 `Git BASH here`클릭 
2. `git init`
3. `touch README.md`로 새로운 파일 만들기 

4. `git add README.md`

5. Git 페이지에서 `TIL` repository 만들고 경로 복사하기

6. `git commit -m "added README file"`

7. `git remote -v`

8. `git remote add origin https://github.com/dabini/TIL.git`

9.  `git push origin master`

10. 수정하고 싶으면  `git pull origin master`로 파일 다운받아서, 수정하고 `git push origin master`로 다시 올리기

    

## jupyter 시작하기

1. BASH 창에서 `pip install notebook`입력
2. 상위폴더 올라가기 `cd ..`
3. 새로운 폴더 만들기 `mkdir lecture`
4. lecture 폴더로 이동하기 `cd lecture`
5. 쥬피터 실행하기 `jupyter notebook`
6. `ctrl + c`로 나가기



### Jupyter 환경설정



1. `cd ..`으로 상위 폴더로 나간 뒤, `ls -al`로 전체 디렉토리 확인

2. `vim .bashrc`로 새로운 폴더 만들기

3. `alias jp="jupyter notebook"` 

4. `esc` 버튼 누르고 `:` 하고 `wq`누르고 엔터키 누르면 밖으로 나와짐

5. `source ~/.bashrc`

6. `cd lecture/`

7. jp 입력하면 jupyter로 들어가짐

   

### 잘못입력했을 때(init 지우기)

`rm -rf .git` 

