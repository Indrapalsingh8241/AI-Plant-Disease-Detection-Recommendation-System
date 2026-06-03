
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="AI Plant Disease Detector",
    page_icon="🌿",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.stApp{
    background-color:#030712;
}

.title{
    text-align:center;
    color:#22c55e;
    font-size:3rem;
    font-weight:700;
}

.subtitle{
    text-align:center;
    color:#9ca3af;
    font-size:1.1rem;
}

.result-card{
    padding:20px;
    border-radius:15px;
    background:#111827;
    border-left:8px solid #22c55e;
}

.support-card{
    padding:20px;
    border-radius:15px;
    background:#1e3a5f;
}

.support-title{
    color:#60a5fa;
    font-size:30px;
    font-weight:bold;
}

.plant{
    color:white;
    font-size:18px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown(
    "<div class='title'>🌿 AI Plant Disease Prediction System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Upload a leaf image and get instant disease prediction using Deep Learning</div>",
    unsafe_allow_html=True
)

st.divider()

# ==========================
# UPLOAD SECTION
# ==========================

uploaded_file = st.file_uploader(
    "📸 Upload Leaf Image",
    type=["jpg","jpeg","png"]
)

# ==========================
# IMAGE + SUPPORTED PLANTS
# ==========================

if uploaded_file:

    col1, col2 = st.columns([1,1])

    with col1:

        st.image(
            uploaded_file,
            width=420,
            caption="Uploaded Leaf"
        )

    with col2:

        st.markdown(
        """
        <div class="support-card">

        <div class="support-title">
        Supported Plants
        </div>

        <br>

        <div class="plant">🍅 Tomato</div>

        <div class="plant">🌽 Corn</div>

        <div class="plant">🍎 Apple</div>

        <div class="plant">🍇 Grape</div>

        <div class="plant">🥔 Potato</div>

        <div class="plant">🌶 Pepper</div>
        

        </div>
        """,
        unsafe_allow_html=True
        )

    st.divider()

    # ==========================
    # PREDICT BUTTON
    # ==========================

    if st.button(
        "🔍 Predict Disease",
        use_container_width=True
    ):

        with st.spinner("Analyzing image..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }

            response = requests.post(
                API_URL,
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                disease = result["disease"]
                confidence = result["confidence"]

                st.success(
                    "Prediction Completed Successfully!"
                )

                color = (
                    "#22c55e"
                    if "healthy" in disease.lower()
                    else "#ef4444"
                )
                display_name = disease.replace("_", " ").replace("___", " - ")
                st.markdown(
                f"""
                <div class="result-card">
                    <h2>🦠 Disease Detected</h2>

                   
                        {display_name}
                  
                </div>
                """,
                unsafe_allow_html=True
                )

                

                st.subheader(
                    "Confidence Score"
                )

                st.progress(
                    int(confidence)
                )

                st.metric(
                    "Confidence",
                    f"{confidence}%"
                )
                st.markdown("## 🌱 AI Recommendation")

                st.info(
                    result["recommendation"]
                    )

            else:

                st.error(
                    response.text
                )

st.divider()

st.markdown("""
### About Project

This AI-powered system uses a CNN model to detect plant diseases from leaf images.

✅ Deep Learning

✅ FastAPI Backend

✅ Streamlit Frontend

✅ Real-Time Prediction

✅ Agriculture AI Solution
""")

