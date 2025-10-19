import os
from src.data_generator import fake_data_generator
from src.data_analysis import analyze_sales
from src.visualization import tum_gorsellestirme
from src.report_generator import create_pdf_report

#/* Sahte veri oluştur */#
fake_data_generator()

#/* Analiz */#
en_cok_satan_df, kategori_gelir_df, aylik_satis_df = analyze_sales("data/satis_verileri.csv")

#/* Görselleştirme */#
os.makedirs("plots", exist_ok=True)
tum_gorsellestirme("data/satis_verileri.csv")  # Bu fonksiyon zaten grafikleri kaydediyor

#/* PDF rapor oluştur */#
aylik_grafik_path = "plots/aylik_satis.png"
pasta_grafik_path = "plots/kategori_gelir.png"
kitap_cubuk_grafik_path = "plots/en_cok_satan_kitaplar.png"

create_pdf_report(
    en_cok_satan_df,
    kategori_gelir_df,
    aylik_grafik_path,
    pasta_grafik_path,
    kitap_cubuk_grafik_path,
    "rapor.pdf"
)
