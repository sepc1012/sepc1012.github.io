
async function getRepoData() {
    const response = await fetch('https://api.github.com/repos/sepc1012/servicore-asuservicio');
    const data = await response.json();
        
    document.getElementById('repo-description').innerText = data.description; // inyeccion de info
        
    const date = new Date(data.updated_at).toLocaleDateString('es-ES', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
    });
    document.getElementById('repo-updated').innerText = `Último commit: ${date}`;
}
getRepoData();
