from tkinter import font

from matplotlib.font_manager import weight_dict
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

configurations = ["1 node\n1 core", "1 node\n8 cores", "2 nodes\n8 cores"]
mastodon_times = [898.748182, 112.960295, 118.849409]
bluesky_times = [1310.767941, 173.917788, 133.725501]

x_positions = range(len(configurations))
bar_width = 0.4

fig, ax = plt.subplots(figsize=(10, 7), facecolor="white")

bars_mastodon = ax.bar(
    [x - bar_width / 2 for x in x_positions],
    mastodon_times,
    width=bar_width,
    label="Mastodon",
    color="#1f77b4",
    edgecolor="white",
    linewidth=1.0,
    zorder=3,
)
bars_bluesky = ax.bar(
    [x + bar_width / 2 for x in x_positions],
    bluesky_times,
    width=bar_width,
    label="BlueSky",
    color="#ff7f0e",
    edgecolor="white",
    linewidth=1.0,
    zorder=3,
)

ax.grid(linestyle="--", linewidth=0.8, alpha=0.5, zorder=0)

ax.set_xticks(list(x_positions))
ax.set_xticklabels(configurations, weight="bold", fontsize=12)
ax.set_ylabel("Execution time (seconds)", weight="bold", fontsize=12)
ax.set_title("Mastodon and BlueSky Execution Times", weight="bold", fontsize=16)
ax.legend(fontsize=12)

for bars in (bars_mastodon, bars_bluesky):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.1f}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
        )

fig.tight_layout()
plt.savefig("execution_times.pdf", format="pdf", bbox_inches="tight")
plt.show()

