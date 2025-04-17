import streamlit as st
import json
from collections import defaultdict

# Carregar receptes
with open('receptes.json', 'r', encoding='utf-8') as f:
    receptes = json.load(f)

# Dies de la setmana
dies = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]

# Menú setmanal
st.title("🍽️ Planificador de Menú Setmanal")
menu_setmanal = {}

for dia in dies:
    plats = st.selectbox(f"{dia}:", [r['nom'] for r in receptes], key=dia)
    menu_setmanal[dia] = plats

# Generar llista de la compra
if st.button("📝 Generar llista de la compra"):
    ingredients_totals = defaultdict(int)
    plats_seleccionats = [r for r in receptes if r['nom'] in menu_setmanal.values()]

    for plat in plats_seleccionats:
        for ingredient in plat['ingredients']:
            ingredients_totals[ingredient] += 1

    st.subheader("🛒 Llista de la compra")
    for ingredient, qty in ingredients_totals.items():
        st.write(f"- {ingredient}")
