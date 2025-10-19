import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")  #/* Grafik stili */#


def veri_yukle(dosya_yolu="data/satis_verileri.csv"):

    try:
        df = pd.read_csv(dosya_yolu)
        df['tarih'] = pd.to_datetime(df['tarih'])
        return df
    except FileNotFoundError:
        print(f"❌ Dosya bulunamadı: {dosya_yolu}")
        return None


def kitap_cubuk_grafik(df):

    kitap_satis = df.groupby('kitap_adi')['adet'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=kitap_satis.values, y=kitap_satis.index, color="mediumslateblue")
    plt.title("En Çok Satan 10 Kitap")
    plt.xlabel("Satış Adedi")
    plt.ylabel("Kitap Adı")
    plt.tight_layout()

    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/en_cok_satan_kitaplar.png")
    plt.show()


def kategori_pasta_grafik(df):

    kategori_gelir = df.groupby('kategori').apply(lambda x: (x['adet'] * x['fiyat']).sum())

    plt.figure(figsize=(7, 7))
    plt.pie(kategori_gelir, labels=kategori_gelir.index, autopct='%1.1f%%', startangle=140,
            colors=sns.color_palette("pastel"))
    plt.title("Kategori Bazlı Gelir Dağılımı")
    plt.tight_layout()

    plt.savefig("plots/kategori_gelir.png")
    plt.show()


def aylik_satis_cizgi(df):

    df['ay'] = df['tarih'].dt.month
    aylik_satis = df.groupby('ay')['adet'].sum()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=aylik_satis.index, y=aylik_satis.values, marker='o')
    plt.title("Aylara Göre Satış Adedi")
    plt.xlabel("Ay")
    plt.ylabel("Satış Adedi")
    plt.xticks(range(1, 13))
    plt.tight_layout()

    plt.savefig("plots/aylik_satis.png")
    plt.show()


def tum_gorsellestirme(dosya_yolu="data/satis_verileri.csv"):
    df = veri_yukle(dosya_yolu)
    if df is not None:
        kitap_cubuk_grafik(df)
        kategori_pasta_grafik(df)
        aylik_satis_cizgi(df)
    else:
        print("Veri bulunamadı, görselleştirme yapılamıyor.")

if __name__ == "__main__":
    tum_gorsellestirme()
