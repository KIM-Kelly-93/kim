import streamlit as st

def run(client):
    st.header("🌈 우주 알림장 댓글 생성기")

    teacher_note = st.text_area("👩‍🏫 선생님 알림장 글을 입력하세요")
    previous_reply = st.text_area("🧡 내가 이전에 쓴 댓글 예시 (선택)")

    if st.button("✏️ 우주엄마 댓글 생성하기"):
        if not teacher_note:
            st.warning("선생님 알림장 내용을 입력해주세요")
            return

        with st.spinner("우주엄마 댓글 생성 중..."):
            prompt = f"""
            선생님 알림장 글:
            {teacher_note}

            나의 댓글 예시:
            {previous_reply}

            위 알림장에 대한 우주엄마의 댓글을 생성해주세요. 형식은 다음과 같아야 합니다:
            - #용~ 과 #요!! 를 섞어서 쓰기
            - 우주를 주인공으로 표현
            - 선생님에게 감동과 응원을 줄 수 있는 말투
            - 5~7줄 내외로 짧게 쓰기
            - 밝고 사랑스럽게 마무리
            - 초등학생도 읽기 쉬운 문장으로 구성
            """

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "당신은 다정한 학부모입니다."},
                    {"role": "user", "content": prompt}
                ]
            )

            st.write(response.choices[0].message.content)