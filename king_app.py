import streamlit as st

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

# 🔹 หน้าแรก
def show_home():
    st.image(get_image_url("king1.PNG"), width=300)
    st.markdown("<h2 style='text-align: center; color: red;'>To: พี่คิง 💖</h2>", unsafe_allow_html=True)
    if st.button("💖 กดเปิดจดหมาย 💖"):
        st.session_state.page = "letter"
        st.rerun()

# 🔹 จดหมาย
def show_letter():
    st.markdown("<h2 style='text-align: center; color: pink;'>Happy Valentine's Day 💖</h2>", unsafe_allow_html=True)
    st.write("""
    ถึงพี่คิง,\n
    แบร่ๆพี่พระราชาคนเย็นชา หนุ่มป.โทจอมนิ่ง\n
    แต่เวลายิ้มน่ารักสุดๆ (ถึงกาฟิวส์จะเห็นแต่ในรูป555)\n\n
    เวลาคุยกันกับพี่คิงอาจจะไม่นานหรอก\n
    แต่คุยแล้วมีความสุขทุกครั้ง\n
    งื้อโอกาสที่ไปต่อกาฟิวส์ก็พอรู้แหละว่าน่าจะ 0%\n
    แต่ก็อยากลองพยายามให้เต็มที่ง่าาา
    """)
    
    if st.button("💖 พร้อมเล่นเกมหรือยัง? 💖"):
        st.session_state.page = "password"
        st.rerun()

# 🔹 ใส่รหัสเข้าเกม
def ask_password():
    st.write("🔑 **ใส่รหัสลับเพื่อเข้าเกม!**")
    password = st.text_input("รหัสผ่าน", type="password")
    
    if st.button("ยืนยัน"):
        if password == "loveKing":
            st.session_state.page = "game"
            st.rerun()
        else:
            st.error("❌ รหัสผิด! ลองใหม่สิพี่คิง 😉")

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

# 🔹 ฟังก์ชันเริ่มเกม
def start_game():
    st.session_state.answers = []
    st.write("🎮 **เกมเริ่มแล้ว!** ตอบคำถามต่อไปนี้:")
    
    for i, (question, options) in enumerate(questions):
        answer = st.radio(f"**{i+1}. {question}**", options, key=f"q{i}")
        st.session_state.answers.append(answer)
    
    if st.button("ส่งคำตอบ 💖"):
        save_answers()
        st.session_state.page = "final"
        st.rerun()

# 🔹 บันทึกคำตอบ (ให้เธอดู แต่พี่คิงไม่เห็น!)
def save_answers():
    file_path = "king_answers.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("💖 คำตอบของพี่คิง 💖\n\n")
        for i, (question, answer) in enumerate(zip(questions, st.session_state.answers)):
            f.write(f"{i+1}. {question[0]} → {answer}\n")
    st.success("✅ คำตอบถูกบันทึก! (เธอเปิดไฟล์ `king_answers.txt` ดูได้)")

# 🔹 หน้าสุดท้าย (ข้อความ + รูปแนวนอน)
def show_final_message():
    st.markdown("<h2 style='text-align: center; color: red;'>ขอบคุณที่เล่นเกมนี้! 💖</h2>", unsafe_allow_html=True)
    
    image_urls = [
        get_image_url("king1.PNG"), get_image_url("king2.PNG"),
        get_image_url("king3.PNG"), get_image_url("king4.PNG"),
        get_image_url("king5.PNG"), get_image_url("king6.PNG"),
        get_image_url("king7.PNG")
    ]
    
    st.image(image_urls, width=100)

    if st.button("🎉 หน้าสุดท้าย 🎉"):
        st.session_state.page = "special"
        st.rerun()

# 🔹 หน้าพิเศษ (Valentine's Surprise!)
def show_special_page():
    st.markdown("<h1 style='text-align: center; color: pink;'>HAPPY VALENTINE'S DAY นะครับพี่คิง 💖</h1>", unsafe_allow_html=True)
    st.image(get_image_url("king8.PNG"), width=300)
    
    st.markdown("<h3 style='text-align: center; color: red;'>ขอบคุณนะครับที่คุยกับกฟแล้วทำให้กฟยิ้มได้ทุกวัน 😊</h3>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: pink;'>💖💖💖💖💖💖💖</h2>", unsafe_allow_html=True)

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
elif st.session_state.page == "special":
    show_special_page()
