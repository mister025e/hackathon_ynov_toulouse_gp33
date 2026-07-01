import streamlit as st
import requests
import json
import time

# --- Configuration de la page ---
st.set_page_config(
    page_title="TechCorp Assistant Financier",
    page_icon="🤖",
    layout="centered"
)

# --- Custom CSS pour un design Premium ---
st.markdown("""
<style>
    /* Police personnalisée */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Arrière-plan principal avec dégradé subtil */
    .stApp {
        background: radial-gradient(circle at top right, #13111C, #000000);
        color: #E2E8F0;
    }
    
    /* Panneau latéral style Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(19, 17, 28, 0.6) !important;
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Conteneurs de messages */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 15px;
        padding: 15px;
        border: 1px solid rgba(255, 255, 255, 0.04);
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(4px);
    }
    
    /* Avatars du Chat */
    [data-testid="chatAvatarIcon-user"] {
        background-color: #2D3748;
    }
    [data-testid="chatAvatarIcon-assistant"] {
        background: linear-gradient(135deg, #00F2FE, #4FACFE);
    }
    
    /* Barre de saisie de chat */
    [data-testid="stChatInput"] {
        border-radius: 25px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        background: rgba(255, 255, 255, 0.03) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Boutons avec animation au survol */
    .stButton>button {
        background: linear-gradient(135deg, #667EEA, #764BA2) !important;
        border: none !important;
        color: white !important;
        border-radius: 8px !important;
        transition: all 0.3s ease;
        font-weight: 600;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(118, 75, 162, 0.5);
    }
    
    /* Titres (dégradés) */
    h1 {
        background: -webkit-linear-gradient(45deg, #00F2FE, #4FACFE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# --- Initialisation de l'état ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Barre latérale (Sidebar) ---
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # URL du serveur d'inférence
    st.subheader("Serveur d'inférence")
    server_url = st.text_input("URL du serveur", "http://localhost:11434")
    
    st.markdown("---")
    
    # Test de connexion
    st.subheader("Statut de connexion")
    
    @st.cache_data(ttl=5) # Cache pour éviter de surcharger le serveur
    def check_connection(url):
        try:
            # On teste la racine d'Ollama qui doit répondre "Ollama is running"
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException:
            pass
        return False

    is_connected = check_connection(server_url)
    
    if is_connected:
        st.success("✅ Connecté au serveur")
    else:
        st.error("❌ Serveur déconnecté")
        st.caption("En attente de l'équipe INFRA pour le déploiement du modèle.")

    if st.button("Effacer l'historique"):
        st.session_state.messages = []
        st.rerun()

# --- Titre Principal ---
st.title("🤖 Assistant Financier - TechCorp")
st.markdown("Posez vos questions sur la finance, les investissements, ou la gestion de budget.")

# --- Affichage de l'historique ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Fonction d'appel API Mock/Réel ---
def generate_response(prompt, url, connected):
    if not connected:
        # Fallback hors-ligne (Simulé)
        time.sleep(1) # Simuler un délai de traitement
        return "⚠️ **Mode hors-ligne** : Le serveur d'inférence n'est pas encore accessible. \n\n*Note de développement : L'interface fonctionne correctement, nous attendons le déploiement du modèle par l'équipe INFRA.*"
    
    try:
        # Appel API réel pour Ollama (basé sur l'API Generate ou Chat)
        api_url = f"{url.rstrip('/')}/api/generate"
        payload = {
            "model": "phi3.5", # Le nom défini dans le Modelfile
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(api_url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "Erreur: Pas de réponse dans la payload.")
        
    except Exception as e:
        return f"❌ **Erreur de communication avec le serveur** : {str(e)}"

# --- Saisie Utilisateur ---
if prompt := st.chat_input("Votre message..."):
    # Afficher le message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Afficher un indicateur de chargement et la réponse
    with st.chat_message("assistant"):
        with st.spinner("L'assistant réfléchit..."):
            response = generate_response(prompt, server_url, is_connected)
            st.markdown(response)
            
    # Sauvegarder la réponse dans l'historique
    st.session_state.messages.append({"role": "assistant", "content": response})
