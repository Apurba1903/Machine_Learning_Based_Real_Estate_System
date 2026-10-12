import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Predictor",
    page_icon="🏙️",
    layout="wide"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        
        .hero {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            padding: 3.5rem 2.5rem;
            border-radius: 16px;
            margin-bottom: 2.5rem;
            color: white;
        }
        .hero h1 { font-size: 2.6rem; font-weight: 700; margin: 0 0 0.5rem 0; letter-spacing: -0.5px; }
        .hero p  { font-size: 1.1rem; color: #a8c0cc; margin: 0; font-weight: 300; }

        .stat-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.4rem 1.6rem;
            text-align: center;
        }
        .stat-num  { font-size: 2rem; font-weight: 700; color: #0f2027; }
        .stat-label{ font-size: 0.82rem; color: #64748b; margin-top: 4px; font-weight: 500; }

        /* Fix: bright text so it shows on both light and dark Streamlit themes */
        .section-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #e2e8f0;
            margin: 2rem 0 1rem 0;
            border-left: 4px solid #38bdf8;
            padding-left: 0.75rem;
        }

        /* Fix: equal height cards using flex */
        .steps-row {
            display: flex;
            gap: 1rem;
        }
        .step-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.2rem 1.4rem;
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        .step-num  { font-size: 0.75rem; font-weight: 600; color: #2c5364; letter-spacing: 1px; margin-bottom: 6px; }
        .step-title{ font-size: 1rem; font-weight: 600; color: #0f2027; margin-bottom: 4px; }
        .step-desc { font-size: 0.875rem; color: #64748b; line-height: 1.5; flex-grow: 1; }

        .info-boxes {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        .info-box {
            background: #f0f7fb;
            border-left: 4px solid #2c5364;
            border-radius: 0 10px 10px 0;
            padding: 1rem 1.2rem;
            font-size: 0.9rem;
            color: #334155;
            line-height: 1.6;
            flex: 1;
        }

        /* Fix: all pills on one line, wrapping naturally */
        .tech-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 0.5rem;
        }
        .tech-pill {
            background: #e8f4f8;
            color: #2c5364;
            border-radius: 20px;
            padding: 5px 16px;
            font-size: 0.82rem;
            font-weight: 500;
            white-space: nowrap;
        }

        .footer {
            text-align: center;
            color: #94a3b8;
            font-size: 0.8rem;
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid #e2e8f0;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero ---
st.markdown("""
<div class="hero">
    <h1>🏙️ Gurgaon Real Estate Predictor</h1>
    <p>Machine learning-powered property price estimation for Gurgaon, India</p>
</div>
""", unsafe_allow_html=True)

# --- Stats ---
c1, c2, c3, c4 = st.columns(4)
for col, num, label in zip(
    [c1, c2, c3, c4],
    ["3,600+", "12", "90%+", "50+"],
    ["Properties in Dataset", "ML Models Evaluated", "Best Model R² Score", "Sectors Covered"]
):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div>
        </div>""", unsafe_allow_html=True)

# --- How It Works --- (rendered as one HTML block so flex works)
st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
st.markdown("""
<div class="steps-row">
    <div class="step-card">
        <div class="step-num">STEP 1</div>
        <div class="step-title">Data Collection</div>
        <div class="step-desc">Scraped 3,600+ listings from 99acres covering Gurgaon's residential market.</div>
    </div>
    <div class="step-card">
        <div class="step-num">STEP 2</div>
        <div class="step-title">Cleaning & Engineering</div>
        <div class="step-desc">Handled missing values, encoded localities, extracted area types and furnishing details.</div>
    </div>
    <div class="step-card">
        <div class="step-num">STEP 3</div>
        <div class="step-title">Model Training</div>
        <div class="step-desc">Evaluated 12 algorithms with 10-fold cross-validation. Random Forest & XGBoost led the pack.</div>
    </div>
    <div class="step-card">
        <div class="step-num">STEP 4</div>
        <div class="step-title">Price Prediction</div>
        <div class="step-desc">Enter property details and get an estimated price range in seconds.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Features Used ---
st.markdown('<div class="section-title">Features Used in Prediction</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-boxes">
    <div class="info-box">
        <b>Property Attributes</b><br>
        Property type · Sector/locality · Bedrooms · Bathrooms · Balconies ·
        Built-up area · Servant room · Store room · Furnishing type ·
        Floor category · Luxury category · Age of possession
    </div>
    <div class="info-box">
        <b>Engineered Features</b><br>
        Log-transformed price target · Label-encoded sectors ·
        Ordinal-encoded age categories · Area normalized to sq.ft ·
        Furnishing count extracted from raw text · Luxury score derived
        from amenities data
    </div>
</div>
""", unsafe_allow_html=True)

# --- Tech Stack ---
st.markdown('<div class="section-title">Tech Stack</div>', unsafe_allow_html=True)
techs = ["Python", "Pandas", "Scikit-learn", "XGBoost", "Streamlit",
         "BeautifulSoup", "Matplotlib", "Seaborn", "NumPy"]
pills_html = "".join(f'<span class="tech-pill">{t}</span>' for t in techs)
st.markdown(f'<div class="tech-pills">{pills_html}</div>', unsafe_allow_html=True)

# --- Nav hint ---
st.markdown("<br>", unsafe_allow_html=True)
st.info("👈 Use the sidebar to navigate to **Price Predictor** or **Analysis App**")

st.markdown('<div class="footer">Built by Apurba · Gurgaon Real Estate ML System</div>', unsafe_allow_html=True)