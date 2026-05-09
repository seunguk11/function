import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from font_utils import configure_matplotlib_font

configure_matplotlib_font()

st.title("x축 평행이동 : y=a(x-p)")
st.write("a와 p값을 바꾸면 그래프가 좌우로 평행 이동합니다.")

a_values = [i * 0.5 for i in range(-10, 0)] + [i * 0.5 for i in range(1, 11)]
a = st.select_slider("a값 선택", options=a_values, value=1.0)
p = st.slider("p값", -5.0, 5.0, 0.0, step=0.5)
st.latex(rf"y = {a:g}(x - {p:g})^2")

x = np.linspace(-10, 10, 401)
y_original = a * x ** 2
y_shifted = a * (x - p) ** 2

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y_original, color="#009e73", linewidth=2, label=f"y = {a:g}x²")
ax.plot(x, y_shifted, color="#d55e00", linewidth=2, label=f"y = {a:g}(x - {p:g})²")
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.axvline(p, color="#555555", linestyle="--", linewidth=1)
ax.scatter([p], [0], color="red", zorder=5)
ax.annotate("꼭짓점", xy=(p, 0), xytext=(p + 1, 3), arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xticks(range(-10, 11))
ax.set_yticks(range(-10, 11))
ax.grid(True, which='both', color='lightgray', linestyle='-', linewidth=0.5)
ax.legend()

col1, col2 = st.columns([1, 1])

with col1:
    st.pyplot(fig)

with col2:
    st.markdown(
        f"""
        <div style='display:flex; flex-direction:column; justify-content:center; min-height:480px;'>
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- 꼭짓점 좌표: ({p:g}, 0)</p>
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- 축의 방정식: x = {p:g}</p>
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- x축으로 이동: {p:g}</p>
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- y축으로 이동: 0</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
