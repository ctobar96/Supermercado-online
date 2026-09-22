"""
Subir los CSVs a la zona raw

En un entorno real usarías boto3 (el SDK de AWS para Python) para subir archivos a S3. Como estamos 
trabajando en local con los datasets descargados, vamos a simular la estructura de carpetas que tendría el lake. 
Esto te enseña la convención sin necesidad de tener una cuenta de AWS.
"""
"""
## 14:00 — El DM de Raúl: cómo funciona el lake
    ey! perdona que no te he escrito antes
    he estado con lo del pipeline de inventario que lleva roto 3 días 😅
    mira, para subir cosas al lake:
        - el bucket es s3://freshmart-lake/raw/
        - la convención es raw/{fuente}/{tabla}/{año}/{mes}/{dia}/
        - hay un script en /scripts/upload_to_raw.py que te puede servir (no sé si funciona, creo que lo hice hace 6 meses jaja)
si te atascas dime!
"""

import shutil
from pathlib import Path
from datetime import date

# Configuración de paths
RAW_PATH = Path("freshmart-lake")
FUENTE = "marketing"
FECHA = date(2024, 9, 16) #L afecha de ingesta del ticket, no la de hoy

# Archivos de María
archivos = [
    "campana_verano_clientes.csv",
    "campana_verano_ventas.csv",
    "productos_promo_verano.csv"
]

for archivo in archivos:
    # Nombre de la "tabla" = nombre del archivo sin extensión
    tabla =  archivo.replace(".csv", "")

    # Estructura de carpetas: raw/{fuente}/{tabla}/{año}/{mes}/{dia}/
    destino = RAW_PATH / "raw" / FUENTE / tabla / str(FECHA.year) / f"{FECHA.month:02d}" / f"{FECHA.day:02d}"
    destino.mkdir(parents=True, exist_ok=True)

print("\nTodos los archivos subidos a raw (sin modificar)")