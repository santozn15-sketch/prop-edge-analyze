📈 Odds Analyzer
Overview
The Odds Analyzer is a Streamlit web application designed to help analyze betting odds. It currently provides functionalities to convert American odds to implied probabilities and remove the sportsbook's 'vig' (juice) to reveal true probabilities. Future enhancements will include data pulling from various sources to estimate true probabilities for events.

Features
Home Tab: An introductory section for the application.
Odds Conversion: Converts American odds to implied probabilities.
No-Vig Calculator: Automatically removes the sportsbook's vig to show fair probabilities.
True Probability (Work In Progress): A placeholder section for future development to integrate data fetching and predictive modeling for true probabilities.
Setup and Local Development
To run this application on your local machine, follow these steps:

Save the files: Save app.py and requirements.txt into a folder named odds_analyzer.

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run the Streamlit application:

streamlit run app.py
The application will open in your web browser, typically at http://localhost:8501.
