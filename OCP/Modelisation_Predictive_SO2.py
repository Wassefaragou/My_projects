import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from io import BytesIO
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError

def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #e0f7fa;  
            color: #424242;  
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #ffffff;
            background-color: #26a69a;  
            padding: 20px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  
        }
        .hr {
            border: 1px solid #ffffff;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .section-header {
            color: #26a69a;  
            font-size: 26px;
            margin-bottom: 15px;
            font-weight: bold;
            text-align: center;
        }
        .stButton > button {
            background-color: #26a69a;  
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .stButton > button:hover {
            background-color: #00796b;  
            transform: scale(1.05);
        }
        .stButton > button:focus {
            outline: none;
        }
        .stNumberInput input, .stSelectbox > div {
            background-color: #fafafa;  
            color: #424242;  
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #bdbdbd;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); 
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def calculate_results(Ds, VTs, TE_1er, TS_1er, TE_2eme, TS_2eme, TE_3eme, TS_3eme, TE_4eme, TS_4eme):
    try:
        model = load_model('prediction_SO2.h5', custom_objects={'mse': MeanSquaredError()})
        x = np.array([Ds, VTs, TE_1er, TS_1er, TE_2eme, TS_2eme, TE_3eme, TS_3eme, TE_4eme, TS_4eme])
        o = pd.DataFrame(x.reshape(1, -1))
        y = model.predict(o)
        SO2_emissions = y
        return SO2_emissions
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {str(e)}")
        return None

def process_data(df):
    required_columns = ['Ds', 'VTs', 'TE_1er', 'TS_1er', 'TE_2eme', 'TS_2eme', 'TE_3eme', 'TS_3eme', 'TE_4eme', 'TS_4eme']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        st.error(f"Les colonnes suivantes sont manquantes : {', '.join(missing_columns)}")
        return df

    try:
        with st.spinner("Prédiction des résultats en cours..."):
            model = load_model('prediction_SO2.h5', custom_objects={'mse': MeanSquaredError()})
            y = model.predict(df[required_columns])
            SO2_emissions = y

            df["Émissions de SO2 (KG/H)"] = SO2_emissions
        return df

    except Exception as e:
        st.error(f"Erreur de traitement des données : {str(e)}")
        return df

def display_table_results(df):
    st.markdown("<hr class='hr'>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>📊 Résultats</div>", unsafe_allow_html=True)
    st.write(df['Émissions de SO2 (KG/H)'])

    format_options = st.selectbox("Choisissez le format de téléchargement", options=["Excel", "CSV"])

    output = BytesIO()
    if format_options == "Excel":
        df.to_excel(output, index=False, engine='xlsxwriter')
        mime = "application/vnd.ms-excel"
        file_name = "résultats_SO2.xlsx"
    else:
        df.to_csv(output, index=False)
        mime = "text/csv"
        file_name = "résultats_SO2.csv"

    st.download_button(
        label="💾 Télécharger les résultats",
        data=output.getvalue(),
        file_name=file_name,
        mime=mime
    )

def show_home():
    st.markdown("<div class='title'>Modélisation Prédicative Avancée des Émissions de SO2 au Service 01J/S de Jorf Lasfar, OCP, à l’Aide de Réseaux de Neurones</div>", unsafe_allow_html=True)
    st.markdown("<hr class='hr'>", unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: justify; margin-top: 20px; font-size: 18px; color: #D3D3D3;'>
            Bienvenue sur notre application de modélisation prédictive pour les Émissions de SO2 à 
                l’aide de réseaux de neurones avancés.
                 Cette application vous permet de prédire les niveaux d'émission de SO2 en 
                fonction des variables d'entrée. 
                Choisissez une option dans la barre latérale pour démarrer,
                 ou explorez les sections ci-dessous pour obtenir plus d'informations.
        </p>
    """, unsafe_allow_html=True)
    st.markdown("<hr class='hr'>", unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center;'>
            <h3 style='color: #26a69a;'>Sélectionnez une option dans la barre latérale</h3>
            <p style='color: #D3D3D3;'>Choisissez entre entrer des variables individuellement ou utiliser des tables pour prédire les résultats.</p>
        </div>
    """, unsafe_allow_html=True)

def main():
    add_custom_css()

    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Choisissez une option", ["Accueil", "Prédiction avec Variables", "Prédiction avec Table"])

    if options == "Accueil":
        show_home()

    elif options == "Prédiction avec Variables":
        st.markdown("<div class='section-header'>Prédiction avec Variables</div>", unsafe_allow_html=True)
        Ds = st.number_input("Débit de la Solution (Ds)", step=0.5, min_value=0.0, help="En m³/h")
        VTs = st.number_input("Volume de Tonne de Soufre (VTs)", step=0.5, min_value=0.0, help="En tours par minute (Tr/min)")
        TE_1er = st.number_input("Température d'entrée à la 1ère masse catalytique (TE_1er)", step=0.5, min_value=-50.0, help="En °C")
        TS_1er = st.number_input("Température de sortie à la 1ère masse catalytique (TS_1er)", step=0.5, min_value=-50.0, help="En °C")
        TE_2eme = st.number_input("Température d'entrée à la 2ème masse catalytique (TE_2eme)", step=0.5, min_value=-50.0, help="En °C")
        TS_2eme = st.number_input("Température de sortie à la 2ème masse catalytique (TS_2eme)", step=0.5, min_value=-50.0, help="En °C")
        TE_3eme = st.number_input("Température d'entrée à la 3ème masse catalytique (TE_3eme)", step=0.5, min_value=-50.0, help="En °C")
        TS_3eme = st.number_input("Température de sortie à la 3ème masse catalytique (TS_3eme)", step=0.5, min_value=-50.0, help="En °C")
        TE_4eme = st.number_input("Température d'entrée à la 4ème masse catalytique (TE_4eme)", step=0.5, min_value=-50.0, help="En °C")
        TS_4eme = st.number_input("Température de sortie à la 4ème masse catalytique (TS_4eme)", step=0.5, min_value=-50.0, help="En °C")

        if st.button("Prédire"):
            SO2_emissions = calculate_results(Ds, VTs, TE_1er, TS_1er, TE_2eme, TS_2eme, TE_3eme, TS_3eme, TE_4eme, TS_4eme)
            if SO2_emissions is not None:
                st.success(f"Émissions de SO2 (KG/H) : {SO2_emissions[0][0]:.2f}")

    elif options == "Prédiction avec Table":
        st.markdown("<div class='section-header'>Prédiction avec Table</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Téléchargez votre fichier Excel/CSV", type=["xlsx", "csv"], help="""
**Les tableaux doivent inclure les variables suivantes :**  
- **Ds** : Débit de soufre  
- **VTs** : Volume de Tonne de Soufre  
- **TE_1er** : Température d'entrée à la 1ère masse catalytique (en °C)  
- **TS_1er** : Température de sortie à la 1ère masse catalytique (en °C)  
- **TE_2eme** : Température d'entrée à la 2ème masse catalytique (en °C)  
- **TS_2eme** : Température de sortie à la 2ème masse catalytique (en °C)  
- **TE_3eme** : Température d'entrée à la 3ème masse catalytique (en °C)  
- **TS_3eme** : Température de sortie à la 3ème masse catalytique (en °C)  
- **TE_4eme** : Température d'entrée à la 4ème masse catalytique (en °C)  
- **TS_4eme** : Température de sortie à la 4ème masse catalytique (en °C)
        """)

        if uploaded_file is not None:
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                df = pd.read_csv(uploaded_file)

            df = process_data(df)
            if not df.empty:
                display_table_results(df)

if __name__ == "__main__":
    main()