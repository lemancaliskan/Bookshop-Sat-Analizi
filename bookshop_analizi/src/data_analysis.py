import pandas as pd

def analyze_sales(file_path="data/satis_verileri.csv"):
    df = pd.read_csv(file_path, parse_dates=["tarih"])

    en_cok_satan_df = df.groupby("kitap_adi")["adet"].sum().reset_index()
    en_cok_satan_df = en_cok_satan_df.sort_values(by="adet", ascending=False).head(10)

    kategori_gelir_df = df.groupby("kategori").apply(lambda x: (x["adet"] * x["fiyat"]).sum()).reset_index()
    kategori_gelir_df.columns = ["kategori", "toplam_gelir"]

    df["ay"] = df["tarih"].dt.month
    aylik_satis_df = df.groupby("ay")["adet"].sum().reset_index()

    return en_cok_satan_df, kategori_gelir_df, aylik_satis_df
