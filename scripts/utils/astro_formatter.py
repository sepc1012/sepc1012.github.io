from datetime import datetime

def format_for_astro(repos):
    projects = []
    
    for repo in repos:
        if not repo['fork'] and repo.get('description'):
            clean_name = repo['name'].replace("-", " ").replace("_", " ").title()
            
            date_obj = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            readable_date = date_obj.strftime("%d %b %Y")

            project_data = {
                "name": clean_name,
                "description": repo['description'],
                "url": repo['html_url'],
                "stars": repo['stargazers_count'],
                "language": repo['language'] if repo['language'] else "Multiple",
                "topics": repo.get('topics', []),
                "last_update": readable_date,
                "size": repo.get('size', 0) 
            }
            projects.append(project_data)
    
    projects.sort(key=lambda x: x['size'], reverse=True)
    
    return projects