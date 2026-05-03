import streamlit as st

st.set_page_config(page_title="이차함수 배우기", page_icon="📘", layout="wide")

st.title("📘 이차함수 배우기")
st.write("이 앱은 고등학생을 위한 이차함수 학습 도구입니다.")
st.write("왼쪽 상단의 페이지 메뉴에서 주제를 선택하고 그래프와 방정식을 함께 확인해보세요.")

st.markdown(
    """
    - 기본 형태: $f(x)=x^2$
    - 최고차항의 계수: $f(x)=ax^2$
    - y축 평행이동: $f(x)=x^2+c$
    - x축 평행이동: $f(x)=(x-p)^2$
    - 표준형: $f(x)=a(x-p)^2+c$
    - 일반형: $f(x)=ax^2+bx+c$
    - 개형 분석: 계수의 역할과 꼭짓점, y절편
    """
)

st.info("그래프 범위는 x = -10부터 x = 10까지입니다. 슬라이더를 조절하며 이차함수의 변화를 관찰해보세요.")
