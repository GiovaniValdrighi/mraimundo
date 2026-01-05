#!/bin/bash

# --- 1. CONFIGURAÇÃO AUTOMÁTICA (O "Setup") ---
# Calcula a URL dinâmica deste Codespace específico
URL="https://${CODESPACE_NAME}-1313.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}/mraimundo/"

# Injeta essa URL no arquivo tasks.json (substitui o placeholder)
sed -i "s|FULL_LINK|$URL|g" .vscode/tasks.json

# Diz para o Git ignorar mudanças no tasks.json (para não sujar o commit dos alunos)
git update-index --skip-worktree .vscode/tasks.json 2>/dev/null

echo "✅ Ambiente configurado para: $URL"
echo "🚀 Iniciando Hugo Server..."
echo "---------------------------------------------------"

# --- 2. INICIAR O SERVIDOR (O comando simples) ---
# Usamos baseURL relativa para garantir que funcione em qualquer lugar
hugo server --baseURL=/mraimundo/ --appendPort=false --bind=0.0.0.0
