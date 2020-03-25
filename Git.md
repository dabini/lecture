# Git

> 분산 버전 관리 시스템(DVCS)

## 주요 명령어

###  init (저장소 생성)

```bash
~/git
$ git init
Initialized empty git repository in C:/user/.../git
```



### 버전관리

- `git status`

```bash
$git status
on branch master

#commit이 아직 없다. (버전 이력이 없다.)
no commits yet

#untracked files(현재 버전에 등록되지 않은 파일)
untrakced files:
	#커밋될 곳에 포함시키려면(staging area) add 명령어를 써
	(use "git add <file> .. ")

#정리멘트 - 커밋할 것도 없고, 다만 새로 생긴 파일이 있어.
nothing added to commit but untracked files present ...
```

```bash
$git status
on branch master

on branch master

No commits yet

#커밋될 변경 사항
Changes to be committed:
	#unstage하려면 아래의 명령어를...
	(use "git rm--cached <file>..." to unstage)
		#새로운 파일 a.txt 입니다.
    	new file: a.txt
```

```bash
$ git commit -m "Init"
[master 
(root- commit) ebd83a4] Init
1 file changed, 0 insertions(+), 0 deletions(-)
created mode ... a.txt

$git status
on branch master
#커밋할 거 없고 작업 공간도 깨끗
nothing to commit, working tree clean

$git log --oneline
ebd83a4 (HEAD -> master) Init
```



### 원격 저장소

- 원격 저장소 등록

```bash
$git remote add origin https://lab.ssafy.com/git
```



git아, 원격저장소에(remote) 에 추가해줘(add) origin이라는 이름으로 url을

```bash
$ git remote -v
```



- push

``` bash
$ git push origin master
```



- remove

```bash
$ git remote rm origin
```

