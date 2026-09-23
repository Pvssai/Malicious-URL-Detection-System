import pickle
import streamlit as st
import base64
from streamlit_option_menu import option_menu



st.set_page_config(
    page_title="Detecting Harmful Web Links Using Intelligent Machine Learning Models",
    page_icon="🌐",
    layout="wide"
)


def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/jpg;base64,{encoded}") no-repeat center center fixed;
            background-size: cover;
        }}
        .title {{
            color: #00ffea;
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            text-shadow: 2px 2px 8px black;
        }}
        .header {{
            color: #ffffff;
            font-size: 28px;
            font-weight: bold;
            text-shadow: 1px 1px 5px black;
        }}
        .text {{
            color: #ffdd55;
            font-size: 20px;
        }}
        .list-item {{
            color: #ffffff;
            font-size: 18px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_background("1.jpg")



harmful_links_model = pickle.load(open('network.sav', 'rb'))  

with st.sidebar:
    selected = option_menu(
        "🌐 Harmful Web Link Detection",
        ["🏠 Home", "🛡 URL Prediction", "📖 About", "📞 Contact"],
        icons=["house", "shield-check", "info-circle", "phone"],
        default_index=0
    )



if selected == "🏠 Home":
    st.markdown(
        "<h1 class='title'>🌐 Detecting Harmful Web Links Using Intelligent Machine Learning Models</h1>",
        unsafe_allow_html=True
    )

    st.markdown("""
    ### 🔍 Welcome!
    <span style='color:#FF0000; font-size:22px;'>
    This system intelligently analyzes URLs to identify **malicious, phishing, suspicious, or harmful web links** using advanced **Machine Learning algorithms**.
    </span>
    """, unsafe_allow_html=True)



if selected == "🛡 URL Prediction":
    st.markdown("<h1 class='header'>🛡 Harmful Web Link Prediction</h1>", unsafe_allow_html=True)

    st.markdown("### 📝 Enter URL Features Below (numeric / extracted attributes)")

    col1, col2, col3 = st.columns(3)

    
    with col1:
        url_length = st.text_input("🔗 **URL Length**")
        num_digits = st.text_input("🔢 **Number of Digits in URL**")
        num_params = st.text_input("⚙ **Number of Parameters**")
        num_fragments = st.text_input("🧩 **Fragments Count**")
        has_https = st.text_input("🔐 **HTTPS (1/0)**")
        domain_entropy = st.text_input("🌀 **Domain Entropy**")
        num_subdomains = st.text_input("📍 **Number of Subdomains**")
        is_ip = st.text_input("🌐 **Is IP Address URL (1/0)**")

    with col2:
        num_hyphens = st.text_input("➖ **Hyphens Count**")
        num_special_chars = st.text_input("✨ **Special Characters Count**")
        domain_length = st.text_input("📏 **Domain Length**")
        tld_length = st.text_input("🧩 **TLD Length**")
        num_uppercase = st.text_input("🔠 **Uppercase Letters Count**")
        num_lowercase = st.text_input("🔡 **Lowercase Letters Count**")
        url_depth = st.text_input("📚 **URL Depth**")
        suspicious_words = st.text_input("⚠ **Suspicious Words Count**")

    with col3:
        redirect_count = st.text_input("🔁 **Redirect Count**")
        shortening_service = st.text_input("✂ **Shortening Service (1/0)**")
        num_dots = st.text_input("🟣 **Dots in URL**")
        unicode_chars = st.text_input("🌈 **Unicode Characters Count**")
        abnormal_url = st.text_input("🔥 **Abnormal URL (1/0)**")
        on_mouseover = st.text_input("🖱 Hover Script (1/0)**")
        popup_activity = st.text_input("🪟 Popup Activity (1/0)**")
        last_feature = st.text_input("🔎 **Enter Missing Feature**")

  
    if st.button("🔍 **Detect Harmful Link**"):
        try:
            features = [
                url_length, num_digits, num_params, num_fragments, has_https,
                domain_entropy, num_subdomains, is_ip, num_hyphens,
                num_special_chars, domain_length, tld_length, num_uppercase,
                num_lowercase, url_depth, suspicious_words, redirect_count,
                shortening_service, num_dots, unicode_chars, abnormal_url,
                on_mouseover, popup_activity, last_feature
            ]

            # convert inputs to floats
            features = [float(i) if i.replace('.', '', 1).isdigit() else 0 for i in features]

            prediction = harmful_links_model.predict([features])

            st.success(f"🌐 **URL Classification Result: {prediction[0]}**")

        except Exception as e:
            st.error(f"⚠ **Error: {e}**")



if selected == "📖 About":
    st.markdown("<h2 class='header'>📖 About – Detecting Harmful Web Links Using Machine Learning</h2>", unsafe_allow_html=True)

    st.markdown("""
### 🌐 **Introduction**
The rise of cybercrime makes it essential to automatically detect **malicious and harmful URLs** before users access them.  
This project uses **Machine Learning algorithms** to analyze URL structures, patterns, and hidden characteristics to classify whether a link is **Safe / Suspicious / Phishing / Malware**.

### 🎯 **Purpose**
- 🔍 Identify harmful URLs in real-time  
- 🤖 Automate phishing & malware detection  
- 🛡 Prevent financial loss and data theft  
- 🚀 Improve cybersecurity using AI-driven models  

### ⭐ **Advantages**
- ✅ High detection accuracy  
- ✅ Early threat identification  
- ✅ Prevents human error in link validation  
- ✅ Lightweight + fast processing  
- ✅ Suitable for browsers, apps, and security tools  

### 📊 **Applications**
- 🌐 Web Browsers  
- 🏢 Enterprise Network Security  
- 📱 Mobile Apps  
- 🔐 Email Filtering  
- 🧑‍💻 Cyber Forensics  

### 🔐 **Conclusion**
Machine Learning–based URL classification provides **proactive protection** from phishing, malware, ransomware, and harmful sites—ensuring safer browsing for all users.
""", unsafe_allow_html=True)



st.markdown("---")
st.markdown(
    "<h4 style='color:#00ffea;'>🌐 Intelligent Harmful Link Detection System | Built with ❤️ using Streamlit</h4>",
    unsafe_allow_html=True
)
