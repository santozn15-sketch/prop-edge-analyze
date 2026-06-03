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

    # New input fields for Player Name and Prop Line
    player_name = st.text_input("Player Name (for history)", "Player A")
    prop_line = st.number_input("Prop Line (for history)", value=0.0, step=0.5)

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

            # --- INTEGRATED BETTING HISTORY LOGIC ---
            # Collect all relevant data for the current analysis
            current_analysis_data = {
                "Player Name": player_name, # Now uses the input field
                "Stat Type": "No-Vig Calculation",
                "Prop Line": prop_line, # Now uses the input field
                "Over Odds": over_odds,
                "Under Odds": under_odds,
                "Over Implied Probability": f"{over_implied_prob:.2%}",
                "Under Implied Probability": f"{under_implied_prob:.2%}",
                "No-Vig Over Probability": f"{no_vig_over_prob:.2%}",
                "No-Vig Under Probability": f"{no_vig_under_prob:.2%}",
                "Projected Hit Rate (Over)": "N/A", # Still N/A as it's not calculated here
                "Fair Odds (Over)": "N/A", # Still N/A
                "Edge (%)": "N/A", # Still N/A
                "Expected Value (Over)": "N/A", # Still N/A
                "Recommendation": "N/A", # Still N/A
                "Bankroll": "N/A", # Still N/A
                "Risk Percentage": "N/A", # Still N/A
                "Recommended Bet Size ($)": "N/A" # Still N/A
            }

            # Append the current analysis to the history
            st.session_state['betting_history'].append(current_analysis_data)

with true_probability_tab:
    st.header("True Probability (Work In Progress)")
    st.markdown("This section will be dedicated to pulling data from various sources to help determine the 'true' probability of an event.")
    st.markdown("**To implement this, you would typically:**")
    st.markdown("-   Identify specific data sources (e.g., sports statistics APIs, historical performance data websites)." )
    st.markdown("-   Use libraries like `requests` or `BeautifulSoup` to fetch and parse data.")
    st.markdown("-   Develop statistical models (e.g., regression, machine learning) to predict outcomes based on the collected data.")
    st.warning("This feature requires further development based on your specific data needs and sources.")


# --- SECTION FOR BETTING HISTORY DISPLAY AND EXPORT ---

# Initialize session state for betting history if not already present
if 'betting_history' not in st.session_state:
    st.session_state['betting_history'] = []

st.header("### 9. Betting History and Export")
st.markdown("View your past betting analyses and export them to a CSV file.")

if st.session_state['betting_history']:
    history_df = pd.DataFrame(st.session_state['betting_history'])
    st.subheader("Your Analysis History")
    st.dataframe(history_df)

    # Download button for full history
    csv_history = history_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Full History as CSV",
        data=csv_history,
        file_name="betting_history.csv",
        mime="text/csv",
        help="Download all saved betting analyses as a CSV file."
    )
else:
    st.info("No betting history yet. Perform an analysis to start building your history!")
