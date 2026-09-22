import time
import streamlit as st

st.title("⏱️ เกมเติมคำศัพท์จับเวลา")

# -----------------------------
# ตั้งค่าเริ่มต้น (จุดที่ 1)
# -----------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# -----------------------------
# ฟังก์ชันเริ่มเกมใหม่ (จุดที่ 2)
# -----------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# -----------------------------
# แสดงผลลัพธ์ (จุดที่ 3, 4, 5, 8)
# -----------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):  # จุดที่ 8: รับค่า ans3, ans4
    st.balloons()

    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()  # จุดที่ 3
    u_ans4 = ans4.strip().lower()  # จุดที่ 3

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ตรวจข้อ 3 (จุดที่ 4)
    if u_ans3 == "dog":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4 (จุดที่ 4)
    if u_ans4 == "bird":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    st.info(f"🏆 ได้คะแนนรวม: {score}/4 คะแนน")

    if score == 4:  # จุดที่ 5
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# -----------------------------
# ปุ่มเริ่มเกม
# -----------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# -----------------------------
# นับเวลาถอยหลัง 30 วินาที
# -----------------------------
if st.session_state.start is not None and not st.session_state.is_ended:

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")

        # รีเฟรชทุก 1 วินาที
        time.sleep(1)
        st.rerun()

    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# -----------------------------
# ช่องกรอกคำตอบ (จุดที่ 6, 7)
# -----------------------------
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val
)

# เพิ่มช่องรับคำตอบ ข้อ 3 และ 4 (จุดที่ 6)
ans3 = st.text_input(
    "ข้อ 3: A `d _ g` is man's best friend. 🐶",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: A `b _ r d` can fly in the sky. 🐦",
    value=st.session_state.ans4_val
)

# อัปเดตค่าล่าสุดเข้า session_state (จุดที่ 7)
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# -----------------------------
# ปุ่มส่งคำตอบ
# -----------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()


# -----------------------------
# แสดงผลลัพธ์ (จุดที่ 8)
# -----------------------------
if st.session_state.is_ended:
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


st.divider()

st.write("นางสาวธัญสุดา แก้ววิเชียร เลขที่ 40 ม.4/10")
