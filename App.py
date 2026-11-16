import streamlit as st
from pathlib import Path

from utils.history import load_history
from utils.bird_data import bird_database


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="BirdScope | Bird Classification",
    page_icon="🐦",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #f5f8f6;
    color: #000000;
}

/* Page spacing */
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

/* General text colour */
.stApp p,
.stApp label,
.stApp li,
.stApp [data-testid="stCaptionContainer"] {
    color: #000000 !important;
}

/* Hero section */
.st-key-hero_section {
    background: linear-gradient(120deg, #123f35, #26745d);
    padding: 35px 45px;
    border-radius: 20px;
    margin-bottom: 25px;
}

/* Hero heading */
.st-key-hero_section h1 {
    color: #ffffff !important;
    font-size: 38px !important;
}

/* Hero description */
.st-key-hero_section p {
    color: #ffffff !important;
    font-size: 17px !important;
    line-height: 1.7;
}

/* Section headings */
.section-heading {
    color: #164e43;
    font-size: 25px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Feature cards */
.feature-card {
    background-color: #ffffff;
    border: 1px solid #dce7e1;
    border-radius: 14px;
    padding: 20px;
    min-height: 155px;
}

/* Feature card headings */
.feature-card h3 {
    color: #164e43;
    font-size: 19px;
}

/* Feature card descriptions */
.feature-card p {
    color: #000000;
    font-size: 14px;
    line-height: 1.6;
}

/* Metric labels */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p,
[data-testid="stMetricValue"] {
    color: #000000 !important;
}

/* Captions */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    color: #000000 !important;
}

/* Footer */
.footer-text {
    text-align: center;
    color: #000000;
    padding: 20px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD DATA
# =====================================================

history = load_history()

if not isinstance(history, list):
    history = []

total_identifications = len(history)

unique_birds = len(set(
    record.get("bird_name", "")
    for record in history
    if record.get("bird_name")
))

total_birds = len(bird_database)


# =====================================================
# HERO SECTION
# =====================================================

with st.container(key="hero_section"):

    st.title("Discover the World of Birds 🦩")

    st.write(
        "Explore bird species, identify birds through photographs, "
        "and learn about their habitats, characteristics and "
        "fascinating facts using artificial intelligence."
    )


# =====================================================
# DASHBOARD OVERVIEW
# =====================================================

st.markdown(
    '<p class="section-heading">Dashboard Overview</p>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Identifications",
        value=total_identifications
    )

with col2:
    st.metric(
        label="Unique Predicted Labels",
        value=unique_birds
    )

with col3:
    st.metric(
        label="Birds in Library",
        value=total_birds
    )


# =====================================================
# PAGE NAVIGATION
# =====================================================

st.divider()

st.markdown(
    '<p class="section-heading">Explore BirdScope</p>',
    unsafe_allow_html=True
)

pages = [
    {
        "title": "🔍 Identify a Bird",
        "description": (
            "Upload a bird photograph and use artificial "
            "intelligence to predict its label."
        ),
        "path": "pages/Identify_Bird.py",
        "button": "Start Identification"
    },
    {
        "title": "📚 Bird Library",
        "description": (
            "Explore bird information, scientific names, "
            "habitats and interesting facts."
        ),
        "path": "pages/Bird_Library.py",
        "button": "Explore Bird Library"
    },
    {
        "title": "🕒 Classification History",
        "description": (
            "Review previous identifications and "
            "their prediction scores."
        ),
        "path": "pages/Classification_history.py",
        "button": "View History"
    },
    {
        "title": "ℹ️ About BirdScope",
        "description": (
            "Learn about the project's objectives, "
            "technologies and working methodology."
        ),
        "path": "pages/About.py",
        "button": "Learn More"
    }
]

col1, col2 = st.columns(2)

for index, page in enumerate(pages):

    current_col = col1 if index % 2 == 0 else col2

    with current_col:

        with st.container(border=True):

            st.subheader(page["title"])

            st.write(page["description"])

            if Path(page["path"]).is_file():

                st.page_link(
                    page["path"],
                    label=page["button"],
                    icon="➡️"
                )

            else:

                st.warning(
                    f"Page file not found: {page['path']}"
                )


# =====================================================
# RECENT IDENTIFICATIONS
# =====================================================

st.divider()

st.markdown(
    '<p class="section-heading">Recent Identifications</p>',
    unsafe_allow_html=True
)

if history:

    recent_records = history[:5]

    for record in recent_records:

        bird_name = record.get(
            "bird_name",
            "Unknown"
        )

        scientific_name = record.get(
            "scientific_name",
            "Not available"
        )

        confidence = float(
            record.get("confidence", 0)
        )

        date = record.get(
            "date",
            "Not available"
        )

        with st.container(border=True):

            col1, col2, col3 = st.columns([2, 2, 1])

            with col1:

                st.subheader(f"🐦 {bird_name}")

                st.write(scientific_name)

            with col2:

                st.caption("Identification Date")

                st.write(date)

            with col3:

                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

else:

    st.info(
        "No identifications yet. Upload your first bird image "
        "to get started."
    )


# =====================================================
# HOW IT WORKS
# =====================================================

st.divider()

st.markdown(
    '<p class="section-heading">How BirdScope Works</p>',
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3)

with step1:

    with st.container(border=True):

        st.subheader("01. Upload Image")

        st.write(
            "Select and upload a photograph of a bird."
        )


with step2:

    with st.container(border=True):

        st.subheader("02. AI Classification")

        st.write(
            "The pretrained deep learning model "
            "analyses the uploaded image."
        )


with step3:

    with st.container(border=True):

        st.subheader("03. View Results")

        st.write(
            "Explore the predicted label, confidence "
            "score and available bird information."
        )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown(
    """
    <div class="footer-text">
        🐦 BirdScope
        <br>
        Bird Classification & Identification
        <br>
        Explore. Identify. Learn.
    </div>
    """,
    unsafe_allow_html=True
)