import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from font_utils import configure_matplotlib_font

configure_matplotlib_font()

st.title("2. 최고차항의 계수")
st.write("a값이 바뀌면 포물선의 넓이와 방향이 달라집니다.")

a_values = [i * 0.5 for i in range(-10, 0)] + [i * 0.5 for i in range(1, 11)]
a = st.select_slider("a값 선택", options=a_values, value=1.0)

st.latex(rf"f(x) = {a:g}x^2")

x = np.linspace(-10, 10, 401)
y = a * x ** 2

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#0072b2", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.scatter([0], [0], color="red", zorder=5)
ax.annotate("꼭짓점 (0,0)", xy=(0, 0), xytext=(2, 8), arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(False)

st.pyplot(fig)

st.write("- a > 0이면 위로 볼록, a < 0이면 아래로 볼록입니다.")
st.write("- |a|가 커질수록 그래프는 더 좁아지고, |a|가 작을수록 더 넓어집니다.")
