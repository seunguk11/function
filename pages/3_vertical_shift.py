import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from font_utils import configure_matplotlib_font

configure_matplotlib_font()

st.title("y축 평행이동 : y=ax+q")
st.write("a와 q값을 바꾸면 그래프가 위아래로 평행 이동합니다.")

a_values = [i * 0.5 for i in range(-10, 0)] + [i * 0.5 for i in range(1, 11)]
a = st.select_slider("a값 선택", options=a_values, value=1.0)
q = st.slider("q값", -10, 10, 0, step=1)
st.latex(rf"y = {a:g}x^2 + {q:g}")

x = np.linspace(-10, 10, 401)
y = a * x ** 2 + q

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#009e73", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.scatter([0], [q], color="red", zorder=5)
ax.annotate("꼭짓점", xy=(0, q), xytext=(2, max(min(q + 3, 9), -6)), arrowprops=dict(arrowstyle="->", color="red"))
ax.scatter([0], [q], color="orange", zorder=6)
if a > 0 and q <= 0:
    roots = np.sqrt(-q / a)
    if roots <= 10:
        ax.scatter([-roots, roots], [0, 0], color="blue", zorder=5)
        ax.annotate("x절편", xy=(roots, 0), xytext=(roots + 1, 2), arrowprops=dict(arrowstyle="->", color="blue"))
elif a < 0 and q >= 0:
    roots = np.sqrt(q / (-a))
    if roots <= 10:
        ax.scatter([-roots, roots], [0, 0], color="blue", zorder=5)
        ax.annotate("x절편", xy=(roots, 0), xytext=(roots + 1, 2), arrowprops=dict(arrowstyle="->", color="blue"))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(False)

st.pyplot(fig)

st.write("- 꼭짓점은 (0, q)이고, y절편도 q입니다.")
st.write("- q가 커지면 그래프가 위로, 작아지면 아래로 이동합니다.")
