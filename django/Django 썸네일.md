# Django 썸네일



## 웹/앱에서 많이 쓰이는 이미지 포맷

- 이미지 용량을 줄이려면 메타데이터를 제거하고, 적절한 크기로 리사이징, 가급적 JPG 포맷 사용



## 파이썬 이미지 처리 라이브러리

- PIL > Pillow > PILKit(라이브러리) > django-imagekit(앱)

  1. **PIL** : 09년 이후 업데이트가 없음
  2. **Pillow** : Pillow는 PIL 프로젝트에서 fork 되어서 나온 라이브러리로, PIL이 python 3를 지원하지 않기 때문에 pillow를 많이 사용하는 추세 (ImageField 사용시 필수)
  3. **PILKit** : PIL, Pillow를 좀 더 쓰기 쉽도록 도와주는 라이브러리
  4. **(참고) django-imagekit** : 이미지 썸네일 helper 장고 앱 (실제 이미지 처리시에는 PILKit 이 사용됨)

  - 설치 후, settings.INSTALLED_APPS에 imagekit 추가 필요



### ImageKit

> 이미지 썸네일 helper 장고 앱



- 설치

  ```bash
  $ pip install pillow
  $ pip install pilkit
  $ pip install django-imagekit
  ```

  

- settings.py > INSTALLED_APPS에 `imagekit`추가 

  