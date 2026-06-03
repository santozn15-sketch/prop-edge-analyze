import streamlit as st
import pandas as pd
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="Odds Analyzer",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Helper Functions ---
def american_to_implied(odds):
    """Converts American odds to implied probability."""
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

def remove_vig(prob_over, prob_under):
    """Removes vig from implied probabilities."""
    total_prob = prob_over + prob_under
    no_vig_over = prob_over / total_prob
    no_vig_under = prob_under / total_prob
    return no_vig_over, no_vig_under

# --- Streamlit App Layout ---
st.title("📈 Odds Analyzer")
st.markdown("Welcome to the **Odds Analyzer**! Use this tool to calculate implied probabilities and remove vig from betting odds.")

home_tab, no_vig_tab, true_probability_tab = st.tabs(["Home", "No-Vig Calculator", "True Probability (WIP)"])

with home_tab:
    st.header("Welcome Home!")
    st.markdown("This is the home tab of your application. You can add introductory content, explanations, or any other general information here.")
    st.markdown("Navigate to the 'No-Vig Calculator' tab to start analyzing odds.")

with no_vig_tab:
    st.header("No-Vig Odds Calculator")

    st.markdown("Enter the American odds for an 'Over' and 'Under' bet to calculate their implied probabilities and then remove the sportsbook's vig.")

    col1, col2 = st.columns(2)
    with col1:
        over_odds = st.number_input("Over Odds (American)", value=106, step=1, help="e.g., 106 for +106, -110 for -110")
    with col2:
        under_odds = st.number_input("Under Odds (American)", value=-134, step=1, help="e.g., 106 for +106, -110 for -110")

    if st.button("Calculate No-Vig"):
        if over_odds == 0 or under_odds == 0:
            st.error("Odds cannot be zero. Please enter valid American odds.")
        else:
            # Calculate implied probabilities
            over_implied_prob = american_to_implied(over_odds)
            under_implied_prob = american_to_implied(under_odds)

            st.subheader("Implied Probabilities")
            st.write(f"**Over Odds ({over_odds}):** {over_implied_prob:.2%} implied probability")
            st.write(f"**Under Odds ({under_odds}):** {under_implied_prob:.2%} implied probability")

            # Calculate no-vig probabilities
            no_vig_over_prob, no_vig_under_prob = remove_vig(over_implied_prob, under_implied_prob)

            st.subheader("No-Vig Probabilities")
            st.write(f"**No-Vig Over Probability:** {no_vig_over_prob:.2%}")
            st.write(f"**No-Vig Under Probability:** {no_vig_under_prob:.2%}")

            st.success("No-vig probabilities calculated successfully!")

with true_probability_tab:
    st.header("True Probability (Work In Progress)")
    st.markdown("This section will be dedicated to pulling data from various sources to help determine the 'true' probability of an event.")
    st.markdown("**To implement this, you would typically:**")
    st.markdown("-   Identify specific data sources (e.g., sports statistics APIs, historical performance data websites)." )
    st.markdown("-   Use libraries like `requests` or `BeautifulSoup` to fetch and parse data.")
    st.markdown("-   Develop statistical models (e.g., regression, machine learning) to predict outcomes based on the collected data.")
    st.warning("This feature requires further development based on your specific data needs and sources.")
