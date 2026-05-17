import streamlit as st
from font_utils import configure_matplotlib_font

configure_matplotlib_font()

st.set_page_config(page_title="이차함수 배우기", page_icon="📘", layout="wide")

st.title("📘 이차함수 배우기")
st.write("이 앱은 고등학생을 위한 이차함수 학습 도구입니다.")
st.write("왼쪽 상단 페이지 메뉴에서 각 주제를 선택하여 그래프와 수식을 함께 확인하세요.")

st.markdown(
    """
    - y축 평행이동 : y=ax^2+q
    - x축 평행이동 : y=a(x-p)^2
    - x축 y축 동시 평행이동
    """
)
