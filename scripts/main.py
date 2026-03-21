import json
import os
from core.github_client import GitHubClient
from utils.astro_formatter import format_for_astro

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASTRO_OUTPUT = os.path.join(BASE_DIR, "..", "src", "data", "projects.json")
def main():
    client = GitHubClient()
    
    raw_data = client.fetch_repositories()
    
    if not raw_data:
        print("No hay datos que procesar. Revisa tu .env y conexión.")
        return

    print("Formateando datos para Astro...")
    final_projects = format_for_astro(raw_data)

    try:
        folder = os.path.dirname(ASTRO_OUTPUT)
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
            print(f"Carpeta creada: {folder}")
        
        with open(ASTRO_OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(final_projects, f, indent=4, ensure_ascii=False)
            
        print(f"¡ÉXITO! {len(final_projects)} proyectos sincronizados en: {ASTRO_OUTPUT}")
        
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()