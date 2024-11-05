import streamlit as st

# Título y descripción de la aplicación
st.title("Asistente Médico Personal")
st.write("Selecciona tus síntomas de la lista a continuación y haz clic en 'Continuar' para obtener un diagnóstico.")

# Lista de síntomas
sintomas = [
    "Tos", "Congestión nasal", "Dificultad para respirar", "Dolor de garganta",
    "Dolor de cabeza", "Dolor general", "Cansancio", "Diarrea", "Vómito",
    "Escalofríos", "Dolor de estómago", "Picazón en la piel",
    "Picazón en la garganta", "Enrojecimiento de la piel", "Hinchazón"
]

# Agrupar síntomas por categorías de diagnóstico
resfriado_comun = {"Tos", "Congestión nasal", "Dificultad para respirar", "Dolor de garganta", 
                   "Dolor de cabeza", "Dolor general", "Cansancio"}
infeccion_gastrointestinal = {"Diarrea", "Vómito", "Escalofríos", "Dolor de estómago"}
alergia = {"Picazón en la piel", "Picazón en la garganta", "Enrojecimiento de la piel", "Hinchazón"}

# Crear checkbox para cada síntoma
sintomas_seleccionados = []
for sintoma in sintomas:
    if st.checkbox(sintoma):
        sintomas_seleccionados.append(sintoma)

# Evaluar síntomas al presionar el botón "Continuar"
if st.button("Continuar"):
    if not sintomas_seleccionados:
        st.warning("Por favor, selecciona tus síntomas. Pide ayuda a tus padres si es necesario.")
    else:
        # Convertir a conjunto para facilitar la comparación
        sintomas_set = set(sintomas_seleccionados)
        
        # Verificar coincidencia con los diagnósticos
        es_resfriado = sintomas_set.intersection(resfriado_comun)
        es_infeccion_gastro = sintomas_set.intersection(infeccion_gastrointestinal)
        es_alergia = sintomas_set.intersection(alergia)
        
        # Determinar el diagnóstico basado en los síntomas seleccionados
        if (es_resfriado and not es_infeccion_gastro and not es_alergia):
            st.success("Padeces de Resfriado común.")
        elif (es_infeccion_gastro and not es_resfriado and not es_alergia):
            st.success("Padeces de Infección Gastrointestinal.")
        elif (es_alergia and not es_resfriado and not es_infeccion_gastro):
            st.success("Padeces de Alergia.")
        else:
            st.warning("No puedo generar un diagnóstico para tu enfermedad, lo mejor sería que fueras al médico.")

