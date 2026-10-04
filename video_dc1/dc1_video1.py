"""
DC 1 · Video 1: Zahlensysteme – Dezimal, Binär, Hexadezimal
Umsetzung von Drehbuch_DC1_Video1_Inhalte.md mit Manim (Community Edition)
und manim-voiceover.

Jede Drehbuch-Szene ist eine eigene Manim-Szene (Szene0_… bis Szene8_…).
Der Sprechtext steht direkt im Code: `with self.sage("…"):` lässt die
KI-Stimme den Satz sprechen; die Animationen im Block laufen gleichzeitig,
danach wartet die Szene, bis der Satz zu Ende gesprochen ist.

Für die Stimme sind Hex-Ziffern mit Leerzeichen und Ziffern als Wörter
geschrieben („A D“, „acht null“), damit die Sprachausgabe sie nicht als
„A bis D“ oder als Spielstand „8 zu 0“ vorliest.

Vorschau einer Szene:   manim -pql dc1_video1.py Szene1_Stellenwertsystem
Alles in Full HD:       python render.py
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.background_color = "#FAFAF7"


def sprachdienst():
    """Hier die Stimme wechseln, z. B. ElevenLabsService, OpenAIService, AzureService
    oder RecorderService (eigene Stimme aufnehmen)."""
    return GTTSService(lang="de", tld="de")


# ---------------------------------------------------------------- Farben, Schriften
INK = "#222222"
GRAU = "#8A8A8A"
HELLGRAU = "#E6E6E1"
DEZ = "#1F5FBF"      # Dezimal: blau
BIN = "#2E8B3E"      # Binär: grün
HEX = "#D9730D"      # Hexadezimal: orange
ROT = "#C0392B"      # Hinweise

MONO = "Consolas"
SANS = "Segoe UI"


def mono(s, color=INK, size=48, **kw):
    return Text(s, font=MONO, color=color, font_size=size, **kw)


def sans(s, color=INK, size=36, **kw):
    return Text(s, font=SANS, color=color, font_size=size, **kw)


def markup(s, color=INK, size=48, font=MONO):
    return MarkupText(s, font=font, color=color, font_size=size)


def zahl(ziffern, basis, color, size=96):
    """Zahl mit Basis als Index, z. B. AD₁₆."""
    return markup(f'{ziffern}<sub>{basis}</sub>', color, size)


def span(s, color):
    return f'<span fgcolor="{color}">{s}</span>'


def teil(mob, s, sub, start=0):
    """Die Zeichen von `sub` innerhalb des Text-Objekts `mob` (Leerzeichen zählen nicht mit)."""
    i = s.index(sub, start)
    a = len("".join(s[:i].split()))
    b = a + len("".join(sub.split()))
    return mob[a:b]


def zeichenbreite(size):
    return mono("0" * 20, size=size).width / 20


def merksatz(text, color=INK, size=34):
    t = sans(text, color, size, weight=BOLD)
    box = RoundedRectangle(
        corner_radius=0.12, width=t.width + 0.7, height=t.height + 0.5,
        stroke_color=color, stroke_width=3, fill_color=WHITE, fill_opacity=1,
    ).move_to(t)
    return VGroup(box, t)


def stellen(ziffern, werte, color, size=110, abstand=1.3, wsize=30):
    """Ziffern nebeneinander, darüber klein und grau die Stellenwerte.
    Rückgabe: (ziffern_gruppe, werte_gruppe)."""
    zg = VGroup(*[mono(z, color, size) for z in ziffern])
    wg = VGroup(*[mono(str(w), GRAU, wsize) for w in werte])
    for i, (z, w) in enumerate(zip(zg, wg)):
        z.move_to(RIGHT * i * abstand)
        w.move_to(RIGHT * i * abstand)
    VGroup(zg, wg).move_to(ORIGIN)
    oben = zg.get_top()[1] + 0.45
    for w in wg:
        w.set_y(oben)
    return zg, wg


class Szene(VoiceoverScene):
    titel = ""

    def setup(self):
        super().setup()
        self.set_speech_service(sprachdienst())
        self.kopfzeile = None
        if self.titel:
            self.kopfzeile = sans(self.titel, GRAU, 26).to_corner(UL, buff=0.4)
            self.add(self.kopfzeile)

    def sage(self, text):
        return self.voiceover(text=text)

    def pause(self):
        """Entspricht [Pause] im Drehbuch."""
        self.wait(0.8)

    def ausblenden(self):
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ================================================================ Szene 0
class Szene0_Einstieg(Szene):
    def construct(self):
        code_s = "color: #FF8000;"
        code = mono(code_s, INK, 56)
        box = RoundedRectangle(
            corner_radius=0.15, width=code.width + 1.0, height=code.height + 0.9,
            fill_color=HELLGRAU, fill_opacity=1, stroke_width=0,
        ).move_to(code)
        quelltext = VGroup(box, code).move_to(LEFT * 2.2 + UP * 0.3)
        quadrat = Square(2.2, fill_color="#FF8000", fill_opacity=1, stroke_width=0)
        quadrat.next_to(quelltext, RIGHT, buff=1.2)

        with self.sage("Wenn wir uns den Quelltext einer Webseite anschauen, finden wir solche "
                       "Angaben: Raute F F acht null null null."):
            self.play(FadeIn(quelltext, shift=UP * 0.2))
        with self.sage("Das ist eine Farbe – genauer gesagt dieses Orange."):
            self.play(FadeIn(quadrat, scale=0.8))

        ff = teil(code, code_s, "FF")
        frage = sans("Buchstaben in einer Zahl?", ROT, 36).next_to(quelltext, UP, buff=1.0)
        pfeil = Arrow(frage.get_bottom(), ff.get_top(), buff=0.15, color=ROT, stroke_width=4)
        with self.sage("Aber warum stehen da Buchstaben zwischen den Ziffern?"):
            self.play(ff.animate.set_color(ROT), FadeIn(frage), GrowArrow(pfeil))
        self.pause()

        hex_t = sans("Hexadezimalsystem", HEX, 56, weight=BOLD).to_edge(DOWN, buff=1.6)
        with self.sage("Das ist eine Zahl im Hexadezimalsystem."):
            self.play(Write(hex_t))

        drei = VGroup(
            sans("Dezimal", DEZ, 36), sans("·", GRAU, 36),
            sans("Binär", BIN, 36), sans("·", GRAU, 36),
            sans("Hexadezimal", HEX, 36),
        ).arrange(RIGHT, buff=0.3).next_to(hex_t, DOWN, buff=0.4)
        with self.sage("In diesem Video lernen wir, wie das Hexadezimalsystem funktioniert und wie "
                       "es mit dem Binärsystem und unserem Dezimalsystem zusammenhängt."):
            self.play(FadeIn(drei, shift=UP * 0.2))
        with self.sage("Und am Ende können wir diesen Farbcode selbst entschlüsseln."):
            self.play(Circumscribe(quelltext, color=HEX, buff=0.1))
        self.ausblenden()


# ================================================================ Szene 1
class Szene1_Stellenwertsystem(Szene):
    titel = "Was ist ein Stellenwertsystem?"

    def construct(self):
        zg, wg = stellen("173", [100, 10, 1], DEZ, abstand=1.8)
        VGroup(zg, wg).shift(UP * 1.0)

        with self.sage("Fangen wir mit etwas an, das wir schon kennen: unserem Dezimalsystem. "
                       "Nehmen wir die Zahl 173."):
            self.play(Write(zg))

        namen = ["Hunderter", "Zehner", "Einer"]
        namen_g = VGroup(*[sans(n, GRAU, 24).next_to(zg[i], DOWN, buff=0.3) for i, n in enumerate(namen)])
        with self.sage("Die 3 steht ganz rechts an der Einerstelle, die 7 an der Zehnerstelle, "
                       "die 1 an der Hunderterstelle.") as t:
            for i in (2, 1, 0):
                self.play(Indicate(zg[i], color=DEZ), FadeIn(wg[i], shift=DOWN * 0.2),
                          FadeIn(namen_g[i]), run_time=t.duration / 3)

        gl_s = "1 · 100 + 7 · 10 + 3 · 1 = 173"
        gl = mono(gl_s, INK, 44).next_to(namen_g, DOWN, buff=0.8)
        for z in ("1 ", "7 ", "3 "):
            teil(gl, gl_s, z).set_color(DEZ)
        with self.sage("Die Zahl bedeutet also: 1 mal 100 plus 7 mal 10 plus 3 mal 1.") as t:
            self.play(FadeOut(namen_g), Write(gl), run_time=t.duration)
        self.pause()

        potenzen = VGroup(*[
            markup(f"10<sup>{p}</sup>", GRAU, 32).move_to(w) for p, w in zip((2, 1, 0), wg)
        ])
        with self.sage("Die Stellenwerte 1, 10, 100 sind Potenzen von 10, von rechts beginnend "
                       "mit 10 hoch null."):
            self.play(*[ReplacementTransform(w, p) for w, p in zip(wg, potenzen)])

        index = mono("10", DEZ, 44).next_to(zg, DR, buff=0.05).shift(UP * 0.15)
        basis = sans("Basis 10  →  Ziffern 0 bis 9", DEZ, 36).next_to(gl, DOWN, buff=0.6)
        with self.sage("Die 10 nennt man die Basis des Systems. Deshalb gibt es auch genau zehn "
                       "Ziffern, von 0 bis 9."):
            self.play(FadeIn(index, shift=LEFT * 0.2), FadeIn(basis))

        ms = merksatz("Stellenwerte = Potenzen der Basis").to_edge(DOWN, buff=0.5)
        with self.sage("Ein solches System heißt Stellenwertsystem: Was eine Ziffer wert ist, "
                       "hängt davon ab, an welcher Stelle sie steht."):
            self.play(FadeOut(basis), FadeIn(ms, shift=UP * 0.2))
        self.pause()

        with self.sage("Und jetzt das Entscheidende: Die Basis muss nicht 10 sein."):
            self.play(Indicate(index, color=ROT, scale_factor=1.5))
        self.ausblenden()


# ================================================================ Szene 2
class Szene2_Binaer(Szene):
    titel = "Das Binärsystem"

    def construct(self):
        def zustand(an, text, ziffer):
            kreis = Circle(0.7, stroke_color=BIN if an else GRAU, stroke_width=4,
                           fill_color=BIN if an else WHITE, fill_opacity=1)
            return VGroup(kreis, sans(text, GRAU, 30).next_to(kreis, DOWN, buff=0.3),
                          mono(ziffer, BIN, 72).next_to(kreis, UP, buff=0.3))

        aus = zustand(False, "Strom aus", "0")
        an = zustand(True, "Strom an", "1")
        zustaende = VGroup(aus, an).arrange(RIGHT, buff=2.5)
        with self.sage("Computer arbeiten mit nur zwei Zuständen: Strom an oder aus,"):
            self.play(FadeIn(aus[:2]), FadeIn(an[:2]))
        with self.sage("eins oder null."):
            self.play(FadeIn(aus[2], shift=DOWN * 0.2), FadeIn(an[2], shift=DOWN * 0.2))
        kopf = sans("Basis 2  ·  Ziffern: 0, 1", BIN, 44, weight=BOLD).to_edge(UP, buff=1.1)
        with self.sage("Darum verwenden sie das Binärsystem mit der Basis 2. Es gibt nur zwei "
                       "Ziffern, 0 und 1."):
            self.play(FadeIn(kopf, shift=DOWN * 0.2))
        self.play(FadeOut(zustaende))

        werte = [32, 16, 8, 4, 2, 1]
        reihe = VGroup(*[mono(str(w), INK, 56) for w in werte]).arrange(RIGHT, buff=1.4).shift(DOWN * 0.2)
        boegen = VGroup()
        for rechts, links in zip(reihe[1:], reihe[:-1]):
            b = CurvedArrow(rechts.get_top() + UP * 0.2, links.get_top() + UP * 0.2,
                            angle=PI / 2, color=GRAU, stroke_width=3, tip_length=0.18)
            lab = mono("·2", GRAU, 28).next_to(b, UP, buff=0.08)
            boegen.add(VGroup(b, lab))
        with self.sage("Die Stellenwerte sind Potenzen von 2: von rechts 1, 2, 4, 8, dann 16, 32 "
                       "und so weiter. Jede Stelle ist doppelt so viel wert wie die rechts daneben."):
            self.play(FadeIn(reihe[-1]))
            for i in range(len(werte) - 2, -1, -1):
                self.play(Create(boegen[i][0]), FadeIn(boegen[i][1]), FadeIn(reihe[i]), run_time=0.8)
        self.play(FadeOut(reihe), FadeOut(boegen))

        zg, wg = stellen("1101", [8, 4, 2, 1], BIN, abstand=1.4)
        VGroup(zg, wg).shift(UP * 0.6)
        with self.sage("Schauen wir uns die Binärzahl eins eins null eins an."):
            self.play(FadeIn(wg), Write(zg))

        produkte = VGroup()
        for i, (z, w) in enumerate(zip("1101", [8, 4, 2, 1])):
            farbe = INK if z == "1" else GRAU
            produkte.add(mono(f"{z}·{w}", farbe, 32).next_to(zg[i], DOWN, buff=0.5))
        with self.sage("Ganz rechts eine 1 an der Einerstelle: 1. Dann eine 0 an der Zweierstelle: "
                       "nichts. Dann eine 1 an der Viererstelle: 4. Und eine 1 an der Achterstelle: 8.") as t:
            for i in (3, 2, 1, 0):
                self.play(Indicate(zg[i], color=BIN), FadeIn(produkte[i], shift=DOWN * 0.2),
                          run_time=t.duration / 4)

        summe = mono("8 + 4 + 1 = 13", INK, 48).next_to(produkte, DOWN, buff=0.6)
        teil(summe, "8 + 4 + 1 = 13", "13").set_color(DEZ)
        index = mono("2", BIN, 44).next_to(zg, DR, buff=0.05).shift(UP * 0.15)
        with self.sage("Zusammen: 8 plus 4 plus 1 gleich 13."):
            self.play(Write(summe), FadeIn(index))
        self.pause()

        ms = merksatz("Ziffer · Stellenwert, dann addieren").to_edge(DOWN, buff=0.5)
        with self.sage("Das Prinzip ist genau dasselbe wie im Dezimalsystem: Ziffer mal Stellenwert, "
                       "dann addieren."):
            self.play(FadeIn(ms, shift=UP * 0.2))

        self.play(*[FadeOut(m) for m in (zg, wg, produkte, summe, index, ms)])
        lang = markup(f'{span("200", DEZ)}<sub>{span("10", DEZ)}</sub> = '
                      f'{span("11001000", BIN)}<sub>{span("2", BIN)}</sub>', INK, 72)
        bits = teil(lang, "20010=110010002", "11001000", 5)
        klammer = Brace(bits, DOWN, color=ROT)
        acht = sans("8 Stellen!", ROT, 36).next_to(klammer, DOWN, buff=0.2)
        with self.sage("Der Nachteil: Binärzahlen werden schnell sehr lang."):
            self.play(Write(lang))
        with self.sage("Schon die Zahl 200 braucht acht Stellen. Für Menschen ist das schwer zu lesen."):
            self.play(GrowFromCenter(klammer), FadeIn(acht))
        self.ausblenden()


# ================================================================ Szene 3
class Szene3_Hexadezimal(Szene):
    titel = "Das Hexadezimalsystem"

    def construct(self):
        kopf = sans("Basis 16  →  16 Ziffern nötig", HEX, 44, weight=BOLD).to_edge(UP, buff=1.1)
        with self.sage("Hier kommt das Hexadezimalsystem ins Spiel. Es hat die Basis 16. Das heißt: "
                       "Wir brauchen sechzehn verschiedene Ziffern."):
            self.play(FadeIn(kopf, shift=DOWN * 0.2))

        ziffern = VGroup(*[mono(z, HEX, 64) for z in "0123456789ABCDEF"]).arrange(RIGHT, buff=0.32)
        ziffern.shift(UP * 0.6)
        with self.sage("Die Ziffern 0 bis 9 haben wir schon."):
            self.play(LaggedStart(*[FadeIn(z) for z in ziffern[:10]], lag_ratio=0.15))

        werte = VGroup(*[mono(str(10 + k), INK, 30).next_to(z, DOWN, buff=0.35)
                         for k, z in enumerate(ziffern[10:])])
        with self.sage("Für die Werte 10 bis 15 nimmt man Buchstaben:"):
            pass
        with self.sage("A steht für 10, B für 11, C für 12, D für 13, E für 14 und F für 15.") as t:
            for z, w in zip(ziffern[10:], werte):
                self.play(FadeIn(z, scale=1.4), FadeIn(w, shift=UP * 0.1), run_time=t.duration / 6)

        wg = VGroup(*[mono(str(w), INK, 40) for w in (4096, 256, 16, 1)]).arrange(RIGHT, buff=0.9)
        wg.next_to(werte, DOWN, buff=1.0)
        lab = sans("Stellenwerte:", GRAU, 30).next_to(wg, LEFT, buff=0.6)
        VGroup(lab, wg).set_x(0)
        with self.sage("Die Stellenwerte sind Potenzen von 16: von rechts 1, dann 16, dann 256, "
                       "dann 4096.") as t:
            self.play(FadeIn(lab), LaggedStart(*[FadeIn(w) for w in reversed(wg)], lag_ratio=0.6),
                      run_time=t.duration)
        self.pause()

        self.play(*[FadeOut(m) for m in (kopf, ziffern, werte, wg, lab)])

        zeilen = [
            ("System", "Basis", "Ziffern", "Stellenwerte"),
            ("Dezimal", "10", "0–9", "… 1000, 100, 10, 1"),
            ("Binär", "2", "0, 1", "… 8, 4, 2, 1"),
            ("Hexadezimal", "16", "0–9, A–F", "… 4096, 256, 16, 1"),
        ]
        farben = [INK, DEZ, BIN, HEX]
        spalten_x = [-5.0, -1.6, 0.6, 3.0]
        tab = VGroup()
        for r, (zeile, farbe) in enumerate(zip(zeilen, farben)):
            y = 1.6 - r * 1.1
            reihe = VGroup()
            for c, (txt, x) in enumerate(zip(zeile, spalten_x)):
                if r == 0:
                    t = sans(txt, GRAU, 30, weight=BOLD)
                elif c == 0:
                    t = sans(txt, farbe, 34, weight=BOLD)
                else:
                    t = mono(txt, INK, 32)
                t.move_to([x, y, 0], aligned_edge=LEFT)
                reihe.add(t)
            tab.add(reihe)
        linie = Line([tab.get_left()[0], 1.05, 0], [tab.get_right()[0], 1.05, 0], color=GRAU, stroke_width=2)
        VGroup(tab, linie).move_to(DOWN * 0.2)

        with self.sage("Hier noch einmal alle drei Systeme im Überblick."):
            self.play(FadeIn(tab[0]), Create(linie))
        with self.sage("Jedes hat eine Basis, so viele Ziffern, wie die Basis angibt, und Stellenwerte, "
                       "die Potenzen der Basis sind."):
            for reihe in tab[1:]:
                self.play(FadeIn(reihe, shift=RIGHT * 0.3), run_time=0.8)
        self.ausblenden()


# ================================================================ Szene 4
class Szene4_HexNachDez(Szene):
    titel = "Hexadezimal → Dezimal"

    def construct(self):
        zg, wg = stellen("AD", [16, 1], HEX, abstand=1.6)
        VGroup(zg, wg).shift(UP * 1.4)
        index = mono("16", HEX, 44).next_to(zg, DR, buff=0.05).shift(UP * 0.15)
        with self.sage("Wie viel ist dann die Hexadezimalzahl A D? Wir gehen vor wie gewohnt: "
                       "jede Ziffer mal ihren Stellenwert."):
            self.play(Write(zg), FadeIn(index), FadeIn(wg))

        s1 = "D:  13 ·  1 =  13"
        s2 = "A:  10 · 16 = 160"
        r1 = mono(s1, INK, 44)
        r2 = mono(s2, INK, 44)
        rechnung = VGroup(r1, r2).arrange(DOWN, aligned_edge=RIGHT, buff=0.35).next_to(zg, DOWN, buff=0.8)
        for r, s, h in ((r1, s1, "D"), (r2, s2, "A")):
            teil(r, s, h).set_color(HEX)
        teil(r1, s1, "13", s1.index("=")).set_color(DEZ)
        teil(r2, s2, "160").set_color(DEZ)

        with self.sage("Das D steht an der Einerstelle und ist 13 wert: 13 mal 1 gleich 13."):
            self.play(Indicate(zg[1], color=HEX), FadeIn(r1, shift=DOWN * 0.2))
        with self.sage("Das A steht an der Sechzehnerstelle und ist 10 wert: 10 mal 16 gleich 160."):
            self.play(Indicate(zg[0], color=HEX), FadeIn(r2, shift=DOWN * 0.2))

        summe_s = "160 + 13 = 173"
        summe = mono(summe_s, INK, 44).next_to(rechnung, DOWN, buff=0.5).align_to(rechnung, RIGHT)
        teil(summe, summe_s, "173").set_color(DEZ)
        with self.sage("Zusammen: 160 plus 13 gleich 173."):
            self.play(Write(summe))
        self.pause()

        ergebnis = markup(f'{span("AD", HEX)}<sub>{span("16", HEX)}</sub> = '
                          f'{span("173", DEZ)}<sub>{span("10", DEZ)}</sub>', INK, 72)
        ergebnis.to_edge(DOWN, buff=0.6)
        rahmen = SurroundingRectangle(ergebnis, color=INK, buff=0.25, stroke_width=2)
        with self.sage("A D im Hexadezimalsystem ist also dieselbe Zahl wie 173 im Dezimalsystem."):
            self.play(FadeIn(ergebnis, shift=UP * 0.2), Create(rahmen))
        self.ausblenden()


# ================================================================ Szene 5
class Szene5_Division(Szene):
    titel = "Dezimal → Hexadezimal und Binär"

    def construct(self):
        kopf = sans("Fortgesetzte Division mit Rest", INK, 40, weight=BOLD).to_edge(UP, buff=1.0)
        frage = markup(f'{span("173", DEZ)}<sub>{span("10", DEZ)}</sub>  →  '
                       f'{span("?", HEX)}<sub>{span("16", HEX)}</sub>', INK, 80).shift(UP * 0.6)
        regel = VGroup(
            sans("1.  Immer wieder durch die Basis teilen", INK, 34),
            sans("2.  Jedes Mal den Rest notieren", INK, 34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(frage, DOWN, buff=0.8)
        with self.sage("Und wie kommt man umgekehrt von 173 auf A D?"):
            self.play(FadeIn(frage))
        with self.sage("Dafür gibt es ein Verfahren: die fortgesetzte Division mit Rest."):
            self.play(FadeIn(kopf, shift=DOWN * 0.2))
        with self.sage("Man teilt die Zahl immer wieder durch die Basis, hier also durch 16,"):
            self.play(FadeIn(regel[0], shift=RIGHT * 0.2))
        with self.sage("und notiert jedes Mal den Rest."):
            self.play(FadeIn(regel[1], shift=RIGHT * 0.2))
        self.pause()
        self.play(FadeOut(frage), FadeOut(regel))

        # ---- Teil A: nach Hexadezimal
        a_s = "173 : 16 = 10  Rest 13  → D\n 10 : 16 =  0  Rest 10  → A"
        blockA = mono(a_s, INK, 40, line_spacing=1.2).shift(UP * 0.6)
        teil(blockA, a_s, "173").set_color(DEZ)
        for sub, start in (("13", 20), ("D", 0), ("10", 40), ("A", 0)):
            teil(blockA, a_s, sub, start).set_color(HEX)
        zeile1 = teil(blockA, a_s, "173 : 16 = 10  Rest 13")
        pfeil1 = teil(blockA, a_s, "→ D")
        zeile2 = teil(blockA, a_s, "10 : 16 =  0  Rest 10", 20)
        pfeil2 = teil(blockA, a_s, "→ A")

        with self.sage("173 geteilt durch 16 ergibt 10, Rest 13. Denn 10 mal 16 sind 160, und bis "
                       "173 fehlen noch 13."):
            self.play(Write(zeile1), run_time=1.5)
        with self.sage("Rest 13, das ist die Hexadezimalziffer D."):
            self.play(FadeIn(pfeil1, shift=LEFT * 0.2))

        quot = teil(blockA, a_s, "10", 8)
        ziel = teil(blockA, a_s, "10", 25)
        with self.sage("Jetzt rechnen wir mit dem Ergebnis weiter: 10 geteilt durch 16 ergibt 0, "
                       "Rest 10."):
            self.play(Indicate(quot, color=DEZ))
            self.play(TransformFromCopy(quot, ziel))
            self.play(Write(zeile2[2:]), run_time=1.3)
        with self.sage("Rest 10, das ist die Ziffer A."):
            self.play(FadeIn(pfeil2, shift=LEFT * 0.2))

        null = teil(blockA, a_s, "0", 34)
        fertig = sans("Ergebnis 0 → fertig", GRAU, 26).next_to(blockA, DOWN, buff=0.4).align_to(null, LEFT)
        with self.sage("Sobald das Ergebnis 0 ist, sind wir fertig."):
            self.play(Create(SurroundingRectangle(null, color=GRAU, buff=0.08)), FadeIn(fertig))
        self.pause()

        D = teil(blockA, a_s, "D", 20)
        A = teil(blockA, a_s, "A", 40)
        hoch = Arrow(A.get_bottom() + DOWN * 0.1 + RIGHT * 0.6, D.get_top() + UP * 0.1 + RIGHT * 0.6,
                     buff=0, color=ROT, stroke_width=5)
        hoch_lab = sans("von unten\nnach oben", ROT, 24).next_to(hoch, RIGHT, buff=0.2)
        ergA = zahl("AD", "16", HEX, 80).next_to(fertig, DOWN, buff=0.5).set_x(blockA.get_x())
        with self.sage("Jetzt kommt der wichtige Schritt: Wir lesen die Reste von unten nach oben."):
            self.play(GrowArrow(hoch), FadeIn(hoch_lab))
        with self.sage("Also erst A, dann D: A D. Das passt zu unserer Rechnung von eben."):
            self.play(TransformFromCopy(A, ergA[0]))
            self.play(TransformFromCopy(D, ergA[1]), FadeIn(ergA[2:]))
        self.pause()

        # ---- Teil B: nach Binär
        teilA = Group(*[m for m in self.mobjects if m not in (kopf, self.kopfzeile)])
        trenner = DashedLine(UP * 2.3, DOWN * 3.3, color=HELLGRAU, stroke_width=3).shift(RIGHT * 0.9)

        b_s = "13 : 2 = 6  Rest 1\n 6 : 2 = 3  Rest 0\n 3 : 2 = 1  Rest 1\n 1 : 2 = 0  Rest 1"
        blockB = mono(b_s, INK, 34, line_spacing=1.2).move_to(RIGHT * 3.6 + UP * 0.6)
        teil(blockB, b_s, "13").set_color(DEZ)
        zeilen = b_s.split("\n")
        start = 0
        reste = []
        zeilen_mob = []
        for z in zeilen:
            pos = b_s.index(z, start)
            zeilen_mob.append(teil(blockB, b_s, z.strip(), pos))
            rest = teil(blockB, b_s, z[-1], pos + len(z) - 1)
            rest.set_color(BIN)
            reste.append(rest)
            start = pos + len(z)

        with self.sage("Dasselbe Verfahren funktioniert für das Binärsystem, dann teilt man eben "
                       "durch 2. Nehmen wir die 13."):
            self.play(teilA.animate.scale(0.72).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3))
            self.play(Create(trenner))
        with self.sage("13 geteilt durch 2 ist 6, Rest 1. 6 geteilt durch 2 ist 3, Rest 0. "
                       "3 geteilt durch 2 ist 1, Rest 1. 1 geteilt durch 2 ist 0, Rest 1.") as t:
            for zm in zeilen_mob:
                self.play(Write(zm), run_time=t.duration / 4)

        hochB = Arrow(reste[-1].get_bottom() + DOWN * 0.1 + RIGHT * 0.45,
                      reste[0].get_top() + UP * 0.1 + RIGHT * 0.45, buff=0, color=ROT, stroke_width=5)
        ergB = zahl("1101", "2", BIN, 72).next_to(blockB, DOWN, buff=0.7)
        with self.sage("Von unten nach oben gelesen: eins eins null eins."):
            self.play(GrowArrow(hochB), run_time=0.8)
            for k, r in enumerate(reversed(reste)):
                self.play(TransformFromCopy(r, ergB[k]), run_time=0.5)
            self.play(FadeIn(ergB[4:]), run_time=0.4)
        haken = sans("✓ wie vorhin", BIN, 30).next_to(ergB, DOWN, buff=0.3)
        with self.sage("Genau die Binärzahl, die wir vorhin hatten."):
            self.play(FadeIn(haken))
        self.ausblenden()


# ================================================================ Szene 6
def tab_eintrag(h, size=36):
    a = zeichenbreite(size)
    d = mono(h, HEX, size).move_to(ORIGIN)
    eq = mono("=", GRAU, size).move_to(RIGHT * 2 * a)
    b = mono(f"{int(h, 16):04b}", BIN, size).move_to(RIGHT * 6 * a)
    return VGroup(d, eq, b)


class Szene6_HexBinaer(Szene):
    titel = "Hexadezimal ↔ Binär"

    def construct(self):
        gl = markup(f'{span("13", DEZ)} = {span("D", HEX)}<sub>{span("16", HEX)}</sub> = '
                    f'{span("1101", BIN)}<sub>{span("2", BIN)}</sub>', INK, 80).shift(UP * 1.5)
        with self.sage("Fällt etwas auf? Die 13 ist im Hexadezimalsystem die Ziffer D und im "
                       "Binärsystem eins eins null eins."):
            self.play(Write(gl))
        with self.sage("Zwischen diesen beiden Systemen gibt es eine besonders praktische Verbindung."):
            pass
        self.pause()

        potenz = markup("16 = 2<sup>4</sup>", INK, 72).next_to(gl, DOWN, buff=0.8)
        with self.sage("Der Grund: 16 ist gleich 2 hoch 4."):
            self.play(Write(potenz))

        kette = VGroup(
            sans("4 Bits", BIN, 36, weight=BOLD), sans("→", GRAU, 36),
            markup("2<sup>4</sup> = 16 Werte", INK, 36, font=SANS), sans("→", GRAU, 36),
            sans("genau 16 Hex-Ziffern", HEX, 36, weight=BOLD),
        ).arrange(RIGHT, buff=0.3).next_to(potenz, DOWN, buff=0.8)
        with self.sage("Mit vier Binärstellen kann man genau 16 verschiedene Werte darstellen, von "
                       "null null null null bis eins eins eins eins. Das sind genau so viele, wie es "
                       "Hexadezimalziffern gibt.") as t:
            self.play(LaggedStart(*[FadeIn(k, shift=RIGHT * 0.2) for k in kette], lag_ratio=0.5),
                      run_time=t.duration * 0.8)
        with self.sage("Jede Hexadezimalziffer entspricht also genau vier Binärstellen."):
            self.play(Indicate(kette[0], color=BIN), Indicate(kette[-1], color=HEX))
        self.pause()
        self.play(*[FadeOut(m) for m in (gl, potenz, kette)])

        # ---- Tabelle 4 × 4, spaltenweise
        eintraege = {}
        spalten = VGroup()
        for c in range(4):
            spalte = VGroup()
            for r in range(4):
                h = "0123456789ABCDEF"[4 * c + r]
                e = tab_eintrag(h).move_to([c * 3.0, -r * 0.75, 0], aligned_edge=LEFT)
                eintraege[h] = e
                spalte.add(e)
            spalten.add(spalte)
        spalten.move_to(UP * 0.4)
        with self.sage("Hier ist die vollständige Tabelle. Damit kann man Ziffer für Ziffer "
                       "übersetzen, ganz ohne zu rechnen."):
            for spalte in spalten:
                self.play(LaggedStart(*[FadeIn(e) for e in spalte], lag_ratio=0.2), run_time=1.0)
        self.pause()

        tabelle = spalten
        self.play(tabelle.animate.scale(0.7).to_edge(UP, buff=0.9))

        # ---- Beispiel 1: 2F → 0010 1111
        def markiere(h):
            return SurroundingRectangle(eintraege[h], color=ROT, buff=0.08, stroke_width=3)

        bsp1 = mono("2F", HEX, 72).move_to(LEFT * 3.5 + DOWN * 1.3)
        pfeil = Arrow(LEFT * 2.4, LEFT * 0.6, color=GRAU, stroke_width=4).set_y(bsp1.get_y())
        g1 = mono("0010", BIN, 64)
        g2 = mono("1111", BIN, 64)
        VGroup(g1, g2).arrange(RIGHT, buff=0.5).next_to(pfeil, RIGHT, buff=0.4)
        with self.sage("Beispiel: die Hexadezimalzahl zwei F."):
            self.play(Write(bsp1))
        m = markiere("2")
        with self.sage("Die 2 wird zu null null eins null,"):
            self.play(Indicate(bsp1[0], color=ROT), Create(m))
            self.play(GrowArrow(pfeil), TransformFromCopy(eintraege["2"][2], g1))
        m2 = markiere("F")
        with self.sage("das F zu eins eins eins eins."):
            self.play(Indicate(bsp1[1], color=ROT), ReplacementTransform(m, m2))
            self.play(TransformFromCopy(eintraege["F"][2], g2))
        with self.sage("Ergebnis: null null eins null, eins eins eins eins."):
            self.play(Indicate(VGroup(g1, g2), color=BIN, scale_factor=1.1))
        self.pause()
        self.play(*[FadeOut(x) for x in (bsp1, pfeil, g1, g2, m2)])

        # ---- Beispiel 2: 1010 0011 → A3
        h1 = mono("1010", BIN, 64)
        h2 = mono("0011", BIN, 64)
        bits = VGroup(h1, h2).arrange(RIGHT, buff=0.5).move_to(LEFT * 2.8 + DOWN * 1.1)
        k1 = Brace(h1, DOWN, color=GRAU)
        k2 = Brace(h2, DOWN, color=GRAU)
        with self.sage("Und umgekehrt: Die Binärzahl eins null eins null, null null eins eins "
                       "teilen wir in zwei Vierergruppen."):
            self.play(Write(bits))
            self.play(GrowFromCenter(k1), GrowFromCenter(k2))
        a = mono("A", HEX, 64).next_to(k1, DOWN, buff=0.2)
        drei = mono("3", HEX, 64).next_to(k2, DOWN, buff=0.2)
        m = markiere("A")
        with self.sage("Eins null eins null ist A,"):
            self.play(Create(m), TransformFromCopy(eintraege["A"][0], a))
        m2 = markiere("3")
        with self.sage("null null eins eins ist 3."):
            self.play(ReplacementTransform(m, m2), TransformFromCopy(eintraege["3"][0], drei))
        erg = mono("A3", HEX, 80).move_to(RIGHT * 3.5 + bits.get_y() * UP + DOWN * 0.5)
        pfeil2 = Arrow(bits.get_right() + RIGHT * 0.3, erg.get_left() + LEFT * 0.3, color=GRAU, stroke_width=4)
        with self.sage("Ergebnis: A drei."):
            self.play(GrowArrow(pfeil2), TransformFromCopy(VGroup(a, drei), erg), FadeOut(m2))

        ms = merksatz("1 Hex-Ziffer = 4 Bits").to_edge(DOWN, buff=0.4)
        self.play(FadeIn(ms, shift=UP * 0.2))
        self.wait(1.5)
        self.ausblenden()


# ================================================================ Szene 7
class Szene7_Anwendung(Szene):
    titel = "Wozu Hexadezimal?"

    def construct(self):
        bits = "00101111"
        kaesten = VGroup()
        for b in bits:
            q = Square(0.8, stroke_color=BIN, stroke_width=3, fill_color=WHITE, fill_opacity=1)
            kaesten.add(VGroup(q, mono(b, BIN, 40).move_to(q)))
        kaesten.arrange(RIGHT, buff=0.12).shift(UP * 1.4)
        kaesten[:4].shift(LEFT * 0.15)
        kaesten[4:].shift(RIGHT * 0.15)

        hexk = VGroup()
        for gruppe, h in ((kaesten[:4], "2"), (kaesten[4:], "F")):
            q = Square(0.8, stroke_color=HEX, stroke_width=3, fill_color=WHITE, fill_opacity=1)
            q.next_to(gruppe, DOWN, buff=1.1)
            hexk.add(VGroup(q, mono(h, HEX, 40).move_to(q)))
        klammern = VGroup(Brace(kaesten[:4], DOWN, color=GRAU), Brace(kaesten[4:], DOWN, color=GRAU))

        satz = markup(f'1 Byte = {span("8 Bit", BIN)} = {span("2 Hex-Ziffern", HEX)}', INK, 44, font=SANS)
        satz.next_to(hexk, DOWN, buff=0.7)

        with self.sage("Jetzt verstehen wir, warum Hexadezimal so beliebt ist: Es ist eine kurze "
                       "Schreibweise für Binärzahlen."):
            self.play(LaggedStart(*[FadeIn(k) for k in kaesten], lag_ratio=0.1))
        with self.sage("Ein Byte besteht aus acht Bits, also acht Binärstellen."):
            self.play(Circumscribe(kaesten, color=BIN, buff=0.1))
        with self.sage("Im Hexadezimalsystem sind das nur zwei Ziffern, und die Umrechnung geht "
                       "ohne Rechnen."):
            self.play(GrowFromCenter(klammern[0]), GrowFromCenter(klammern[1]),
                      FadeIn(hexk[0], shift=UP * 0.2), FadeIn(hexk[1], shift=UP * 0.2))
            self.play(Write(satz))
        self.pause()
        self.play(*[FadeOut(m) for m in (kaesten, hexk, klammern, satz)])

        def karte(titel, wert):
            t = sans(titel, GRAU, 26)
            w = markup(wert, HEX, 36)
            inhalt = VGroup(t, w).arrange(DOWN, buff=0.3)
            box = RoundedRectangle(corner_radius=0.15, width=4.0, height=1.9,
                                   stroke_color=HELLGRAU, stroke_width=3, fill_color=WHITE, fill_opacity=1)
            return VGroup(box, inhalt.move_to(box))

        karten = VGroup(
            karte("MAC-Adresse", "3C:52:82:1A:7F:E0"),
            karte("Zeichencode", "A = 41<sub>16</sub>"),
            karte("Speicheradresse", "0x7FFE"),
        ).arrange(RIGHT, buff=0.35).shift(UP * 0.3)
        ueberall = sans("Hexadezimal begegnet uns überall, wo es um Bits und Bytes geht:",
                        INK, 34).next_to(karten, UP, buff=0.9)
        with self.sage("Darum begegnet uns Hexadezimal überall dort, wo es eigentlich um Bits und "
                       "Bytes geht:"):
            self.play(FadeIn(ueberall, shift=DOWN * 0.2))
        with self.sage("bei MAC-Adressen von Netzwerkgeräten, bei Zeichencodes, bei Speicheradressen") as t:
            for k in karten:
                self.play(FadeIn(k, shift=UP * 0.2), run_time=t.duration / 3)

        # ---- Farbcode #FF8000
        code = mono("#FF8000", INK, 96).shift(UP * 1.5)
        with self.sage("und bei Farben."):
            self.play(FadeOut(karten), FadeOut(ueberall))
            self.play(Write(code))
        self.pause()

        kanalfarben = (ROT, BIN, DEZ)
        paare = VGroup(*[mono(p, f, 96) for p, f in zip(("FF", "80", "00"), kanalfarben)]).arrange(RIGHT, buff=2.6)
        paare.move_to(UP * 1.5 + RIGHT * 0.4)
        raute = mono("#", GRAU, 96).next_to(paare, LEFT, buff=0.8)
        namen = VGroup(*[sans(n, f, 32, weight=BOLD).next_to(p, DOWN, buff=0.3)
                         for n, f, p in zip(("Rot", "Grün", "Blau"), kanalfarben, paare)])
        with self.sage("Zurück zu unserem Farbcode: Raute F F acht null null null. Er besteht aus "
                       "drei Bytes, also drei Ziffernpaaren:"):
            self.play(ReplacementTransform(code[0], raute),
                      ReplacementTransform(code[1:3], paare[0]),
                      ReplacementTransform(code[3:5], paare[1]),
                      ReplacementTransform(code[5:7], paare[2]))
        with self.sage("F F für Rot, acht null für Grün, null null für Blau.") as t:
            self.play(LaggedStart(*[FadeIn(n) for n in namen], lag_ratio=0.9), run_time=t.duration)

        e_ff = VGroup(sans("größter Wert", INK, 28), sans("→ volles Rot", ROT, 28),
                      markup('= ?<sub>10</sub>  → Aufgabe 1', GRAU, 26, font=SANS)).arrange(DOWN, buff=0.15)
        e_ff.next_to(namen[0], DOWN, buff=0.5)
        e_80 = VGroup(mono("8·16 + 0 = 128", INK, 28), sans("→ halbes Grün", BIN, 28)).arrange(DOWN, buff=0.15)
        e_80.next_to(namen[1], DOWN, buff=0.5)
        e_00 = VGroup(mono("0", INK, 28), sans("→ kein Blau", DEZ, 28)).arrange(DOWN, buff=0.15)
        e_00.next_to(namen[2], DOWN, buff=0.5)

        with self.sage("F F ist der größte Wert, den zwei Hexadezimalziffern darstellen können, "
                       "also volles Rot."):
            self.play(FadeIn(e_ff[:2], shift=DOWN * 0.2))
        with self.sage("Wie viel das im Dezimalsystem ist, rechnen wir in Aufgabe 1 selbst aus."):
            self.play(FadeIn(e_ff[2]))
        with self.sage("Acht null ist 8 mal 16 plus 0, also 128. Das ist etwa die Hälfte: halbes Grün."):
            self.play(FadeIn(e_80, shift=DOWN * 0.2))
        with self.sage("Und null null ist null, also kein Blau."):
            self.play(FadeIn(e_00, shift=DOWN * 0.2))
        self.pause()

        rot = Square(1.4, fill_color="#FF0000", fill_opacity=1, stroke_width=0).to_edge(DOWN, buff=0.4).shift(LEFT * 2)
        gruen = Square(1.4, fill_color="#008000", fill_opacity=1, stroke_width=0).to_edge(DOWN, buff=0.4).shift(RIGHT * 2)
        orange = Square(1.4, fill_color="#FF8000", fill_opacity=1, stroke_width=0).to_edge(DOWN, buff=0.4)
        plus = sans("+", GRAU, 48).move_to((rot.get_center() + gruen.get_center()) / 2)
        orange_lab = sans("Orange", HEX, 32, weight=BOLD).next_to(orange, RIGHT, buff=0.4)
        with self.sage("Volles Rot mit halbem Grün ergibt: Orange."):
            self.play(FadeIn(rot), FadeIn(gruen), FadeIn(plus), run_time=0.6)
            self.play(rot.animate.move_to(orange), gruen.animate.move_to(orange), FadeOut(plus), run_time=0.8)
            self.play(FadeOut(rot), ReplacementTransform(gruen, orange), run_time=0.6)
            self.play(FadeIn(orange_lab), run_time=0.5)
        self.wait(1)
        self.ausblenden()


# ================================================================ Szene 8
class Szene8_Zusammenfassung(Szene):
    titel = "Zusammenfassung"

    def construct(self):
        punkte = [
            ("1", "Stellenwerte = Potenzen der Basis", "(10 · 2 · 16)"),
            ("2", "→ Dezimal:", "Ziffer · Stellenwert, dann addieren"),
            ("3", "Dezimal →:", "Division mit Rest, Reste von unten nach oben"),
            ("4", "Hex ↔ Binär:", "1 Hex-Ziffer = 4 Bits, ohne Rechnen"),
        ]
        zeilen = VGroup()
        for nr, fett, rest in punkte:
            kreis = Circle(0.28, color=HEX, fill_color=HEX, fill_opacity=1)
            z = VGroup(kreis, sans(nr, WHITE, 28, weight=BOLD).move_to(kreis))
            text = VGroup(sans(fett, INK, 34, weight=BOLD), sans(rest, INK, 34)).arrange(RIGHT, buff=0.25)
            zeilen.add(VGroup(z, text).arrange(RIGHT, buff=0.4))
        zeilen.arrange(DOWN, aligned_edge=LEFT, buff=0.55).shift(UP * 0.5)

        sprechtexte = [
            "Fassen wir zusammen. Erstens: Dezimal-, Binär- und Hexadezimalsystem funktionieren "
            "nach demselben Prinzip. Die Stellenwerte sind Potenzen der Basis.",
            "Zweitens: Ins Dezimalsystem rechnen wir um, indem wir jede Ziffer mit ihrem "
            "Stellenwert multiplizieren und alles addieren.",
            "Drittens: Aus dem Dezimalsystem heraus kommen wir mit der fortgesetzten Division "
            "mit Rest. Die Reste lesen wir von unten nach oben.",
            "Und viertens: Zwischen Hexadezimal und Binär übersetzen wir Ziffer für Ziffer. "
            "Eine Hexadezimalziffer, vier Bits.",
        ]
        for z, text in zip(zeilen, sprechtexte):
            with self.sage(text):
                self.play(FadeIn(z, shift=RIGHT * 0.3), run_time=0.8)
        self.pause()

        weiter = merksatz("Weiter mit Aufgabe 1 – erst selbst probieren!", HEX).to_edge(DOWN, buff=0.6)
        with self.sage("Jetzt sind wir dran: Im nächsten Video geht es um Aufgabe 1. Am besten "
                       "probieren wir sie vorher selbst aus!"):
            self.play(FadeIn(weiter, shift=UP * 0.2))
        self.wait(1)
        self.ausblenden()
