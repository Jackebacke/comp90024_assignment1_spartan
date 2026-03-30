from matplotlib import axes, figure
import matplotlib.pyplot as plt

configurations = ["1 node\n1 core", "1 node\n8 cores", "2 nodes\n8 cores"]
mastodon_times = [0.0, 0.0, 0.0]
bluesky_times = [0.0, 0.0, 0.0]

x_positions = range(len(configurations))
bar_width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(
    [x - bar_width / 2 for x in x_positions],
    mastodon_times,
    width=bar_width,
    label="Mastodon",
    color="orange",
)
plt.bar(
    [x + bar_width / 2 for x in x_positions],
    bluesky_times,
    width=bar_width,
    label="BlueSky",
    color="blue",
)

plt.xticks(list(x_positions), configurations)
plt.ylabel("Execution time (seconds)")
plt.title("Mastodon vs BlueSky Execution Times")
plt.legend()
plt.tight_layout()
plt.show()
