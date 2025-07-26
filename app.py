import streamlit as st
import random

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Tarot de las Emociones",
    page_icon="🔮",
    layout="wide"
)

# --- 1. Definición del Mazo de Cartas ---
mazo_emociones = [
    {"titulo": "Afecto", "imagen": "afecto.png"},
    {"titulo": "Alegría", "imagen": "alegria.png"},
    {"titulo": "Ambivalencia", "imagen": "ambivalencia.png"},
    {"titulo": "Arraigo", "imagen": "arraigo.png"},
    {"titulo": "Asombro", "imagen": "asombro.png"},
    {"titulo": "Colectivo", "imagen": "colectivo.png"},
    {"titulo": "Confusión", "imagen": "confusion.png"},
    {"titulo": "Culpa", "imagen": "culpa.png"},
    {"titulo": "Curiosidad", "imagen": "curiosidad.png"},
    {"titulo": "Decisión", "imagen": "decision.png"},
    {"titulo": "Deseo", "imagen": "deseo.png"},
    {"titulo": "Duda", "imagen": "duda.png"},
    {"titulo": "Entusiasmo", "imagen": "entusiasmo.png"},
    {"titulo": "Fascinación", "imagen": "fascinacion.png"},
    {"titulo": "Frustración", "imagen": "frustracion.png"},
    {"titulo": "Miedo", "imagen": "miedo.png"},
    {"titulo": "Nostalgia", "imagen": "nostalgia.png"},
    {"titulo": "Orgullo", "imagen": "orgullo.png"},
    {"titulo": "Ternura", "imagen": "ternura.png"},
    {"titulo": "Valentía", "imagen": "valenta.png"},
    {"titulo": "Vergüenza", "imagen": "verguenza.png"},
]

# --- 2. Diseño de la Interfaz con Streamlit ---

st.title("🔮 Tarot de las Emociones")
st.write("Una herramienta de arteterapia para la reflexión. Haz clic para sacar una carta.")

# Portada
try:
    # CORRECCIÓN: Se añadió el paréntesis de cierre ')'
    st.image("Portada.png", use_container_width=True) 
except Exception:
    st.info("Sube un archivo llamado 'Portada.png' para mostrar una imagen de bienvenida.")

st.markdown("---")

# Botón para sacar una carta
if st.button("Revelar una Emoción"):
    carta_seleccionada = random.choice(mazo_emociones)
    st.session_state.carta_actual = carta_seleccionada

# --- 3. Mostrar la Carta Seleccionada ---
if 'carta_actual' in st.session_state:
    carta = st.session_state.carta_actual
    
    with st.container(border=True):
        st.subheader(carta["titulo"])
        
        try:
            st.image(carta["imagen"], use_container_width=True)
        except Exception:
            st.error(f"Error: No se encontró la imagen '{carta['imagen']}'. Asegúrate de que el archivo esté subido y el nombre sea correcto.")

# --- MÓDULO DE APOYO ---
st.sidebar.markdown("---")
st.sidebar.header("Apoya este Proyecto")
st.sidebar.write(
    """
    ¿Te ha gustado esta herramienta?
    Tu apoyo me ayuda a seguir creando y mejorando más juegos educativos como este.

    ¡Gracias por tu generosidad!
    """
)
st.sidebar.link_button("Invítame un café ☕", "https://coff.ee/regifreyman8")
