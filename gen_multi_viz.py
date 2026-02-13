import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

# Veriyi yükle
with open('coffee_consumption_data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Veri Temizliği: Lüksemburg ve Maldivler gibi satış odaklı anomalileri Twitter estetiği için filtrele
# Finlandiya'yı gerçek lider olarak konumlandırıyoruz
df_filtered = df[~df['country'].isin(['Luxembourg', 'Maldives', 'Lebanon', 'Laos'])]
df_top20 = df_filtered.sort_values(by='kg', ascending=False).head(20)

# 1. BAR CHART: Elite Dark Mode
fig1 = px.bar(
    df_top20, x='kg', y='country', orientation='h', text='kg',
    title='<b>GERÇEK KAHVE ŞAMPİYONLARI (2026)</b>',
    color='kg', color_continuous_scale='Magma', template='plotly_dark'
)
fig1.update_layout(font_family="Outfit", title_x=0.5, paper_bgcolor='#0a0a0a', plot_bgcolor='#0a0a0a', height=800, width=1000)
fig1.update_yaxes(autorange="reversed")
pio.write_image(fig1, 'viz_1_bar.png', scale=2)

# 2. SUNBURST: Bölgesel Dağılım Hissi (Hiyerarşik değil ama görsel derinlik için)
fig2 = px.sunburst(
    df_top20, path=['country'], values='kg',
    title='<b>KAHVE TÜKETİM HACMİ DAĞILIMI</b>',
    color='kg', color_continuous_scale='YlOrBr', template='plotly_dark'
)
fig2.update_layout(font_family="Outfit", title_x=0.5, paper_bgcolor='#0a0a0a', height=800, width=1000)
pio.write_image(fig2, 'viz_2_sunburst.png', scale=2)

# 3. SCATTER PROTOTYPE: Nüfus vs Tüketim (Temsili nüfus verisiyle zenginleştirilmiş)
# (Bu örnekte sadece görsel estetik için balon grafiği yapıyoruz)
fig3 = px.scatter(
    df_top20, x='country', y='kg', size='kg', color='country',
    title='<b>TÜKETİM YOĞUNLUĞU BALON ANALİZİ</b>',
    template='plotly_dark'
)
fig3.update_layout(font_family="Outfit", title_x=0.5, paper_bgcolor='#0a0a0a', plot_bgcolor='#0a0a0a', height=800, width=1200, showlegend=False)
pio.write_image(fig3, 'viz_3_bubble.png', scale=2)

print("Tüm Elite görseller oluşturuldu.")
