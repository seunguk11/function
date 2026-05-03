import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("4. x축 평행이동")
st.write("값 p가 바뀌면 그래프가 오른쪽 또는 왼쪽으로 이동합니다.")

p = st.slider("p값", -5.0, 5.0, 0.0, step=0.5)
st.latex(rf"f(x) = (x - {p:g})^2")

x = np.linspace(-10, 10, 401)
y = (x - p) ** 2

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#d55e00", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.axvline(p, color="#555555", linestyle="--", linewidth=1)
ax.scatter([p], [0], color="red", zorder=5)
ax.annotate("꼭짓점 (p,0)", xy=(p, 0), xytext=(p + 1, 10), arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlim(-10, 10)
ax.set_ylim(-1, 100)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig)

st.write("- 꼭짓점은 (p, 0)입니다.")
st.write("- x축 평행이동은 축의 위치를 x = p로 바꿉니다.")
