import pandas as pd
import numpy as np
from faker import Faker
import random
import os

def fake_data_generator():
    fake = Faker()

    kitaplar = [
        ("Nutuk", "Tarih"),
        ("Çalıkuşu", "Roman"),
        ("Acımak", "Roman"),
        ("Büyük Saat", "Şiir"),
        ("Kuzgun", "Şiir"),
        ("Tanzimat", "Tarih"),
        ("Jön Türkler İttihat ve Terakki","Tarih"),
        ("Kısa Türkiye Tarihi", "Tarih"),
        ("Siyasi Tarih: İlkçağlardan 1918'e", "Tarih"),
        ("Veronika Ölmek İstiyor", "Roman"),
        ("Kim Jiyeong Doğum 1982", "Roman"),
        ("1984", "Roman"),
        ("Küçük Prens", "Çocuk"),
        ("Python 101", "Eğitim"),

    ]

    N = 500
    veriler = []
    for _ in range(N):
        kitap, kategori = random.choice(kitaplar)
        fiyat = round(random.uniform(20, 150), 2)
        adet = random.randint(1, 5)
        tarih = fake.date_between(start_date='-1y', end_date='today')
        musteri_id = random.randint(1000, 1999)
        toplam_tutar = round(fiyat * adet, 2)
        veriler.append([tarih, musteri_id, kitap, kategori, fiyat, adet, toplam_tutar])

    df = pd.DataFrame(veriler, columns=[
        "tarih", "musteri_id", "kitap_adi", "kategori", "fiyat", "adet", "toplam_tutar"
    ])

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/satis_verileri.csv", index=False, encoding="utf-8")
    print("satis_verileri.csv oluşturuldu!")
