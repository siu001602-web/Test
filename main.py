import base64
from datetime import datetime
import hashlib
json = __import__("json")
os = __import__("os")
random = __import__("random")
sqlite3 = __import__("sqlite3")
time = __import__("time")
colorsys = __import__("colorsys")
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="아우라 AI 배틀로얄 & 가챠", page_icon="✨", layout="wide"
)

# 등급 리스트 정의 (희귀도 높은 순)
items = [
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭", "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻", "사도:베일", "수확가", "악몽의 하늘", "𝓘𝓬𝓮𝓐𝓰𝓮", "𝓜𝓪𝓶𝓶𝓸𝓽𝓱",
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧", "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤", "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐", "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒", "감시자",
    "아쿠아리움", "선원", "샤킨", "포세이돈", "에바네샌트",
    "기원", "망령", "듀라한", "영혼 사냥꾼", "묘화", "밤나팔꽃", "바이탈", "룬(나이트)", "펌프",
    "블리자드", "이상", "크로마틱", "자장가",
    "그래피티", "헬리오스", "속력", "황혼",
    "아파타이트", "대마법사", "아케인", "워록",
    "테러", "바운디드", "재즈", "스펙터",
    "이색", "노틸러스", "아쿠아틱",
    "만년서리", "태양", "달", "와트",
    "힘", "카와이", "석영", "출혈",
    "시데리움", "콜라", "빙하", "재",
    "자력", "글록", "아쿠아마린", "사파이어", "잉크",
    "에메랄드", "루비", "분노", "토파즈",
    "결정화", "현기증", "원자", "수소", "레어", "자연",
    "굿", "희귀", "일반",
]

denominators = {
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": 7500000000, "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": 2222222222,
    "사도:베일": 800000000, "수확가": 666000000, "악몽의 하늘": 190000000,
    "𝓘𝓬𝓮𝓐𝓰𝓮": 1500000000, "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": 300000000,
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": 200000000, "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": 175000000, "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": 100000000,
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": 1730400000, "감시자": 45000000,
    "아쿠아리움": 80000000, "선원": 12000000, "샤킨": 10000000, "포세이돈": 4000000, "에바네샌트": 3360000,
    "기원": 6500000, "망령": 4100000,
    "듀라한": 72000000, "영혼 사냥꾼": 40000000, "묘화": 21000000, "밤나팔꽃": 10000000, "바이탈": 6000000, "룬(나이트)": 1000000, "펌프": 200000,
    "블리자드": 27315000, "이상": 24691356, "크로마틱": 20000000, "자장가": 17000000,
    "그래피티": 12000000, "헬리오스": 9000000, "속력": 7630000, "황혼": 6000000,
    "아파타이트": 3133133, "대마법사": 1766000, "아케인": 1000000, "워록": 660000,
    "테러": 400000, "바운디드": 200000, "재즈": 160000, "스펙터": 140000,
    "이색": 99999, "노틸러스": 70000, "아쿠아틱": 40000,
    "만년서리": 73500, "태양": 50000, "달": 50000, "와트": 32768,
    "힘": 16384, "카와이": 12300, "석영": 8192, "출혈": 4444,
    "시데리움": 4096, "콜라": 3999, "빙하": 2304, "재": 2300,
    "자력": 2048, "글록": 1700, "아쿠아마린": 900, "사파이어": 800, "잉크": 700,
    "에메랄드": 500, "루비": 350, "분노": 256, "토파즈": 150,
    "결정화": 128, "현기증": 123, "원자": 1180, "수소": 1111, "레어": 16, "자연": 8,
    "굿": 5, "희귀": 4, "일반": 2,
}

