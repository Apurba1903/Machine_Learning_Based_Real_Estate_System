import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Price Predictor", page_icon="💰", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        .page-title { font-size: 1.6rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.1rem; }
        .page-sub   { font-size: 0.88rem; color: #94a3b8; margin-bottom: 1rem; }

        .section-title {
            font-size: 0.82rem;
            font-weight: 600;
            color: #38bdf8;
            border-left: 3px solid #38bdf8;
            padding-left: 0.6rem;
            margin: 1.2rem 0 0.6rem 0;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        div[data-testid="column"] { padding: 0 0.8rem !important; }
        div[data-testid="stHorizontalBlock"] { gap: 1.2rem; margin-bottom: 0.5rem; }

        /* FIX: Make selected values clearly visible in dropdowns */
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div {
            color: #f1f5f9 !important;
            font-weight: 500 !important;
        }

        /* FIX: Number input value text */
        input[type="number"] {
            color: #f1f5f9 !important;
            font-weight: 500 !important;
            font-size: 0.95rem !important;
        }

        /* FIX: Dropdown option list text */
        li[role="option"] span {
            color: #0f172a !important;
        }

        /* FIX: Widget labels */
        label[data-testid="stWidgetLabel"] p {
            color: #cbd5e1 !important;
            font-size: 0.85rem !important;
        }

        /* Selectbox and number input background */
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div {
            background-color: #1e293b !important;
            border-color: #334155 !important;
        }

        /* Hover state on dropdown */
        div[data-baseweb="select"] > div:hover,
        div[data-baseweb="input"] > div:hover {
            border-color: #38bdf8 !important;
        }

        .result-box {
            background: linear-gradient(135deg, #0f2027, #2c5364);
            color: white; border-radius: 12px;
            padding: 1.4rem 2rem; text-align: center; margin-top: 1rem;
        }
        .result-range { font-size: 1.8rem; font-weight: 700; margin: 0.3rem 0; }
        .result-label { font-size: 0.85rem; color: #a8c0cc; }
        .result-base  { font-size: 0.9rem; color: #cbd5e1; margin-top: 0.3rem; }
    </style>
""", unsafe_allow_html=True)

# --- Load assets ---
@st.cache_resource
def load_assets():
    with open(r'C:\Users\ACER\Desktop\Projects\Machine Learning Based Real Estate System\Frontend\df.pkl', 'rb') as f:
        df = pickle.load(f)
    with open(r'C:\Users\ACER\Desktop\Projects\Machine Learning Based Real Estate System\Frontend\pipeline.pkl', 'rb') as f:
        pipeline = pickle.load(f)
    return df, pipeline

df, pipeline = load_assets()

st.markdown('<div class="page-title">💰 Property Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">Estimate residential property prices across Gurgaon sectors</div>', unsafe_allow_html=True)

# ── Row 1: Property basics ──────────────────────────────────────────────────
st.markdown('<div class="section-title">Property Basics</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    property_type = st.selectbox('Property Type', ['', 'flat', 'house'])
with c2:
    sector_options = [''] + sorted(df['sector'].unique().tolist())
    sector = st.selectbox('Sector', sector_options)
with c3:
    built_up_area = st.number_input(
        'Built-up Area (sq.ft)',
        min_value=0.0, max_value=15000.0,
        value=0.0, step=50.0,
        help="Enter area between 100 and 15,000 sq.ft"
    )

# ── Row 2: Rooms ────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Rooms</div>', unsafe_allow_html=True)
c4, c5, c6 = st.columns(3)

bedroom_options  = [''] + sorted([x for x in df['bedRoom'].unique().tolist() if 1 <= x <= 10])
bathroom_options = [''] + sorted([x for x in df['bathroom'].unique().tolist() if 1 <= x <= 10])
balcony_options  = [''] + sorted(df['balcony'].unique().tolist())

with c4:
    bedrooms_raw = st.selectbox('Bedrooms', bedroom_options)
with c5:
    bathroom_raw = st.selectbox('Bathrooms', bathroom_options)
with c6:
    balcony = st.selectbox('Balconies', balcony_options)

# ── Row 3: Additional rooms ─────────────────────────────────────────────────
st.markdown('<div class="section-title">Additional Rooms & Furnishing</div>', unsafe_allow_html=True)
c7, c8, c9 = st.columns(3)

with c7:
    servant_room = float(st.selectbox('Servant Room', [0.0, 1.0], format_func=lambda x: 'Yes' if x == 1.0 else 'No'))
with c8:
    store_room = float(st.selectbox('Store Room', [0.0, 1.0], format_func=lambda x: 'Yes' if x == 1.0 else 'No'))
with c9:
    furnishing_options = [''] + sorted(df['furnishing_type'].unique().tolist())
    furnishing_type = st.selectbox('Furnishing Type', furnishing_options)

# ── Row 4: Property profile ─────────────────────────────────────────────────
st.markdown('<div class="section-title">Property Profile</div>', unsafe_allow_html=True)
c10, c11, c12 = st.columns(3)

age_options     = [''] + sorted(df['agePossession'].unique().tolist())
luxury_options  = [''] + sorted(df['luxury_category'].unique().tolist())
floor_options   = [''] + sorted(df['floor_category'].unique().tolist())

with c10:
    property_age = st.selectbox('Property Age', age_options)
with c11:
    luxury_category = st.selectbox('Luxury Category', luxury_options)
with c12:
    floor_category = st.selectbox('Floor Category', floor_options)

# ── Predict ─────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
predict_btn = st.button('Predict Price', type='primary', use_container_width=True)

if predict_btn:
    errors = []

    # Blank field checks
    if not property_type:
        errors.append("Please select a Property Type")
    if not sector:
        errors.append("Please select a Sector")
    if built_up_area <= 0:
        errors.append("Please enter a Built-up Area greater than 0")
    if built_up_area > 15000:
        errors.append("Built-up area cannot exceed 15,000 sq.ft")
    if built_up_area > 0 and built_up_area < 100:
        errors.append("Built-up area must be at least 100 sq.ft")
    if bedrooms_raw == '':
        errors.append("Please select number of Bedrooms")
    if bathroom_raw == '':
        errors.append("Please select number of Bathrooms")
    if balcony == '':
        errors.append("Please select number of Balconies")
    if not furnishing_type:
        errors.append("Please select a Furnishing Type")
    if not property_age:
        errors.append("Please select Property Age")
    if not luxury_category:
        errors.append("Please select a Luxury Category")
    if not floor_category:
        errors.append("Please select a Floor Category")

    # Cross-field checks (only if core fields filled)
    if bedrooms_raw != '' and bathroom_raw != '':
        bedrooms = float(bedrooms_raw)
        bathroom = float(bathroom_raw)
        if bathroom > bedrooms + 2:
            errors.append(f"Unusually high bathroom count ({int(bathroom)}) for {int(bedrooms)} bedrooms — please verify")

    if errors:
        for e in errors:
            st.error(f"⚠️ {e}")
    else:
        bedrooms = float(bedrooms_raw)
        bathroom = float(bathroom_raw)

        data = [[
            property_type, sector, bedrooms, bathroom, balcony,
            property_age, built_up_area, servant_room, store_room,
            furnishing_type, luxury_category, floor_category
        ]]
        columns = [
            'property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
            'agePossession', 'built_up_area', 'servant room', 'store room',
            'furnishing_type', 'luxury_category', 'floor_category'
        ]
        one_df = pd.DataFrame(data, columns=columns)

        try:
            base_price = np.expm1(pipeline.predict(one_df))[0]
            low  = round(base_price - 0.22, 2)
            high = round(base_price + 0.22, 2)
            base = round(base_price, 2)

            st.markdown(f"""
            <div class="result-box">
                <div class="result-label">Estimated Price Range</div>
                <div class="result-range">₹ {low} Cr — ₹ {high} Cr</div>
                <div class="result-base">Base estimate: ₹ {base} Cr</div>
            </div>""", unsafe_allow_html=True)

            st.caption("Estimate based on comparable listings in the training dataset. Actual prices may vary.")

        except Exception as e:
            st.error(f"Prediction failed: {e}")