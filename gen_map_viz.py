import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

# Veriyi yükle
with open('coffee_consumption_data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Harita Görselleştirmesi (Choropleth Map)
fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="kg",
    hover_name="country",
    title='<b>DÜNYA KAHVE TÜKETİM HARİTASI (2026)</b><br><span style="font-size:14px; color:#888;">Ülke Bazında Yıllık Kişi Başına Tüketim (Kilogram)</span>',
    color_continuous_scale='YlOrBr', # Kahve tonlarına yakın sarı-turuncu-kahverengi skalası
    template='plotly_dark'
)

# Harita tasarımı iyileştirmeleri
fig.update_layout(
    font_family="Outfit, sans-serif",
    title_font_size=24,
    title_x=0.5,
    margin=dict(l=0, r=0, t=100, b=0),
    height=700,
    width=1200,
    paper_bgcolor='#0f0f0f',
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular',
        bgcolor='#0f0f0f',
        landcolor='#1a1a1a',
        subunitcolor='#333'
    ),
    coloraxis_colorbar=dict(
        title="kg",
        thicknessmode="pixels", thickness=15,
        lenmode="fraction", len=0.6,
        yanchor="middle", y=0.5,
        ticks="outside"
    )
)

# Yüksek çözünürlüklü kaydet
pio.write_image(fig, 'coffee_world_map.png', scale=2)
print("Harita görseli başarıyla oluşturuldu: coffee_world_map.png")
