import random
import streamlit as st

st.set_page_config(
    page_title="아우라 AI 스테이지 배틀로얄", page_icon="✨", layout="centered"
)

denominators = {
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": 7500000000,
    "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": 2222222222,
    "사도:베일": 800000000,
    "수확가": 666000000,
    "악몽의 하늘": 190000000,
    "𝓘𝓬𝓮𝓐𝓰𝓮": 1500000000,
    "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": 300000000,
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": 200000000,
    "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": 175000000,
    "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": 100000000,
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": 1730400000,
    "감시자": 45000000,
    "아쿠아리움": 80000000,
    "선원": 12000000,
    "샤킨": 10000000,
    "포세이돈": 4000000,
    "에바네샌트": 3360000,
    "기원": 6500000,
    "망령": 4100000,
    "듀라한": 72000000,
    "영혼 사냥꾼": 40000000,
    "묘화": 21000000,
    "밤나팔꽃": 10000000,
    "바이탈": 6000000,
    "룬(나이트)": 1000000,
    "펌프": 200000,
    "블리자드": 27315000,
    "이상": 24691356,
    "크로마틱": 20000000,
    "자장가": 17000000,
    "그래피티": 12000000,
    "헬리오스": 9000000,
    "속력": 7630000,
    "황혼": 6000000,
    "아파타이트": 3133133,
    "대마법사": 1766000,
    "아케인": 1000000,
    "워록": 660000,
    "테러": 400000,
    "바운디드": 200000,
    "재즈": 160000,
    "스펙터": 140000,
    "이색": 99999,
    "노틸러스": 70000,
    "아쿠아틱": 40000,
    "만년서리": 73500,
    "태양": 50000,
    "달": 50000,
    "와트": 32768,
    "힘": 16384,
    "카와이": 12300,
    "석영": 8192,
    "출혈": 4444,
    "시데리움": 4096,
    "콜라": 3999,
    "빙하": 2304,
    "재": 2300,
    "자력": 2048,
    "글록": 1700,
    "아쿠아마린": 900,
    "사파이어": 800,
    "잉크": 700,
    "에메랄드": 500,
    "루비": 350,
    "분노": 256,
    "토파즈": 150,
    "결정화": 128,
    "현기증": 123,
    "원자": 1180,
    "수소": 1111,
    "레어": 16,
    "자연": 8,
    "굿": 5,
    "희귀": 4,
    "일반": 2,
}

items = list(denominators.keys())

icons = {
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": "🖐️✨🌌👑",
    "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": "🕸️🌙✨🦋",
    "사도:베일": "🎃👁️",
    "수확가": "🎃🗡️",
    "악몽의 하늘": "🎃🌌",
    "𝓘𝓬𝓮𝓐𝓰𝓮": "❄️🧊👑",
    "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": "🦣❄️🧊",
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": "🌈💎✨",
    "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": "🎼🎻✨♠️",
    "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": "🌌💠💫",
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": "🌊🐉🌀",
    "감시자": "👁️‍🗨️⚡",
    "아쿠아리움": "🐠🌊🏛️",
    "선원": "⚓⛵🌊",
    "샤킨": "🦈🌊⚡",
    "포세이돈": "🔱🌊🌊",
    "에바네샌트": "🌀✨🌌",
    "기원": "🌌✨",
    "망령": "👻⚡",
    "듀라한": "🎃🗡️",
    "영혼 사냥꾼": "🎃👻",
    "묘화": "🎃🔥",
    "밤나팔꽃": "🎃🌸",
    "바이탈": "🎃💉",
    "룬(나이트)": "🎃🛡️",
    "펌프": "🎃✨",
    "블리자드": "❄️🌨️🌀",
    "이상": "🌀❓🌌",
    "크로마틱": "🌈💫",
    "자장가": "🌌🎵💤",
    "그래피티": "🎨✨",
    "헬리오스": "☀️🔥",
    "속력": "⚡💨",
    "황혼": "🌆✨💜",
    "아파타이트": "💠💎",
    "대마법사": "🧙‍♂️✨",
    "아케인": "🔮👑",
    "워록": "💀🔥",
    "테러": "💣💥",
    "바운디드": "🌌👑",
    "재즈": "🎶🎷",
    "스펙터": "👻🔮",
    "이색": "🌈✨",
    "노틸러스": "🐚🌊",
    "아쿠아틱": "💧✨",
    "만년서리": "❄️💎",
    "태양": "☀️✨",
    "달": "🌙✨",
    "와트": "⚡👑⚡",
    "힘": "⚡🔥",
    "카와이": "🎀💖✨",
    "석영": "💎✨",
    "출혈": "🩸⚔️",
    "시데리움": "🌟🛡️",
    "콜라": "🥤🫧",
    "빙하": "🧊❄️",
    "재": "🌫️🔥",
    "자력": "🧲💫",
    "글록": "🔫💥",
    "아쿠아마린": "🌊💎",
    "사파이어": "💙💎",
    "잉크": "🖋️🖤",
    "에메랄드": "💚💎",
    "루비": "❤️💎",
    "분노": "😡💢",
    "토파즈": "💛💎",
    "결정화": "🔮✨",
    "현기증": "😵‍💫🌀",
    "원자": "⚛️✨",
    "수소": "🧪✨",
    "레어": "💙📦",
    "자연": "🌿🍃",
    "굿": "👍✨",
    "희귀": "💧📘",
    "일반": "⚪📦",
}

