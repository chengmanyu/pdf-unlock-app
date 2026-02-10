import streamlit as st
import pikepdf
import os
from io import BytesIO

# 网页标题和描述，使其吸引人
st.title("PDF解锁工具")
st.markdown("### 简单易用！上传你的PDF，输入密码，一键解锁并下载。🔓")
st.markdown("支持用户输入密码，确保安全和灵活。")

# 用户上传PDF文件
uploaded_file = st.file_uploader("上传你的PDF文件", type=["pdf"])

# 用户输入密码
password = st.text_input("输入PDF密码", type="password")

# 解锁按钮
if st.button("解锁PDF"):
    if uploaded_file and password:
        try:
            # 读取上传文件
            input_pdf = BytesIO(uploaded_file.read())
            
            # 使用pikepdf解锁
            with pikepdf.open(input_pdf, password=password) as pdf:
                output_pdf = BytesIO()
                pdf.save(output_pdf, encryption=None)
                output_pdf.seek(0)
                
                # 下载按钮
                st.download_button(
                    label="下载解锁后的PDF",
                    data=output_pdf,
                    file_name="unlocked_pdf.pdf",
                    mime="application/pdf"
                )
                st.success("解锁成功！点击下载。")
        except Exception as e:
            st.error(f"解锁失败：{str(e)}。请检查密码或文件。")
    else:
        st.warning("请上传文件并输入密码。")