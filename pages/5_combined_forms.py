import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from font_utils import configure_matplotlib_font

configure_matplotlib_font()

st.title("이차함수의 일반형과 표준형")
st.write("일반형과 표준형을 비교하며 이차함수의 특징을 알아봅니다.")

st.subheader("일반형: y = ax² + bx + c")
a_values = [i * 0.5 for i in range(-10, 0)] + [i * 0.5 for i in range(1, 11)]
a1 = st.select_slider("a값 선택 (일반형)", options=a_values, value=1.0, key="a1")
b = st.slider("b값", -10, 10, 0, step=1, key="b")
c = st.slider("c값", -10, 10, 0, step=1, key="c")
st.latex(rf"y = {a1:g}x^2 + {b:g}x + {c:g}")

x = np.linspace(-10, 10, 401)
y1 = a1 * x ** 2 + b * x + c

vertex_x1 = -b / (2 * a1)
vertex_y1 = a1 * vertex_x1 ** 2 + b * vertex_x1 + c

fig1, ax1 = plt.subplots(figsize=(7, 4))
ax1.plot(x, y1, color="#56b4e9", linewidth=2)
ax1.axhline(0, color="#999999", linewidth=0.8)
ax1.axvline(0, color="#999999", linewidth=0.8)
ax1.axvline(vertex_x1, color="#555555", linestyle="--", linewidth=1)
ax1.scatter([vertex_x1], [vertex_y1], color="red", zorder=5)
ax1.scatter([0], [c], color="orange", zorder=5)
ax1.annotate("꼭짓점", xy=(vertex_x1, vertex_y1), xytext=(vertex_x1 + 1, max(min(vertex_y1 + 3, 9), -7)), arrowprops=dict(arrowstyle="->", color="red"))
ax1.annotate("y절편", xy=(0, c), xytext=(1, max(min(c + 3, 9), -7)), arrowprops=dict(arrowstyle="->", color="orange"))
ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(False)

st.pyplot(fig1)

st.write(f"- 꼭짓점: ({vertex_x1:.2f}, {vertex_y1:.2f})")
st.write(f"- 대칭축: x = {vertex_x1:.2f}")

st.subheader("표준형: y = a(x - p)² + q")
a2 = st.select_slider("a값 선택 (표준형)", options=a_values, value=1.0, key="a2")
p = st.slider("p값", -5.0, 5.0, 0.0, step=0.5, key="p")
q = st.slider("q값", -10, 10, 0, step=1, key="q")
st.latex(rf"y = {a2:g}(x - {p:g})^2 + {q:g}")

y2 = a2 * (x - p) ** 2 + q

vertex_x2 = p
vertex_y2 = q

fig2, ax2 = plt.subplots(figsize=(7, 4))
ax2.plot(x, y2, color="#cc79a7", linewidth=2)
ax2.axhline(0, color="#999999", linewidth=0.8)
ax2.axvline(0, color="#999999", linewidth=0.8)
ax2.axvline(p, color="#555555", linestyle="--", linewidth=1)
ax2.scatter([vertex_x2], [vertex_y2], color="red", zorder=5)
ax2.annotate("꼭짓점", xy=(vertex_x2, vertex_y2), xytext=(vertex_x2 + 1, max(min(vertex_y2 + 3, 8), -7)), arrowprops=dict(arrowstyle="->", color="red"))
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid(False)

st.pyplot(fig2)

st.write(f"- 꼭짓점: ({vertex_x2:.1f}, {vertex_y2:.1f})")

st.subheader("비교와 얻을 수 있는 정보")
st.write("일반형과 표준형은 같은 이차함수를 표현하는 서로 다른 형태입니다.")
st.write("- **변환 관계**: 일반형 y = ax² + bx + c를 표준형 y = a(x - p)² + q로 변환할 수 있습니다.")
st.write(f"  - p = -b/(2a) = {-b/(2*a1):.2f}")
st.write(f"  - q = c - a p² = {c - a1 * (vertex_x1)**2:.2f}")
st.write("- **얻을 수 있는 정보**:")
st.write("  - 표준형에서는 p와 q가 직접 꼭짓점의 좌표를 나타냅니다.")
st.write("  - 일반형에서는 b와 a로부터 대칭축을 계산할 수 있습니다.")
st.write("  - 두 형태 모두에서 a는 그래프의 방향과 넓이를 결정합니다.")

# 같은 a, p, q로 설정된 경우 비교
if abs(a1 - a2) < 0.1 and abs(vertex_x1 - p) < 0.1 and abs(vertex_y1 - q) < 0.1:
    st.write("현재 설정에서 일반형과 표준형이 같은 그래프를 나타냅니다.")
else:
    st.write("현재 설정에서 일반형과 표준형이 다른 그래프를 나타냅니다.")