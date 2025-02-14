from faker import Faker
import pandas as pd
from sqlalchemy import create_engine
# Configurazione Faker per la generazione di dati
casuali
faker = Faker()
Faker.seed(98765)
def generate_fake_data(records=10):
"""Genera un dataset di utenti con informazioni
casuali."""
data = {
'Nome': [faker.first_name() for _ in
range(records)],
'Cognome': [faker.last_name() for _ in
range(records)],
'Email': [faker.email() for _ in
range(records)],
'Telefono': [faker.phone_number() for _ in
range(records)]
}
return pd.DataFrame(data)
def save_to_excel(dataframe,
filename="utenti_nuovo.xlsx"):
"""Salva il dataset in un file Excel."""
dataframe.to_excel(filename, index=False)
print(f"Dati salvati con successo in {filename}")
def save_to_sql(dataframe,
db_name="sqlite:///database_utenti_nuovo.db"):
"""Salva il dataset in un database SQLite."""
engine = create_engine(db_name)
dataframe.to_sql("utenti", con=engine,
if_exists="replace", index=False)
print("Dati inseriti con successo nel database.")
def
fetch_from_sql(db_name="sqlite:///database_utenti_nuovo
.db"):
"""Recupera i dati dalla tabella utenti."""
engine = create_engine(db_name)
query = "SELECT * FROM utenti"
df = pd.read_sql(query, con=engine)
print("Dati recuperati dalla tabella utenti:")
print(df)
return df
if __name__ == "__main__":
df_users = generate_fake_data(10)
save_to_excel(df_users)
save_to_sql(df_users)
fetch_from_sql()