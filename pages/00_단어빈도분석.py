from collections import Counter

import streamlit as st
import plotly.express as px

st.set_page_config(page_title="자주 나온 단어", page_icon="📊")
st.title("📊 자주 나온 단어 TOP 20")

if "comments" not in st.session_state:
    st.warning("먼저 메인 페이지에서 댓글을 가져와 주세요! 👈 왼쪽 메뉴에서 이동할 수 있어요.")
else:
    comments = st.session_state.comments

    # ── 2단계: 단어 빈도 분석 ──────────────────
    words = " ".join(comments).split()          # 댓글 전체를 단어로 나누기
    words = [w for w in words if len(w) > 1]    # 한 글자 단어 제외
    top20 = Counter(words).most_common(20)      # 많이 나온 순서로 20개

    freq = {"단어": [w for w, _ in top20], "횟수": [n for _, n in top20]}
    fig = px.bar(freq, x="횟수", y="단어", orientation="h")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)
