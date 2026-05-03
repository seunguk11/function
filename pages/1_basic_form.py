import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from font_utils import configure_matplotlib_font

configure_matplotlib_font()

st.title("1. 기본 형태")
st.write("가장 기본적인 이차함수의 그래프를 확인합니다.")
st.latex(r"f(x)=x^2")

x = np.linspace(-10, 10, 401)
y = x ** 2

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#0055cc", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.scatter([0], [0], color="red", zorder=5)
ax.annotate("꼭짓점 (0,0)", xy=(0, 0), xytext=(2, 4), arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(False)

st.pyplot(fig)

st.write("- 그래프 축은 x=-10에서 10, y=-10에서 10으로 고정되어 있습니다.")
st.write("- 꼭짓점은 (0, 0)이며, y절편과 x절편 모두 0입니다.")
