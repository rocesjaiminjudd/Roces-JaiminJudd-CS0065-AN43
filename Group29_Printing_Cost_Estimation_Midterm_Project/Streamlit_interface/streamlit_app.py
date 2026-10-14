import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = "printing_cost_pipeline.joblib"

st.set_page_config(
    page_title="Printing Cost Estimator",
    page_icon="🖨️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f6f8fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    .hero {
        background: linear-gradient(135deg, #17324d 0%, #25636f 55%, #f2a541 100%);
        padding: 28px 32px;
        border-radius: 16px;
        color: white;
        margin-bottom: 24px;
    }

    .hero h1 {
        margin: 0;
        font-size: 2.2rem;
    }

    .hero p {
        margin-top: 8px;
        font-size: 1rem;
        opacity: 0.95;
    }

    .info-card {
        background-color: white;
        padding: 18px 20px;
        border-radius: 14px;
        border: 1px solid #e3e8ef;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
        min-height: 105px;
    }

    .info-label {
        color: #64748b;
        font-size: 0.85rem;
        margin-bottom: 4px;
    }

    .info-value {
        color: #102a43;
        font-size: 1.35rem;
        font-weight: 700;
    }

    .result-card {
        background-color: #ffffff;
        border: 1px solid #d9e2ec;
        border-left: 7px solid #f2a541;
        border-radius: 14px;
        padding: 22px 24px;
        margin-top: 8px;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
    }

    .result-title {
        color: #52606d;
        font-size: 0.95rem;
        margin-bottom: 4px;
    }

    .result-price {
        color: #17324d;
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .result-note {
        color: #52606d;
        font-size: 0.95rem;
    }

    div.stButton > button {
        background-color: #17324d;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 1.2rem;
        font-weight: 700;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #25636f;
        color: white;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except FileNotFoundError:
    st.error(
        "Model file not found. Make sure printing_cost_pipeline.joblib is in the same folder as streamlit_app.py."
    )
    st.stop()

st.markdown(
    """
    <div class="hero">
        <h1>Printing Cost Estimator</h1>
        <p>Group 29 predictive regression app for estimating total printing cost.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

summary_left, summary_mid, summary_right = st.columns(3)

with summary_left:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">Selected Model</div>
            <div class="info-value">Linear Regression</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with summary_mid:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">Output</div>
            <div class="info-value">Estimated Cost</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with summary_right:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">Dataset Size</div>
            <div class="info-value">100 Records</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

left, right = st.columns([1.2, 1])

with left:
    st.subheader("Print Job Details")

    col1, col2 = st.columns(2)

    with col1:
        pages = st.number_input(
            "Pages",
            min_value=1,
            max_value=1000,
            value=40,
            step=1,
        )

        paper_type = st.selectbox(
            "Paper type",
            ["standard", "recycled", "premium", "glossy"],
        )

        binding = st.selectbox(
            "Binding",
            ["none", "staple", "spiral", "perfect"],
        )

    with col2:
        color_pages = st.number_input(
            "Color pages",
            min_value=0,
            max_value=1000,
            value=10,
            step=1,
        )

        copies = st.number_input(
            "Number of copies",
            min_value=1,
            max_value=500,
            value=2,
            step=1,
        )

        delivery_speed = st.selectbox(
            "Delivery speed",
            ["standard", "rush"],
        )

    estimate_clicked = st.button("Estimate Printing Cost")

with right:
    st.subheader("Input Review")

    st.write(f"Pages per copy: **{pages}**")
    st.write(f"Color pages: **{color_pages}**")
    st.write(f"Copies: **{copies}**")
    st.write(f"Paper type: **{paper_type}**")
    st.write(f"Binding: **{binding}**")
    st.write(f"Delivery speed: **{delivery_speed}**")

    total_pages = pages * copies
    color_ratio = (color_pages / pages) * 100

    st.caption(f"Total printed pages: {total_pages:,}")
    st.caption(f"Color page ratio: {color_ratio:.1f}%")

st.divider()

if estimate_clicked:
    if color_pages > pages:
        st.error("Color pages cannot be greater than total pages.")
    else:
        if pages > 300 or copies > 50:
            st.warning(
                "This input is outside the main dataset range, so the estimate may be less reliable."
            )

        input_data = pd.DataFrame(
            [
                {
                    "pages": pages,
                    "color_pages": color_pages,
                    "paper_type": paper_type,
                    "copies": copies,
                    "binding": binding,
                    "delivery_speed": delivery_speed,
                }
            ]
        )

        prediction = float(model.predict(input_data)[0])

        if prediction < 0:
            st.warning(
                "The model could not produce a reliable positive estimate for "
                "this order. Please request a manual quotation."
            )
            st.stop()

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">Estimated Printing Cost</div>
                <div class="result-price">PHP {prediction:,.2f}</div>
                <div class="result-note">
                    This estimate is based on page count, color pages, paper type,
                    number of copies, binding, and delivery speed.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.info("Enter the print job details, then click Estimate Printing Cost.")
