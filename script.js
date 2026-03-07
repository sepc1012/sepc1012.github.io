
const USER = 'sepc1012';
const REPO = 'servicore-asuservicio';

async function loadServiCoreData() {
    try {
        const repoRes = await fetch(`https://api.github.com/repos/${USER}/${REPO}`);
        const repoData = await repoRes.json();

        document.getElementById('repo-description').innerText = repoData.description;
        
        const date = new Date(repoData.updated_at).toLocaleDateString('es-ES', {
            day: 'numeric', month: 'short', year: 'numeric'
        });
        document.getElementById('repo-updated').innerText = `Update: ${date}`;

        const langRes = await fetch(`https://api.github.com/repos/${USER}/${REPO}/languages`);
        const languages = await langRes.json();
        
        const langContainer = document.getElementById('repo-languages');
        langContainer.innerHTML = '';

        Object.keys(languages).forEach(lang => {
            const span = document.createElement('span');
            span.className = 'badge';
            span.innerText = lang;
            langContainer.appendChild(span);
        });

    } catch (error) {
        console.error("Error al dote... digo, al cargar la API:", error);
    }
}

document.addEventListener('DOMContentLoaded', loadServiCoreData);