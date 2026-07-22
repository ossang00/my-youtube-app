import os
from wordcloud import WordCloud

# 한글 폰트 준비 (없으면 한 번만 내려받기)
FONT_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Regular.ttf"
FONT_PATH = "NanumGothic.ttf"
if not os.path.exists(FONT_PATH):
    try:
        with open(FONT_PATH, "wb") as f:
            f.write(requests.get(FONT_URL).content)
    except Exception:
        st.error("한글 폰트를 내려받지 못했어요. 잠시 후 새로고침해 주세요.")

# ...빈도 그래프 아래에 추가...

    # ── 3단계: 워드클라우드 ──────────────────
    st.subheader("☁️ 댓글 워드클라우드")
    wc = WordCloud(
        font_path=FONT_PATH, width=800, height=400,
        background_color="white",
    ).generate(" ".join(words))   # 2단계에서 걸러낸 단어 재사용 (한 글자 조사 제외)
    st.image(wc.to_array())
