

# 댓글이 준비되면 요약 버튼과 목록 표시
if "comments" in st.session_state:
    comments = st.session_state.comments
    st.metric("가져온 댓글 수", f"{len(comments)}개")

    # ── AI 세 줄 요약 + 긍·부정 비율 ──────────────────
    if st.button("🤖 AI 세 줄 요약"):
        joined = "\n".join(comments)
        with st.spinner("AI가 댓글을 읽고 있어요..."):
            try:
                resp = client.chat.completions.create(
                    model="solar-open2",     # 모델 이름은 그대로 유지
                    messages=[
                        {"role": "system", "content": "너는 댓글 분석가야. 받은 댓글 전체의 전반적인 반응을 한국어 세 줄로 요약하고, 마지막 줄에 긍정과 부정의 대략적인 비율(백분율)을 덧붙여. 반드시 순수 한국어로만 답해."},
                        {"role": "user", "content": joined},
                    ],
                    reasoning_effort="none",  # 추론 끄기 -> 즉시 답변
                )
                st.info(resp.choices[0].message.content)
            except Exception:
                st.error("요약을 받지 못했어요 😢 잠시 후 다시 시도해 주세요.")

    st.dataframe({"좋아요": st.session_state.likes, "댓글": comments}, use_container_width=True)
