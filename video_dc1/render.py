"""
Rendert alle Szenen von Video 1 und fügt sie zu einem Video zusammen.

    python render.py          Full HD (1080p, 60 fps) → DC1_Video1.mp4 + DC1_Video1.srt
    python render.py -ql      schnelle Vorschau (480p) → DC1_Video1_vorschau.mp4 + .srt

Die .srt-Datei enthält den Sprechtext mit Zeitangaben für das ganze Video
(z. B. als Untertitel in Camtasia importieren und beim Einsprechen ablesen).
Die einzelnen Szenen liegen danach unter media/videos/dc1_video1/<Auflösung>/.
Braucht ffmpeg im PATH.
"""

import re
import subprocess
import sys
from pathlib import Path

SZENEN = [
    "Szene0_Einstieg",
    "Szene1_Stellenwertsystem",
    "Szene2_Binaer",
    "Szene3_Hexadezimal",
    "Szene4_HexNachDez",
    "Szene5_Division",
    "Szene6_HexBinaer",
    "Szene7_Anwendung",
    "Szene8_Zusammenfassung",
]

ORDNER = {"-ql": "480p15", "-qm": "720p30", "-qh": "1080p60", "-qk": "2160p60"}

ZEIT = re.compile(r"(\d+):(\d+):(\d+),(\d+)")


def dauer(datei):
    aus = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", str(datei)])
    return float(aus)


def verschiebe(zeile, versatz):
    def neu(m):
        h, mi, s, ms = map(int, m.groups())
        t = round((h * 3600 + mi * 60 + s) * 1000 + ms + versatz * 1000)
        return f"{t // 3600000:02d}:{t // 60000 % 60:02d}:{t // 1000 % 60:02d},{t % 1000:03d}"
    return ZEIT.sub(neu, zeile)


def untertitel_zusammenfuegen(videos, ziel):
    bloecke = []
    versatz = 0.0
    for s in SZENEN:
        srt = videos / f"{s}.srt"
        if srt.exists():
            for block in srt.read_text(encoding="utf-8").strip().split("\n\n"):
                zeilen = block.splitlines()
                if len(zeilen) >= 3:
                    bloecke.append([verschiebe(zeilen[1], versatz), *zeilen[2:]])
        versatz += dauer(videos / f"{s}.mp4")
    # utf-8-sig (mit BOM), damit auch ältere Programme wie Camtasia die Umlaute erkennen
    ziel.write_text("".join(f"{i}\n" + "\n".join(b) + "\n\n" for i, b in enumerate(bloecke, 1)),
                    encoding="utf-8-sig")


hier = Path(__file__).parent
qualitaet = sys.argv[1] if len(sys.argv) > 1 else "-qh"
ziel = hier / ("DC1_Video1.mp4" if qualitaet == "-qh" else "DC1_Video1_vorschau.mp4")

subprocess.run([sys.executable, "-m", "manim", qualitaet, "dc1_video1.py", *SZENEN], cwd=hier, check=True)

videos = hier / "media" / "videos" / "dc1_video1" / ORDNER[qualitaet]
liste = hier / "media" / "szenen.txt"
liste.write_text("".join(f"file '{(videos / f'{s}.mp4').as_posix()}'\n" for s in SZENEN), encoding="utf-8")

subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                "-i", str(liste), "-c", "copy", str(ziel)], check=True)
untertitel_zusammenfuegen(videos, ziel.with_suffix(".srt"))
print(f"Fertig: {ziel}")
