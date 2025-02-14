import streamlit as st
import os
import smtplib
from email.mime.text import MIMEText

# 🔹 ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Happy Valentine's Day 💖", page_icon="💌", layout="centered")

# 🔹 ฟังก์ชันโหลดรูปจาก GitHub
GITHUB_REPO = "https://raw.githubusercontent.com/narainritjaksoongnern22/king/main/"
def get_image_url(filename):
    return f"{GITHUB_REPO}{filename}"

# 🔹 ตั้งค่าคำตอบ
if "answers" not in st.session_state:
    st.session_state.answers = []
if "page" not in st.session_state:
    st.session_state.page = "home"

# 🔹 ตั้งค่าไฟล์ซ่อนคำตอบ
HIDDEN_ANSWERS_FILE = "hidden_answers.txt"
YOUR_EMAIL = "narainritjaksoongnern22@gmail.com"  # 🔥 เปลี่ยนเป็นอีเมลของเธอ

# 🔹 ฟังก์ชันบันทึกคำตอบแบบลับ
def save_hidden_answers():
    answers_text = "💖 คำตอบของพี่คิง 💖\n\n"
    for i, (question, answer) in enumerate(zip(questions, st.session_state.answers)):
        answers_text += f"{i+1}. {question[0]} → {answer}\n"

    with open(HIDDEN_ANSWERS_FILE, "a", encoding="utf-8") as f:  # 🔥 ใช้ "a" เพื่อเพิ่มข้อมูล (ไม่ลบของเก่า)
        f.write(answers_text + "\n---\n")

    # 🔥 ส่งอีเมลไปให้เธอ (เธอเท่านั้นที่เห็น)
    send_email(answers_text)

# 🔹 ฟังก์ชันส่งอีเมล (ให้เธอเท่านั้นที่เห็น)
def send_email(content):
    try:
        sender_email = "your-email@gmail.com"  # 🔥 ต้องใช้ Gmail จริง (แนะนำใช้บัญชีสำรอง)
        sender_password = "your-app-password"  # 🔥 ต้องใช้ "App Password" (ไม่ใช่รหัสผ่านปกติ)
        recipient_email = YOUR_EMAIL

        msg = MIMEText(content)
        msg["Subject"] = "💖 คำตอบของพี่คิง 💖"
        msg["From"] = sender_email
        msg["To"] = recipient_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        st.success("✅ คำตอบของพี่คิงถูกส่งไปที่อีเมลของเธอแล้ว!")

    except Exception as e:
        st.error(f"❌ ไม่สามารถส่งอีเมลได้: {e}")

# 🔹 ฟังก์ชันแสดงคำตอบที่ถูกบันทึก (เธอเท่านั้นที่เห็น!)
def show_hidden_answers():
    st.markdown("<h3 style='color: red;'>🔒 คำตอบของพี่คิง (เธอเท่านั้นที่เห็น!)</h3>", unsafe_allow_html=True)
    
    if os.path.exists(HIDDEN_ANSWERS_FILE):
        with open(HIDDEN_ANSWERS_FILE, "r", encoding="utf-8") as f:
            hidden_answers = f.read()
            st.text_area("📜 คำตอบของพี่คิง", hidden_answers, height=300)

        # ✅ ปุ่มให้เธอโหลดไฟล์คำตอบไปดูเอง
        st.download_button(
            label="📥 ดาวน์โหลดคำตอบของพี่คิง",
            data=hidden_answers,
            file_name="king_answers.txt",
            mime="text/plain"
        )
    else:
        st.warning("⚠️ ยังไม่มีคำตอบที่ถูกบันทึก")

# 🔹 ฟังก์ชันเริ่มเกม
def start_game():
    st.session_state.answers = []  # 🔥 รีเซ็ตคำตอบทุกครั้ง
    st.write("🎮 **เกมเริ่มแล้ว!** ตอบคำถามต่อไปนี้:")
    
    for i, (question, options) in enumerate(questions):
        answer = st.radio(
            f"**{i+1}. {question}**",
            options,
            index=None,  # 🔥 ทำให้ตัวเลือกว่างเปล่าตั้งแต่เริ่มต้น
            key=f"q{i}"
        )
        st.session_state.answers.append(answer)
    
    if st.button("📤 บันทึกคำตอบแบบลับ"):
        save_hidden_answers()
        st.success("✅ คำตอบของพี่คิงถูกบันทึกเรียบร้อย! (เธอเปิดดูได้)")
        st.session_state.page = "final"
        st.rerun()

# 🔹 ฟังก์ชันหน้าสุดท้าย
def show_final_message():
    st.markdown("<h2 style='text-align: center; color: red;'>ขอบคุณนะงับพี่คิงเล่นเกมนี้! 💖</h2>", unsafe_allow_html=True)

    if st.button("🔎 ดูคำตอบของพี่คิง"):
        show_hidden_answers()

    if st.button("🎉 หน้าสุดท้าย 🎉"):
        st.session_state.page = "special"
        st.rerun()

# 🔹 รายชื่อคำถาม
questions = [
    ("💖 พี่คิงชอบคนแบบไหน?", ["ขี้อ้อน", "ขี้เล่น", "อบอุ่น", "สายลุย"]),
    ("🌍 พี่คิงชอบเที่ยวที่ไหน?", ["ภูเขา", "ทะเล", "คาเฟ่", "อยู่บ้าน"]),
    ("🍜 พี่คิงชอบกินอะไร?", ["อาหารญี่ปุ่น", "หมูกระทะ", "ส้มตำ", "ของหวาน"]),
    ("🎶 พี่คิงชอบฟังเพลงแนวไหน?", ["ป๊อป", "ลูกทุ่ง", "แร็ป", "ร็อก"]),
    ("📺 พี่คิงดูหนังแนวไหน?", ["โรแมนติก", "แอคชั่น", "สยองขวัญ", "คอมเมดี้"]),
    ("🐶 พี่คิงชอบสัตว์เลี้ยงตัวไหนมากที่สุด?", ["หมา", "แมว", "กระต่าย", "นกแก้ว"]),
    ("🎁 ถ้าได้ของขวัญจากคนพิเศษ อยากได้อะไร?", ["ดอกไม้", "ขนม", "ตุ๊กตา", "เซอร์ไพรส์"]),
    ("💌 สมมติว่ามีคนแอบชอบพี่คิง พี่คิดว่าเขาควรทำไง?", ["บอกตรง ๆ", "ส่งข้อความ", "แอบส่งของให้", "ไม่ต้องบอก"]),
    ("😍 พี่คิงอยากไปเที่ยวด้วยกันมั้ย? 💕", ["ไป!"])
]

# 🔹 เลือกหน้าที่ต้องแสดง
if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "letter":
    show_letter()
elif st.session_state.page == "password":
    ask_password()
elif st.session_state.page == "game":
    start_game()
elif st.session_state.page == "final":
    show_final_message()
