import streamlit as st
import base64

# 1. Configuración de la Página
st.set_page_config(
    page_title="HUPA | Nexus Central", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Estilos CSS: Responsivo, Reflejo (Glass) y Títulos Blancos
def apply_styles():
    try:
        with open("fondo.jpg", "rb") as f: # Debe decir .jpg
            bin_str = base64.b64encode(f.read()).decode()
        bg_style = f'background-image: url("data:image/jpg;base64,{bin_str}");'
    except:
        bg_style = 'background-color: #000000;'

    st.markdown(f'''
    <style>
    /* Fondo con overlay oscuro para que la letra blanca resalte */
    .stApp {{ 
        {bg_style} 
        background-size: cover; 
        background-attachment: fixed; 
    }}
    .stApp::before {{ 
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
        background: rgba(0, 0, 0, 0.6); z-index: -1; 
    }}
    
    /* Títulos de los bloques en BLANCO y centrado */
    .block-header {{
        color: white; font-family: 'Segoe UI', sans-serif; 
        font-weight: bold; font-size: 1.2rem; text-align: center; 
        margin: 30px 0 15px 0; border-bottom: 2px solid #FF6700; padding-bottom: 8px;
    }}

    /* Estilo del Cuadro con Efecto Reflejo (Glassmorphism) */
    .module-card {{
        background: rgba(255, 255, 255, 0.1); /* Transparencia */
        backdrop-filter: blur(10px); /* Desenfoque de reflejo */
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px; 
        padding: 15px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.2); 
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        height: 160px; /* Cuadros más pequeños */
        text-align: center; margin-bottom: 5px;
    }}
    
    .module-emoji {{ font-size: 2.5rem; margin-bottom: 5px; }}
    
    .module-title {{ 
        font-weight: 700; font-size: 0.85rem; color: white; 
        margin-bottom: 10px; height: 40px; display: flex; 
        align-items: center; justify-content: center;
        text-transform: uppercase;
    }}
    
    /* Botón IR optimizado para móvil */
    div.stLinkButton > a {{
        background: #FF6700 !important; color: white !important; border: none !important;
        padding: 6px 0 !important; border-radius: 10px !important; font-weight: bold !important;
        text-transform: uppercase; font-size: 0.75rem !important; width: 100% !important;
        display: block !important; transition: 0.3s ease;
    }}
    
    /* Ocultar espacios innecesarios en móvil */
    [data-testid="stVerticalBlock"] {{ gap: 0.5rem; }}
    </style>
    ''', unsafe_allow_html=True)

apply_styles()

# 3. Header con Logo más pequeño
c_l, c_c, c_r = st.columns([1, 2, 1])
with c_c:
    st.image("logo.png", width=80) # Logo reducido
    st.markdown("<h2 style='text-align: center; color: white; margin:0;'>Nexus Central</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF6700; font-weight: bold; font-size: 0.9rem;'>Terminal HUPA</p>", unsafe_allow_html=True)

# Función para generar las tarjetas
def create_module(emoji, title, url):
    st.markdown(f'''
    <div class="module-card">
        <div class="module-emoji">{emoji}</div>
        <div class="module-title">{title}</div>
    </div>
    ''', unsafe_allow_html=True)
    st.link_button("IR", url, use_container_width=True)

# --- BLOQUE 1 ---
st.markdown('<div class="block-header">📊 DATOS Y ANALISIS</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2) # En móvil Streamlit apila las columnas automáticamente
with c1: create_module("📈", "ANALYST", "https://hupa-analytics.streamlit.app/")
with c1: create_module("🧬", "AVITRACK", "https://avitrack-hupa.streamlit.app/")
with c2: create_module("🔎", "AUDITORÍA", "https://docs.google.com/spreadsheets/d/1GdLtWeDm3ZNR6bUIGmwUQ-T88ijRL8Mfx7IeSAwmjKw/edit")
with c2: create_module("🥚", "CLASIFICADORA", "https://datastudio.google.com/s/uVAocctkKGc")

# --- BLOQUE 2 ---
st.markdown('<div class="block-header">📦 INVENTARIOS Y MP</div>', unsafe_allow_html=True)
c3, c4 = st.columns(2)
with c3: create_module("🏭", "BODEGA UBATÉ", "https://docs.google.com/spreadsheets/d/1urfuUHv_x7kpfMgvsT37kOzBWQnSaBVaH_y-2_fafmA/edit")
with c3: create_module("🏢", "BODEGA BOGOTÁ", "https://docs.google.com/spreadsheets/d/1eJ4jekTfKdrsibOUR-vZhX5_ZXDutfH0xWOw5VorUEw/edit")
with c4: create_module("🚛", "TRÁNSITOS MP", "https://docs.google.com/spreadsheets/d/1XctekGprci0IGlaO55yCbNOIG6a1e-vEgedaiVY6XKY/edit")
with c4: create_module("🔄", "MOVIMIENTO MP", "https://docs.google.com/spreadsheets/d/1bHeSSpu5hoFSWeeyH0nFSJaEH6kxPXtZ0IwwGUp3WXg/edit")

# --- BLOQUE 3 ---
st.markdown('<div class="block-header">🚚 LOGÍSTICA</div>', unsafe_allow_html=True)
c5, c6 = st.columns(2)
with c5: create_module("🛰️", "GPS DETEKTOR", "https://co.skytrack.detektorgps.com/gps_co/framework/modulos/Aplicaciones/EnlaceTemporalMonitoreo/EnlaceExterno/temporalLink.php?token=ysq3y3yth7yimfs76zl8ipyyy4953jp9enj72vi6c06")
with c5: create_module("📅", "REP. SEMANAL", "https://datastudio.google.com/s/nIo_bZI6RVg")
with c6: create_module("📊", "REP. MENSUAL", "https://datastudio.google.com/s/s6qgI5n-PXw")
with c6: create_module("📍", "UBICACIONES GRANJAS Y PLANTAS", "https://www.google.com/maps/d/viewer?mid=15cF8OaX119db-LHJjYFqMT0piiYh-Qo&ll=4.7635066770938135%2C-73.43158572048611&z=9")

st.markdown("<br><center><p style='color: rgba(255,255,255,0.5); font-size: 0.7rem;'>v2.8 Responsiva</p></center>", unsafe_allow_html=True)