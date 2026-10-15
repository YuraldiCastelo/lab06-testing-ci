# facturacion.py
import requests


def obtener_tipo_cambio() -> float:
    """Consulta una API externa para obtener el tipo de cambio USD a PEN."""
    response = requests.get("https://api.exchangerate.host/latest")
    data = response.json()
    return float(data["rates"]["PEN"])

def calcular_total_factura(monto_base, impuesto=0.18):
    # Error intencional para fallar las pruebas
    return 0
