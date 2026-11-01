import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Portal de Notas - INCB",
    page_icon="🎓",
    layout="centered"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-header {
        text-align: center;
        color: #4B5563;
        font-size: 1.1em;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        color: white;
    }
    .card-box {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Datos de los estudiantes
ESTUDIANTES = {
    "6051262": {"nombre": "AGUILAR SANCHEZ, JOSUE ISAAC", "prep": 2.25, "ejec": 5.0, "val": 2.335, "prelim": 9.085, "final": 9.1, "nivel": 5, "pin": "2951"},
    "6051150": {"nombre": "AMAYA ANDRADE, ROSA LISBETH", "prep": 2.25, "ejec": 5.0, "val": 1.91, "prelim": 8.91, "final": 8.9, "nivel": 4, "pin": "6234"},
    "19941987": {"nombre": "AMAYA GUZMÁN, YANCY MARELY", "prep": 2.25, "ejec": 3.0, "val": 2.27, "prelim": 7.603, "final": 7.6, "nivel": 4, "pin": "9233"},
    "6051041": {"nombre": "AMAYA PINEDA, LILIAN ENEYDA", "prep": 1.75, "ejec": 3.0, "val": 2.095, "prelim": 7.178, "final": 7.2, "nivel": 4, "pin": "9385"},
    "6050391": {"nombre": "CENTENO CHICAS, ALEXANDER SALATIEL", "prep": 2.25, "ejec": 5.0, "val": 2.09, "prelim": 9.00, "final": 9.0, "nivel": 4, "pin": "2681"},
    "20040769": {"nombre": "CHICAS HERNÁNDEZ, HEYSEL DAYANARA", "prep": 1.75, "ejec": 3.0, "val": 2.095, "prelim": 7.178, "final": 7.2, "nivel": 4, "pin": "4658"},
    "1133262": {"nombre": "DEL CID OCHOA, LUZ ENEDINA", "prep": 2.25, "ejec": 3.0, "val": 2.335, "prelim": 7.685, "final": 7.7, "nivel": 4, "pin": "7891"},
    "19942150": {"nombre": "DÍAZ CHICAS, OSCAR EDUARDO", "prep": 2.25, "ejec": 3.0, "val": 1.91, "prelim": 7.00, "final": 7.0, "nivel": 4, "pin": "9975"},
    "19942151": {"nombre": "DÍAZ CHICAS, OSCAR GABRIEL", "prep": 2.25, "ejec": 3.0, "val": 2.335, "prelim": 7.785, "final": 7.8, "nivel": 4, "pin": "9042"},
    "19942187": {"nombre": "FUENTES PORTILLO, BRIANA MARIELA", "prep": 1.75, "ejec": 3.0, "val": 2.095, "prelim": 7.178, "final": 7.2, "nivel": 4, "pin": "8226"},
    "6051268": {"nombre": "GÓMEZ BONILLA, LESLY DAYANA", "prep": 1.75, "ejec": 3.0, "val": 2.095, "prelim": 7.178, "final": 7.2, "nivel": 4, "pin": "4931"},
    "5825498": {"nombre": "GUEVARA PORTILLO, ENOC BLADIMIR", "prep": 0.0, "ejec": 0.0, "val": 0.0, "prelim": 0.0, "final": 0.0, "nivel": 0, "pin": "1041"},
    "6051136": {"nombre": "GUZMÁN FRANCO, GABRIELA YAMILETH", "prep": 2.25, "ejec": 5.0, "val": 2.27, "prelim": 9.42, "final": 9.4, "nivel": 5, "pin": "2322"},
    "19942288": {"nombre": "HERNÁNDEZ CHICAS, MARLEN ESTÉFANY", "prep": 1.75, "ejec": 3.0, "val": 2.095, "prelim": 7.145, "final": 7.1, "nivel": 4, "pin": "2814"},
    "6051266": {"nombre": "LOVO BARAHONA, GUSTAVO ALEXIS", "prep": 2.25, "ejec": 3.0, "val": 2.335, "prelim": 7.985, "final": 8.0, "nivel": 4, "pin": "5706"},
    "19942412": {"nombre": "MEDRANO MEMBREÑO, JOSÉ GEOVANY", "prep": 2.25, "ejec": 3.0, "val": 2.27, "prelim": 7.62, "final": 7.6, "nivel": 4, "pin": "2606"},
    "6051215": {"nombre": "MEMBREÑO DÍAZ, NORELVI TATIANA", "prep": 2.25, "ejec": 3.0, "val": 1.91, "prelim": 7.01, "final": 7.0, "nivel": 3, "pin": "8367"},
    "19942443": {"nombre": "MONJARAS MARTÍNEZ, ASHLEY DANIELA", "prep": 1.75, "ejec": 3.0, "val": 2.095, "prelim": 7.178, "final": 7.2, "nivel": 4, "pin": "1188"},
    "20040911": {"nombre": "ORELLANA GUTIERREZ, MEILIN JULISSA", "prep": 2.25, "ejec": 5.0, "val": 1.91, "prelim": 8.91, "final": 8.9, "nivel": 4, "pin": "9032"},
    "6050388": {"nombre": "PORTILLO CENTENO, ANA SARAÍ", "prep": 1.75, "ejec": 3.0, "val": 2.095, "prelim": 7.178, "final": 7.2, "nivel": 4, "pin": "6148"},
    "19942642": {"nombre": "SALGADO SORIANO, INMER ELISEO", "prep": 2.50, "ejec": 5.0, "val": 2.50, "prelim": 10.0, "final": 10.0, "nivel": 5, "pin": "4444"},
    "19942673": {"nombre": "SORIANO MÁRQUEZ, YESSENIA YASMIN", "prep": 2.25, "ejec": 4.0, "val": 2.335, "prelim": 8.585, "final": 8.6, "nivel": 4, "pin": "7508"},
    "19942682": {"nombre": "SORTO HERNÁNDEZ, SOREYNI GISSELLE", "prep": 2.25, "ejec": 4.0, "val": 1.91, "prelim": 8.16, "final": 8.2, "nivel": 4, "pin": "5120"}
}

# Inicializar sesión
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.estudiante = None

# Encabezado Institucional
st.markdown("<h2 class='main-header'>Instituto Nacional de Ciudad Barrios</h2>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Módulo 2.2: Elaboración y Análisis de Estados Financieros<br><b>Docente:</b> Prof. José de la Paz Gutiérrez | <b>Sección:</b> 2TA 2026</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.autenticado:
    st.subheader("🔐 Consulta Privada de Calificaciones")
    st.write("Ingresa tu número de NIE y tu contraseña (PIN) personal para consultar tus notas.")
    
    with st.form("form_login"):
        nie = st.text_input("Número de NIE (Usuario):", placeholder="Ej. 6051262").strip()
        pin = st.text_input("Contraseña / PIN (4 dígitos):", type="password", placeholder="****").strip()
        submit = st.form_submit_button("Ingresar al Portal")
        
        if submit:
            if nie in ESTUDIANTES and ESTUDIANTES[nie]["pin"] == pin:
                st.session_state.autenticado = True
                st.session_state.estudiante = ESTUDIANTES[nie]
                st.rerun()
            else:
                st.error("❌ NIE o PIN incorrecto. Por favor verifica tus credenciales.")
else:
    est = st.session_state.estudiante
    
    # Saludo y datos del alumno
    st.success(f"👋 Bienvenid@, **{est['nombre']}**")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Nota Final", value=f"{est['final']:.1f} / 10.0")
    with col_b:
        st.metric(label="Nivel de Competencia", value=f"Nivel {est['nivel']}")
    
    st.subheader("📊 Desglose Detallado de Calificaciones")
    
    df_notas = pd.DataFrame([
        {"Evaluación": "Preparación", "Porcentaje": "25%", "Puntaje Obtenido": f"{est['prep']:.2f} / 2.50"},
        {"Evaluación": "Ejecución", "Porcentaje": "50%", "Puntaje Obtenido": f"{est['ejec']:.2f} / 5.00"},
        {"Evaluación": "Valoración", "Porcentaje": "25%", "Puntaje Obtenido": f"{est['val']:.2f} / 2.50"},
        {"Evaluación": "Nota Preliminar", "Porcentaje": "100%", "Puntaje Obtenido": f"{est['prelim']:.3f}"},
        {"Evaluación": "Nota Final Redondeada", "Porcentaje": "100%", "Puntaje Obtenido": f"{est['final']:.1f}"}
    ])
    
    st.table(df_notas)
    
    # Leyenda de Niveles de Competencia
    with st.expander("ℹ️ ¿Qué significa mi Nivel de Competencia?"):
        st.markdown("""
        * **Nivel 5 (Excelente: 9.1 - 10.0):** Domina con maestría la elaboración y análisis de estados financieros.
        * **Nivel 4 (Muy Bueno: 7.1 - 9.0):** Desarrolla las competencias del módulo con autonomía y precisión.
        * **Nivel 3 (Bueno: 6.0 - 7.0):** Cumple con los requerimientos básicos de competencia.
        * **Nivel 0-2 (En Proceso):** Requiere reforzamiento académico.
        """)
    
    if st.button("🔒 Cerrar Sesión"):
        st.session_state.autenticado = False
        st.session_state.estudiante = None
        st.rerun()
