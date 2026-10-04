# Drehbuch · DC 1 · Video 1: Zahlensysteme – Dezimal, Binär, Hexadezimal

**Grundlage:** Brueckenkurs_Informatik.html, Abschnitt DC 1, Teil „Inhalte“
**Zielgruppe:** Schülerinnen und Schüler im Brückenkurs (Klasse 9/10), Anrede mit „wir“
**Länge:** ca. 8 Minuten (etwa 1 050 Wörter Sprechtext bei rund 130 Wörtern pro Minute)
**Folgevideos:** Video 2 – Aufgabe 1 · Video 3 – Aufgabe 2 (Farbcode #2E8B57)

---

## Gestaltung (gilt für alle drei Videos)

- **Format:** 16:9, ruhiger heller Hintergrund, viel Weißraum.
- **Zahlen** immer in einer Festbreitenschrift (z. B. Consolas oder IBM Plex Mono), damit die Ziffern untereinander stehen.
- **Feste Farbe pro System**, durchgehend gleich:
  - Dezimal: **blau**
  - Binär: **grün**
  - Hexadezimal: **orange**
- **Basis als Index:** 173₁₀ · 1101₂ · AD₁₆. Gleich in Szene 1 einführen und dann immer verwenden.
- **Stellenwerte** stehen klein und grau *über* den Ziffern.
- **Einblendungen erscheinen genau dann, wenn sie genannt werden**, nicht vorher. Die nummerierten Einblendungen in jeder Szene geben die Reihenfolge vor.

## Hinweise zur Vertonung

Der Sprechtext ist schon in Sprechform geschrieben: Hex-Ziffern und Bitfolgen mit Bindestrich („A-D“, „eins-null-eins-null“), Rechenzeichen ausgeschrieben („geteilt durch“, „hoch“). So liest auch eine KI-Stimme richtig vor.

| Auf dem Bildschirm | Gesprochen |
|---|---|
| `#FF8000` | „Raute F-F-8-0-0-0“ |
| `AD₁₆` | „A-D“ (nicht „ad“) |
| `1101₂` | „eins-eins-null-eins“ (nicht „tausendeinhunderteins“) |
| `2⁴` | „2 hoch 4“ |
| `173 : 16` | „173 geteilt durch 16“ |

Wenn du selbst sprichst: Nach jeder Rechnung kurz pausieren. Die Pausen markiert der Text mit **[Pause]**.

---

## Szene 0 · Einstieg · 0:00–0:30

**Bild:** Ausschnitt aus einem Webseiten-Quelltext mit der Zeile `color: #FF8000;`. Daneben ein orangefarbenes Quadrat.

**Einblendungen:**
1. Quelltextzeile `color: #FF8000;`
2. Orangefarbenes Quadrat
3. Fragezeichen über `FF`: „Buchstaben in einer Zahl?“

**Sprechtext:**
> Wenn wir uns den Quelltext einer Webseite anschauen, finden wir solche Angaben: Raute F-F-8-0-0-0. Das ist eine Farbe – genauer gesagt dieses Orange. Aber warum stehen da Buchstaben zwischen den Ziffern? **[Pause]** Das ist eine Zahl im Hexadezimalsystem. In diesem Video lernen wir, wie das Hexadezimalsystem funktioniert und wie es mit dem Binärsystem und unserem Dezimalsystem zusammenhängt. Und am Ende können wir diesen Farbcode selbst entschlüsseln.

---

## Szene 1 · Was ist ein Stellenwertsystem? · 0:30–1:20

**Bild:** Die Zahl 173 groß in Blau. Darüber erscheinen die Stellenwerte.

**Einblendungen:**
1. `173`
2. Über den Ziffern: `100  10  1`
3. Darunter: `1 · 100 + 7 · 10 + 3 · 1 = 173`
4. Stellenwerte umgeschrieben: `10²  10¹  10⁰`
5. Merksatz-Kasten: **Stellenwerte = Potenzen der Basis**
6. Index ergänzen: `173₁₀`

**Sprechtext:**
> Fangen wir mit etwas an, das wir schon kennen: unserem Dezimalsystem. Nehmen wir die Zahl 173. Die 3 steht ganz rechts an der Einerstelle, die 7 an der Zehnerstelle, die 1 an der Hunderterstelle. Die Zahl bedeutet also: 1 mal 100 plus 7 mal 10 plus 3 mal 1. **[Pause]** Die Stellenwerte 1, 10, 100 sind Potenzen von 10, von rechts beginnend mit 10 hoch null. Die 10 nennt man die **Basis** des Systems. Deshalb gibt es auch genau zehn Ziffern, von 0 bis 9. Ein solches System heißt **Stellenwertsystem**: Was eine Ziffer wert ist, hängt davon ab, an welcher Stelle sie steht. **[Pause]** Und jetzt das Entscheidende: Die Basis muss nicht 10 sein.

---

## Szene 2 · Das Binärsystem · 1:20–2:15

**Bild:** Stellenwerte `8  4  2  1` grau, darunter die Binärzahl in Grün.

**Einblendungen:**
1. „Basis 2 · Ziffern: 0, 1“
2. Stellenwerte `… 32  16  8  4  2  1`, jeweils mit Pfeil „· 2“ nach links
3. `1101₂`, Ziffern unter `8  4  2  1`
4. Von rechts nacheinander: `1 · 1`, `0 · 2`, `1 · 4`, `1 · 8`
5. `8 + 4 + 1 = 13`
6. Zum Schluss: `200₁₀ = 11001000₂`, Stellen durchzählen: „8 Stellen!“

**Sprechtext:**
> Computer arbeiten mit nur zwei Zuständen: Strom an oder aus, eins oder null. Darum verwenden sie das **Binärsystem** mit der Basis 2. Es gibt nur zwei Ziffern, 0 und 1. Die Stellenwerte sind Potenzen von 2: von rechts 1, 2, 4, 8, dann 16, 32 und so weiter. Jede Stelle ist doppelt so viel wert wie die rechts daneben. **[Pause]** Schauen wir uns die Binärzahl eins-eins-null-eins an. Ganz rechts eine 1 an der Einerstelle: 1. Dann eine 0 an der Zweierstelle: nichts. Dann eine 1 an der Viererstelle: 4. Und eine 1 an der Achterstelle: 8. Zusammen: 8 plus 4 plus 1 gleich 13. **[Pause]** Das Prinzip ist genau dasselbe wie im Dezimalsystem: Ziffer mal Stellenwert, dann addieren. Der Nachteil: Binärzahlen werden schnell sehr lang. Schon die Zahl 200 braucht acht Stellen. Für Menschen ist das schwer zu lesen.

---

## Szene 3 · Das Hexadezimalsystem · 2:15–3:10

**Bild:** „Basis 16“ in Orange, darunter die Ziffernreihe.

**Einblendungen:**
1. „Basis 16 → 16 Ziffern nötig“
2. Ziffernreihe `0 1 2 3 4 5 6 7 8 9` und dann, einzeln erscheinend: `A B C D E F`
3. Unter den Buchstaben: `A = 10  B = 11  C = 12  D = 13  E = 14  F = 15`
4. Stellenwerte `4096  256  16  1`
5. Überblickstabelle (bleibt stehen, bis die Szene endet):

| System | Basis | Ziffern | Stellenwerte |
|---|---|---|---|
| Dezimal | 10 | 0–9 | … 1000, 100, 10, 1 |
| Binär | 2 | 0, 1 | … 8, 4, 2, 1 |
| Hexadezimal | 16 | 0–9, A–F | … 4096, 256, 16, 1 |

**Sprechtext:**
> Hier kommt das **Hexadezimalsystem** ins Spiel. Es hat die Basis 16. Das heißt: Wir brauchen sechzehn verschiedene Ziffern. Die Ziffern 0 bis 9 haben wir schon. Für die Werte 10 bis 15 nimmt man Buchstaben: A steht für 10, B für 11, C für 12, D für 13, E für 14 und F für 15. **[Pause]** Die Stellenwerte sind Potenzen von 16: von rechts 1, dann 16, dann 256, dann 4096. **[Pause]** Hier noch einmal alle drei Systeme im Überblick. Jedes hat eine Basis, so viele Ziffern, wie die Basis angibt, und Stellenwerte, die Potenzen der Basis sind.

---

## Szene 4 · Hexadezimal → Dezimal · 3:10–3:45

**Bild:** `AD₁₆` in Orange, darüber die Stellenwerte `16  1`.

**Einblendungen:**
1. `AD₁₆`, darüber `16  1`
2. Unter D: `13 · 1 = 13`
3. Unter A: `10 · 16 = 160`
4. `160 + 13 = 173`
5. Ergebnis: `AD₁₆ = 173₁₀`

**Sprechtext:**
> Wie viel ist dann die Hexadezimalzahl A-D? Wir gehen vor wie gewohnt: jede Ziffer mal ihren Stellenwert. Das D steht an der Einerstelle und ist 13 wert: 13 mal 1 gleich 13. Das A steht an der Sechzehnerstelle und ist 10 wert: 10 mal 16 gleich 160. Zusammen: 160 plus 13 gleich 173. **[Pause]** A-D im Hexadezimalsystem ist also dieselbe Zahl wie 173 im Dezimalsystem.

---

## Szene 5 · Dezimal → Hexadezimal und Binär: Division mit Rest · 3:45–5:00

**Bild:** Rechnung wird Zeile für Zeile aufgebaut, wie an der Tafel.

**Einblendungen (Teil A – nach Hexadezimal):**
1. `173 : 16 = 10  Rest 13`
2. Neben dem Rest: `= D`
3. Pfeil: die 10 wandert in die nächste Zeile
4. `10 : 16 = 0  Rest 10` → `= A`
5. Kasten um die 0: „Ergebnis 0 → fertig“
6. Pfeil an den Resten **von unten nach oben**, ergibt `AD`

**Einblendungen (Teil B – nach Binär):**
7. `13 : 2 = 6  Rest 1`
8. `6 : 2 = 3  Rest 0`
9. `3 : 2 = 1  Rest 1`
10. `1 : 2 = 0  Rest 1`
11. Pfeil von unten nach oben, ergibt `1101`, Verweis auf Szene 2: „✓ wie vorhin“

**Sprechtext:**
> Und wie kommt man umgekehrt von 173 auf A-D? Dafür gibt es ein Verfahren: die **fortgesetzte Division mit Rest**. Man teilt die Zahl immer wieder durch die Basis, hier also durch 16, und notiert jedes Mal den Rest. **[Pause]** 173 geteilt durch 16 ergibt 10, Rest 13. Denn 10 mal 16 sind 160, und bis 173 fehlen noch 13. Rest 13, das ist die Hexadezimalziffer D. Jetzt rechnen wir mit dem Ergebnis weiter: 10 geteilt durch 16 ergibt 0, Rest 10. Rest 10, das ist die Ziffer A. Sobald das Ergebnis 0 ist, sind wir fertig. **[Pause]** Jetzt kommt der wichtige Schritt: Wir lesen die Reste **von unten nach oben**. Also erst A, dann D: A-D. Das passt zu unserer Rechnung von eben. **[Pause]** Dasselbe Verfahren funktioniert für das Binärsystem, dann teilt man eben durch 2. Nehmen wir die 13. 13 geteilt durch 2 ist 6, Rest 1. 6 geteilt durch 2 ist 3, Rest 0. 3 geteilt durch 2 ist 1, Rest 1. 1 geteilt durch 2 ist 0, Rest 1. Von unten nach oben gelesen: eins-eins-null-eins. Genau die Binärzahl, die wir vorhin hatten.

---

## Szene 6 · Hexadezimal ↔ Binär: ohne Rechnen · 5:00–6:15

**Bild:** Links `D` in Orange, rechts `1101` in Grün, dazwischen ein Gleichheitszeichen.

**Einblendungen:**
1. `13 = D₁₆ = 1101₂`
2. `16 = 2⁴`
3. „4 Bits → 2⁴ = 16 Werte → genau 16 Hex-Ziffern“
4. Vollständige Tabelle, spaltenweise aufbauen:
   ```
   0 = 0000   4 = 0100   8 = 1000   C = 1100
   1 = 0001   5 = 0101   9 = 1001   D = 1101
   2 = 0010   6 = 0110   A = 1010   E = 1110
   3 = 0011   7 = 0111   B = 1011   F = 1111
   ```
5. Beispiel 1: `2F` → `2` wird zu `0010`, `F` wird zu `1111` → `0010 1111`
6. Beispiel 2: `1010 0011` → Klammer um jede Vierergruppe → `A` und `3` → `A3`
7. Merksatz-Kasten: **1 Hex-Ziffer = 4 Bits**

**Sprechtext:**
> Fällt etwas auf? Die 13 ist im Hexadezimalsystem die Ziffer D und im Binärsystem eins-eins-null-eins. Zwischen diesen beiden Systemen gibt es eine besonders praktische Verbindung. **[Pause]** Der Grund: 16 ist gleich 2 hoch 4. Mit vier Binärstellen kann man genau 16 verschiedene Werte darstellen, von null-null-null-null bis eins-eins-eins-eins. Das sind genau so viele, wie es Hexadezimalziffern gibt. Jede Hexadezimalziffer entspricht also genau **vier** Binärstellen. **[Pause]** Hier ist die vollständige Tabelle. Damit kann man Ziffer für Ziffer übersetzen, ganz ohne zu rechnen. **[Pause]** Beispiel: die Hexadezimalzahl 2-F. Die 2 wird zu null-null-eins-null, das F zu eins-eins-eins-eins. Ergebnis: null-null-eins-null, eins-eins-eins-eins. **[Pause]** Und umgekehrt: Die Binärzahl eins-null-eins-null, null-null-eins-eins teilen wir in zwei Vierergruppen. Eins-null-eins-null ist A, null-null-eins-eins ist 3. Ergebnis: A-3.

---

## Szene 7 · Wozu Hexadezimal? · 6:15–7:25

**Bild:** Ein Byte als 8 grüne Kästchen, darunter 2 orange Kästchen.

**Einblendungen:**
1. `1 Byte = 8 Bit = 2 Hex-Ziffern`, z. B. `0010 1111 = 2F`
2. Drei kleine Beispiele nebeneinander (nur zeigen, nicht vorlesen):
   - MAC-Adresse: `3C:52:82:1A:7F:E0`
   - Zeichencode: `A = 41₁₆`
   - Speicheradresse: `0x7FFE`
3. Zurück zu `#FF8000`, aufgeteilt in drei Paare: `FF | 80 | 00`, darunter `Rot | Grün | Blau`
4. Unter `FF`: „größter Wert → volles Rot“ und ein Fragezeichen „= ?₁₀ → Aufgabe 1“
5. Unter `80`: `8 · 16 + 0 = 128` → „halbes Grün“
6. Unter `00`: `0` → „kein Blau“
7. Rotes und halb grünes Farbfeld blenden ineinander, es entsteht das orangefarbene Quadrat aus Szene 0

**Sprechtext:**
> Jetzt verstehen wir, warum Hexadezimal so beliebt ist: Es ist eine **kurze Schreibweise für Binärzahlen**. Ein Byte besteht aus acht Bits, also acht Binärstellen. Im Hexadezimalsystem sind das nur zwei Ziffern, und die Umrechnung geht ohne Rechnen. **[Pause]** Darum begegnet uns Hexadezimal überall dort, wo es eigentlich um Bits und Bytes geht: bei MAC-Adressen von Netzwerkgeräten, bei Zeichencodes, bei Speicheradressen – und bei Farben. **[Pause]** Zurück zu unserem Farbcode: Raute F-F-8-0-0-0. Er besteht aus drei Bytes, also drei Ziffernpaaren: F-F für Rot, 8-0 für Grün, 0-0 für Blau. F-F ist der größte Wert, den zwei Hexadezimalziffern darstellen können, also volles Rot. Wie viel das im Dezimalsystem ist, rechnen wir in Aufgabe 1 selbst aus. 8-0 ist 8 mal 16 plus 0, also 128. Das ist etwa die Hälfte: halbes Grün. Und 0-0 ist null, also kein Blau. **[Pause]** Volles Rot mit halbem Grün ergibt: Orange.

---

## Szene 8 · Zusammenfassung · 7:25–8:00

**Bild:** Vier Merksätze, die nacheinander erscheinen. Am Ende ein Hinweis auf das nächste Video.

**Einblendungen:**
1. **Stellenwerte = Potenzen der Basis** (10 · 2 · 16)
2. **→ Dezimal:** Ziffer · Stellenwert, dann addieren
3. **Dezimal →:** fortgesetzte Division mit Rest, Reste von unten nach oben
4. **Hex ↔ Binär:** 1 Hex-Ziffer = 4 Bits, ohne Rechnen
5. „Weiter mit Aufgabe 1 – erst selbst probieren!“

**Sprechtext:**
> Fassen wir zusammen. Erstens: Dezimal-, Binär- und Hexadezimalsystem funktionieren nach demselben Prinzip. Die Stellenwerte sind Potenzen der Basis. Zweitens: Ins Dezimalsystem rechnen wir um, indem wir jede Ziffer mit ihrem Stellenwert multiplizieren und alles addieren. Drittens: Aus dem Dezimalsystem heraus kommen wir mit der fortgesetzten Division mit Rest. Die Reste lesen wir von unten nach oben. Und viertens: Zwischen Hexadezimal und Binär übersetzen wir Ziffer für Ziffer. Eine Hexadezimalziffer, vier Bits. **[Pause]** Jetzt sind wir dran: Im nächsten Video geht es um Aufgabe 1. Am besten probieren wir sie vorher selbst aus!

---

## Abgleich mit dem HTML-Abschnitt

**Vollständig enthalten:** Basis und Stellenwerte, Tabelle der drei Systeme, A–F, Zuordnung Hex ↔ 4 Bits mit Tabelle, Beispiele `2F → 0010 1111` und `1010 0011 → A3`, Division `173 → AD`, Rückrechnung `AD → 173`, Byte = 2 Hex-Ziffern, Anwendungen (Farbe `#FF8000`, MAC-Adressen, Zeichencodes, Speicheradressen).

**Ergänzt gegenüber dem HTML (bitte prüfen, ob gewünscht):**
- Szene 1: `173` als Stellenwert-Zerlegung im Dezimalsystem, als Einstieg über Bekanntes
- Szene 2 und 5: das Binärbeispiel `13 = 1101₂` in beide Richtungen. Es schlägt in Szene 6 die Brücke über `D = 1101`.
- Szene 7: Auflösung des Farbcodes `#FF8000`

**Bewusst ausgelassen, damit die Aufgaben nicht vorweggenommen werden:**
- Den Dezimalwert von `FF` (Aufgabe 1.1): Szene 7 verweist nur darauf.
- Das Gruppieren von rechts mit führenden Nullen und die Begründung, warum Dezimal ↔ Binär nicht ziffernweise geht (Lösung zu Aufgabe 1.3/1.4): Das gehört in Video 2.
- Den Vergleich mit dem Oktalsystem (Lösung zu Aufgabe 1.4).
