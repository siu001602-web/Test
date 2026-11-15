```python
import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(
    page_title="아우라 AI 배틀로얄", page_icon="⚔️", layout="wide"
)

# Initialize Session States
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.player_name = "플레이어"
    st.session_state.player_alive = True
    st.session_state.player_aura = "없음"
    st.session_state.player_history = []
    
    # Generate 100 AI Bots
    ai_names = [
        "알파", "베타", "가마", "델타", "에실론", "제타", "에타", "테타", "요타", "카파",
        "람다", "뮤", "뉴", "크시", "오미크론", "피", "로", "시그마", "타우", "우프",
        "발키리", "제우스", "포세이돈", "하데스", "아테나", "아폴로", "아르테미스", "아레스", "헤르메스", "디오니소스",
        "크로노스", "타이탄", "드래곤", "피닉스", "그리핀", "히드라", "키메라", "켄타우로스", "페가수스", "오딘",
        "토르", "로키", "헤임달", "발더", "프레야", "티르", "시프", "묠니르", "비프로스트", "발할라",
        "섀도우", "팬텀", "고스트", "스펙터", "나이트", "다크", "라이트", "썬더", "블리자드", "스톰",
        "네오", "사이퍼", "매트릭스", "글리치", "바이러스", "핵", "비트", "바이트", "픽셀", "버그",
        "아담", "이브", "카인", "아벨", "노아", "아브라함", "모세", "다윗", "솔로몬", "이사야",
        "예레미야", "에스겔", "다니엘", "호세아", "요엘", "아모스", "오바댜", "요나", "미가", "나훔",
        "하박국", "스바냐", "학개", "스가랴", "말라기", "루시퍼", "미카엘", "가브리엘", "라파엘", "우리엘"
    ]
    
    st.session_state.bots = []
    for i in range(100):
        name = f"AI_{ai_names[i] if i < len(ai_names) else i+1}"
        st.session_state.bots.append({
            "id": i,
            "name": name,
            "alive": True,
            "aura": "없음",
            "eliminated_round": None,
            "elimination_reason": ""
        })
    
    st.session_state.round_count = 0
    st.session_state.battle_log = ["게임이 시작되었습니다. 버튼을 눌러 라운드를 진행하세요!"]

# Gacha pool for 1,000,000x luck draws
aura_pool = [
    ("𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭", "🖐️✨🌌👑", 5),
    ("𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻", "🕸️🌙✨🦋", 15),
    ("사도:베일", "🎃👁️", 30),
    ("수확가", "🎃🗡️", 50),
    ("악몽의 하늘", "🎃🌌", 80),
    ("𝓘𝓬𝓮𝓐𝓰𝓮", "❄️🧊👑", 120),
    ("𝓜𝓪𝓶𝓶𝓸𝓽𝓱", "🦣❄️🧊", 180),
    ("✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧", "🌈💎✨", 250),
    ("𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤", "🎼🎻✨♠️", 350),
    ("𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐", "🌌💠💫", 500),
    ("༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒", "🌊🐉🌀", 700),
    ("감시자", "👁️‍🗨️⚡", 1000),
    ("아쿠아리움", "🐠🌊🏛️", 1500),
    ("크로마틱", "🌈💫", 2500),
    ("대마법사", "🧙‍♂️✨", 4000),
    ("아케인", "🔮👑", 7000),
    ("태양", "☀️✨", 10000),
    ("달", "🌙✨", 10000),
    ("레어", "💙📦", 30000),
    ("일반", "⚪📦", 50000)
]

def roll_aura():
    # 1,000,000x luck roll: weighted random choice favoring higher tier auras
    weights = [item[2] for item in aura_pool]
    chosen = random.choices(aura_pool, weights=weights, k=1)[0]
    return f"{chosen[1]} {chosen[0]}"

st.title("⚔️ 아우라 AI 배틀로얄 대전")
st.markdown("플레이어와 100명의 AI가 매 라운드 **1,000,000x 행운 아우라**를 뽑으며 생존 경쟁을 펼칩니다! 사망해도 **관전 모드**로 계속 참여할 수 있습니다.")

# Top Status Bar
col_s1, col_s2, col_s3, col_s4 = st.columns(4)
alive_ai_count = sum(1 for b in st.session_state.bots if b["alive"])
with col_s1:
    st.metric("라운드", f"제 {st.session_state.round_count} 라운드")
with col_s2:
    st.metric("생존 AI 수", f"{alive_ai_count} / 100명")
with col_s3:
    status_text = "🟢 생존 중" if st.session_state.player_alive else "👻 관전 모드 (사망)"
    st.metric("내 상태", status_text)
with col_s4:
    st.metric("내 아우라", st.session_state.player_aura)

st.divider()

# Control Panel
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    if st.button("🎲 다음 라운드 진행 (전원 뽑기)", type="primary", use_container_width=True):
        st.session_state.round_count += 1
        round_desc = f"--- [라운드 {st.session_state.round_count}] ---"
        
        # Player rolls if alive
        if st.session_state.player_alive:
            st.session_state.player_aura = roll_aura()
            round_desc += f"\n플레이어가 '{st.session_state.player_aura}' 아우라를 획득했습니다!"
        else:
            round_desc += "\n플레이어는 사망하여 관전 중입니다."
            
        # AI bots roll if alive
        for bot in st.session_state.bots:
            if bot["alive"]:
                bot["aura"] = roll_aura()
                
        st.session_state.battle_log.insert(0, round_desc)
        st.rerun()

with col_btn2:
    if st.button("🔄 게임 초기화 (새 게임)", type="secondary", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

st.markdown("### 🎮 플레이어 조작 및 관리 패널")
col_p_ctrl1, col_p_ctrl2 = st.columns(2)

with col_p_ctrl1:
    st.markdown("#### 내 캐릭터 관리")
    if st.session_state.player_alive:
        if st.button("💀 항복하기 (사망 후 관전 전환)", use_container_width=True):
            st.session_state.player_alive = False
            st.session_state.battle_log.insert(0, "🚨 플레이어가 스스로 항복하여 관전 모드로 전환되었습니다.")
            st.rerun()
    else:
        st.info("현재 관전 모드입니다. AI들의 생존 경쟁을 지켜보세요!")

with col_p_ctrl2:
    st.markdown("#### ⚖️ 탈락자 직접 지정 (처형)")
    target_options = [b["name"] for b in st.session_state.bots if b["alive"]]
    if target_options:
        selected_target = st.selectbox("탈락시킬 AI 선택", target_options)
        if st.button("⚡ 선택한 AI 강제 탈락시키기", type="primary", use_container_width=True):
            for b in st.session_state.bots:
                if b["name"] == selected_target:
                    b["alive"] = False
                    b["eliminated_round"] = st.session_state.round_count
                    b["elimination_reason"] = "플레이어의 직접 처형"
                    st.session_state.battle_log.insert(0, f"⚡ [처형] 플레이어가 {b['name']}을(를) 강제 탈락시켰습니다!")
                    break
            st.rerun()
    else:
        st.success("모든 AI가 탈락했습니다!")

st.divider()

# Layout Tabs: Arena Status / Battle Log / Elimination Manager
tab_arena, tab_log = st.tabs(["🏟️ 배틀로얄 아레나 (참가자 목록)", "📜 실시간 배틀 로그"])

with tab_arena:
    st.markdown("### 생존 및 탈락 AI 목록")
    
    # Filter controls
    filter_mode = st.radio("보기 필터", ["전체 보기", "생존자만", "탈락자만"], horizontal=True)
    
    display_bots = st.session_state.bots
    if filter_mode == "생존자만":
        display_bots = [b for b in st.session_state.bots if b["alive"]]
    elif filter_mode == "탈락자만":
        display_bots = [b for b in st.session_state.bots if not b["alive"]]
        
    cols = st.container()
    for bot in display_bots:
        status_badge = "🟢 생존" if bot["alive"] else f"❌ 탈락 (R.{bot['eliminated_round']})"
        border_color = "#00ffcc" if bot["alive"] else "#555555"
        
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([2, 2, 3, 2])
            with c1:
                st.markdown(f"**{bot['name']}**")
            with c2:
                st.markdown(status_badge)
            with c3:
                st.markdown(f"최근 아우라: `{bot['aura']}`")
            with c4:
                if bot["alive"]:
                    if st.button("탈락시키기", key=f"kill_{bot['id']}"):
                        bot["alive"] = False
                        bot["eliminated_round"] = st.session_state.round_count
                        bot["elimination_reason"] = "플레이어의 수동 지정"
                        st.session_state.battle_log.insert(0, f"💀 플레이어가 {bot['name']}을(를) 탈락시켰습니다.")
                        st.rerun()
                else:
                    if st.button("부활시키기", key=f"revive_{bot['id']}"):
                        bot["alive"] = True
                        bot["eliminated_round"] = None
                        st.session_state.battle_log.insert(0, f"✨ 플레이어가 {bot['name']}을(를) 부활시켰습니다!")
                        st.rerun()

with tab_log:
    st.markdown("### 📜 전투 기록 및 이벤트 로그")
    for log in st.session_state.battle_log:
        st.text(log)
```