AI_NAMES = [
    "김철수",
    "이영희",
    "박민수",
    "정지은",
    "최동현",
    "강서윤",
    "조민재",
    "윤서연",
    "장도현",
    "한소율",
    "오지호",
    "서아린",
    "신예준",
    "권나은",
    "황지후",
    "안채원",
    "백도현",
    "송하은",
    "문준서",
    "배서현",
    "유도윤",
    "홍채은",
    "류지호",
    "전서우",
    "손민준",
    "허유진",
    "고시우",
    "남지안",
    "심재원",
    "엄하윤",
    "변도윤",
    "여서윤",
    "석민준",
    "표채은",
    "국준서",
    "구서현",
    "나도윤",
    "라채은",
    "마지호",
    "방서우",
    "사민준",
    "아유진",
    "차시우",
    "카지안",
    "타재원",
    "파하윤",
    "하도윤",
    "거서윤",
    "너민준",
    "더채은",
    "러준서",
    "머서현",
    "버도윤",
    "서채은",
    "어지호",
    "저서우",
    "처민준",
    "커유진",
    "터시우",
    "퍼지안",
    "호재원",
    "고하윤",
    "노도윤",
    "도서윤",
    "모민준",
    "보채은",
    "소준서",
    "아서현",
    "자도윤",
    "차채은",
    "카지호",
    "타서우",
    "파민준",
    "하유진",
    "거시우",
    "너지안",
    "더재원",
    "러하윤",
    "머도윤",
    "버서윤",
    "서민준",
    "어채은",
    "저준서",
    "처서현",
    "커도윤",
    "터채은",
    "퍼지호",
    "호서우",
    "김민준",
    "이유진",
    "박시우",
    "정지안",
    "최재원",
    "강하윤",
    "조도윤",
    "윤서윤",
    "장민준",
    "한채은",
    "오민서",
    "서지훈",
]

MILLION_ELIGIBLE_ITEMS = [
    it for it in items if denominators[it] >= 1000000
]
MILLION_ELIGIBLE_WEIGHTS = [
    max(1, int(7500000000000 / denominators[it]))
    for it in MILLION_ELIGIBLE_ITEMS
]


def roll_million_luck():
  return random.choices(
      MILLION_ELIGIBLE_ITEMS, weights=MILLION_ELIGIBLE_WEIGHTS, k=1
  )[0]


def init_game():
  st.session_state.stage = 1
  st.session_state.round_num = 1
  st.session_state.my_name = "나 (플레이어)"
  st.session_state.my_aura = "일반"
  st.session_state.my_alive = True
  st.session_state.ai_players = [
      {"name": name, "aura": "일반", "alive": True} for name in AI_NAMES
  ]
  st.session_state.battle_log = [
      "게임 시작! 100명이 1라운드(5천만 확률 컷)를 시작합니다."
  ]


if "stage" not in st.session_state or "ai_players" not in st.session_state:
  init_game()

st.title("✨ 아우라 AI 스테이지 배틀로얄")

alive_ai_count = sum(1 for ai in st.session_state.ai_players if ai["alive"])
total_alive = alive_ai_count + (1 if st.session_state.my_alive else 0)
stage = st.session_state.stage

stage_names = {
    1: "1라운드 (5천만 컷)",
    2: "2라운드 (7천만 컷)",
    3: "3라운드 (1억 컷)",
    4: "최종 라운드 (서바이벌)",
}

