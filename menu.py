import streamlit as st
import json
from collections import defaultdict

# Carregar receptes
with open("receptes.json", "r", encoding="utf-8") as f:
    receptes = json.load(f)

receptes_dict = {r["nom"]: r for r in receptes}
dies = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]
menu_setmanal = {}

st.title("🍽️ Planificador de Menú Setmanal")

for dia in dies:
    st.markdown(f"### 📅 {dia}")
    col1, col2 = st.columns(2)
    
    with col1:
        plat_dinar = st.selectbox(f"{dia} – Dinar", [r["nom"] for r in receptes], key=f"{dia}-dinar")
    with col2:
        plat_sopar = st.selectbox(f"{dia} – Sopar", [r["nom"] for r in receptes], key=f"{dia}-sopar")
    
    menu_setmanal[dia] = {
        "dinar": plat_dinar,
        "sopar": plat_sopar
    }

# 🛒 Botó per generar llista de la compra
if st.button("📝 Generar llista de la compra"):
    ingredients_totals = defaultdict(list)

    for dia in dies:
        for àpat in ["dinar", "sopar"]:
            nom_plat = menu_setmanal[dia][àpat]
            recepta = receptes_dict[nom_plat]
            for ing, quantitat in recepta["ingredients"].items():
                ingredients_totals[ing].append(quantitat)
    
    st.subheader("🛍️ Ingredients totals per la setmana:")
    for ing, quantitats in ingredients_totals.items():
        llista_text = " + ".join(quantitats)
        st.write(f"- {ing}: {llista_text}")
