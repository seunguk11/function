import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("5. 표준형")
st.write("표준형 방정식으로 꼭짓점의 위치와 그래프 이동을 확인합니다.")

a_values = [i * 0.5 for i in range(-10, 0)] + [i * 0.5 for i in range(1, 11)]
a = st.select_slider("a값 선택", options=a_values, value=1.0)
p = st.slider("p값", -5.0, 5.0, 0.0, step=0.5)
c = st.slider("c값", -20, 20, 0, step=1)

st.latex(rf"f(x) = {a:g}(x - {p:g})^2 + {c:g}")

x = np.linspace(-10, 10, 401)
y = a * (x - p) ** 2 + c

vertex_x = p
vertex_y = c

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#cc79a7", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.axvline(p, color="#555555", linestyle="--", linewidth=1)
ax.scatter([vertex_x], [vertex_y], color="red", zorder=5)
ax.annotate("꼭짓점", xy=(vertex_x, vertex_y), xytext=(vertex_x + 1, vertex_y + 10), arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlim(-10, 10)
ax.set_ylim(min(np.min(y), vertex_y - 10), max(np.max(y), vertex_y + 10))
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig)

st.write(f"- 꼭짓점: ({vertex_x:.1f}, {vertex_y:.1f})")
st.write("- x축 평행이동은 x = p, y축 평행이동은 c에 영향을 줍니다.")
