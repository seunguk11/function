import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from font_utils import configure_matplotlib_font

configure_matplotlib_font()

st.title("x축 y축 동시 평행이동")
st.write("a, p, q값을 바꾸면 그래프가 x축과 y축 방향으로 동시에 평행 이동합니다.")

a_values = [i * 0.5 for i in range(-10, 0)] + [i * 0.5 for i in range(1, 11)]
a = st.select_slider("a값 선택", options=a_values, value=1.0)
p = st.slider("p값", -5.0, 5.0, 0.0, step=0.5)
q = st.slider("q값", -10, 10, 0, step=1)
st.latex(rf"y = {a:g}(x - {p:g})^2 + {q:g}")

x = np.linspace(-10, 10, 401)
y_original = a * x ** 2
y_shifted = a * (x - p) ** 2 + q

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y_original, color="#009e73", linewidth=2, label=f"y = {a:g}x²")
ax.plot(x, y_shifted, color="#d55e00", linewidth=2, label=f"y = {a:g}(x - {p:g})² + {q:g}")
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.scatter([p], [q], color="red", zorder=5)
ax.annotate("꼭짓점", xy=(p, q), xytext=(p + 1, max(min(q + 3, 9), -6)), arrowprops=dict(arrowstyle="->", color="red"))
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
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- 꼭짓점 좌표: ({p:g}, {q:g})</p>
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- 축의 방정식: x = {p:g}</p>
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- x축으로 이동: {p:g}</p>
            <p style='font-size:1.15rem; margin:0.5rem 0;'>- y축으로 이동: {q:g}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
