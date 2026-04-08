import sys
import os

filepath = 'aatiacademy-v7.html'

with open(filepath, 'r', encoding='utf-8') as f:
    orig = f.read()

def replace_theme(content, font_url, primary_font, secondary_font, dark_vars, light_vars):
    # replace font link
    content = content.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=Lexend:wght@200;300;400;500&display=swap" rel="stylesheet"/>',
        f'<link href="{font_url}" rel="stylesheet"/>'
    )
    # replace font families
    content = content.replace("'Cormorant',Georgia,serif", f"'{primary_font}', serif")
    content = content.replace("'Cormorant',serif", f"'{primary_font}', serif")
    content = content.replace("'Lexend',system-ui,sans-serif", f"'{secondary_font}', sans-serif")
    content = content.replace("'Lexend',sans-serif", f"'{secondary_font}', sans-serif")
    
    # replace dark theme
    dark_start = content.find('[data-theme="dark"]{')
    dark_end = content.find('}', dark_start)
    if dark_start != -1 and dark_end != -1:
        dark_block = "[data-theme=\"dark\"]{\n" + dark_vars + "}"
        content = content[:dark_start] + dark_block + content[dark_end+1:]
        
    # replace light theme
    light_start = content.find('[data-theme="light"]{')
    light_end = content.find('}', light_start)
    if light_start != -1 and light_end != -1:
        light_block = "[data-theme=\"light\"]{\n" + light_vars + "}"
        content = content[:light_start] + light_block + content[light_end+1:]
        
    return content

# Variation 1: Emerald & Gold
font_url_1 = "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Work+Sans:wght@300;400;500&display=swap"
dark_vars_1 = """
  --bg:#05140e;--bg2:#0a1f16;--bg3:#102b1f;--bg4:#163828;
  --fg:#e8f5f0;--fg2:rgba(232,245,240,0.65);--fg3:rgba(232,245,240,0.3);--fg4:rgba(232,245,240,0.1);
  --gold:#d4af37;--gold2:#ebd173;--gold3:#f5eaad;--gold-glow:rgba(212,175,55,0.25);
  --rule:rgba(232,245,240,0.07);--rule2:rgba(212,175,55,0.2);
  --card-bg:rgba(255,255,255,0.025);--card-border:rgba(232,245,240,0.07);
  --about-bg:#e8f5f0;--about-fg:#05140e;--about-fg2:rgba(5,20,14,0.55);--about-gold:var(--gold);
  --feat-bg:#e8f5f0;--feat-fg:#05140e;--feat-fg2:rgba(5,20,14,0.5);
  --form-bg:rgba(255,255,255,0.04);--form-border:rgba(255,255,255,0.09);--form-fg:var(--fg);
  --footer-bg:#05140e;
  --ticker-bg:#0a1f16;
  --scrollbar:var(--gold);
"""
light_vars_1 = """
  --bg:#f4faf8;--bg2:#e6f2ec;--bg3:#d1e6db;--bg4:#bedbc9;
  --fg:#0a1f16;--fg2:rgba(10,31,22,0.62);--fg3:rgba(10,31,22,0.35);--fg4:rgba(10,31,22,0.1);
  --gold:#b8860b;--gold2:#d4af37;--gold3:#ebd173;--gold-glow:rgba(184,134,11,0.2);
  --rule:rgba(10,31,22,0.1);--rule2:rgba(184,134,11,0.25);
  --card-bg:rgba(255,255,255,0.7);--card-border:rgba(10,31,22,0.1);
  --about-bg:#0a1f16;--about-fg:#e8f5f0;--about-fg2:rgba(232,245,240,0.6);--about-gold:#ebd173;
  --feat-bg:#e8f5f0;--feat-fg:#0a1f16;--feat-fg2:rgba(10,31,22,0.5);
  --form-bg:rgba(10,31,22,0.04);--form-border:rgba(10,31,22,0.12);--form-fg:var(--fg);
  --footer-bg:#0a1f16;
  --ticker-bg:#e6f2ec;
  --scrollbar:var(--gold2);
"""

