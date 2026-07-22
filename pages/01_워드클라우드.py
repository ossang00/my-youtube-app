import os

import streamlit as st
import requests
from wordcloud import WordCloud

st.set_page_config(page_title="댓글 워드클라우드", page_icon="☁️")
st.title("☁️ 댓글 워드클라우드")

# 한글 폰트 준비 (없거나 깨져 있으면 다시 내려받기)
FONT_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Regular.ttf"
FONT_PATH = "NanumGothic.ttf"

# 이전 실행에서 다운로드가 중간에 실패해 깨진 파일이 남아있을 수 있어서
# "존재하는지"뿐 아니라 "제대로 된 크기인지"도 함께 확인해요.
font_ok = os.path.exists(FONT_PATH) and os.path.getsize(FONT_PATH) > 100_000

if not font_ok:
    try:
        res = requests.get(FONT_URL, timeout=10)
        if res.status_code == 200 and len(res.content) > 100_000:
            with open(FONT_PATH, "wb") as f:
                f.write(res.content)
            font_ok = True
        else:
            st.error(f"한글 폰트를 내려받지 못했어요 (상태코드: {res.status_code}). 잠시 후 새로고침해 주세요.")
    except Exception as e:
        st.error(f"한글 폰트를 내려받지 못했어요: {e}")

if not font_ok:
    st.stop()  # 폰트가 없으면 아래 워드클라우드 코드를 아예 실행하지 않음

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
