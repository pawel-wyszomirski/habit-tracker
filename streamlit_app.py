import streamlit as st
import pandas as pd
import datetime

# Inicjalizacja lub załadowanie danych
if 'habit_data' not in st.session_state:
    st.session_state.habit_data = pd.DataFrame(columns=['Data', 'Nawyk', 'Wykonano'])

st.title("📝 Tracker Nawyków")

# Dodawanie nowego nawyku
st.header("Dodaj Nowy Nawyk")
new_habit = st.text_input("Nazwa nawyku")
add_habit = st.button("Dodaj Nawyk")
if add_habit and new_habit:
    new_entry = {'Data': datetime.date.today(), 'Nawyk': new_habit, 'Wykonano': False}
    st.session_state.habit_data = pd.concat([st.session_state.habit_data, pd.DataFrame([new_entry])], ignore_index=True)
    st.success(f'Nawyk "{new_habit}" dodany!')

# Monitorowanie nawyków
st.header("Monitorowanie Nawyków")
today = datetime.date.today()
today_habits = st.session_state.habit_data[st.session_state.habit_data['Data'] == today]

for index, row in today_habits.iterrows():
    checked = st.checkbox(f"{row['Nawyk']}", value=row['Wykonano'])
    st.session_state.habit_data.at[index, 'Wykonano'] = checked

# Analiza wyników
st.header("📊 Analiza Nawyków")
if not st.session_state.habit_data.empty:
    habit_counts = st.session_state.habit_data.groupby('Nawyk')['Wykonano'].sum()
    st.bar_chart(habit_counts)

    success_rate = st.session_state.habit_data['Wykonano'].mean() * 100
    st.metric("Średnia Skuteczność Nawyków", f"{success_rate:.2f}%")
else:
    st.write("Brak danych do analizy.")

st.button("Zapisz i odśwież", on_click=lambda: None)
