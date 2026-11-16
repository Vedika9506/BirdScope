import streamlit as st
from utils.history import load_history, clear_history


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Classification History | BirdScope",
    page_icon="🕒",
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
    padding: 35px;
    border-radius: 16px;
    margin-bottom: 25px;
}

.page-header h1 {
    color: white !important;
    font-size: 34px;
}

.page-header p {
    color: white !important;
    font-size: 16px;
    line-height: 1.7;
}

/* Section headings */
.section-title {
    color: #164e43 !important;
    font-size: 24px;
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

/* Captions */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
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
    <h1>🕒 Classification History</h1>
    <p>
        Review your previous bird identifications, explore
        prediction scores and revisit classification records.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# LOAD HISTORY
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


# =====================================================
# HISTORY OVERVIEW
# =====================================================

st.markdown(
    '<div class="section-title">History Overview</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Total Identifications",
        total_identifications
    )

with col2:

    st.metric(
        "Unique Predicted Labels",
        unique_birds
    )


# =====================================================
# PREVIOUS IDENTIFICATIONS
# =====================================================

st.divider()

st.markdown(
    '<div class="section-title">Previous Identifications</div>',
    unsafe_allow_html=True
)


if not history:

    st.info(
        "No classification records found. "
        "Identify your first bird to see it here."
    )

    from pathlib import Path

    identify_page = Path("pages/Identify_Bird.py")

    if identify_page.is_file():

        st.page_link(
            "pages/Identify_Bird.py",
            label="Identify a Bird",
            icon="🔍"
        )

else:

    # Search history
    search_query = st.text_input(
        "🔍 Search History",
        placeholder="Search by bird name or scientific name..."
    )

    search_text = search_query.lower().strip()

    filtered_history = [
        record for record in history
        if (
            search_text in str(
                record.get("bird_name", "")
            ).lower()
            or search_text in str(
                record.get("scientific_name", "")
            ).lower()
        )
    ]

    st.caption(
        f"Showing {len(filtered_history)} of "
        f"{total_identifications} records."
    )

    if filtered_history:

        for record in filtered_history:

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

            image_name = record.get(
                "image_name",
                "Not available"
            )

            with st.container(border=True):

                col1, col2, col3 = st.columns([2, 2, 1])

                with col1:

                    st.subheader(f"🐦 {bird_name}")

                    st.caption(scientific_name)

                with col2:

                    st.caption("Identification Date")

                    st.write(date)

                    st.caption("Image Filename")

                    st.write(image_name)

                with col3:

                    st.metric(
                        "Confidence",
                        f"{confidence:.2f}%"
                    )

                with st.expander("View Classification Details"):

                    predictions = record.get(
                        "predictions",
                        []
                    )

                    if predictions:

                        st.markdown("**Top Predictions**")

                        for prediction in predictions:

                            label = prediction.get(
                                "label",
                                "Unknown"
                            )

                            score = float(
                                prediction.get("confidence", 0)
                            )

                            st.write(
                                f"**{label}** — {score:.2f}%"
                            )

                            st.progress(
                                min(max(score / 100, 0), 1)
                            )

                    else:

                        st.info(
                            "No prediction details available."
                        )

    else:

        st.warning(
            "No matching records found. Try another search."
        )


# =====================================================
# CLEAR HISTORY
# =====================================================

st.divider()

if history:

    st.markdown(
        '<div class="section-title">Manage History</div>',
        unsafe_allow_html=True
    )

    st.warning(
        "Clearing history will permanently delete all locally "
        "stored classification records."
    )

    if st.button(
        "🗑️ Clear All History",
        type="secondary"
    ):

        st.session_state["confirm_clear_history"] = True

    if st.session_state.get("confirm_clear_history", False):

        st.error(
            "Are you sure you want to clear all history?"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "Yes, Clear History",
                type="primary"
            ):

                clear_history()

                st.session_state["confirm_clear_history"] = False

                st.rerun()

        with col2:

            if st.button("Cancel"):

                st.session_state["confirm_clear_history"] = False

                st.rerun()


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">
    🐦 BirdScope | Classification History
    <br>
    Explore. Identify. Learn.
</div>
""", unsafe_allow_html=True)