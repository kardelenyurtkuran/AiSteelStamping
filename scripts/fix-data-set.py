import pandas as pd

dosya_adi = "..\\data\\production-plan.csv"

df = pd.read_csv(dosya_adi, delimiter=";")

# Düzeltilmiş CSV'yi kaydet
df.to_csv("..\\data\\fix-production-plan.csv", index=False)

print("CSV başarıyla düzenlendi ve 'fix-production-plan.csv' olarak kaydedildi.")
