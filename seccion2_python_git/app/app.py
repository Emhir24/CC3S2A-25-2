# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3

def summarize(nums):
    """
    Recibe una lista/tupla con números o cadenas que se puedan convertir a número.
    Valida que no esté vacía y que todo sea convertible a float.
    """
    # Validación 
    if not isinstance(nums, (list, tuple)):
        raise ValueError("La entrada debe ser lista/tupla de números.")
    if len(nums) == 0:
        raise ValueError("La lista está vacía.")

    convertidos = []
    for item in nums:
        # Permitimos strings con espacios
        if isinstance(item, str):
            item = item.strip()
        try:
            convertidos.append(float(item))
        except Exception:
            # Si no es número, avisamos
            raise ValueError(f"Valor no numérico: {item!r}")

    total = sum(convertidos)
    n = len(convertidos)
    promedio = total / n

    # Retornamos el dict con los resultados
    return {"count": n, "sum": total, "avg": promedio}


if __name__ == "__main__":
    # Leer argumentos de línea de comandos
    import sys
    entrada = sys.argv[1] if len(sys.argv) > 1 else ""
    elementos = [p.strip() for p in entrada.split(",") if p.strip()]
    try:
        res = summarize(elementos)
        # Imprimimos en el formato pedido
        print(f"sum={res['sum']} avg={res['avg']} count={res['count']}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
