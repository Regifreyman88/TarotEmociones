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
    st.image("Portada.png", use_container_width
