# 이차함수 멀티페이지 학습 앱

이 리포지토리는 고등학생을 위한 이차함수 학습용 Streamlit 앱 프로젝트 예시입니다.

## 프로젝트 구조

- `streamlit_app.py` - 앱 첫 화면 및 소개 페이지
- `pages/`
  - `1_basic_form.py` - 기본 형태
  - `2_leading_coefficient.py` - 최고차항의 계수
  - `3_vertical_shift.py` - y축 평행이동
  - `4_horizontal_shift.py` - x축 평행이동
  - `5_standard_form.py` - 표준형
  - `6_general_form.py` - 일반형
  - `7_shape_analysis.py` - 개형 분석
- `font/` - 로컬 한국어 글꼴 파일
- `requirements.txt` - 필요한 패키지 목록

## 앱 특징

- Streamlit 네이티브 멀티페이지 시스템 사용
- 각 주제별로 별도 페이지 구현
- 로컬 TTF 한국어 글꼴을 matplotlib에 적용
- 슬라이더로 매개변수 조절
- `st.latex`로 수식 표현
- 꼭짓점, y절편, 축 등 주요 점 강조
- x 범위는 -10부터 10까지, y 범위는 -10부터 10까지 고정

## 페이지 설명

1. Basic Form: `f(x)=x^2`
2. Leading Coefficient: `f(x)=ax^2` (a 조절)
3. Vertical Shift: `f(x)=x^2+c` (c 조절)
4. Horizontal Shift: `f(x)=(x-p)^2` (p 조절)
5. Standard Form: `f(x)=a(x-p)^2+c` (a, p, c 조절)
6. General Form: `f(x)=ax^2+bx+c` (a, b, c 조절)
7. Shape Analysis: a, b, c의 역할 설명, 꼭짓점과 y절편 표시

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

앱 실행 후 왼쪽 상단의 페이지 메뉴에서 학습 주제를 선택하면 됩니다.
