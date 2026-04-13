import matplotlib.pyplot as plt
from datetime import date
import numpy as np
import matplotlib as mpl

path = "/home/swan/Downloads/iansui/Iansui-Regular.ttf"

mpl.font_manager.fontManager.addfont(path)

mpl.rcParams["font.family"] = "Iansui"
mpl.rcParams["font.size"] = 28

# 日期僅作為等間距設定用
dates = [date(1900, 1, 1), date(1905, 1, 1), date(1910, 1, 1)]
min_date = date(np.min(dates).year - 5, np.min(dates).month, np.min(dates).day)
max_date = date(np.max(dates).year + 5, np.max(dates).month, np.max(dates).day)

label_dates = [date(1897, 1, 1), date(1901, 7, 1), date(1907, 7, 1)]

str4 = """大三：
     1. 學習微算機原理與應用、
        作業系統、編譯系統等核心課程。
     2. 選修「多媒體系統與應用」、
        「Linux 核心設計」等課程。
     3. 製作與數位人權相關的資訊專題。"""

str5 = """大四：
     1. 選修「人工智慧導論」、
        「影像處理、電腦視覺及深度學習概論」
        等課程。"""

str6 = """大學畢業後：
     1. 繼續升學，前進資訊工程研究所。
     2. 研究所畢業後，到科技公司就業。"""

labels = [str4, str5, str6]

fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
ax.set_xlim(min_date, max_date)
ax.set_ylim(-2.5, 2)
ax.axhline(0, xmin=0.05, xmax=0.95, color=(0.5, 0, 0), zorder=1, lw=3)

ax.scatter(dates, np.zeros(len(dates)), s=240, color=(1, 0, 0), zorder=2)

label_offsets = [-1.6, 0.3, -0.9]
for i in range(len(dates)):
    ax.text(label_dates[i], label_offsets[i], labels[i], ha='left',
            color=(0, 0, 0), linespacing=2, backgroundcolor=(1, 0.9, 0.9))

stems = np.zeros(len(dates))
stems[::2] = -0.3
stems[1::2] = 0.3
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
