
import streamlit as st
from openai import OpenAI
import fitz  # PyMuPDF

st.set_page_config(page_title="KellyBot - 기업분석", layout="centered")
st.title("📊 KellyBot: 기업분석 AI")
st.write("PDF 업로드만 하면, GPT가 요약 리포트를 만들어드립니다.")

uploaded_file = st.file_uploader("분석할 IR 또는 기업소개서 PDF를 업로드하세요", type="pdf")
openai_api_key = st.text_input("🔑 OpenAI API 키 입력", type="password")

if uploaded_file and openai_api_key:
    st.info("파일 처리 중... 잠시만 기다려주세요!")
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    system_prompt = """
    너는 투자 전문가야. 사용자가 제공한 기업 IR 문서를 읽고 아래 기준으로 요약해줘:

    1. 기업 개요 요약 (무엇을 하는 회사인지)
    2. 핵심 사업모델 또는 제품/서비스
    3. 주요 재무 성과 또는 지표 요약
    4. 투자 매력 포인트 3가지
    5. 주요 리스크 요인 2가지
    6. 이 기업에 대한 GPT 한줄평

    결과는 깔끔하고 전문적으로 정리해서 출력해줘.
    """

    client = OpenAI(api_key=openai_api_key)

    with st.spinner("GPT가 분석 중입니다..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text[:6000]}
            ],
            temperature=0.7
        )
        summary = response.choices[0].message.content

    st.subheader("📄 GPT 기업분석 리포트")
    st.write(summary)
    st.download_button("⬇️ 결과 복사 or 다운로드", summary, file_name="kellybot_summary.txt")

else:
    st.warning("PDF와 API 키를 입력하면 분석을 시작할 수 있습니다.")
