import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("7. 개형 분석")
st.write("a, b, c가 각각 이차함수 개형에 어떤 영향을 주는지 알아봅니다.")

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
ax.plot(x, y, color="#0072b2", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
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

st.subheader("계수의 역할")
st.write("- a: 그래프의 위/아래 방향과 개방 정도를 결정합니다.")
st.write("- b: 대칭축의 위치와 그래프의 좌우 이동을 간접적으로 조절합니다.")
st.write("- c: y절편을 결정하며 그래프를 위아래로 이동합니다.")

st.subheader("중요한 점")
st.write(f"- 꼭짓점: ({vertex_x:.2f}, {vertex_y:.2f})")
st.write(f"- y절편: (0, {c})")
