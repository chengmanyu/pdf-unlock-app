import streamlit as st
import pikepdf
from io import BytesIO

# ── 語言字典 ────────────────────────────────────────────────────────────────
translations = {
    "English": {
        "title": "PDF Unlock Tool",
        "subtitle": "### Simple & Easy! Upload your PDF, enter password, unlock & download. 🔓",
        "desc": "User-input password for security and flexibility.",
        "upload_label": "Upload your PDF file",
        "password_label": "Enter PDF password",
        "button_unlock": "Unlock PDF",
        "button_download": "Download Unlocked PDF",
        "success": "Unlocked successfully! Click to download.",
        "error": "Unlock failed: {error}. Please check password or file.",
        "warning": "Please upload a file and enter the password.",
    },
    "简体中文": {
        "title": "PDF 解锁工具",
        "subtitle": "### 简单易用！上传你的 PDF，输入密码，一键解锁并下载。🔓",
        "desc": "支持用户输入密码，确保安全和灵活。",
        "upload_label": "上传你的 PDF 文件",
        "password_label": "输入 PDF 密码",
        "button_unlock": "解锁 PDF",
        "button_download": "下载解锁后的 PDF",
        "success": "解锁成功！点击下载。",
        "error": "解锁失败：{error}。请检查密码或文件。",
        "warning": "请上传文件并输入密码。",
    },
    "繁體中文": {
        "title": "PDF 解鎖工具",
        "subtitle": "### 簡單易用！上傳你的 PDF，輸入密碼，一鍵解鎖並下載。🔓",
        "desc": "支援使用者輸入密碼，確保安全與彈性。",
        "upload_label": "上傳你的 PDF 檔案",
        "password_label": "輸入 PDF 密碼",
        "button_unlock": "解鎖 PDF",
        "button_download": "下載解鎖後的 PDF",
        "success": "解鎖成功！點擊下載。",
        "error": "解鎖失敗：{error}。請檢查密碼或檔案。",
        "warning": "請上傳檔案並輸入密碼。",
    }
}

# ── 初始化 session_state 中的語言（預設英文） ──────────────────────────────
if "language" not in st.session_state:
    st.session_state.language = "English"

# ── 語言選擇器（放在最上面，吸引眼球） ─────────────────────────────────────
lang_options = ["English", "简体中文", "繁體中文"]
selected_lang = st.selectbox(
    "Language / 语言 / 語言",
    options=lang_options,
    index=lang_options.index(st.session_state.language),
    key="lang_selector"
)

# 當選擇改變時，更新 session_state 並重新執行
if selected_lang != st.session_state.language:
    st.session_state.language = selected_lang
    st.rerun()  # 強制重新渲染整個頁面

# 取得當前語言的翻譯
t = translations[st.session_state.language]

# ── 主頁面 ───────────────────────────────────────────────────────────────────
st.title(t["title"])
st.markdown(t["subtitle"])
st.markdown(t["desc"])

uploaded_file = st.file_uploader(t["upload_label"], type=["pdf"])

password = st.text_input(t["password_label"], type="password")

if st.button(t["button_unlock"]):
    if uploaded_file and password:
        try:
            input_pdf = BytesIO(uploaded_file.read())
            with pikepdf.open(input_pdf, password=password) as pdf:
                output_pdf = BytesIO()
                pdf.save(output_pdf, encryption=None)
                output_pdf.seek(0)
                
                st.download_button(
                    label=t["button_download"],
                    data=output_pdf,
                    file_name="unlocked_pdf.pdf",
                    mime="application/pdf"
                )
                st.success(t["success"])
        except Exception as e:
            st.error(t["error"].format(error=str(e)))
    else:
        st.warning(t["warning"])