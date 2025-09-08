
#!/usr/bin/env python3
import sys
from .app import summarize

def main():
    if len(sys.argv) < 2:
        print('Uso: python -m app "1,2,3"')
        sys.exit(2)

    entrada = sys.argv[1]
    elementos = [p.strip() for p in entrada.split(",") if p.strip()]

    try:
        res = summarize(elementos)
    except ValueError as e:
        # Manejo de errores
        print(f"Error: {e}")
        sys.exit(1)

    # Imprimimos
    print(f"sum={res['sum']} avg={res['avg']} count={res['count']}")

if __name__ == "__main__":
    main()