st.info(
    f"🏆 **현재 단계**: {stage_names.get(stage, '')} | 👥 **생존자**:"
    f" {total_alive}명"
)
st.write(
    f"🙋 **내 상태**: {'🟢 생존 중' if st.session_state.my_alive else '👻 탈락'}"
    f" (마지막 아우라: {st.session_state.my_aura})"
)

st.divider()

if total_alive <= 1 or (stage == 4 and total_alive <= 1):
  winner = "없음"
  if st.session_state.my_alive:
    winner = f"나 ({st.session_state.my_aura})"
  else:
    alive_list = [ai for ai in st.session_state.ai_players if ai["alive"]]
    if alive_list:
      winner = f"{alive_list[0]['name']} ({alive_list[0]['aura']})"

  st.success(f"🎉 **게임 종료! 우승자: {winner}**")
  if st.button("🔄 다시 시작하기", type="primary", use_container_width=True):
    init_game()
    st.rerun()
else:
  btn_labels = {
      1: "🎯 1라운드 진행 (5천만 이상 컷 통과)",
      2: "🎯 2라운드 진행 (7천만 이상 컷 통과)",
      3: "🎯 3라운드 진행 (1억 이상 컷 통과)",
      4: "🚀 최종 라운드 진행 (매턴 최하위 동시 탈락)",
  }

  if st.button(
      btn_labels.get(stage, "다음 진행"), type="primary", use_container_width=True
  ):
    st.session_state.round_num += 1
    rolls = []

    if st.session_state.my_alive:
      my_roll = roll_million_luck()
      st.session_state.my_aura = my_roll
      rolls.append(
          ("me", st.session_state.my_name, my_roll, denominators[my_roll])
      )

    for ai in st.session_state.ai_players:
      if ai["alive"]:
        ai_roll = roll_million_luck()
        ai["aura"] = ai_roll
        rolls.append((ai, ai["name"], ai_roll, denominators[ai_roll]))

    if stage in [1, 2, 3]:
      cutoffs = {1: 50000000, 2: 70000000, 3: 100000000}
      target_val = cutoffs[stage]

      for target, name, aura, denom in rolls:
        if denom < target_val:
          if target == "me":
            st.session_state.my_alive = False
          else:
            target["alive"] = False

      new_alive = (1 if st.session_state.my_alive else 0) + sum(
          1 for ai in st.session_state.ai_players if ai["alive"]
      )
      st.session_state.battle_log.insert(
          0,
          f"[라운드 {st.session_state.round_num}] 컷진행 완료. 남은 생존자:"
          f" {new_alive}명",
      )

      if stage == 1 and new_alive <= 50:
        st.session_state.stage = 2
        st.session_state.battle_log.insert(
            0, "🔥 2라운드(7천만 컷)로 진입합니다!"
        )
      elif stage == 2 and new_alive <= 25:
        st.session_state.stage = 3
        st.session_state.battle_log.insert(
            0, "🔥 3라운드(1억 컷)로 진입합니다!"
        )
      elif stage == 3 and new_alive <= 10:
        st.session_state.stage = 4
        st.session_state.battle_log.insert(0, "⚡ 최종 라운드로 진입합니다!")

    else:
      if rolls:
        min_d = min(r[3] for r in rolls)
        for target, name, aura, denom in rolls:
          if denom == min_d:
            if target == "me":
              st.session_state.my_alive = False
            else:
              target["alive"] = False
        st.session_state.battle_log.insert(
            0, f"[최종라운드] 최하위(1 in {min_d:,}) 탈락 발생"
        )

    st.rerun()

st.subheader("📜 최근 로그")
for log in st.session_state.get("battle_log", [])[:5]:
  st.text(log)

st.divider()

st.subheader("🏆 생존자 상위 랭킹 (TOP 10)")
all_alive = []
if st.session_state.my_alive:
  all_alive.append({
      "name": st.session_state.my_name,
      "aura": st.session_state.my_aura,
      "denom": denominators[st.session_state.my_aura],
  })
for ai in st.session_state.ai_players:
  if ai["alive"]:
    all_alive.append({
        "name": ai["name"],
        "aura": ai["aura"],
        "denom": denominators[ai["aura"]],
    })

all_alive.sort(key=lambda x: x["denom"], reverse=True)

for i, p in enumerate(all_alive[:10], 1):
  ic = icons.get(p["aura"], "✨")
  st.write(f"{i}. **{p['name']}** — {ic} `{p['aura']}` (1 in {p['denom']:,})")
