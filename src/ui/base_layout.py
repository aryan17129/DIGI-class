import streamlit as st

def style_background_home(theme="Green"):

    themes = {
        "Green": {
            "bg": "linear-gradient(135deg,#0B3D2E,#14532D,#166534,#22C55E)",
            "button": "#22C55E",
        },
        "Blue": {
            "bg": "linear-gradient(135deg,#1E3A8A,#2563EB,#3B82F6,#60A5FA)",
            "button": "#2563EB",
        },
        "Purple": {
            "bg": "linear-gradient(135deg,#4C1D95,#6D28D9,#7C3AED,#A855F7)",
            "button": "#7C3AED",
        },
        "Dark": {
            "bg": "linear-gradient(135deg,#111827,#1F2937,#374151,#4B5563)",
            "button": "#374151",
        },
        "Orange": {
            "bg": "linear-gradient(135deg,#7C2D12,#C2410C,#EA580C,#FB923C)",
            "button": "#EA580C",
        },
    }

    current = themes[theme]

    st.markdown(
        f"""
        <style>

        [data-testid="stAppViewContainer"] {{
            background: {current['bg']};
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        div[data-testid="stColumn"] {{
            background: rgba(255,255,255,.12);
            backdrop-filter: blur(15px);
            border-radius:20px;
            padding:2rem;
            border:1px solid rgba(255,255,255,.2);
        }}

        .stButton > button {{
            width:100%;
            border-radius:15px;
            height:55px;
            background:{current['button']} !important;
            color:white !important;
            border:none;
            font-weight:600;
        }}

        .stButton > button:hover {{
            transform:scale(1.05);
        }}

        h1,h2,h3,h4,p {{
            color:white;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )
def style_base_layout():
    pass