import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("3. y축 평행이동")
st.write("값 c를 높이면 그래프가 위로, 낮추면 아래로 이동합니다.")

c = st.slider("c값", -20, 20, 0, step=1)
st.latex(rf"f(x) = x^2 + {c:g}")

x = np.linspace(-10, 10, 401)
y = x ** 2 + c

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, color="#009e73", linewidth=2)
ax.axhline(0, color="#999999", linewidth=0.8)
ax.axvline(0, color="#999999", linewidth=0.8)
ax.scatter([0], [c], color="red", zorder=5)
ax.annotate("꼭짓점 (0, c)", xy=(0, c), xytext=(2, c + 10), arrowprops=dict(arrowstyle="->", color="red"))
ax.scatter([0], [c], color="orange", zorder=6)
if c <= 0:
    roots = np.sqrt(-c)
    ax.scatter([-roots, roots], [0, 0], color="blue", zorder=5)
    ax.annotate("x절편", xy=(roots, 0), xytext=(roots + 1, 5), arrowprops=dict(arrowstyle="->", color="blue"))
ax.set_xlim(-10, 10)
ax.set_ylim(min(np.min(y), c - 5), max(np.max(y), c + 5))
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig)

st.write("- 꼭짓점은 (0, c)이고 y절편도 c입니다.")
st.write("- c가 증가하면 그래프 전체가 위로 이동합니다.")
