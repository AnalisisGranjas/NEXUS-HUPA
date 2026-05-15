import streamlit as st
import base64

# 1. Configuración de la Página (Modo ancho e icono de pestaña)
st.set_page_config(
    page_title="HUPA | Nexus Central", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Estilos CSS: Responsivo, Reflejo (Glassmorphism) y Títulos Blancos
def apply_styles():
    try:
        with open("fondo.jpg", "rb") as f:
            bin_str = base64.b64encode(f.read()).decode()
        bg_style = f'background-image: url("data:image/jpeg;base64,{bin_str}");'
    except:
        bg_style = 'background-color: #0e1117;'

    st.markdown(f'''
    <style>
    /* Fondo con overlay oscuro para asegurar contraste */
    .stApp {{ 
        {bg_style} 
        background-size: cover; 
        background-position: center;
        background-attachment: fixed; 
    }}
    .stApp::before {{ 
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
        background: rgba(0, 0, 0, 0.65); z-index: -1; 
    }}
    
    /* Títulos de los bloques en BLANCO y centrados */
    .block-header {{
        color: white !important; font-family: 'Segoe UI', Arial, sans-serif; 
        font-weight: bold; font-size: 1.2rem; text-align: center; 
        margin: 35px 0 15px 0; border-bottom: 2px solid #FF6700; padding-bottom: 8px;
    }}

    /* Estilo del Cuadro con Efecto Reflejo */
    .module-card {{
        background: rgba(255, 255, 255, 0.1); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px);
        border-radius: 15px; 
        padding: 15px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.15); 
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        height: 150px; 
        text-align: center; margin-bottom: 5px;
    }}
    
    .module-emoji {{ font-size: 2.3rem; margin-bottom: 5px; }}
    
    .module-title {{ 
        font-weight: 700; font-size: 0.85rem; color: white !important; 
        margin-bottom: 10px; height: 35px; display: flex; 
        align-items: center; justify-content: center;
        text-transform: uppercase;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}
    
    /* Botón IR centrado y óptimo para móvil */
    div.stLinkButton > a {{
        background: #FF6700 !important; color: white !important; border: none !important;
        padding: 6px 0 !important; border-radius: 10px !important; font-weight: bold !important;
        text-transform: uppercase; font-size: 0.75rem !important; width: 100% !important;
        display: block !important; transition: 0.3s ease;
    }}
    
    div.stLinkButton > a:hover {{
        background: #e65c00 !important;
        transform: translateY(-2px);
    }}
    
    /* Compactar espacios en vistas móviles */
    [data-testid="stVerticalBlock"] {{ gap: 0.4rem; }}
    </style>
    ''', unsafe_allow_html=True)

apply_styles()

# 3. Cabecera (Logo pequeño y títulos principales)
c_l, c_c, c_r = st.columns([1, 2, 1])
with c_c:
    try:
        st.image("logo.png", width=75) 
    except:
        pass
    st.markdown("<h2 style='text-align: center; color: white; margin:0; font-family: sans-serif;'>Nexus Central</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF6700; font-weight: bold; font-size: 0.9rem; margin-top: -5px;'>Terminal HUPA</p>", unsafe_allow_html=True)

# Función constructora de tarjetas
def create_module(emoji, title, url):
    st.markdown(f'''
    <div class="module-card">
        <div class="module-emoji">{emoji}</div>
        <div class="module-title">{title}</div>
    </div>
    ''', unsafe_allow_html=True)
    st.link_button("IR", url, use_container_width=True)

# --- BLOQUE 1: DATOS Y ANÁLISIS ---
st.markdown('<div class="block-header">📊 DATOS Y ANÁLISIS</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1: create_module("📈", "ANALYST", "https://hupa-analytics.streamlit.app/")
with c1: create_module("🧬", "AVITRACK", "https://avitrack-hupa.streamlit.app/")
with c2: create_module("🔎", "AUDITORÍA", "https://docs.google.com/spreadsheets/d/1GdLtWeDm3ZNR6bUIGmwUQ-T88ijRL8Mfx7IeSAwmjKw/edit")
with c2: create_module("🥚", "CLASIFICADORA", "https://datastudio.google.com/s/uVAocctkKGc")

# --- BLOQUE 2: INVENTARIOS Y MP ---
st.markdown('<div class="block-header">📦 INVENTARIOS Y MP</div>', unsafe_allow_html=True)
c3, c4 = st.columns(2)
with c3: create_module("🏭", "BODEGA UBATÉ", "https://docs.google.com/spreadsheets/d/1urfuUHv_x7kpfMgvsT37kOzBWQnSaBVaH_y-2_fafmA/edit")
with c3: create_module("🏢", "BODEGA BOGOTÁ", "https://docs.google.com/spreadsheets/d/1eJ4jekTfKdrsibOUR-vZhX5_ZXDutfH0xWOw5VorUEw/edit")
with c4: create_module("🚛", "TRÁNSITOS MP", "https://docs.google.com/spreadsheets/d/1XctekGprci0IGlaO55yCbNOIG6a1e-vEgedaiVY6XKY/edit")
with c4: create_module("🔄", "MOVIMIENTO MP", "https://docs.google.com/spreadsheets/d/1bHeSSpu5hoFSWeeyH0nFSJaEH6kxPXtZ0IwwGUp3WXg/edit")

# --- BLOQUE 3: LOGÍSTICA ---
st.markdown('<div class="block-header">🚚 LOGÍSTICA</div>', unsafe_allow_html=True)
c5, c6 = st.columns(2)
with c5: create_module("🛰️", "GPS DETEKTOR", "https://co.skytrack.detektorgps.com/gps_co/framework/modulos/Aplicaciones/EnlaceTemporalMonitoreo/EnlaceExterno/temporalLink.php?token=ysq3y3yth7yimfs76zl8ipyyy4953jp9enj72vi6c06")
with c5: create_module("📅", "REP. SEMANAL", "https://datastudio.google.com/s/nIo_bZI6RVg")
with c6: create_module("📊", "REP. MENSUAL", "https://datastudio.google.com/s/s6qgI5n-PXw")
with c6: create_module("📍", "UBICACIONES GRANJAS Y PLANTAS", "https://www.google.com/maps/d/viewer?mid=15cF8OaX119db-LHJjYFqMT0piiYh-Qo&ll=4.7635066770938135%2C-73.43158572048611&z=9")

# Pie de página responsivo
st.markdown("<br><center><p style='color: rgba(255,255,255,0.4); font-size: 0.7rem;'>HUPA Nexus System v2.8</p></center>", unsafe_allow_html=True)