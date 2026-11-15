from datetime import datetime
import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="아우라 AI 배틀로얄 (1만 명 대규모)", page_icon="✨", layout="wide"
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
    "테러": "💣💥", "바운디드": "🌌👑", "재즈": "🎶🎷", "스펙터": "👻🔮",
    "이색": "🌈✨", "노틸러스": "🐚🌊", "아쿠아틱": "💧✨",
    "만년서리": "❄️💎", "태양": "☀️✨", "달": "🌙✨", "와트": "⚡👑⚡",
    "힘": "⚡🔥", "카와이": "🎀💖✨", "석영": "💎✨", "출혈": "🩸⚔️",
    "시데리움": "🌟🛡️", "콜라": "🥤🫧", "빙하": "🧊❄️", "재": "🌫️🔥",
    "자력": "🧲💫", "글록": "🔫💥", "아쿠아마린": "🌊💎", "사파이어": "💙💎", "잉크": "🖋️🖤",
    "에메랄드": "💚💎", "루비": "❤️💎", "분노": "😡💢", "토파즈": "💛💎",
    "결정화": "🔮✨", "현기증": "😵‍💫🌀", "원자": "⚛️✨", "수소": "🧪✨", "레어": "💙📦", "자연": "🌿🍃",
    "굿": "👍✨", "희귀": "💧📘", "일반": "⚪📦",
}

# 1만 명(AI 9,999명 + 나) 자동 생성
TOTAL_PLAYERS = 10000
AI_COUNT = TOTAL_PLAYERS - 1

last_names = ["김", "이", "박", "정", "최", "강", "조", "윤", "장", "한", "오", "서", "신", "권", "황", "안", "송", "전", "홍", "유"]
first_names = ["민준", "서윤", "도윤", "서연", "예준", "지우", "도현", "서현", "주원", "하은", "지호", "지유", "준우", "채원", "현우", "지민", "은우", "민서", "시우", "하윤"]

def generate_ai_names(count):
  names = set()
  while len(names) < count:
    family = random.choice(last_names)
    given = random.choice(first_names) + random.choice(first_names)
    names.add(family + given)
  return list(names)

MILLION_ELIGIBLE_ITEMS = [it for it in items if denominators[it] >= 1000000]
MILLION_ELIGIBLE_WEIGHTS = [max(1, int(7500000000000 / denominators[it])) for it in MILLION_ELIGIBLE_ITEMS]

def roll_million_luck():
  return random.choices(MILLION_ELIGIBLE_ITEMS, weights=MILLION_ELIGIBLE_WEIGHTS, k=1)[0]

def init_game():
  st.session_state.round_num = 0
  st.session_state.my_name = "나 (플레이어)"
  st.session_state.my_aura = "일반"
  st.session_state.my_alive = True

  generated_names = generate_ai_names(AI_COUNT)
  st.session_state.ai_players = [
      {"name": name, "aura": "일반", "alive": True}
      for name in generated_names
  ]
  st.session_state.battle_log = ["게임이 시작되었습니다! 나와 9,999명의 AI가 1만 명 대규모 100만배 행운 배틀을 시작합니다."]

if "round_num" not in st.session_state:
  init_game()

st.title("✨ 아우라 AI 배틀로얄 (1만 명 대규모 서바이벌)")
st.write("버튼을 누르면 생존자 전원이 **100만배 행운**으로 아우라를 뽑고, **가장 낮은 등급을 뽑은 인원들이 자동으로 동시 탈락**합니다!")

alive_ai_count = sum(1 for ai in st.session_state.ai_players if ai["alive"])
total_alive = alive_ai_count + (1 if st.session_state.my_alive else 0)

c_info1, c_info2, c_info3, c_info4 = st.columns(4)
with c_info1:
  st.metric(label="🔄 진행 라운드", value=f"{st.session_state.round_num} 라운드")
with c_info2:
  st.metric(label="👥 총 생존자 수", value=f"{total_alive:,} / {TOTAL_PLAYERS:,}명")
with c_info3:
  st.metric(label="🙋 내 상태", value="🟢 생존 중" if st.session_state.my_alive else "👻 탈락 (관전 중)")
with c_info4:
  st.metric(label="✨ 내 마지막 아우라", value=st.session_state.my_aura)

st.divider()

if total_alive <= 1:
  winner_name = "없음 (전원 동시 탈락)"
  if st.session_state.my_alive:
    winner_name = f"👑 {st.session_state.my_name} ({st.session_state.my_aura})"
  elif alive_ai_count == 1:
    last_ai = [ai for ai in st.session_state.ai_players if ai["alive"]][0]
    winner_name = f"👑 {last_ai['name']} ({last_ai['aura']})"

  st.success(f"🎉 **배틀 종료! 최종 우승자: {winner_name}**")
  if st.button("🔄 새 게임 시작하기", type="primary", use_container_width=True):
    init_game()
    st.rerun()