# Variation 2: Navy & Silver/Platinum
font_url_2 = "https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500&display=swap"
dark_vars_2 = """
  --bg:#070a14;--bg2:#0d1222;--bg3:#151c33;--bg4:#1e2744;
  --fg:#f0f4f8;--fg2:rgba(240,244,248,0.65);--fg3:rgba(240,244,248,0.3);--fg4:rgba(240,244,248,0.1);
  --gold:#a0aab2;--gold2:#d1d5db;--gold3:#f3f4f6;--gold-glow:rgba(160,170,178,0.25);
  --rule:rgba(240,244,248,0.07);--rule2:rgba(160,170,178,0.2);
  --card-bg:rgba(255,255,255,0.025);--card-border:rgba(240,244,248,0.07);
  --about-bg:#f0f4f8;--about-fg:#070a14;--about-fg2:rgba(7,10,20,0.55);--about-gold:var(--gold);
  --feat-bg:#f0f4f8;--feat-fg:#070a14;--feat-fg2:rgba(7,10,20,0.5);
  --form-bg:rgba(255,255,255,0.04);--form-border:rgba(255,255,255,0.09);--form-fg:var(--fg);
  --footer-bg:#070a14;
  --ticker-bg:#0d1222;
  --scrollbar:var(--gold);
"""
light_vars_2 = """
  --bg:#f8fafc;--bg2:#f1f5f9;--bg3:#e2e8f0;--bg4:#cbd5e1;
  --fg:#0d1222;--fg2:rgba(13,18,34,0.62);--fg3:rgba(13,18,34,0.35);--fg4:rgba(13,18,34,0.1);
  --gold:#64748b;--gold2:#94a3b8;--gold3:#cbd5e1;--gold-glow:rgba(100,116,139,0.2);
  --rule:rgba(13,18,34,0.1);--rule2:rgba(100,116,139,0.25);
  --card-bg:rgba(255,255,255,0.7);--card-border:rgba(13,18,34,0.1);
  --about-bg:#0d1222;--about-fg:#f0f4f8;--about-fg2:rgba(240,244,248,0.6);--about-gold:#94a3b8;
  --feat-bg:#f0f4f8;--feat-fg:#0d1222;--feat-fg2:rgba(13,18,34,0.5);
  --form-bg:rgba(13,18,34,0.04);--form-border:rgba(13,18,34,0.12);--form-fg:var(--fg);
  --footer-bg:#0d1222;
  --ticker-bg:#f1f5f9;
  --scrollbar:var(--gold2);
"""

# Variation 3: Rose & Plum
font_url_3 = "https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;1,300;1,400&family=Montserrat:wght@300;400;500&display=swap"
dark_vars_3 = """
  --bg:#140c0e;--bg2:#1c1114;--bg3:#2c1b20;--bg4:#3c252b;
  --fg:#fdfaf9;--fg2:rgba(253,250,249,0.65);--fg3:rgba(253,250,249,0.3);--fg4:rgba(253,250,249,0.1);
  --gold:#c47e8c;--gold2:#e5a8b4;--gold3:#f6ced5;--gold-glow:rgba(196,126,140,0.25);
  --rule:rgba(253,250,249,0.07);--rule2:rgba(196,126,140,0.2);
  --card-bg:rgba(255,255,255,0.025);--card-border:rgba(253,250,249,0.07);
  --about-bg:#fdfaf9;--about-fg:#140c0e;--about-fg2:rgba(20,12,14,0.55);--about-gold:var(--gold);
  --feat-bg:#fdfaf9;--feat-fg:#140c0e;--feat-fg2:rgba(20,12,14,0.5);
  --form-bg:rgba(255,255,255,0.04);--form-border:rgba(255,255,255,0.09);--form-fg:var(--fg);
  --footer-bg:#140c0e;
  --ticker-bg:#1c1114;
  --scrollbar:var(--gold);
"""
light_vars_3 = """
  --bg:#fefaf9;--bg2:#fbeeed;--bg3:#f4d9d8;--bg4:#ecc6c4;
  --fg:#211417;--fg2:rgba(33,20,23,0.62);--fg3:rgba(33,20,23,0.35);--fg4:rgba(33,20,23,0.1);
  --gold:#9e525c;--gold2:#b76e79;--gold3:#dca0a9;--gold-glow:rgba(158,82,92,0.2);
  --rule:rgba(33,20,23,0.1);--rule2:rgba(158,82,92,0.25);
  --card-bg:rgba(255,255,255,0.7);--card-border:rgba(33,20,23,0.1);
  --about-bg:#211417;--about-fg:#fdfaf9;--about-fg2:rgba(253,250,249,0.6);--about-gold:#dca0a9;
  --feat-bg:#fdfaf9;--feat-fg:#211417;--feat-fg2:rgba(33,20,23,0.5);
  --form-bg:rgba(33,20,23,0.04);--form-border:rgba(33,20,23,0.12);--form-fg:var(--fg);
  --footer-bg:#211417;
  --ticker-bg:#fbeeed;
  --scrollbar:var(--gold2);
"""

# Write out the variations
v1_content = replace_theme(orig, font_url_1, "Playfair Display", "Work Sans", dark_vars_1, light_vars_1)
with open('aatiacademy_emerald.html', 'w', encoding='utf-8') as f: f.write(v1_content)

v2_content = replace_theme(orig, font_url_2, "Lora", "Inter", dark_vars_2, light_vars_2)
with open('aatiacademy_navy.html', 'w', encoding='utf-8') as f: f.write(v2_content)

v3_content = replace_theme(orig, font_url_3, "Merriweather", "Montserrat", dark_vars_3, light_vars_3)
with open('aatiacademy_rose.html', 'w', encoding='utf-8') as f: f.write(v3_content)

print("Generated 3 variants successfully.")
