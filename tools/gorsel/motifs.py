# Aymati Proje — özgün teknik çizim motifleri (640x440 tuval, blueprint stili)
import math
L = '#e6ecf5'; T = '#48c9c6'; G = '#d3a467'; D = '#7f95b5'; BG = '#0d2547'; F = '#48c9c61f'

def P(d, c=L, w=3, f='none', o=1, extra=''):
    return f'<path d="{d}" stroke="{c}" stroke-width="{w}" fill="{f}" opacity="{o}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def R(x, y, w, h, c=L, sw=3, f='none', rx=0, o=1, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" stroke="{c}" stroke-width="{sw}" fill="{f}" opacity="{o}" {extra}/>'
def C(cx, cy, r, c=L, sw=3, f='none', o=1, extra=''):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{c}" stroke-width="{sw}" fill="{f}" opacity="{o}" {extra}/>'
def Ln(x1, y1, x2, y2, c=L, w=3, o=1, dash=''):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" opacity="{o}" stroke-linecap="round"{da}/>'
def Tx(x, y, s, size=16, c=D, anchor='start', weight=500, mono=True):
    fam = "'DejaVu Sans Mono',Menlo,monospace" if mono else "Poppins,'DejaVu Sans',Arial,sans-serif"
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{c}" text-anchor="{anchor}" font-weight="{weight}" font-family="{fam}" letter-spacing=".04em">{s}</text>'
def ground(x1, x2, y):
    s = Ln(x1, y, x2, y, D, 2)
    for x in range(int(x1) + 6, int(x2), 16):
        s += Ln(x, y + 2, x - 10, y + 12, D, 1.5, .7)
    return s
def dimv(x, y1, y2, lab):
    s = Ln(x, y1, x, y2, G, 1.5) + Ln(x - 7, y1, x + 7, y1, G, 1.5) + Ln(x - 7, y2, x + 7, y2, G, 1.5)
    return s + f'<text x="{x - 10}" y="{(y1 + y2) / 2}" font-size="15" fill="{G}" text-anchor="middle" font-family="\'DejaVu Sans Mono\',monospace" transform="rotate(-90 {x - 10} {(y1 + y2) / 2})">{lab}</text>'
def dimh(x1, x2, y, lab):
    s = Ln(x1, y, x2, y, G, 1.5) + Ln(x1, y - 7, x1, y + 7, G, 1.5) + Ln(x2, y - 7, x2, y + 7, G, 1.5)
    return s + Tx((x1 + x2) / 2, y - 8, lab, 15, G, 'middle')
def tag(x, y, s, c=G):
    w = 14 + 9.2 * len(s)
    return R(x, y, w, 26, c, 1.5, '#0d2547', 4) + Tx(x + w / 2, y + 18, s, 14, c, 'middle', 600)
def arrow(x1, y1, x2, y2, c=T, w=2.5):
    a = math.atan2(y2 - y1, x2 - x1); h = 11
    p1 = (x2 - h * math.cos(a - .45), y2 - h * math.sin(a - .45)); p2 = (x2 - h * math.cos(a + .45), y2 - h * math.sin(a + .45))
    return Ln(x1, y1, x2, y2, c, w) + P(f'M{p1[0]:.1f} {p1[1]:.1f} L{x2} {y2} L{p2[0]:.1f} {p2[1]:.1f}', c, w)
def bolt(x, y, s=1, c=G):
    return P(f'M{x} {y} l{-22*s} {50*s} h{18*s} l{-14*s} {46*s} l{40*s} {-60*s} h{-19*s} l{14*s} {-36*s} z', c, 2.5, '#d3a46733')
def hook(x, y, c=L):
    return P(f'M{x} {y} v16 q0 18 -14 18 q-14 0 -14 -12', c, 3) + C(x, y - 6, 6, c, 2.5)
def person(x, y, s=1, c=D):
    return C(x, y - 54 * s, 8 * s, c, 2) + P(f'M{x} {y - 46*s} v26 m0 0 l-10 {20*s} m10 {-20*s} l10 {20*s} M{x - 12*s} {y - 36*s} h{24*s}', c, 2)
def lattice(x, y, w, h, n, c=L, horiz=False):
    s = R(x, y, w, h, c, 2.5)
    if horiz:
        st = w / n
        for i in range(n):
            s += Ln(x + i * st, y + h, x + (i + .5) * st, y, c, 1.6) + Ln(x + (i + .5) * st, y, x + (i + 1) * st, y + h, c, 1.6)
    else:
        st = h / n
        for i in range(n):
            s += Ln(x, y + i * st, x + w, y + (i + .5) * st, c, 1.6) + Ln(x + w, y + (i + .5) * st, x, y + (i + 1) * st, c, 1.6)
    return s
