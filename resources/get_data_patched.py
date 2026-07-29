import cv2
import numpy as np
import csv
from pathlib import Path

# ======================================
# CONFIGURACIÓN
# ======================================

BASE_DIR = Path(__file__).resolve().parent

VIDEO = BASE_DIR / "pendulo.mp4"

CSV_SALIDA = BASE_DIR / "theta.csv"

DT = 0.02

# ======================================

puntos = []


def mouse(event, x, y, flags, param):

    global puntos

    if event == cv2.EVENT_LBUTTONDOWN:
        puntos.append((x, y))


def angulo_entre(v1, v2):

    v1 = v1 / np.linalg.norm(v1)
    v2 = v2 / np.linalg.norm(v2)

    det = v1[0] * v2[1] - v1[1] * v2[0]
    dot = np.dot(v1, v2)

    return np.arctan2(det, dot)


# ======================================
# ABRIR VIDEO
# ======================================

cap = cv2.VideoCapture(str(VIDEO))

if not cap.isOpened():
    raise RuntimeError("No se pudo abrir el vídeo.")

fps = cap.get(cv2.CAP_PROP_FPS)

nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

duracion = nframes / fps

print(f"FPS       : {fps:.2f}")
print(f"Frames    : {nframes}")
print(f"Duración  : {duracion:.2f} s")

# ======================================
# CSV
# ======================================

csv_file = open(CSV_SALIDA, "w", newline="")

writer = csv.writer(csv_file)

writer.writerow([
    "tiempo",
    "theta(rad)",
    "theta(deg)"
])

csv_file.flush()

# ======================================

cv2.namedWindow("Frame")

cv2.setMouseCallback("Frame", mouse)

t = 0.0

while t <= duracion:

    frame_id = int(round(t * fps))

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)

    ret, frame = cap.read()

    if not ret:
        break

    puntos.clear()

    while True:

        img = frame.copy()

        cv2.putText(
            img,
            f"t = {t:.2f} s",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        instrucciones = [
            "1) Clic en el pivote",
            "2) Clic en la referencia vertical",
            "3) Clic en el hilo",
            "ENTER = guardar",
            "R = repetir",
            "ESC = salir"
        ]

        y = 70

        for texto in instrucciones:

            cv2.putText(
                img,
                texto,
                (20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                (255, 255, 255),
                2
            )

            y += 30

        colores = [
            (0, 0, 255),
            (255, 0, 0),
            (0, 255, 255)
        ]

        for i, p in enumerate(puntos):

            cv2.circle(
                img,
                p,
                5,
                colores[min(i, 2)],
                -1
            )

        if len(puntos) == 3:

            pivote = np.array(puntos[0], dtype=float)

            referencia = np.array(puntos[1], dtype=float)

            hilo = np.array(puntos[2], dtype=float)

            v_vertical = referencia - pivote

            v_hilo = hilo - pivote

            theta = angulo_entre(v_vertical, v_hilo)

            grados = np.degrees(theta)

            cv2.line(
                img,
                tuple(map(int, pivote)),
                tuple(map(int, referencia)),
                (255, 0, 0),
                2
            )

            cv2.line(
                img,
                tuple(map(int, pivote)),
                tuple(map(int, hilo)),
                (0, 255, 0),
                2
            )

            cv2.putText(
                img,
                f"Theta = {grados:.2f} deg",
                (20, 270),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 255),
                2
            )

        cv2.imshow("Frame", img)

        tecla = cv2.waitKey(20)

        if tecla == ord('r'):

            puntos.clear()

        elif tecla == 13 and len(puntos) == 3:

            writer.writerow([
                t,
                theta,
                grados
            ])

            csv_file.flush()

            break

        elif tecla == 27:

            csv_file.close()

            cap.release()

            cv2.destroyAllWindows()

            exit()

    t += DT

# ======================================

csv_file.close()

cap.release()

cv2.destroyAllWindows()

print("Proceso terminado.")