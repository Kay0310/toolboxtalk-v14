import streamlit as st
import datetime
import pytz

# 한국 시간 기준
kst = pytz.timezone("Asia/Seoul")
now_kst = datetime.datetime.now(kst)
today_kst = now_kst.date()
time_kst = now_kst.strftime("%H:%M")

# 회의록 예시 데이터 (session_state로 연결 필요)
example_data = {
    "company": "HealSE Construction Co., Ltd.",
    "team": "건설팀",
    "leader": "김강윤",
    "date": str(today_kst),
    "time": time_kst,
    "place": "건설현장 16층",
    "task": "고소작업",
    "attendees": ["김강윤", "이민우", "박지현"],
    "discussion": [
        ("안전난간 없음", "발끝막이 설치"),
        ("사다리 미고정", "작업 전 고정 확인")
    ],
    "additional": "작업 시 기상변화 주의 필요",
    "tasks": [
        ("김강윤", "사다리 고정점 점검", "2025-05-12"),
        ("이민우", "안전벨트 지급 확인", "2025-05-13")
    ],
    "confirmations": ["김강윤", "이민우"]
}

# HTML 템플릿 출력
st.title("📋 인쇄용 회의록 미리보기")

with st.expander("▶ 미리보기 열기 (인쇄 시 Ctrl+P)", expanded=True):
    html = f'''
    <div style="font-family: sans-serif; padding: 30px; line-height: 1.6; font-size: 16px;">
        <h2 style="text-align: center; font-size: 24px;">📋 Toolbox Talk 회의록 - [{example_data["team"]}]</h2>
        <p style="text-align: center; font-size: 14px;">회사명: {example_data["company"]}</p>
        <p><b>날짜:</b> {example_data["date"]} &nbsp;&nbsp;&nbsp; <b>시간:</b> {example_data["time"]}</p>
        <p><b>장소:</b> {example_data["place"]} &nbsp;&nbsp;&nbsp; <b>작업내용:</b> {example_data["task"]}</p>
        <p><b>리더:</b> {example_data["leader"]}</p>
        
        <h4 style="margin-top: 30px;">👥 참석자</h4>
        <ul>
            {''.join([f'<li>{name}</li>' for name in example_data["attendees"]])}
        </ul>
        
        <h4 style="margin-top: 30px;">🧠 논의 내용</h4>
        <ol>
            {''.join([f"<li><b>위험요소:</b> {r} <br> <b>안전대책:</b> {m}</li>" for r, m in example_data["discussion"]])}
        </ol>
        
        <h4 style="margin-top: 30px;">📌 추가 논의 사항</h4>
        <p>{example_data["additional"]}</p>

        <h4 style="margin-top: 30px;">✅ 결정사항 및 조치</h4>
        <ul>
            {''.join([f"<li>{p}: {r} (완료예정일: {d})</li>" for p, r, d in example_data["tasks"]])}
        </ul>

        <h4 style="margin-top: 30px;">✍ 회의록 확인자</h4>
        <ul>
            {''.join([f"<li>{n} (확인 완료)</li>" for n in example_data["confirmations"]])}
        </ul>

        <hr>
        <p style="text-align: right; font-size: 10px; color: gray;">
            App. support by HealSE Co., Ltd.
        </p>
    </div>
    '''
    st.components.v1.html(html, height=1000, scrolling=True)