import streamlit as st
from utils.bird_data import bird_database


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Bird Library | BirdScope",
    page_icon="📚",
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
    font-size: 35px;
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

/* Bird card headings */
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
# HELPER FUNCTION
# =====================================================

def get_value(data, *keys, default="Not available"):

    for key in keys:

        value = data.get(key)

        if value is not None and value != "":
            return value

    return default


def format_list(value):

    if isinstance(value, list):
        return value

    if isinstance(value, str):
        return [value]

    return []


# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="page-header">
    <h1>📚 Explore the Bird Library</h1>
    <p>
        Discover different birds, explore their characteristics
        and learn about their habitats, diets and interesting facts.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# LOAD BIRD DATABASE
# =====================================================

if isinstance(bird_database, dict):

    birds = []

    for key, value in bird_database.items():

        if isinstance(value, dict):

            bird = value.copy()

            bird.setdefault("name", str(key))

            birds.append(bird)

elif isinstance(bird_database, list):

    birds = [
        bird for bird in bird_database
        if isinstance(bird, dict)
    ]

else:

    birds = []


total_birds = len(birds)

habitats = sorted(set(
    str(bird.get("habitat"))
    for bird in birds
    if bird.get("habitat")
    and bird.get("habitat") != "Not available"
))


# =====================================================
# LIBRARY STATISTICS
# =====================================================

st.markdown(
    '<div class="section-title">Library Overview</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Total Bird Entries",
        total_birds
    )

with col2:

    st.metric(
        "Available Habitats",
        len(habitats)
    )


# =====================================================
# SEARCH AND FILTER
# =====================================================

st.divider()

st.markdown(
    '<div class="section-title">Find a Bird</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])

with col1:

    search_query = st.text_input(
        "Search Birds",
        placeholder="Search by bird name or scientific name..."
    )

with col2:

    selected_habitat = st.selectbox(
        "Filter by Habitat",
        ["All Habitats"] + habitats
    )


# =====================================================
# FILTER BIRDS
# =====================================================

filtered_birds = []

for bird in birds:

    name = str(
        get_value(bird, "name", "common_name", "bird_name")
    )

    scientific_name = str(
        get_value(bird, "scientific_name")
    )

    description = str(
        get_value(bird, "description")
    )

    habitat = str(
        get_value(bird, "habitat")
    )

    search_text = search_query.lower().strip()

    matches_search = (
        search_text in name.lower()
        or search_text in scientific_name.lower()
        or search_text in description.lower()
    )

    matches_habitat = (
        selected_habitat == "All Habitats"
        or selected_habitat == habitat
    )

    if matches_search and matches_habitat:

        filtered_birds.append(bird)


# =====================================================
# DISPLAY BIRD CARDS
# =====================================================

st.divider()

st.markdown(
    '<div class="section-title">Bird Collection</div>',
    unsafe_allow_html=True
)

st.caption(
    f"Showing {len(filtered_birds)} of {total_birds} bird entries."
)


if filtered_birds:

    for i in range(0, len(filtered_birds), 2):

        cols = st.columns(2)

        for col, bird in zip(cols, filtered_birds[i:i + 2]):

            with col:

                name = get_value(
                    bird,
                    "name",
                    "common_name",
                    "bird_name"
                )

                scientific_name = get_value(
                    bird,
                    "scientific_name"
                )

                description = get_value(
                    bird,
                    "description"
                )

                habitat = get_value(
                    bird,
                    "habitat"
                )

                diet = get_value(
                    bird,
                    "diet"
                )

                lifespan = get_value(
                    bird,
                    "lifespan"
                )

                facts = format_list(
                    bird.get("facts", [])
                )

                with st.container(border=True):

                    st.subheader(f"🐦 {name}")

                    st.caption(scientific_name)

                    st.write(description)

                    st.markdown("**Habitat**")

                    st.write(habitat)

                    with st.expander("Explore More Information"):

                        st.markdown("**Diet**")

                        st.write(diet)

                        st.markdown("**Lifespan**")

                        st.write(lifespan)

                        if facts:

                            st.markdown("**Interesting Facts**")

                            for fact in facts:

                                st.write(f"• {fact}")


else:

    st.warning(
        "No birds found. Try changing your search or habitat filter."
    )


# =====================================================
# ABOUT THE LIBRARY
# =====================================================

st.divider()

st.markdown(
    '<div class="section-title">About the Bird Library</div>',
    unsafe_allow_html=True
)

st.write("""
The Bird Library provides a searchable collection of bird
information available within BirdScope.

Users can explore common names, scientific names, habitats,
diets and other available information.

The collection can be expanded by adding more verified
bird entries to the project's bird database.
""")


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">
    🐦 BirdScope | Bird Library
    <br>
    Explore. Identify. Learn.
</div>
""", unsafe_allow_html=True)