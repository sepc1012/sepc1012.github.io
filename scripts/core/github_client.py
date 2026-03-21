import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubClient:
    def __init__(self):
        self.username = os.getenv("GITHUB_USER")
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = f"https://api.github.com/users/{self.username}/repos"

    def fetch_repositories(self):
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        params = {"sort": "updated", "per_page": 100}
        
        try:
            print(f"Conectando con GitHub API: {self.username}")
            response = requests.get(self.base_url, headers=headers, params=params)
            
            response.raise_for_status()
            
            repos = response.json()
            print(f"Se obtuvieron {len(repos)} repos.")
            return repos

        except requests.exceptions.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Error de Conexión: {conn_err}")
        except Exception as err:
            print(f"Ocurrió un error inesperado: {err}")
        
        return []