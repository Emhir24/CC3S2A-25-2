
# Pruebas para summarize 
import pytest 
from app.app import summarize

def test_summarize_caso_normal():
    # Tres números: suma 6.0, promedio 2.0, conteo 3
    datos = [1, 2, 3]
    assert summarize(datos) == {"count": 3, "sum": 6.0, "avg": 2.0}

def test_summarize_borde_un_elemento():
    # Un solo valor (string)  debe funcionar
    datos = ["5"]
    assert summarize(datos) == {"count": 1, "sum": 5.0, "avg": 5.0}

def test_summarize_error_no_numerico():
    # Si hay un valor no convertible a número, debe salir ValueError
    with pytest.raises(ValueError):
        summarize(["1", "x"])
