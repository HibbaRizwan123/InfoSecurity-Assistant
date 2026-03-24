import streamlit as st
from query import query_rag

# --- Page Configuration ---
st.set_page_config(
    page_title="InfoSecurity Assistant",
    layout="centered"
)

# CSS
st.markdown("""
    <style>
    /* ── Fully remove Streamlit's default header ── */
    header[data-testid="stHeader"] {
    height: 0 !important;
    min-height: 0 !important;
    display: none !important;
    }

/* ── Remove the toolbar/decoration bar ── */
    [data-testid="stToolbar"] {
    display: none !important;
    }
    
    [data-testid="stDecoration"] {
    display: none !important;
    }
        /* ── Navbar ── */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 65px;
            background: #023E8A;
            border-bottom: 1px solid #023E8A;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 999999;
        }

        .navbar-title {
            font-size: 30px;
            font-weight: 600;
            font-family: 'sans-serif';
            color: #ffffff;
            letter-spacing: -0.2px;
        }

        /* Push page content down so it doesn't hide under the navbar */
        section.main > div:first-child {
            padding-top: 72px !important;
        }

        /* ── Base ── */
        .example-box {
            background-color: #1e1e2e;
            border-left: 4px solid #00b4d8;
            padding: 12px 16px;
            border-radius: 6px;
            color: #cdd6f4;
            font-family: 'sans-serif';
            margin: 10px 0;
        }
        [data-testid="stTextInput"] > div > div {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
            outline: none !important;
            }

        /* ── Fuse columns together with no gap ── */
        [data-testid="stHorizontalBlock"] {
            gap: 0 !important;
            align-items: center !important;
            background: #ffffff;
            border-radius: 999px;
            padding: 6px 6px 6px 20px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);
            border: 1px solid #e5e7eb;
        }

        /* ── Text input: no border, transparent bg ── */
        .stTextInput > div > div > input {
            border: none !important;
            background: transparent !important;
            border-radius: 0 !important;
            height: 44px !important;
            padding: 0 !important;
            font-size: 1rem !important;
            color: #111827 !important;
            box-shadow: none !important;
            outline: none !important;
        }
        .stTextInput > div > div > input::placeholder {
            color: #9ca3af !important;
        }
        .stTextInput > div > div > input:focus {
            border: none !important;
            box-shadow: none !important;
        }
        [data-testid="stTextInput"] > div {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
        }

        /* ── Arrow button: dark circle on the right ── */
        [data-testid="stButton"] > button {
            background: #023E8A !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 50% !important;
            width: 44px !important;
            height: 44px !important;
            min-width: 44px !important;
            padding: 0 !important;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            line-height: 1 !important;
            cursor: pointer !important;
            flex-shrink: 0 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: background 0.2s, transform 0.15s !important;
        }

        [data-testid="stButton"] > button:hover {
            background: #374151 !important;
            transform: scale(1.07) !important;
        }

        [data-testid="stButton"] > button:active {
            transform: scale(0.95) !important;
        }

        /* ── Remove Streamlit spacing ── */
        [data-testid="stTextInput"] { margin-bottom: 0 !important; }
        [data-testid="stVerticalBlock"] > div { gap: 0 !important; }
        div[data-testid="column"] { padding: 0 !important; }
    </style>
     
""", unsafe_allow_html=True)

# 2nd st.markdown — Navbar HTML
st.markdown("""
    <div class="navbar">
        <span class="navbar-title">InfoSecurity Assistant</span>
    </div>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <style>
    section.main > div:first-child {
        padding-top: 45vh !important;
        min-height: calc(100vh - 65px);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; font-size:1rem; color:#111827; margin-bottom:24px;'>"
    "Ask any question from your <strong>Information Security PDFs</strong> and get an answer instantly!"
    "</p>",
    unsafe_allow_html=True
)


# --- Session State ---
if "query" not in st.session_state:
    st.session_state.query = ""
if "clear" not in st.session_state:
    st.session_state.clear_input = False

def submit():
    st.session_state.query = st.session_state.input_box
    st.session_state.input_box = ""

# --- Input Section ---
col1, col2 = st.columns([14, 1])

with col1:
    st.text_input(
        "Enter your question!",
        placeholder="What is a threat?",
        label_visibility="collapsed",
        key="input_box",
        on_change=submit
    )

with col2:
    ask_button = st.button("↑", on_click=submit)


# --- Answer Section ---
if ask_button or st.session_state.query:
    if st.session_state.query.strip():
        with st.spinner("Searching PDFs and generating answer..."):
            response = query_rag(st.session_state.query)
        st.session_state.query = ""

        st.divider()
        st.markdown(response)

    else:
        st.warning("Please enter a question before clicking Ask!")