def meter(x, y, disp='Ω', c=T, probes=True):
    s = R(x, y, 120, 170, L, 3, '#0d2547', 14) + R(x + 16, y + 18, 88, 46, c, 2, F, 4) + Tx(x + 60, y + 50, disp, 22, c, 'middle', 700)
    s += C(x + 60, y + 112, 26, L, 2.5) + Ln(x + 60, y + 112, x + 76, y + 96, G, 2.5) + C(x + 30, y + 152, 5, D, 2) + C(x + 90, y + 152, 5, D, 2)
    if probes:
        s += P(f'M{x + 30} {y + 170} q-20 60 -70 70', T, 2.5) + P(f'M{x + 90} {y + 170} q20 60 70 70', G, 2.5)
    return s
def building(x, y, w, h, c=L):
    s = R(x, y, w, h, c, 3)
    for i in range(1, 4):
        for j in range(int(w // 70)):
            s += R(x + 20 + j * 70, y + 20 + (i - 1) * (h - 30) / 3, 34, (h - 30) / 3 - 22, D, 1.5)
    return s
def panel(x, y, w=180, h=250, rows=4):
    s = R(x, y, w, h, L, 3, '#0d2547', 6) + Ln(x + 12, y + 30, x + w - 12, y + 30, T, 3)
    for r in range(rows):
        yy = y + 50 + r * ((h - 70) / rows)
        for k in range(int((w - 30) // 26)):
            s += R(x + 16 + k * 26, yy, 18, 30, L, 1.8) + Ln(x + 25 + k * 26, yy + 8, x + 25 + k * 26, yy + 18, G, 2)
    return s

# ---------------- motifler ----------------
def raf():
    s = ground(40, 600, 390)
    xs = [110, 250, 390, 530]
    for x in xs: s += lattice(x - 8, 70, 16, 320, 8, L)
    for y in [150, 240, 330]:
        for i in range(3): s += R(xs[i] + 8, y, xs[i + 1] - xs[i] - 16, 9, T, 2, F)
    for y in [150, 240, 330]:
        for i in range(3):
            x0 = xs[i] + 22
            for k in range(2):
                s += R(x0 + k * 56, y - 14, 48, 12, D, 1.8) + R(x0 + k * 56 + 4, y - 66, 40, 52, L, 2, F)
    s += tag(110, 34, 'WLL / göz') + dimv(70, 70, 390, 'H') + arrow(320, 40, 320, 90, G)
    return s
def platform():
    s = ground(40, 610, 390)
    s += R(150, 190, 420, 16, L, 3, F)
    for x in [160, 300, 440, 560]: s += R(x - 6, 206, 12, 184, L, 2.5)
    s += Ln(150, 150, 570, 150, T, 2.5) + ''.join(Ln(x, 150, x, 190, T, 2) for x in range(170, 571, 40))
    s += P('M150 390 L265 206', L, 3) + P('M178 390 L293 206', L, 2) + ''.join(Ln(150 + i * 14.4, 390 - i * 23, 178 + i * 14.4, 390 - i * 23, D, 1.8) for i in range(1, 8))
    for x in [360, 470]: s += R(x, 128, 60, 62, D, 2, F)
    s += person(410, 190, 1, T) + dimv(110, 190, 390, 'h') + tag(380, 70, 'q (kN/m²)')
    for x in range(330, 541, 50): s += arrow(x, 96, x, 122, G, 2)
    return s
def iskele():
    s = ground(40, 610, 395) + R(470, 40, 140, 355, D, 2, '#ffffff08')
    for i in range(6): s += R(490, 60 + i * 55, 40, 30, D, 1.2) + R(550, 60 + i * 55, 40, 30, D, 1.2)
    cols = [120, 230, 340, 450]; levels = [395, 305, 215, 125, 50]
    for x in cols: s += Ln(x, 395, x, 40, L, 3)
    for y in levels: s += Ln(110, y, 460, y, L, 2.5)
    for i in range(3):
        for j in range(4): s += Ln(cols[i], levels[j], cols[i + 1], levels[j + 1], T, 1.8, .9)
    for y in levels[1:]: s += R(118, y - 8, 334, 8, G, 1.5, '#d3a46726')
    for x in cols: s += R(x - 16, 395, 32, 8, L, 2)
    s += dimv(80, 50, 395, 'H') + arrow(30, 150, 100, 150, T) + Tx(30, 140, 'w', 16, T)
    return s
def stand():
    s = ground(30, 620, 395)
    s += R(90, 70, 460, 34, T, 2.5, F) + Tx(320, 94, 'STAND', 20, T, 'middle', 700, False)
    for x in [100, 330, 540]: s += R(x - 6, 104, 12, 291, L, 3)
    s += R(94, 220, 452, 14, L, 3, F) + Ln(330, 180, 546, 180, L, 2) + ''.join(Ln(x, 180, x, 220, L, 1.6) for x in range(345, 546, 25))
    s += P('M120 395 L230 234', L, 3) + P('M150 395 L260 234', L, 2) + ''.join(Ln(120 + i * 13.75, 395 - i * 20, 150 + i * 13.75, 395 - i * 20, D, 1.6) for i in range(1, 8))
    s += R(360, 270, 150, 90, D, 2, F) + R(380, 290, 110, 50, T, 1.8) + person(420, 220, .9, D) + person(470, 220, .9, D)
    s += dimv(60, 104, 395, 'H') + tag(360, 140, 'çift kat')
    return s
def sahne():
    s = ground(20, 620, 400)
    s += lattice(70, 60, 28, 300, 10) + lattice(542, 60, 28, 300, 10) + lattice(70, 60, 500, 28, 14, L, True)
    s += R(120, 340, 400, 22, L, 3, F) + ''.join(Ln(x, 362, x, 400, D, 2) for x in [140, 260, 380, 500])
    for x in [170, 260, 380, 470]: s += Ln(x, 88, x, 110, D, 2) + P(f'M{x - 12} 110 h24 l-6 22 h-12 z', G, 2, '#d3a46726') + P(f'M{x - 6} 132 l-40 120 M{x + 6} 132 l40 120', G, 1, extra='opacity=".35"')
    for x in [110, 530]: s += R(x - 22, 120, 44, 80, L, 2.5, F) + C(x, 150, 10, D, 2) + C(x, 182, 6, D, 2)
    s += arrow(600, 200, 640 - 70, 200, T) + arrow(625, 240, 575, 240, T) + Tx(590, 186, 'w', 16, T)
    return s
def kulevinc():
    s = ground(20, 620, 380) + R(150, 380, 120, 40, G, 2, '#d3a46722') + dimh(150, 270, 434, 'B')
    s += lattice(195, 80, 30, 300, 12)
    s += lattice(225, 70, 380, 22, 14, L, True) + lattice(50, 70, 145, 22, 5, L, True) + R(60, 92, 60, 40, L, 2.5, F)
    s += P('M210 70 L210 30 L560 70 M210 30 L90 70', L, 2) + R(470, 92, 30, 14, L, 2) + Ln(485, 106, 485, 250, D, 1.8) + hook(485, 256)
    s += R(450, 285, 70, 46, T, 2.5, F) + arrow(250, 395, 250, 360, G) + Tx(290, 400, 'M · V', 15, G)
    return s
def travers():
    s = hook(320, 46) + Ln(320, 80, 150, 170, L, 2.5) + Ln(320, 80, 490, 170, L, 2.5)
    s += R(110, 170, 420, 34, L, 3, F) + Ln(110, 187, 530, 187, D, 1.2) + C(150, 170, 9, G, 2.5) + C(490, 170, 9, G, 2.5)
    for x in [150, 490]: s += Ln(x, 204, x, 260, L, 2.5) + hook(x, 266, L)
    s += R(120, 300, 400, 90, T, 2.5, F) + Tx(320, 352, 'YÜK', 20, T, 'middle', 700, False)
    s += tag(400, 112, 'WLL') + arrow(320, 400, 320, 430, G)
    return s
def monoray():
    s = Ln(40, 40, 600, 40, D, 2)
    for x in [120, 320, 520]: s += Ln(x, 40, x, 90, L, 2.5)
    s += R(60, 90, 520, 12, L, 3, F) + R(312, 102, 16, 40, L, 2.5) + R(60, 142, 520, 12, L, 3, F)
    s += R(270, 156, 100, 30, L, 2.5) + C(290, 150, 8, G, 2) + C(350, 150, 8, G, 2) + R(285, 186, 70, 60, T, 2.5, F)
    s += Ln(305, 246, 305, 300, L, 2) + Ln(335, 246, 335, 300, L, 2) + hook(320, 306) + R(250, 340, 140, 60, D, 2.5, F)
    s += dimh(120, 320, 70, 'L') + arrow(400, 170, 470, 170, G) + arrow(240, 170, 170, 170, G)
    return s
def tabela():
    s = ground(30, 620, 390) + R(250, 390, 140, 40, G, 2, '#d3a46722')
    s += R(296, 160, 48, 230, L, 3) + R(190, 50, 260, 120, L, 3, F) + Tx(320, 100, 'TABELA', 24, T, 'middle', 700, False) + Ln(215, 130, 425, 130, D, 2)
    for y in [70, 110, 150]: s += arrow(40, y, 160, y, T)
    s += Tx(40, 54, 'rüzgâr', 15, T) + dimv(500, 50, 390, 'H') + arrow(320, 420, 320, 436, G)
    return s
def paratoner():
    s = ground(20, 620, 380)
    s += P('M140 380 V170 L190 120 H560 V380 Z', L, 3) + P('M140 170 H510 L560 120', L, 2)
    for x in range(180, 511, 66): s += Ln(x, 170, x + 50, 120, T, 1.8)
    s += Ln(165, 145, 535, 145, T, 1.8)
    for x in [140, 510]: s += Ln(x, 170, x, 380, G, 3)
    for y in range(205, 380, 45):
        for x in range(170, 500, 80): s += R(x, y, 40, 26, D, 1.5)
    s += P('M120 400 H600', G, 2, extra='stroke-dasharray="10 7"') + bolt(400, 10, 1)
    return s
def pano():
    s = ground(30, 620, 400) + panel(70, 90, 210, 300, 5) + P('M280 90 L340 120 V420 L280 390', L, 2.5)
    s += Tx(440, 70, 'TEK HAT', 14, D, 'middle') + Ln(440, 90, 440, 140, T, 2.5) + R(425, 140, 30, 30, L, 2)
    s += Ln(380, 200, 500, 200, T, 3)
    for x in [390, 440, 490]: s += Ln(x, 200, x, 240, L, 2) + P(f'M{x - 8} 240 l16 22', G, 2) + Ln(x, 262, x, 320, L, 2) + C(x, 330, 9, L, 2)
    return s
def topraklama():
    s = ground(20, 620, 300) + R(40, 300, 580, 140, '#ffffff00', 0, '#7f95b512')
    s += Ln(160, 230, 160, 420, G, 5) + Ln(130, 230, 190, 230, L, 3) + Ln(140, 214, 180, 214, L, 3) + Ln(150, 198, 170, 198, L, 3) + Ln(160, 198, 160, 170, L, 3)
    s += meter(360, 40, 'Ω')
    for x in [300, 470, 580]: s += Ln(x, 290, x, 340, T, 3)
    s += P('M160 170 Q260 150 300 290', D, 1.5, extra='stroke-dasharray="6 5"')
    return s
def olcum(disp='Ω'):
    s = meter(260, 60, disp) + R(70, 120, 120, 200, L, 2.5, F, 8) + ''.join(R(86, 140 + i * 40, 88, 22, D, 1.6) for i in range(4))
    s += P('M210 300 q30 40 40 80', D, 1.5, extra='stroke-dasharray="6 5"') + tag(430, 70, 'ölçüm') + ground(40, 600, 410)
    return s
def termal():
    g = '<defs><radialGradient id="hot" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ff6b3d"/><stop offset=".45" stop-color="#d3a467"/><stop offset="1" stop-color="#48c9c6" stop-opacity="0"/></radialGradient></defs>'
    s = g + panel(60, 80, 200, 290, 4) + C(150, 230, 46, 'none', 0, 'url(#hot)')
    s += R(350, 120, 200, 150, L, 3, '#0d2547', 14) + R(372, 140, 156, 104, T, 2, '#0a1424') + C(450, 192, 34, 'none', 0, 'url(#hot)') + Tx(450, 262, '°C', 15, G, 'middle')
    s += R(420, 270, 60, 110, L, 3) + P('M270 230 L350 190', G, 1.5, extra='stroke-dasharray="6 5"')
    return s
def trafo():
    s = ground(30, 620, 390) + R(170, 150, 300, 200, L, 3, F) + R(190, 350, 260, 40, D, 2)
    for x in range(110, 171, 12): s += Ln(x, 170, x, 330, D, 2)
    for x in range(482, 543, 12): s += Ln(x, 170, x, 330, D, 2)
    s += Ln(110, 170, 170, 170, D, 2) + Ln(470, 170, 542, 170, D, 2)
    for x in [230, 320, 410]: s += R(x - 12, 100, 24, 50, L, 2.5) + ''.join(Ln(x - 18, y, x + 18, y, L, 2) for y in [110, 122, 134]) + Ln(x, 100, x, 60, T, 2.5)
    s += bolt(330, 210, .7) + tag(380, 300, 'kVA')
    return s
def aku():
    s = ground(30, 620, 380)
    for i in range(4):
        for j in range(2):
            x, y = 110 + i * 110, 120 + j * 125
            s += R(x, y, 90, 110, L, 2.5, F, 6) + Tx(x + 22, y + 30, '+', 20, G, 'middle', 700) + Tx(x + 68, y + 30, '−', 20, T, 'middle', 700)
            s += Ln(x + 22, y, x + 22, y - 8, L, 3) + Ln(x + 68, y, x + 68, y - 8, L, 3)
    s += P('M178 112 H242 M288 112 H352 M398 112 H462', G, 2) + tag(260, 54, 'V · Ah')
    return s
def forklift(stacker=False):
    s = ground(30, 620, 380) + C(200, 350, 30, L, 3) + C(420, 350, 30, L, 3) + C(200, 350, 8, D, 2) + C(420, 350, 8, D, 2)
    s += P('M150 320 V230 H330 L380 300 H460 V320 Z', L, 3, F) + P('M250 230 V140 H340 L360 230', L, 2.5) + R(470, 60, 16, 260, L, 3) + R(490, 60, 16, 260, L, 2.5)
    s += Ln(500, 300, 600, 300, G, 4) + R(520, 230, 80, 60, T, 2.5, F) + R(516, 290, 88, 10, D, 2)
    s += C(270, 190, 9, D, 2) + tag(60, 60, 'kaldırma kapasitesi')
    return s
def kopruvinc():
    s = R(40, 60, 560, 16, L, 3, F) + R(40, 380, 560, 0.1, D, 1)
    s += R(60, 76, 18, 300, D, 2.5) + R(562, 76, 18, 300, D, 2.5) + ground(30, 610, 380)
    s += R(60, 110, 520, 30, L, 3, F) + R(280, 140, 80, 36, T, 2.5, F) + Ln(310, 176, 310, 250, L, 2) + Ln(330, 176, 330, 250, L, 2) + hook(320, 256)
    s += R(240, 300, 160, 70, D, 2.5, F) + arrow(380, 92, 460, 92, G) + arrow(260, 92, 180, 92, G) + tag(420, 200, 'SWL')
    return s
def kazan(vertical=False):
    s = ground(30, 620, 380)
    if vertical:
        s += R(240, 70, 160, 290, L, 3, F, 70) + R(260, 360, 30, 20, D, 2) + R(350, 360, 30, 20, D, 2) + R(430, 300, 90, 60, L, 2.5) + C(475, 330, 18, D, 2) + P('M400 330 H430', L, 2.5)
    else:
        s += R(90, 150, 420, 170, L, 3, F, 85) + P('M150 320 l-20 60 h60 l-20 -60 M410 320 l-20 60 h60 l-20 -60', D, 2)
    s += Ln(300, 150 if not vertical else 70, 300, 90 if not vertical else 30, L, 3) + C(300, 70 if not vertical else 10, 0.1)
    gx, gy = (420, 100) if not vertical else (180, 140)
    s += C(gx, gy, 30, G, 3, '#0d2547') + Ln(gx, gy, gx + 16, gy - 16, G, 2.5) + Ln(gx, gy + 30, gx, gy + 50, L, 3) + Tx(gx, gy + 48, 'bar', 13, G, 'middle')
    s += P('M200 150 v-40 h-24 v-20 h48 v20 h-24', T, 2.5) + Tx(200, 80, 'emniyet ventili', 13, T, 'middle')
    return s
def yangin():
    s = Ln(30, 70, 610, 70, D, 2) + ''.join(Ln(x, 70, x - 12, 58, D, 1.2) for x in range(40, 611, 18))
    for x in [130, 320, 510]: s += C(x, 95, 22, L, 2.5, F) + C(x, 95, 5, G, 0, G) + Ln(x, 70, x, 73, L, 3)
    s += Ln(60, 160, 600, 160, T, 4)
    for x in [130, 260, 390, 520]:
        s += Ln(x, 160, x, 186, T, 3) + P(f'M{x - 10} 186 h20 l-4 8 h-12 z', L, 2)
        for a in range(-50, 51, 25): s += Ln(x, 196, x + 70 * math.sin(math.radians(a)), 196 + 70 * math.cos(math.radians(a)), T, 1.2, .55, '4 6')
    s += R(70, 300, 70, 70, G, 3, '#d3a46726', 8) + C(105, 335, 16, G, 3) + ground(30, 610, 400)
    return s
def fan():
    s = R(40, 150, 360, 120, L, 3, F) + R(400, 130, 30, 160, L, 3) + C(470, 210, 90, L, 3)
    for a in range(0, 360, 72):
        r = math.radians(a); s += P(f'M470 210 Q{470 + 70*math.cos(r + .5):.0f} {210 + 70*math.sin(r + .5):.0f} {470 + 80*math.cos(r):.0f} {210 + 80*math.sin(r):.0f}', T, 3)
    s += C(470, 210, 12, G, 3)
    for y in [180, 210, 240]: s += arrow(70, y, 180, y, T) + arrow(220, y, 330, y, T)
    s += tag(60, 80, 'Q (m³/h)') + Ln(40, 330, 400, 330, D, 1.5) + ground(30, 610, 400)
    return s
def tahliye():
    s = R(40, 40, 560, 360, L, 3) + Ln(260, 40, 260, 230, L, 2.5) + Ln(40, 230, 420, 230, L, 2.5) + Ln(420, 230, 420, 400, L, 2.5) + Ln(420, 160, 600, 160, L, 2.5)
    s += ''.join(R(x, 36, 40, 8, BG, 0, BG) for x in [180, 470]) + R(540, 396, 50, 8, BG, 0, BG)
    s += arrow(140, 140, 140, 270, T, 3) + arrow(140, 300, 400, 300, T, 3) + arrow(340, 140, 470, 140, T, 3) + arrow(500, 200, 560, 380, T, 3)
    s += R(520, 330, 74, 36, T, 2, F) + Tx(557, 354, 'ÇIKIŞ', 14, T, 'middle', 700, False) + C(200, 100, 10, G, 0, G) + Tx(220, 106, 'buradasınız', 14, G)
    for x, y in [(80, 360), (300, 80), (480, 60)]: s += R(x, y, 22, 22, '#e8734a', 2, '#e8734a33', 4)
    return s
def atex():
    s = ground(30, 620, 390) + R(120, 160, 220, 230, L, 3, F, 20) + C(230, 160, 0.1)
    s += P('M120 160 Q230 110 340 160', L, 3) + Ln(230, 120, 230, 80, L, 3)
    s += C(230, 270, 160, T, 2, o=.8, extra='stroke-dasharray="10 8"') + C(230, 270, 230, D, 2, o=.7, extra='stroke-dasharray="4 8"')
    s += Tx(230, 140 - 20, 'Bölge 1', 15, T, 'middle') + Tx(430, 90, 'Bölge 2', 15, D, 'middle')
    hx, hy, r = 500, 260, 62
    s += P('M' + ' L'.join(f'{hx + r*math.cos(math.radians(a)):.0f} {hy + r*math.sin(math.radians(a)):.0f}' for a in range(30, 390, 60)) + 'Z', G, 4, '#d3a46733') + Tx(hx, hy + 14, 'Ex', 40, '#0d2547', 'middle', 800, False) + Tx(hx, hy + 12, 'Ex', 40, G, 'middle', 800, False)
    return s
def gurultu():
    s = P('M150 220 a80 80 0 1 1 160 0 v40', L, 3) + R(130, 220, 40, 80, L, 3, F, 10) + R(290, 220, 40, 80, L, 3, F, 10)
    for i in range(1, 4): s += P(f'M{360 + i*24} {160 - i*10} q{30 + i*6} {100 + i*10} 0 {200 + i*20}', T, 2.5, o=1 - i * .2)
    s += meter(470, 120, 'dB', probes=False) + C(530, 110, 14, L, 2.5) + Ln(530, 96, 530, 120, L, 2)
    return s
def toz():
    import random; rnd = random.Random(7)
    s = ''.join(C(rnd.randint(40, 380), rnd.randint(50, 380), rnd.choice([3, 4, 6, 8]), D, 1.5, '#7f95b540') for _ in range(70))
    s += R(430, 160, 130, 180, L, 3, '#0d2547', 14) + R(450, 180, 90, 40, T, 2, F, 4) + Tx(495, 207, 'mg/m³', 14, T, 'middle', 600)
    s += P('M470 160 V110 H400 V90', L, 2.5) + R(380, 60, 40, 30, G, 2.5, '#d3a46726', 6) + P('M380 75 l-40 -10 m40 10 l-40 10', D, 1.5)
    return s
def gaz(disp='LEL'):
    s = P('M60 260 q-30 -60 30 -80 q10 -60 80 -50 q40 -50 110 -10 q70 -10 70 60 q50 30 10 80 z', T, 2.5, '#48c9c61a')
    for x, y in [(120, 210), (190, 170), (250, 220), (300, 190)]: s += C(x, y, 10, T, 2) + C(x + 14, y + 8, 5, T, 1.5)
    s += meter(420, 110, disp, probes=False) + P('M480 110 V70', L, 3) + C(480, 64, 6, G, 2.5)
    return s
def voc():
    s = ''
    for cx, cy in [(150, 160), (260, 260), (130, 330)]:
        s += P('M' + ' L'.join(f'{cx + 44*math.cos(math.radians(a)):.0f} {cy + 44*math.sin(math.radians(a)):.0f}' for a in range(30, 390, 60)) + 'Z', T, 2.5) + C(cx, cy, 22, T, 1.5)
    s += R(400, 170, 140, 170, L, 3, '#0d2547', 14) + R(420, 190, 100, 40, T, 2, F, 4) + Tx(470, 217, 'ppm', 15, T, 'middle', 600) + P('M440 170 V100 H380', L, 2.5) + R(350, 90, 30, 20, G, 2.5)
    return s
def isik():
    s = Ln(320, 20, 320, 60, D, 2) + R(200, 60, 240, 26, L, 3, F, 6) + P('M210 86 L90 360 H550 L430 86', G, 1.5, '#d3a46714')
    s += ground(30, 610, 360) + R(420, 270, 110, 80, L, 3, '#0d2547', 10) + Tx(475, 320, 'lux', 20, T, 'middle', 700) + C(475, 262, 14, L, 2.5)
    s += R(120, 300, 200, 60, D, 2, F) + Ln(130, 300, 310, 300, D, 2)
    return s
def titresim():
    s = P('M60 230 ' + ' '.join(f'L{60 + i*10} {230 + (34 if i % 2 else -34) * math.exp(-((i - 26) / 18) ** 2)}' for i in range(1, 55)), T, 2.5)
    s += R(380, 120, 180, 60, L, 3, F, 12) + R(330, 135, 50, 30, G, 2.5) + R(450, 180, 40, 120, L, 3, F, 10) + tag(70, 70, 'm/s²')
    return s
def manyetik():
    s = R(260, 170, 120, 100, L, 3, F, 10)
    for i in range(6): s += Ln(270 + i * 20, 170, 270 + i * 20, 270, G, 2)
    for k in range(1, 5):
        s += P(f'M260 220 C {260 - 60*k} {220 - 50*k}, {380 + 60*k} {220 - 50*k}, 380 220', T, 1.8, o=1 - k * .15) + P(f'M260 220 C {260 - 60*k} {220 + 50*k}, {380 + 60*k} {220 + 50*k}, 380 220', T, 1.8, o=1 - k * .15)
    s += tag(470, 60, 'µT')
    return s
def termalkonfor():
    s = R(130, 60, 40, 240, L, 3, F, 20) + C(150, 330, 36, L, 3, '#e8734a33') + R(142, 160, 16, 160, '#e8734a', 0, '#e8734a', 6)
    s += P('M320 140 q-50 80 0 110 q50 -30 0 -110z', T, 3, '#48c9c61f') + Tx(320, 300, '%RH', 16, T, 'middle')
    for y in [150, 200, 250]: s += P(f'M420 {y} h120 q30 0 30 -20 q0 -20 -20 -20', L, 2.5)
    s += Tx(500, 300, 'm/s', 16, L, 'middle')
    return s
def agirmetal():
    s = ''
    for i, el in enumerate(['Pb', 'Cr', 'Cd', 'Ni']):
        x = 70 + (i % 2) * 140; y = 80 + (i // 2) * 140
        s += R(x, y, 120, 120, L, 3, F, 8) + Tx(x + 60, y + 76, el, 40, G, 'middle', 700, False)
    s += R(420, 170, 130, 170, L, 3, '#0d2547', 14) + R(440, 190, 90, 40, T, 2, F, 4) + Tx(485, 217, 'µg/m³', 14, T, 'middle', 600) + P('M470 170 V110 H390', L, 2.5)
    return s
def makasli():
    s = ground(30, 620, 390) + R(170, 340, 300, 30, L, 3, F) + C(200, 378, 12, L, 2.5) + C(440, 378, 12, L, 2.5)
    for k in range(4):
        y = 340 - k * 60; s += Ln(190, y, 450, y - 60, L, 2.5) + Ln(450, y, 190, y - 60, L, 2.5)
    s += R(160, 90, 320, 20, L, 3, F) + Ln(160, 50, 480, 50, T, 2.5) + ''.join(Ln(x, 50, x, 90, T, 2) for x in range(170, 481, 40)) + person(320, 90, 1, D)
    s += dimv(110, 90, 390, 'h')
    return s
def jenerator():
    s = ground(30, 620, 380) + R(90, 150, 460, 220, L, 3, F, 10) + ''.join(Ln(x, 180, x, 340, D, 2) for x in range(120, 300, 18))
    s += R(340, 180, 180, 120, L, 2.5) + R(360, 200, 70, 40, T, 2, F) + C(470, 220, 20, G, 2.5) + P('M480 150 V90 h30', L, 3) + P('M520 80 q10 -20 0 -40 q-10 -20 0 -40', D, 2)
    s += bolt(240, 200, .6) + tag(360, 320, 'kVA')
    return s
def kompanzasyon():
    s = R(80, 60, 260, 330, L, 3, '#0d2547', 8)
    for i in range(3):
        for j in range(2): s += R(110 + i * 76, 90 + j * 140, 56, 110, L, 2.5, F, 26) + Ln(138 + i * 76, 90 + j * 140, 138 + i * 76, 80 + j * 140, G, 3)
    s += R(400, 120, 180, 120, L, 3, F, 10) + Tx(490, 175, 'cos φ', 24, T, 'middle', 700) + Tx(490, 210, 'kVAr', 15, G, 'middle') + ground(30, 610, 400)
    return s
def katodik():
    s = ground(20, 620, 150) + R(20, 150, 600, 280, '#ffffff00', 0, '#7f95b512') + R(60, 250, 520, 50, L, 3, F, 25)
    s += R(450, 340, 50, 70, G, 2.5, '#d3a46726', 8) + R(300, 40, 120, 80, L, 3, F, 8) + Tx(360, 88, 'mV', 18, T, 'middle', 700)
    s += P('M330 120 V250 M390 120 Q460 200 475 340', T, 2.5) + Tx(475, 432, 'anot', 14, G, 'middle')
    return s
def enerji():
    s = R(60, 60, 520, 230, L, 3, '#0a1424', 10)
    s += P('M80 175 ' + ' '.join(f'L{80 + i*4} {175 - 70*math.sin(i/12) - 16*math.sin(3*i/12) - 9*math.sin(5*i/12)}' for i in range(1, 121)), T, 2.5)
    for i, h in enumerate([150, 60, 38, 24, 16, 10]): s += R(110 + i * 70, 400 - h, 40, h, G if i else T, 2, '#d3a46733' if i else F)
    s += Tx(320, 430, 'THD · harmonikler', 15, D, 'middle')
    return s
def ark():
    s = panel(80, 90, 200, 290, 4)
    for a in range(0, 360, 24):
        r = math.radians(a); s += Ln(380 + 30*math.cos(r), 230 + 30*math.sin(r), 380 + 110*math.cos(r), 230 + 110*math.sin(r), G if a % 48 else '#e8734a', 2.5)
    s += C(380, 230, 26, G, 3, '#d3a46744') + tag(440, 60, 'cal/cm²')
    return s
def zincir():
    s = hook(320, 40)
    for i in range(7): s += R(306 if i % 2 else 312, 80 + i * 30, 28 if i % 2 else 16, 36, L, 3, rx=10)
    s += P('M150 300 q170 -120 340 0', T, 4) + hook(150, 306, T) + hook(490, 306, T) + R(130, 340, 380, 60, D, 2.5, F) + tag(420, 120, 'WLL')
    return s
def caraskal():
    s = Ln(60, 50, 580, 50, L, 4) + R(270, 50, 100, 26, L, 2.5) + R(280, 90, 80, 90, L, 3, F, 12) + C(320, 135, 24, T, 2.5)
    s += ''.join(R(316, 190 + i * 22, 8, 18, L, 2, rx=4) for i in range(5)) + hook(320, 310) + R(240, 340, 160, 60, D, 2.5, F) + P('M360 180 q60 40 30 120', D, 2, extra='stroke-dasharray="4 6"')
    return s
def harita(pin='OSB'):
    s = P('M40 300 Q160 260 260 290 T470 270 T610 300 V420 H40 Z', T, 2, '#48c9c61a')
    for x in range(60, 600, 60): s += Ln(x, 40, x - 20, 270, D, 1, .5)
    for y in range(70, 270, 50): s += Ln(40, y, 600, y + 10, D, 1, .5)
    for x, y, w, h in [(110, 140, 70, 50), (210, 110, 90, 70), (340, 150, 60, 40), (430, 100, 80, 70)]:
        s += R(x, y, w, h, L, 2.5, F) + P(f'M{x} {y} l{w/4} -18 v18 l{w/4} -18 v18', L, 2)
    s += P('M320 40 q-30 0 -30 30 q0 24 30 60 q30 -36 30 -60 q0 -30 -30 -30z', G, 3, '#d3a46744') + C(320, 70, 9, G, 2.5) + tag(360, 40, pin)
    return s
def cizim():
    s = R(60, 40, 520, 360, L, 3, F) + R(380, 320, 200, 80, L, 2) + Ln(380, 345, 580, 345, L, 1.5) + Ln(480, 320, 480, 400, L, 1.5)
    s += Tx(390, 338, 'PROJE', 11, D) + Tx(490, 338, 'PAFTA', 11, D) + Tx(390, 368, 'ÖLÇEK', 11, D) + Tx(490, 368, 'ONAY', 11, D)
    s += R(100, 80, 240, 160, T, 2) + Ln(220, 80, 220, 240, T, 1.5) + Ln(100, 160, 340, 160, T, 1.5) + dimh(100, 340, 268, 'L') + C(440, 150, 50, G, 2) + Ln(440, 100, 440, 200, G, 1) + Ln(390, 150, 490, 150, G, 1)
    return s
def kontrol():
    s = R(170, 50, 300, 360, L, 3, F, 12) + R(260, 34, 120, 32, L, 3, '#0d2547', 8)
    for i in range(5):
        y = 110 + i * 56; s += R(200, y, 26, 26, T, 2.5, rx=4) + P(f'M206 {y + 13} l6 7 l12 -14', T, 3) + Ln(244, y + 13, 430, y + 13, D, 2)
    s += P('M490 380 q0 -60 60 -60 q60 0 60 60 z', G, 3, '#d3a46726') + R(480, 378, 140, 12, G, 2.5, rx=4)
    return s
def kiris():
    s = R(80, 180, 480, 26, L, 3, F) + P('M80 206 l-20 34 h40 z M560 206 l-20 34 h40 z', L, 2.5)
    for x in range(110, 541, 43): s += arrow(x, 110, x, 174, G, 2)
    s += Ln(100, 110, 540, 110, G, 1.5) + Tx(320, 96, 'q', 18, G, 'middle', 700) + P('M80 300 Q320 400 560 300', T, 2.5, '#48c9c61f') + Ln(80, 300, 560, 300, D, 1.5) + Tx(320, 350, 'M', 18, T, 'middle', 700)
    return s
def soru():
    s = C(320, 210, 140, L, 3, F) + Tx(320, 262, '?', 150, T, 'middle', 800, False)
    return s

MOTIFS = {k: v for k, v in globals().items() if callable(v) and k not in ('P', 'R', 'C', 'Ln', 'Tx', 'ground', 'dimv', 'dimh', 'tag', 'arrow', 'bolt', 'hook', 'person', 'lattice', 'meter', 'building', 'panel')}
