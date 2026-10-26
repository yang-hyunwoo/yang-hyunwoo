
from datetime import datetime, timedelta, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager

QUOTES = [
    "좋은 코드는 읽기 쉬운 코드다.",
    "작은 개선이 모여 큰 변화를 만든다.",
    "복잡함을 줄이는 것이 좋은 설계의 시작이다.",
    "동작하는 코드에서 멈추지 말자.",
    "오늘의 배움이 내일의 실력이 된다.",
    "문제를 이해하는 것이 해결의 시작이다.",
    "단순함은 좋은 설계의 핵심이다.",
    "꾸준함은 가장 강력한 성장 전략이다.",
    "완벽함보다 지속적인 개선이 중요하다.",
    "코드는 작성하는 시간보다 읽는 시간이 더 길다.",
    "좋은 개발자는 끊임없이 질문한다.",
    "기술보다 중요한 것은 문제를 해결하는 능력이다.",
    "빠른 코드보다 이해하기 쉬운 코드가 중요하다.",
    "작은 리팩토링이 큰 차이를 만든다.",
    "실패는 더 나은 설계를 위한 과정이다.",
    "배움을 멈추는 순간 성장도 멈춘다.",
    "좋은 설계는 변화에 유연하게 대응한다.",
    "중복을 줄이고 의도를 명확하게 표현하자.",
    "코드는 미래의 나를 위한 문서이기도 하다.",
    "꾸준히 작성한 코드가 결국 실력이 된다.",
]

KST = timezone(timedelta(hours=9))
today = datetime.now(KST).date()

quote = QUOTES[today.toordinal() % len(QUOTES)]

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

font_manager.fontManager.addfont(font_path)
font = font_manager.FontProperties(fname=font_path)

plt.rcParams["svg.fonttype"] = "path"

fig = plt.figure(figsize=(10, 2), dpi=100)
fig.patch.set_facecolor("#1a1b27")

fig.text(
    0.5, 0.76,
    "TODAY'S DEV QUOTE",
    ha="center",
    va="center",
    fontsize=15,
    fontweight="bold",
    color="#7aa2f7"
)

fig.text(
    0.5, 0.48,
    f"“{quote}”",
    ha="center",
    va="center",
    fontsize=16,
    fontproperties=font,
    color="#c0caf5"
)

fig.text(
    0.5, 0.19,
    "Keep Learning, Keep Building!",
    ha="center",
    va="center",
    fontsize=10,
    color="#565f89"
)

Path("dist").mkdir(exist_ok=True)

fig.savefig(
    "dist/dev-quote.svg",
    format="svg",
    facecolor=fig.get_facecolor(),
    bbox_inches="tight",
    pad_inches=0.25
)

plt.close(fig)

print(f"Date: {today}")
print(f"Quote: {quote}")
