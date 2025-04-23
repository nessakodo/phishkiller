# app.py - Streamlit interface for PhishKiller with theme and severity scoring

import streamlit as st
from analyzer import analyze_url, analyze_header_text
import json

# Page setup
st.set_page_config(page_title="PhishKiller", layout="centered")

# Define dark terminal themes
THEMES = {
    "Green Matrix": {
        "bg": "#0b0c10",
        "text": "#00ff00",
        "accent": "#00cc66",
        "alt": "#55ff55",
        "font": "'Share Tech Mono', monospace"
    },
    "Hacker Blue": {
        "bg": "#0d1b2a",
        "text": "#00b4d8",
        "accent": "#90e0ef",
        "alt": "#caf0f8",
        "font": "'Share Tech Mono', monospace"
    }
}

# Sidebar theme selector
selected_theme = st.sidebar.selectbox("Theme", list(THEMES.keys()), index=0)
colors = THEMES[selected_theme]

# Inject CSS for style and mobile responsiveness
st.markdown(f"""
    <style>
        html, body, [class*="css"]  {{
            background-color: {colors['bg']};
            color: {colors['text']};
            font-family: {colors['font']};
        }}
        .stTextInput > div > div > input {{
            background-color: #1f2833;
            color: {colors['alt']};
        }}
        .stTextInput label, .stFileUploader label {{
            font-weight: bold;
            color: {colors['accent']};
        }}
        .stDownloadButton button {{
            background-color: {colors['accent']};
            color: {colors['bg']};
            font-family: {colors['font']};
        }}
        .css-1aumxhk, .stMarkdown, .stSubheader {{
            font-family: {colors['font']};
            color: {colors['text']};
        }}
        code {{
            background-color: #1f2833;
            color: {colors['alt']};
        }}
        @media (max-width: 768px) {{
            .block-container {{
                padding: 1rem;
            }}
        }}
        .stAlert {{
            background-color: transparent;
            border-left: 3px solid {colors['accent']};
            color: {colors['alt']};
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Title and instructions
st.title("PhishKiller - Phishing Threat Analyzer")
st.markdown("""
Analyze suspicious URLs and email headers to detect phishing threats.
Upload a raw header file or enter a URL below.
""")

report_data = {}

# URL analysis section
st.header("URL Analysis")
url_input = st.text_input("Enter a suspicious URL")

if url_input:
    st.write("Analyzing...")
    level, reasons = analyze_url(url_input)
    report_data['url'] = url_input
    report_data['url_risk'] = level
    report_data['url_reasons'] = reasons

    st.subheader("Threat Level:")
    st.markdown(f"<code>{level}</code>", unsafe_allow_html=True)

    if reasons:
        st.subheader("Reasons:")
        for r in reasons:
            st.markdown(f"- {r}")

st.markdown("---")

# Email header analysis section
st.header("Email Header Analysis")
header_file = st.file_uploader("Upload email header (.txt)", type=["txt"])

if header_file:
    header_text = header_file.read().decode("utf-8")
    results = analyze_header_text(header_text)

    report_data['email_header_analysis'] = {
        'ips': results['ips'],
        'spf_dmarc_failures': results['spf_dmarc_failures']
    }

    st.subheader("IP Addresses Found")
    st.code(", ".join(results['ips']) or "None", language='text')

    if results['spf_dmarc_failures']:
        st.subheader("SPF/DMARC Failures")
        for fail in results['spf_dmarc_failures']:
            st.markdown(f"<code>{fail}</code>", unsafe_allow_html=True)
    else:
        st.success("SPF/DMARC checks appear clean.")

# Report export section
if report_data:
    st.markdown("---")
    st.subheader("Download Report")

    report_json = json.dumps(report_data, indent=2)
    st.download_button("Download as JSON", data=report_json, file_name="phishkiller_report.json")

    report_txt = "\n".join([f"{k}: {v}" for k, v in report_data.items()])
    st.download_button("Download as TXT", data=report_txt, file_name="phishkiller_report.txt")

st.markdown("---")
st.markdown("`> _`", unsafe_allow_html=True)
st.caption("Built by Nessa Kodo")
