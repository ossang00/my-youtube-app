from collections import Counter
import plotly.express as px

# ...1단계 코드는 그대로, 댓글 표시 아래에 추가...

    # ── 2단계: 단어 빈도 분석 ──────────────────
    words = " ".join(comments).split()          # 댓글 전체를 단어로 나누기
    words = [w for w in words if len(w) > 1]    # 한 글자 단어 제외
    top20 = Counter(words).most_common(20)      # 많이 나온 순서로 20개

    st.subheader("📊 자주 나온 단어 TOP 20")
    freq = {"단어": [w for w, _ in top20], "횟수": [n for _, n in top20]}
    fig = px.bar(freq, x="횟수", y="단어", orientation="h")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)
