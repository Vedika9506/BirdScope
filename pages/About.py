import streamlit as st


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="About | BirdScope",
    page_icon="ℹ️",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f8f6;
    color: #000000;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

/* General text */
.stApp p,
.stApp span,
.stApp label,
.stApp li,
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    color: #000000 !important;
}

/* Hero section */
.page-header {
    background: linear-gradient(120deg, #123f35, #26745d);
    padding: 40px;
    border-radius: 16px;
    margin-bottom: 30px;
}

.page-header h1 {
    color: white !important;
    font-size: 36px;
}

.page-header p {
    color: white !important;
    font-size: 16px;
    line-height: 1.7;
}

/* Section headings */
.section-title {
    color: #164e43 !important;
    font-size: 25px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Card headings */
.stApp h3,
.stApp h4 {
    color: #164e43 !important;
}

/* Metrics */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p,
[data-testid="stMetricValue"] {
    color: #000000 !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #000000 !important;
    padding: 25px 0;
    font-size: 13px;
}

.footer p {
    color: #000000 !important;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="page-header">
    <h1>ℹ️ About BirdScope</h1>
    <p>
        An AI-powered bird classification and identification
        platform designed to recognise birds from images and
        make bird information easily accessible.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.markdown(
    '<div class="section-title">Project Overview</div>',
    unsafe_allow_html=True
)

st.write("""
BirdScope is a bird classification and identification application
that uses a pretrained deep learning model to analyse bird
photographs and predict their labels.

The application combines image classification with a bird
information database, searchable bird library and classification
history.

Its goal is to make bird identification more accessible while
helping users explore the characteristics and diversity of birds.
""")


# =====================================================
# PROJECT OBJECTIVES
# =====================================================

st.markdown(
    '<div class="section-title">Project Objectives</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("🎯 Automated Identification")

        st.write(
            "Identify birds from uploaded photographs "
            "using a pretrained image classification model."
        )

    with st.container(border=True):

        st.subheader("📖 Knowledge and Awareness")

        st.write(
            "Provide information about bird characteristics, "
            "scientific names, habitats and diets."
        )


with col2:

    with st.container(border=True):

        st.subheader("⚡ Accessible Interface")

        st.write(
            "Provide a simple interface that allows users "
            "to upload images and explore classification results."
        )

    with st.container(border=True):

        st.subheader("🗂️ Classification Records")

        st.write(
            "Maintain a history of previous identifications "
            "and their corresponding prediction scores."
        )


# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.markdown(
    '<div class="section-title">Technology Stack</div>',
    unsafe_allow_html=True
)

tech1, tech2, tech3 = st.columns(3)

with tech1:

    with st.container(border=True):

        st.subheader("🐍 Python")

        st.write("Primary programming language.")

    with st.container(border=True):

        st.subheader("🖥️ Streamlit")

        st.write("Frontend and application interface.")

with tech2:

    with st.container(border=True):

        st.subheader("🧠 PyTorch")

        st.write("Deep learning framework.")

    with st.container(border=True):

        st.subheader("🤗 Transformers")

        st.write("Pretrained model integration.")

with tech3:

    with st.container(border=True):

        st.subheader("🖼️ Pillow")

        st.write("Image processing.")

    with st.container(border=True):

        st.subheader("📄 JSON")

        st.write("Local classification history storage.")


# =====================================================
# WORKING METHODOLOGY
# =====================================================

st.markdown(
    '<div class="section-title">How BirdScope Works</div>',
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3)

with step1:

    with st.container(border=True):

        st.subheader("01. Image Upload")

        st.write(
            "The user uploads a bird photograph "
            "through the application."
        )

with step2:

    with st.container(border=True):

        st.subheader("02. Image Classification")

        st.write(
            "The pretrained model processes the image "
            "and generates predictions."
        )

with step3:

    with st.container(border=True):

        st.subheader("03. Results and Information")

        st.write(
            "The application displays predicted labels "
            "and available bird information."
        )


# =====================================================
# KEY FEATURES
# =====================================================

st.markdown(
    '<div class="section-title">Key Features</div>',
    unsafe_allow_html=True
)

features = [
    (
        "🔍 Bird Identification",
        "Predict bird labels from uploaded images."
    ),
    (
        "📊 Prediction Scores",
        "Display the top five model predictions and their scores."
    ),
    (
        "📚 Bird Library",
        "Search and explore available bird information."
    ),
    (
        "🕒 Classification History",
        "Review previously recorded bird identifications."
    ),
    (
        "🌳 Bird Information",
        "Explore habitats, diets, scientific names and facts."
    ),
    (
        "🎨 Interactive Dashboard",
        "Navigate the application through a user-friendly interface."
    )
]

for i in range(0, len(features), 3):

    cols = st.columns(3)

    for col, feature in zip(cols, features[i:i + 3]):

        title, description = feature

        with col:

            with st.container(border=True):

                st.subheader(title)

                st.write(description)


# =====================================================
# FUTURE SCOPE
# =====================================================

st.markdown(
    '<div class="section-title">Future Scope</div>',
    unsafe_allow_html=True
)

st.write(
    "BirdScope can be further improved through the following developments:"
)

future_scope = [
    "Expand the bird database with more verified bird entries.",
    "Evaluate model performance using a labelled test dataset.",
    "Add bird photographs and visual references to the library.",
    "Introduce cloud-based storage for classification records.",
    "Support multiple users and personalised identification history.",
    "Improve classification performance and handling of non-bird images."
]

for item in future_scope:
    st.write(f"• {item}")


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">
    <h3>🐦 BirdScope</h3>
    <p>Bird Classification & Identification</p>
    <p>Built using Python, Streamlit and Deep Learning.</p>
    <p>Explore. Identify. Learn.</p>
</div>
""", unsafe_allow_html=True)