icons = {
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": "🖐️✨🌌👑", "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": "🕸️🌙✨🦋",
    "사도:베일": "🎃👁️", "수확가": "🎃🗡️", "악몽의 하늘": "🎃🌌",
    "𝓘𝓬𝓮𝓐𝓰𝓮": "❄️🧊👑", "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": "🦣❄️🧊",
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": "🌈💎✨", "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": "🎼🎻✨♠️", "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": "🌌💠💫",
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": "🌊🐉🌀", "감시자": "👁️‍🗨️⚡",
    "아쿠아리움": "🐠🌊🏛️", "선원": "⚓⛵🌊", "샤킨": "🦈🌊⚡", "포세이돈": "🔱🌊🌊", "에바네샌트": "🌀✨🌌",
    "기원": "🌌✨", "망령": "👻⚡",
    "듀라한": "🎃🗡️", "영혼 사냥꾼": "🎃👻", "묘화": "🎃🔥", "밤나팔꽃": "🎃🌸", "바이탈": "🎃💉", "룬(나이트)": "🎃🛡️", "펌프": "🎃✨",
    "블리자드": "❄️🌨️🌀", "이상": "🌀❓🌌", "크로마틱": "🌈💫", "자장가": "🌌🎵💤",
    "그래피티": "🎨✨", "헬리오스": "☀️🔥", "속력": "⚡💨", "황혼": "🌆✨💜",
    "아파타이트": "💠💎", "대마법사": "🧙‍♂️✨", "아케인": "🔮👑", "워록": "💀🔥",
    "테러": "💣💥", "바운디드": "🌌👑", "재즈": "🎶🎷", "ส펙터": "👻🔮",
    "이색": "🌈✨", "노틸러스": "🐚🌊", "아쿠아틱": "💧✨",
    "만년서리": "❄️💎", "태양": "☀️✨", "달": "🌙✨", "와트": "⚡👑⚡",
    "힘": "⚡🔥", "카와이": "🎀💖✨", "석영": "💎✨", "출혈": "🩸⚔️",
    "시데리움": "🌟🛡️", "콜라": "🥤🫧", "빙하": "🧊❄️", "재": "🌫️🔥",
    "자력": "🧲💫", "글록": "🔫💥", "아쿠아마린": "🌊💎", "사파이어": "💙💎", "잉크": "🖋️🖤",
    "에메랄드": "💚💎", "루비": "❤️💎", "분노": "😡💢", "토파즈": "💛💎",
    "결정화": "🔮✨", "현기증": "😵‍💫🌀", "원자": "⚛️✨", "수소": "🧪✨", "레어": "💙📦", "자연": "🌿🍃",
    "굿": "👍✨", "희귀": "💧📘", "일반": "⚪📦",
}

AI_NAMES = [
    "김철수", "이영희", "박민수", "정지은", "최동현", "강서윤", "조민재", "윤서연", "장도현", "한소율",
    "오지호", "서아린", "신예준", "권나은", "황지후", "안채원", "백도현", "송하은", "문준서", "배서현",
    "유도윤", "홍채은", "류지호", "전서우", "손민준", "허유진", "고시우", "남지안", "심재원", "엄하윤",
    "변도윤", "여서윤", "석민준", "표채은", "국준서", "구서현", "나도윤", "라채은", "마지호", "방서우",
    "사민준", "아유진", "차시우", "카지안", "타재원", "파하윤", "하도윤", "거서윤", "너민준", "더채은",
    "러준서", "머서현", "버도윤", "서채은", "어지호", "저서우", "처민준", "커유진", "터시우", "퍼지안",
    "호재원", "고하윤", "노도윤", "도서윤", "모민준", "보채은", "소준서", "아서현", "자도윤", "차채은",
    "카지호", "타서우", "파민준", "하유진", "거시우", "너지안", "더재원", "러하윤", "머도윤", "버서윤",
    "서민준", "어채은", "저준서", "처서현", "커도윤", "터채은", "퍼지호", "호서우", "김민준", "이유진",
    "박시우", "정지안", "최재원", "강하윤", "조도윤", "윤서윤", "장민준", "한채은"
]

if "battle_initialized" not in st.session_state:
  st.session_state.battle_initialized = True
  st.session_state.my_name = "나 (플레이어)"
  st.session_state.my_aura = "일반"
  st.session_state.my_score = 0
  st.session_state.my_alive = True
  
  st.session_state.ai_players = []
  for name in AI_NAMES:
    st.session_state.ai_players.append({
        "name": name,
        "aura": "일반",
        "score": 0,
        "alive": True
    })
  st.session_state.battle_log = ["게임이 시작되었습니다! 버튼을 눌러 AI들과 아우라 배틀을 시작하세요."]

st.title("✨ 아우라 AI 배틀로얄 & 가챠 (관전 모드 지원)")
st.write("버튼을 누르면 나와 100명의 AI들이 **100만배 행운**으로 아우라를 뽑습니다! 나는 죽어도 관전 모드로 게임에 남습니다.")

c_info1, c_info2, c_info3 = st.columns(3)
with c_info1:
  alive_ai_count = sum(1 for ai in st.session_state.ai_players if ai["alive"])
  st.metric(label="👥 생존 AI 수", value=f"{alive_ai_count} / 100명")
with c_info2:
  st.metric(label="🙋 내 상태", value="🛡️ 생존 중" if st.session_state.my_alive else "👻 탈락 (관전 중)")
