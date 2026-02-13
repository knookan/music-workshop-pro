import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

# Load data
with open('coffee_consumption_data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Sort and take top 25 for a cleaner elite look
df = df.sort_values(by='kg', ascending=False).head(25)

# Create Elite Bar Chart
fig = px.bar(
    df, 
    x='kg', 
    y='country', 
    orientation='h',
    text='kg',
    title='<b>KÜRESEL KAHVE TUTKUSU (2026)</b><br><span style="font-size:14px; color:#888;">Kişi Başına Yıllık Ortalama Tüketim (Kilogram)</span>',
    labels={'kg': 'Tüketim (kg)', 'country': 'Ülke'},
    color='kg',
    color_continuous_scale='Sunsetdark',
    template='plotly_dark'
)

# Refine Layout for "Elite" Look
fig.update_layout(
    font_family="Outfit, sans-serif",
    title_font_size=28,
    title_x=0.5,
    xaxis_title="",
    yaxis_title="",
    coloraxis_showscale=False,
    margin=dict(l=150, r=50, t=100, b=50),
    height=800,
    width=1000,
    paper_bgcolor='#0f0f0f',
    plot_bgcolor='#0f0f0f',
)

fig.update_traces(
    texttemplate='%{text:.1f} kg', 
    textposition='outside',
    marker_line_color='rgba(255,255,255,0.2)',
    marker_line_width=1,
    opacity=0.9
)

fig.update_yaxes(autorange="reversed")

# Save as High-Res PNG
pio.write_image(fig, 'coffee_elite_edition.png', scale=2)
print("Elite Edition created successfully: coffee_elite_edition.png")
