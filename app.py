import streamlit as st
import random

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Tarot de las Emociones",
    page_icon="🔮",
    layout="wide"
)

# --- 1. Definición de los Mazos de Cartas ---
# Basado en los nombres de tus archivos de imagen.

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
    {"titulo": "Valentía", "imagen": "valenta.png"}, # Nota: el archivo se llama 'valenta.png'
    {"titulo": "Vergüenza", "imagen": "verguenza.png"},
]


# --- 2. Diseño de la Interfaz con Streamlit ---

# Título de la aplicación
st.title("🔮 Tarot de las Emociones")
st.write("Una herramienta de arteterapia para la reflexión. Haz clic para sacar una carta.")

# Portada (opcional, pero se ve genial)
# Asegúrate de que el archivo 'Portada.png' esté subido.
try:
   st.image(st.session_state.arquetipo_elegido["imagen"], use_container_width=True)
except Exception:
    st.info("Sube un archivo llamado 'Portada.png' para mostrar una imagen de bienvenida.")

st.markdown("---")

# Botón para sacar una carta
if st.button("Revelar una Emoción"):
    # Elige una carta al azar del mazo
    carta_seleccionada = random.choice(mazo_emociones)
    # Guarda la carta seleccionada en el estado de la sesión para que no se pierda
    st.session_state.carta_actual = carta_seleccionada

# --- 3. Mostrar la Carta Seleccionada ---
# Si ya se ha sacado una carta, muéstrala.
if 'carta_actual' in st.session_state:
    carta = st.session_state.carta_actual
    
    # Contenedor para la carta con un borde
    with st.container(border=True):
        # Mostrar el título de la carta
        st.subheader(carta["titulo"])
        
        # Mostrar la imagen
        try:
            st.image(carta["imagen"], use_column_width=True)
        except Exception:
            st.error(f"Error: No se encontró la imagen '{carta['imagen']}'. Asegúrate de que el archivo esté subido y el nombre sea correcto.")
