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
y = a * (x - p) ** 2

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#d55e00", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.axvline(p, color="#555555", linestyle="--", linewidth=1)
ax.scatter([p], [0], color="red", zorder=5)
ax.annotate("꼭짓점", xy=(p, 0), xytext=(p + 1, 3), arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(False)

st.pyplot(fig)

st.write("- 꼭짓점은 (p, 0)이며, p가 바뀌면 그래프가 좌우로 이동합니다.")
st.write("- a가 바뀌면 그래프의 넓이와 방향이 변합니다.")
