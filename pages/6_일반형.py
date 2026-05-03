import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("6. 일반형")
st.write("일반형 이차함수에서 a, b, c는 그래프 모양과 꼭짓점 위치를 결정합니다.")

a_values = [i * 0.5 for i in range(-10, 0)] + [i * 0.5 for i in range(1, 11)]
a = st.select_slider("a값 선택", options=a_values, value=1.0)
b = st.slider("b값", -10, 10, 0, step=1)
c = st.slider("c값", -20, 20, 0, step=1)

st.latex(rf"f(x) = {a:g}x^2 + {b:g}x + {c:g}")

x = np.linspace(-10, 10, 401)
y = a * x ** 2 + b * x + c

vertex_x = -b / (2 * a)
vertex_y = a * vertex_x ** 2 + b * vertex_x + c

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#56b4e9", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.axvline(vertex_x, color="#555555", linestyle="--", linewidth=1)
ax.scatter([vertex_x], [vertex_y], color="red", zorder=5)
ax.scatter([0], [c], color="orange", zorder=5)
ax.annotate("꼭짓점", xy=(vertex_x, vertex_y), xytext=(vertex_x + 1, vertex_y + 10), arrowprops=dict(arrowstyle="->", color="red"))
ax.annotate("y절편", xy=(0, c), xytext=(1, c + 10), arrowprops=dict(arrowstyle="->", color="orange"))
ax.set_xlim(-10, 10)
ax.set_ylim(min(np.min(y), vertex_y - 10, c - 10), max(np.max(y), vertex_y + 10, c + 10))
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig)

st.write(f"- 꼭짓점: ({vertex_x:.2f}, {vertex_y:.2f})")
st.write(f"- 대칭축: x = {vertex_x:.2f}")
