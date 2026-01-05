import requests
import os
import yaml
import re
import sys

# --- ⚙️ CONFIGURAÇÃO DO LABORATÓRIO ⚙️ ---

# 1. Pastas
AUTHORS_DIR = "content/authors"
PUBS_DIR = "content/publication"

# 2. Seu Nome (Para marcar destaque/featured na Home)
ADMIN_NAMES = ["Marcos M. Raimundo", "M. Raimundo", "Marcos Raimundo"]

# 3. Automação de Projetos (Palavra-Chave : Nome-da-Pasta-do-Projeto)
PROJECT_KEYWORDS = {
    "credit": "credit-scoring",
    "fairness": "fairness-ai",
    "optimization": "machine-learning-opt",
    "bilevel": "bilevel-opt"
}

# ----------------------------------------------

def install_dependencies():
    try:
        import requests
        import yaml
    except ImportError:
        print("⚠️ Instalando dependências...")
        os.system(f"{sys.executable} -m pip install requests pyyaml")
        os.execv(sys.executable, ['python'] + sys.argv)

def get_author_data():
    """
    Lê o semantic_scholar_id de todos os autores.
    Suporta múltiplos IDs (ex: "123, 456")
    """
    author_data = {} 
    
    if not os.path.exists(AUTHORS_DIR): return author_data

    for folder in os.listdir(AUTHORS_DIR):
        path = os.path.join(AUTHORS_DIR, folder, "_index.md")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'semantic_scholar_id:\s*(.*)', content)
                if match:
                    raw_ids = match.group(1).strip()
                    clean_ids = re.sub(r'[\[\]"\'\s]', '', raw_ids).split(',')
                    clean_ids = [x for x in clean_ids if x]
                    if clean_ids:
                        author_data[folder] = clean_ids
    return author_data

def fetch_papers_mult(ids_list):
    """Consulta a API para múltiplos IDs e remove duplicatas"""
    all_papers = []
    seen_paper_ids = set()

    for author_id in ids_list:
        print(f"    -> Buscando ID: {author_id}")
        url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
        params = {'fields': 'paperId,title,year,abstract,venue,url,authors,externalIds,openAccessPdf', 'limit': 30}
        
        try:
            r = requests.get(url, params=params)
            if r.status_code == 200:
                data = r.json().get('data', [])
                for p in data:
                    pid = p.get('paperId')
                    if pid and pid not in seen_paper_ids:
                        seen_paper_ids.add(pid)
                        all_papers.append(p)
        except Exception as e:
            print(f"    Erro no ID {author_id}: {e}")
            
    return all_papers

def match_projects(text):
    if not text: return [] # Proteção extra
    text = text.lower()
    matched = []
    for key, proj in PROJECT_KEYWORDS.items():
        if key in text: matched.append(proj)
    return list(set(matched))

def is_admin_author(author_list):
    for author in author_list:
        if author in ADMIN_NAMES:
            return True
    return False

def create_pub_file(paper):
    if not paper.get('title') or not paper.get('year'): return

    # Garante que title e abstract nunca sejam None (Correção do erro TypeError)
    p_title = paper.get('title') or ""
    p_abstract = paper.get('abstract') or ""
    p_venue = paper.get('venue') or "Preprint"
    p_url = paper.get('url') or ""

    clean_title = re.sub(r'[^a-zA-Z0-9]+', '-', p_title.lower()).strip('-')
    folder_name = f"{paper['year']}-{clean_title[:50]}"
    folder_path = os.path.join(PUBS_DIR, folder_name)
    file_path = os.path.join(folder_path, "index.md")

    if os.path.exists(file_path): return 

    os.makedirs(folder_path, exist_ok=True)
    
    # Lista de autores
    author_list = [a['name'] for a in paper.get('authors', [])]

    # Detecta Projetos
    full_text = (p_title + " " + p_abstract).lower()
    projects = match_projects(full_text)

    is_featured = is_admin_author(author_list)

    data = {
        'title': p_title,
        'date': f"{paper['year']}-01-01",
        'authors': author_list,
        'publication_types': ["2"],
        'publication': p_venue,
        'abstract': p_abstract,
        'featured': is_featured,
        'projects': projects,
        'links': [{'name': 'Semantic Scholar', 'url': p_url}]
    }

    if paper.get('openAccessPdf'):
        data['url_pdf'] = paper['openAccessPdf']['url']
    elif paper.get('externalIds', {}).get('ArXiv'):
        data['url_pdf'] = f"https://arxiv.org/pdf/{paper['externalIds']['ArXiv']}.pdf"

    with open(file_path, "w", encoding='utf-8') as f:
        f.write("---\n")
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
        f.write("---\n")
    
    print(f"  [+] Criado: {p_title[:40]}... (Autores: {len(author_list)})")

def main():
    install_dependencies()
    print("--- 📚 Atualizando Publicações (Correção NoneType) ---")
    
    authors_map = get_author_data()
    
    if not authors_map:
        print("Nenhum ID encontrado. Configure 'semantic_scholar_id' nos perfis.")
        return
    
    for folder, ids in authors_map.items():
        print(f"\nProcessando Autor: {folder} (IDs: {ids})")
        papers = fetch_papers_mult(ids)
        print(f"  Encontrados {len(papers)} papers únicos.")
        for p in papers: create_pub_file(p)

if __name__ == "__main__":
    main()