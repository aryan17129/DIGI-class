import streamlit as st
from src.components.header import header_home

from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    # ---------------- Theme Selector ----------------

    if "theme" not in st.session_state:
        st.session_state.theme = "Green"

    with st.sidebar:
        st.title("🎨 Settings")

        st.session_state.theme = st.selectbox(
            "Choose Theme",
            ["Green", "Blue", "Purple", "Dark", "Orange"],
            index=["Green", "Blue", "Purple", "Dark", "Orange"].index(st.session_state.theme),
        )

    header_home()

    # Pass selected theme
    style_background_home(st.session_state.theme)

    style_base_layout()    



    # ------------------ Hero Section ------------------

    st.markdown(
        """
        <h1 style='text-align:center;color:white;'>
            🎓 DIGI CLASS
        </h1>

        <h4 style='text-align:center;color:#E8F5E9;'>
            AI Powered Face Recognition Attendance Management System
        </h4>

        <br>
        """,
        unsafe_allow_html=True,
    )

    # ------------------ Login Cards ------------------

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.header("🎓 Student")

        st.image("assets/student.png", width=220)

        st.write(
            "Access attendance records, classroom updates, and your academic dashboard."
        )

        if st.button(
            "Student Portal",
            key="student",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:

        st.header("👨‍🏫 Teacher")

        st.image("assets/teacher.png", width=220)

        st.write(
            "Manage students, mark attendance, monitor reports, and access analytics."
        )

        if st.button(
            "Teacher Portal",
            key="teacher",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    st.divider()

    # ------------------ Features ------------------

    st.subheader("✨ Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            ### 📷 Face Recognition

            - Fast Attendance
            - High Accuracy
            - Contactless
            """
        )

    with c2:
        st.markdown(
            """
            ### 📊 Reports

            - Attendance History
            - Student Analytics
            - Performance Insights
            """
        )

    with c3:
        st.markdown(
            """
            ### 🔒 Secure System

            - Teacher Authentication
            - Student Login
            - Encrypted Data
            """
        )

    st.divider()

    st.markdown(
        """
        <div style='text-align:center;color:white;padding:15px;'>

        <h3>🚀 Smart Attendance System</h3>

        Designed to automate attendance using AI-powered face recognition,
        reducing manual work while improving accuracy and security.

        </div>
        """,
        unsafe_allow_html=True,
    )

    footer_home()