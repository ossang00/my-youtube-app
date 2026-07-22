import os

import streamlit as st
import requests
from wordcloud import WordCloud

st.set_page_config(page_title="댓글 워드클라우드", page_icon="☁️")
st.title("☁️ 댓글 워드클라우드")

# 한글 폰트 준비 (없으면 한 번만 내려받기)
FONT_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Regular.ttf"
FONT_PATH = "NanumGothic.ttf"

if not os.path.exists(FONT_PATH):
    try:
        with open(FONT_PATH, "wb") as f:
            f.write(requests.get(FONT_URL).content)
    except Exception:
        st.error("한글 폰트를 내려받지 못했어요. 잠시 후 새로고침해 주세요.")

if "comments" not in st.session_state:
    st.warning("먼저 메인 페이지에서 댓글을 가져와 주세요! 👈 왼쪽 메뉴에서 이동할 수 있어요.")
else:
    comments = st.session_state.comments

    # 빈도 페이지와 동일한 방식으로 단어 걸러내기 (한 글자 단어 제외)
    words = " ".join(comments).split()
    words = [w for w in words if len(w) > 1]

    # ── 3단계: 워드클라우드 ──────────────────
    wc = WordCloud(
        font_path=FONT_PATH, width=800, height=400,
        background_color="white",
    ).generate(" ".join(words))   # 2단계에서 걸러낸 단어 재사용 (한 글자 조사 제외)
    st.image(wc.to_array())
