import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider

# Asymptotic growth curves
n = np.arange(1, 31)
y_constant = np.ones_like(n, dtype=float) * 5
y_log = 5 * np.log2(n) + 2
y_linear = 2 * n
y_nlogn = 0.45 * n * np.log2(n) + 2
y_quadratic = 0.4 * n**2

fig, ax = plt.subplots(figsize=(11, 7))
fig.canvas.manager.set_window_title("Asymptotic Notation Animation")
plt.subplots_adjust(bottom=0.25, top=0.84)

fig.suptitle("ASYMPTOTIC NOTATION", fontsize=19, fontweight="bold", y=0.96)
ax.set_title("How algorithm growth changes as input size increases", fontsize=11)
ax.set_xlabel("Input Size (n)", fontsize=12)
ax.set_ylabel("Illustrative Number of Operations", fontsize=12)
ax.set_xlim(1, 30)
ax.set_ylim(0, 390)
ax.set_xticks(np.arange(0, 31, 2))
ax.grid(True, linestyle="--", alpha=0.35)

line_constant, = ax.plot([], [], linewidth=2.8, label="O(1) - Constant")
line_log, = ax.plot([], [], linewidth=2.8, label="O(log n) - Logarithmic")
line_linear, = ax.plot([], [], linewidth=2.8, label="O(n) - Linear")
line_nlogn, = ax.plot([], [], linewidth=2.8, label="O(n log n) - Linearithmic")
line_quad, = ax.plot([], [], linewidth=2.8, label="O(n^2) - Quadratic")
ax.legend(loc="upper left", frameon=True, fontsize=9)

info = fig.text(0.13, 0.13, "Input size n: 0 | Curves are ready to grow...", fontsize=10, fontweight="bold")
status = fig.text(0.13, 0.085, "Status: Playing", fontsize=10)

frame = 0
paused = False
speed = 180

def update(_):
    global frame
    if not paused:
        frame = (frame + 1) % (len(n) + 1)
    k = frame
    x = n[:k]
    line_constant.set_data(x, y_constant[:k])
    line_log.set_data(x, y_log[:k])
    line_linear.set_data(x, y_linear[:k])
    line_nlogn.set_data(x, y_nlogn[:k])
    line_quad.set_data(x, y_quadratic[:k])
    if k == 0:
        info.set_text("Input size n: 0 | Curves are ready to grow...")
    else:
        info.set_text(
            f"Input size n: {k} | O(1): {y_constant[k-1]:.1f}"
            f" | O(log n): {y_log[k-1]:.1f} | O(n): {y_linear[k-1]:.1f}"
        )
    status.set_text("Status: Paused" if paused else "Status: Playing")
    return line_constant, line_log, line_linear, line_nlogn, line_quad, info, status

ani = FuncAnimation(fig, update, interval=speed, blit=False, cache_frame_data=False)

ax_pause = plt.axes([0.13, 0.025, 0.13, 0.045])
ax_restart = plt.axes([0.28, 0.025, 0.13, 0.045])
ax_speed = plt.axes([0.56, 0.035, 0.28, 0.03])
pause_button = Button(ax_pause, "Pause / Play")
restart_button = Button(ax_restart, "Restart")
speed_slider = Slider(ax_speed, "Speed", 50, 500, valinit=speed, valstep=25)

def toggle_pause(_):
    global paused
    paused = not paused

def restart(_):
    global frame, paused
    frame = 0
    paused = False

def change_speed(value):
    ani.event_source.interval = int(value)

pause_button.on_clicked(toggle_pause)
restart_button.on_clicked(restart)
speed_slider.on_changed(change_speed)

plt.show()
