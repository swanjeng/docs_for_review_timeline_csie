import matplotlib.pyplot as plt
from datetime import date
import numpy as np
import matplotlib as mpl

path = "/home/swan/Downloads/LXGWWenKaiMonoTC-Regular.ttf"

mpl.font_manager.fontManager.addfont(path)

mpl.rcParams["font.family"] = "LXGW WenKai Mono TC"
mpl.rcParams["font.size"] = 28

# 日期僅作為等間距設定用
dates = [date(1900, 1, 1), date(1905, 1, 1), date(1910, 1, 1)]
min_date = date(np.min(dates).year - 5, np.min(dates).month, np.min(dates).day)
max_date = date(np.max(dates).year + 5, np.max(dates).month, np.max(dates).day)

label_dates = [date(1898, 1, 1), date(1902, 1, 1), date(1907, 7, 1)]

str1 = """
高中畢業 ~ 入學前：
    1. 考七月的 APCS ，挑戰
       實作四級分以上。
    2. 運用台大開放式課程的
       資源進行微積分、線性
       代數和離散數學的先修。"""

str2 = """大一：
    1. 學習程式設計、數位電路導論、
       微積分、線性代數等核心課程。
    2. 選修「機器人軟體系統專案」、
       通識課 「永續發展目標 (SDGs)
       導論」等課程。
    3. 參與 電腦網路愛好社 社團。"""

str3 = """大二：
    1. 學習數位系統導論與實驗、
       資料結構、離散數學、演算
       法等核心課程。
    2. 選修「Linux 系統與開源軟
       體」、「視窗程式設計」、
       「物聯網設備之程式設計與
       界面」等課程。"""

labels = [str1, str2, str3]

fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
ax.set_xlim(min_date, max_date)
ax.set_ylim(-3, 2)
ax.axhline(0, xmin=0.05, xmax=0.95, color=(0.5, 0, 0), zorder=1, lw=3)

ax.scatter(dates, np.zeros(len(dates)), s=240, color=(1, 0, 0), zorder=2)

label_offsets = [0.3, -2.25, 0.3]
for i in range(len(dates)):
    ax.text(label_dates[i], label_offsets[i], labels[i], ha='left',
            color=(0, 0, 0), linespacing=2, backgroundcolor=(1, 0.9, 0.9))

stems = np.zeros(len(dates))
stems[::2] = 0.3
stems[1::2] = -0.3
markerline, stemline, baseline = ax.stem(
    dates, stems, use_line_collection=True)
plt.setp(stemline, color=(1, 0.5, 0), lw=3)

# hide lines around chart
for spine in ["left", "top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

# hide tick labels
ax.set_xticks([])
ax.set_yticks([])

plt.show()