with c_info3:
  st.metric(label="🏆 내 최고 아우라", value=st.session_state.my_aura)

st.divider()

# 배틀 진행 버튼
if st.button("🚀 전체 100만배 행운 가챠 돌리기 (배틀 1회 진행)", type="primary", use_container_width=True):
  # 내 뽑기 (100만배 행운 적용: 상위권 아우라 중 랜덤)
  top_items = items[:40] # 상위 등급 풀
  my_roll = random.choice(top_items)
  st.session_state.my_aura = my_roll
  st.session_state.my_score += denominators.get(my_roll, 1)

  # AI들 뽑기
  round_log = f"[{datetime.now().strftime('%H:%M:%S')}] 이번 턴 가챠 결과:"
  for ai in st.session_state.ai_players:
    if ai["alive"]:
      roll = random.choice(top_items)
      ai["aura"] = roll
      ai["score"] += denominators.get(roll, 1)

  st.session_state.battle_log.insert(0, f"✨ 모든 참가자가 100만배 행운으로 아우라를 소환했습니다!")
  st.rerun()

st.subheader("⚔️ 생존자 관리 및 탈락자 지정 (관리자 패널)")
st.write("원하는 AI를 직접 탈락시키거나 부활시킬 수 있습니다. (나는 죽어도 관전 모드로 계속 남습니다!)")

col_me, col_ai_mgmt = st.columns([1, 2])

with col_me:
  with st.container(border=True):
    st.markdown(f"### 내 정보: {st.session_state.my_name}")
    st.write(f"현재 아우라: **{icons.get(st.session_state.my_aura, '✨')} {st.session_state.my_aura}**")
    st.write(f"상태: {'🟢 생존' if st.session_state.my_alive else '👻 탈락 (관전 모드)'}")
    if st.session_state.my_alive:
      if st.button("💀 자진 탈락하기 (관전하기)", use_container_width=True):
        st.session_state.my_alive = False
        st.success("탈락하였습니다. 이제 관전 모드로 게임을 계속 지켜봅니다!")
        st.rerun()
    else:
      if st.button("🔄 부활하기", use_container_width=True):
        st.session_state.my_alive = True
        st.rerun()

with col_ai_mgmt:
  with st.container(border=True):
    st.markdown("### 🤖 AI 생존/탈락 관리")
    alive_list = [ai["name"] for ai in st.session_state.ai_players if ai["alive"]]
    dead_list = [ai["name"] for ai in st.session_state.ai_players if not ai["alive"]]

    selected_to_kill = st.selectbox("탈락시킬 AI 선택", ["선택하세요"] + alive_list)
    if selected_to_kill != "선택하세요":
      if st.button(f"'{selected_to_kill}' 탈락시키기", type="secondary"):
        for ai in st.session_state.ai_players:
          if ai["name"] == selected_to_kill:
            ai["alive"] = False
        st.rerun()

    if dead_list:
      selected_to_revive = st.selectbox("부활시킬 AI 선택", ["선택하세요"] + dead_list)
      if selected_to_revive != "선택하세요":
        if st.button(f"'{selected_to_revive}' 부활시키기"):
          for ai in st.session_state.ai_players:
            if ai["name"] == selected_to_revive:
              ai["alive"] = True
          st.rerun()

st.divider()

st.subheader("📜 실시간 배틀 로그")
for log in st.session_state.battle_log[:10]:
  st.text(log)

st.subheader("📋 전체 참가자 현황 (생존 및 아우라)")
tab_alive_list, tab_dead_list = st.tabs(["🟢 생존자 목록", "👻 탈락자 (관전) 목록"])

with tab_alive_list:
  alive_players_data = [ai for ai in st.session_state.ai_players if ai["alive"]]
  if st.session_state.my_alive:
    st.markdown(f"- 🟢 **{st.session_state.my_name} (나)** — {icons.get(st.session_state.my_aura, '✨')} `{st.session_state.my_aura}`")
  for ai in alive_players_data:
    st.markdown(f"- 🟢 **{ai['name']}** — {icons.get(ai['aura'], '✨')} `{ai['aura']}`")

with tab_dead_list:
  dead_players_data = [ai for ai in st.session_state.ai_players if not ai["alive"]]
  if not st.session_state.my_alive:
    st.markdown(f"- 👻 **{st.session_state.my_name} (나)** — (관전 중)")
  for ai in dead_players_data:
    st.markdown(f"- 👻 **{ai['name']}**")
