import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
ax.annotate("꼭짓점 (0,0)", xy=(0, 0), xytext=(2, 20), arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlim(-10, 10)
ax.set_ylim(-1, 100)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig)

st.write("- 이 함수의 꼭짓점은 (0, 0)입니다.")
st.write("- y절편과 x절편은 모두 0입니다.")
