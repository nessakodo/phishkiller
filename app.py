# app.py - Streamlit interface for PhishKiller
# Created by Nessa Kodo

import streamlit as st
from analyzer import analyze_url, analyze_header_text
import json

# -- Page Setup --
st.set_page_config(page_title="PhishKiller", layout="centered")

st.title("PhishKiller - Phishing Threat Analyzer")
st.markdown("""
Analyze suspicious URLs and email headers to detect phishing threats. 
Upload a raw header file or enter a URL below.
""")

report_data = {}

# -- URL Analysis Section --
st.header("URL Analysis")
url_input = st.text_input("Enter a suspicious URL")

if url_input:
    st.write("Analyzing...")
    result = analyze_url(url_input)
    st.success(result)
    report_data['url'] = url_input
    report_data['url_analysis'] = result

st.markdown("---")

# -- Email Header File Upload Section --
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
    st.code(", ".join(results['ips']) or "None")

    if results['spf_dmarc_failures']:
        st.subheader("SPF/DMARC Failures")
        for fail in results['spf_dmarc_failures']:
            st.error(fail)
    else:
        st.success("SPF/DMARC checks appear clean.")

# -- Export Button for Analysis Report --
if report_data:
    st.markdown("---")
    st.subheader("📁 Download Report")
    
    # Download as JSON
    report_json = json.dumps(report_data, indent=2)
    st.download_button("Download as JSON", data=report_json, file_name="phishkiller_report.json")

    # Download as TXT
    report_txt = "\n".join([f"{k}: {v}" for k, v in report_data.items()])
    st.download_button("Download as TXT", data=report_txt, file_name="phishkiller_report.txt")

st.markdown("---")
st.caption("Built by Nessa Kodo")