else:
  btn_label = (
      "🚀 1만 명 전원 100만배 행운 가챠 & 최하위 자동 탈락 진행"
      if st.session_state.my_alive
      else "👁️ [관전 모드] 남은 인원 1만 명 가챠 & 최하위 자동 탈락 진행"
  )
  if st.button(btn_label, type="primary", use_container_width=True):
    st.session_state.round_num += 1
    round_rolls = []

    if st.session_state.my_alive:
      my_roll = roll_million_luck()
      st.session_state.my_aura = my_roll
      round_rolls.append(("me", st.session_state.my_name, my_roll, denominators[my_roll]))

    for ai in st.session_state.ai_players:
      if ai["alive"]:
        ai_roll = roll_million_luck()
        ai["aura"] = ai_roll
        round_rolls.append((ai, ai["name"], ai_roll, denominators[ai_roll]))

    if round_rolls:
      min_denom = min(r[3] for r in round_rolls)
      eliminated_names = []
      elim_count = 0

      for target, name, aura_name, denom in round_rolls:
        if denom == min_denom:
          elim_count += 1
          if target == "me":
            st.session_state.my_alive = False
            eliminated_names.append(f"🙋 {name} [{aura_name}]")
          else:
            target["alive"] = False
            # 지면 로그가 너무 길어지지 않게 최대 5명만 이름 표기
            if len(eliminated_names) < 5:
              eliminated_names.append(f"{name} [{aura_name}]")

      summary_str = ", ".join(eliminated_names)
      if elim_count > 5:
        summary_str += f" 외 {elim_count - 5}명"

      log_msg = f"[Round {st.session_state.round_num}] 최하위 등급 (1 in {min_denom:,}) 탈락 ({elim_count}명): {summary_str}"
      st.session_state.battle_log.insert(0, log_msg)

    st.rerun()

st.subheader("📜 실시간 탈락 및 배틀 로그")
with st.container(border=True):
  for log in st.session_state.battle_log[:8]:
    st.write(log)

st.divider()

st.subheader("🏆 전체 참가자 현황 (상위 순위)")
tab_alive_list, tab_dead_list = st.tabs([f"🟢 생존자 순위 (상위 표시)", f"👻 최근 탈락자 및 관전"])

with tab_alive_list:
  alive_entries = []
  if st.session_state.my_alive:
    alive_entries.append({
        "name": f"🙋 {st.session_state.my_name}",
        "aura": st.session_state.my_aura,
        "denom": denominators.get(st.session_state.my_aura, 1),
        "is_me": True
    })
  for ai in st.session_state.ai_players:
    if ai["alive"]:
      alive_entries.append({
          "name": ai["name"],
          "aura": ai["aura"],
          "denom": denominators.get(ai["aura"], 1),
          "is_me": False
      })

  alive_entries.sort(key=lambda x: x["denom"], reverse=True)

  if alive_entries:
    st.caption(f"총 생존자 {len(alive_entries):,}명 중 가장 잘 뜬 상위 50명만 표시됩니다.")
    for rank, entry in enumerate(alive_entries[:50], start=1):
      icon = icons.get(entry["aura"], "✨")
      denom_str = f"1 in {entry['denom']:,}"
      if entry["is_me"]:
        st.markdown(f"**{rank}위. {entry['name']}** — {icon} **`{entry['aura']}`** (`{denom_str}`)")
      else:
        st.markdown(f"{rank}위. **{entry['name']}** — {icon} `{entry['aura']}` (`{denom_str}`)")
  else:
    st.info("생존자가 없습니다.")

with tab_dead_list:
  dead_entries = []
  if not st.session_state.my_alive:
    dead_entries.append({
        "name": f"🙋 {st.session_state.my_name} (관전 중)",
        "aura": st.session_state.my_aura,
        "denom": denominators.get(st.session_state.my_aura, 1),
        "is_me": True
    })
  for ai in st.session_state.ai_players:
    if not ai["alive"]:
      dead_entries.append({
          "name": ai["name"],
          "aura": ai["aura"],
          "denom": denominators.get(ai["aura"], 1),
          "is_me": False
      })

  dead_entries.sort(key=lambda x: x["denom"], reverse=True)

  if dead_entries:
    st.caption(f"총 탈락자 {len(dead_entries):,}명 중 최근 상위 50명만 표시됩니다.")
    for entry in dead_entries[:50]:
      icon = icons.get(entry["aura"], "✨")
      denom_str = f"1 in {entry['denom']:,}"
      if entry["is_me"]:
        st.markdown(f"- 👻 **{entry['name']}** — 마지막 아우라: {icon} **`{entry['aura']}`** (`{denom_str}`)")
      else:
        st.markdown(f"- 👻 **{entry['name']}** — 마지막 아우라: {icon} `{entry['aura']}` (`{denom_str}`)")
  else:
    st.caption("아직 탈락자가 없습니다.")
