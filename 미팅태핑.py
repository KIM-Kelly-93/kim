import streamlit as st

def run(client):
    st.header("📝 미팅 태핑")
    st.write("여기에 미팅 기록/요약 기능이 들어갑니다.")

    transcript = st.text_area("💬 미팅 원문 입력")

    if st.button("요약 생성"):
        if not transcript:
            st.warning("미팅 내용을 입력해주세요")
            return

        prompt = f"""
        아래의 회의 대화를 읽고 다음 항목에 맞게 분석 요약해줘:
        - 핵심결론 (객관적 사실 위주)
        - 상대방의 질문 요약 (구체적 질문과 맥락)
        - 나를 위한 핵심요약 (초등학생도 이해할 수 있게 짧고 쉽게)

        회의 내용:
        {transcript}
        """

        with st.spinner("요약 중입니다..."):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "당신은 회의 내용을 정리하는 요약 비서입니다."},
                    {"role": "user", "content": prompt}
                ]
            )

            st.write(response.choices[0].message.content)
