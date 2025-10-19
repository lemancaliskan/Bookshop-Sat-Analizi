from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

#/* Times fontunu yükle */#
font_path = r"C:\Users\leman\Desktop\bookshop_analizi\font\times.ttf"
pdfmetrics.registerFont(TTFont('Times', font_path))

def create_pdf_report(en_cok_satan_df, kategori_gelir_df, aylik_grafik_path, pasta_grafik_path, cubuk_grafik_path, output_path="rapor.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    #/* Sabit boşluk */#
    HEADER_TABLE_SPACING = 40

    #/* Başlık */#
    c.setFont("Times", 20)
    c.setFillColor(colors.purple)
    c.drawCentredString(width/2, height - 50, "Kitapçı Satış Analizi Raporu")

    #/* En çok satan kitaplar tablosu */#
    c.setFont("Times", 14)
    y_position = height - 100
    c.drawString(50, y_position, "En Çok Satan Kitaplar")
    y_position -= HEADER_TABLE_SPACING
    data1 = [en_cok_satan_df.columns.to_list()] + en_cok_satan_df.values.tolist()
    table1 = Table(data1, colWidths=[200]*len(data1[0]))
    table1.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times'),
        ('BACKGROUND', (0,0), (-1,0), colors.mediumpurple),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))
    table1.wrapOn(c, width, height)
    table1.drawOn(c, 50, y_position - table1._height)
    y_position -= table1._height + HEADER_TABLE_SPACING

    #/* Kategori bazlı gelir tablosu */#
    c.drawString(50, y_position, "Kategori Bazlı Gelir Dağılımı")
    y_position -= HEADER_TABLE_SPACING
    data2 = [kategori_gelir_df.columns.to_list()] + kategori_gelir_df.values.tolist()
    table2 = Table(data2, colWidths=[200]*len(data2[0]))
    table2.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times'),
        ('BACKGROUND', (0,0), (-1,0), colors.mediumpurple),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))
    table2.wrapOn(c, width, height)
    table2.drawOn(c, 50, y_position - table2._height)
    y_position -= table2._height + HEADER_TABLE_SPACING

    #/* Çizgi grafiği */#
    if os.path.exists(aylik_grafik_path):
        c.drawString(50, y_position, "Aylara Göre Satış Grafiği")
        y_position -= HEADER_TABLE_SPACING
        img3 = Image(aylik_grafik_path, width=500, height=250)
        img3.wrapOn(c, width, height)
        img3.drawOn(c, 50, y_position - 250)

    #/* 2. sayfa: Çubuk ve Pasta grafikleri */#
    c.showPage()

    #/* Başlık (renkli) */#
    c.setFont("Times", 20)
    c.setFillColor(colors.purple)
    c.drawCentredString(width/2, height - 50, "Kitapçı Satış Analizi Raporu")

    #/* Sabit boşluk */#
    y_position = height - 100

    #/* Çubuk grafiği başlığı */#
    c.setFont("Times", 14)
    c.setFillColor(colors.purple)
    c.drawString(50, y_position, "En Çok Satan Kitaplar Grafiği")
    y_position -= HEADER_TABLE_SPACING
    if os.path.exists(cubuk_grafik_path):
        img1 = Image(cubuk_grafik_path, width=500, height=250)
        img1.wrapOn(c, width, height)
        img1.drawOn(c, 50, y_position - 250)
        y_position -= 250 + HEADER_TABLE_SPACING

    #/* Pasta grafiği başlığı */#
    c.drawString(50, y_position, "Kategori Bazlı Gelir Dağılımı Grafiği")
    y_position -= HEADER_TABLE_SPACING
    if os.path.exists(pasta_grafik_path):
        img2 = Image(pasta_grafik_path, width=400, height=250)
        img2.wrapOn(c, width, height)
        img2.drawOn(c, 50, y_position - 250)

    #/* PDF Kaydet */#
    c.save()
    print(f"Rapor oluşturuldu: {output_path}")
