import streamlit as st
from openai import OpenAI

# 🧠 각 기능 파일 불러오기
import 기업분석
import 미팅태핑
import 우주알림장

# 페이지 설정
st.set_page_config(page_title="KellyBot", layout="centered")
st.title("📊 KellyBot")

# API 키 입력
api_key = st.text_input("🔑 OpenAI API 키 입력", type="password")
if not api_key:
    st.warning("API 키를 입력해야 방송을 시작할 수 있습니다.")
    st.stop()

# OpenAI client 설정
client = OpenAI(api_key=api_key)

# 사이드바 메뉴
st.sidebar.title("📁 프로젝트 선택")
tab = st.sidebar.radio("원하는 기능을 선택하세요:", [
    "기업 분석",
    "우주 알림장",
    "업무 미팅 요약"
])

# 각 탭에 따라 다른 화면 실행
if tab == "기업 분석":
    기업분석.run(client)

elif tab == "우주 알림장":
    우주알림장.run(client)

elif tab == "업무 미팅 요약":
    미팅태핑.run(client)
