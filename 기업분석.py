import streamlit as st

def run(client):
    st.header("📊 기업 분석")
    uploaded_file = st.file_uploader("IR 또는 기업소개서 PDF 업로드", type=["pdf"])

    if uploaded_file:
        st.success(f"{uploaded_file.name} 업로드 완료 (분석 준비 중...)")

        # 예시 프롬프트
        prompt = f"""
        쿠키딜의 클라이언트 중 매도 매물에 대한 소개자료를 작성하려고 합니다. 아래 형식에 맞춰 투자 포인트(장문 형식), 회사 소개, 매도가치 선정 사유까지 작성해주세요.
        PDF 이름: {uploaded_file.name}
        """

        with st.spinner("분석 중입니다..."):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "당신은 투자은행 딜소싱 전문가입니다."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.write(response.choices[0].message.content)