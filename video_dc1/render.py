"""
Rendert alle Szenen von Video 1 und fügt sie zu einem Video zusammen.

    python render.py          Full HD (1080p, 60 fps) → DC1_Video1.mp4
    python render.py -ql      schnelle Vorschau (480p) → DC1_Video1_vorschau.mp4

Die einzelnen Szenen liegen danach unter media/videos/dc1_video1/<Auflösung>/.
Braucht ffmpeg im PATH.
"""

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

hier = Path(__file__).parent
qualitaet = sys.argv[1] if len(sys.argv) > 1 else "-qh"
ziel = hier / ("DC1_Video1.mp4" if qualitaet == "-qh" else "DC1_Video1_vorschau.mp4")

subprocess.run([sys.executable, "-m", "manim", qualitaet, "dc1_video1.py", *SZENEN], cwd=hier, check=True)

videos = hier / "media" / "videos" / "dc1_video1" / ORDNER[qualitaet]
liste = hier / "media" / "szenen.txt"
liste.write_text("".join(f"file '{(videos / f'{s}.mp4').as_posix()}'\n" for s in SZENEN), encoding="utf-8")

subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                "-i", str(liste), "-c", "copy", str(ziel)], check=True)
print(f"Fertig: {ziel}")
