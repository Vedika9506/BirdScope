import streamlit as st
import hashlib
from PIL import Image

from utils.classifier import classify_bird
from utils.bird_data import get_bird_info
from utils.history import save_classification


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Identify Bird | BirdScope",
    page_icon="🔍",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

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

    /* General text colour */
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp div,
    .stApp li {
        color: #000000;
    }

    /* Keep header text white */
    .page-header {
        background: linear-gradient(120deg, #123f35, #26745d);
        padding: 35px;
        border-radius: 16px;
        margin-bottom: 25px;
    }

    .page-header h1 {
        color: white !important;
        font-size: 36px;
    }

    .page-header p {
        color: #ffffff !important;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Section headings */
    .section-title {
        color: #164e43 !important;
        font-size: 24px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* Captions */
    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p {
        color: #000000 !important;
    }

    /* Uploaded image container */
    .image-card {
        background: white;
        border: 1px solid #e3ebe6;
        border-radius: 14px;
        padding: 20px;
    }

    /* Result card */
    .result-card {
        background: white;
        border: 1px solid #e3ebe6;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 15px;
    }

    .result-card h2,
    .result-card h3 {
        color: #164e43 !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #000000 !important;
        padding: 25px 0;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- PAGE HEADER ----------------

st.markdown("""
<div class="page-header">
    <h1>🔍 Identify a Bird</h1>
    <p>
        Upload a bird photograph and let BirdScope analyse
        the image to predict its species.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- IMAGE UPLOAD ----------------

st.markdown(
    '<div class="section-title">Upload Bird Image</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose a bird image",
    type=["jpg", "jpeg", "png"],
    help="Upload a clear photograph of a bird."
)


if uploaded_file is not None:

    image_bytes = uploaded_file.getvalue()

    image_id = hashlib.md5(image_bytes).hexdigest()

    image = Image.open(uploaded_file)

    # Reset previous results when a different image is uploaded
    if st.session_state.get("bird_image_id") != image_id:

        st.session_state["bird_image_id"] = image_id
        st.session_state.pop("bird_result", None)

    col1, col2 = st.columns([1, 1])

    with col1:

        st.markdown("### Uploaded Image")

        st.image(
            image,
            caption=uploaded_file.name,
            use_container_width=True
        )

        st.caption(
            f"Image size: {image.size[0]} × {image.size[1]} pixels"
        )

    with col2:

        st.markdown("### Image Details")

        st.write(f"**Filename:** {uploaded_file.name}")

        st.write(f"**Format:** {image.format or 'Unknown'}")

        st.write(f"**Dimensions:** {image.size[0]} × {image.size[1]}")

        st.write(f"**Colour Mode:** {image.mode}")

    st.divider()

    # ---------------- CLASSIFICATION BUTTON ----------------

    if st.button(
        "🔍 Identify Bird",
        type="primary",
        use_container_width=True
    ):

        try:

            with st.spinner("Analysing image... Please wait."):

                predictions = classify_bird(image)

                if not predictions:

                    st.error("No predictions were returned by the model.")

                    st.stop()

                best_prediction = predictions[0]

                bird_name = best_prediction["label"]

                confidence = float(best_prediction["score"])

                bird_info = get_bird_info(bird_name)

                scientific_name = (
                    bird_info.get("scientific_name", "Unknown")
                    if bird_info
                    else "Not available"
                )

                # Save classification record
                save_classification(
                    bird_name=bird_name,
                    confidence=confidence,
                    image_name=uploaded_file.name,
                    predictions=predictions,
                    scientific_name=scientific_name
                )

                st.session_state["bird_result"] = {
                    "bird_name": bird_name,
                    "confidence": confidence,
                    "predictions": predictions,
                    "bird_info": bird_info
                }

        except Exception as error:

            st.error(
                f"Classification failed: {error}"
            )


    # ---------------- CLASSIFICATION RESULTS ----------------

    result = st.session_state.get("bird_result")

    if result and st.session_state.get("bird_image_id") == image_id:

        st.divider()

        st.markdown(
            '<div class="section-title">Classification Results</div>',
            unsafe_allow_html=True
        )

        bird_name = result["bird_name"]

        confidence = result["confidence"]

        bird_info = result["bird_info"]

        predictions = result["predictions"]

        st.success("Bird identification completed successfully!")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"## 🐦 {bird_name}"
            )

            st.metric(
                "Prediction Confidence",
                f"{confidence * 100:.2f}%"
            )

        with col2:

            scientific_name = (
                bird_info.get("scientific_name", "Not available")
                if bird_info
                else "Not available"
            )

            st.markdown("### Scientific Name")

            st.write(scientific_name)

        # ---------------- BIRD INFORMATION ----------------

        if bird_info:

            st.divider()

            st.markdown(
                '<div class="section-title">About This Bird</div>',
                unsafe_allow_html=True
            )

            st.write(
                bird_info.get(
                    "description",
                    "No description available."
                )
            )

            info1, info2, info3 = st.columns(3)

            with info1:

                st.markdown("**Habitat**")

                st.write(
                    bird_info.get("habitat", "Not available")
                )

            with info2:

                st.markdown("**Diet**")

                st.write(
                    bird_info.get("diet", "Not available")
                )

            with info3:

                st.markdown("**Lifespan**")

                st.write(
                    bird_info.get("lifespan", "Not available")
                )

            facts = bird_info.get("facts", [])

            if facts:

                st.markdown("### Interesting Facts")

                for fact in facts:

                    st.write(f"• {fact}")

        else:

            st.info(
                "Additional information for this prediction "
                "is not available in the bird database."
            )

        # ---------------- TOP PREDICTIONS ----------------

        st.divider()

        st.markdown(
            '<div class="section-title">Top 5 Predictions</div>',
            unsafe_allow_html=True
        )

        for prediction in predictions:

            label = prediction["label"]

            score = float(prediction["score"])

            percentage = score * 100

            st.write(
                f"**{label}** — {percentage:.2f}%"
            )

            st.progress(
                min(max(score, 0), 1)
            )


else:

    st.info(
        "Upload a bird photograph to begin identification."
    )


# ---------------- FOOTER ----------------

st.divider()

st.markdown("""
<div class="footer">
    🐦 BirdScope | Bird Classification & Identification
    <br>
    Explore. Identify. Learn.
</div>
""", unsafe_allow_html=True)