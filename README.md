# 🎓 Guia de Colaboração do Laboratório

Bem-vindo ao repositório do site do laboratório! Este guia explica como adicionar seu perfil, publicações e projetos de forma simples, usando um ambiente de desenvolvimento na nuvem.

## 🚀 Como começar (Passo a Passo)

Utilizamos o fluxo **Fork & Pull Request**. Você não precisa instalar nada no seu computador (Git, Hugo, etc); usaremos o **GitHub Codespaces**.

### 1. Faça um Fork (Crie sua cópia)
O primeiro passo é criar uma cópia deste repositório na sua conta.

1.  Role até o topo desta página.
2.  Clique no botão **Fork** (canto superior direito).
3.  Confirme a criação. Agora você tem uma versão `seu-usuario/mraimundo` para editar à vontade.

### 2. Inicie o Ambiente (Codespaces)
O GitHub configurará um computador na nuvem com tudo pronto.

1.  No **seu** repositório forkado, clique no botão verde **Code**.
2.  Vá para a aba **Codespaces**.
3.  Clique em **Create codespace on main**.
4.  *Aguarde alguns minutos enquanto o ambiente é configurado.*

### 3. Rode o Site
Para visualizar suas alterações em tempo real, vamos ligar o servidor.

1.  No VS Code, pressione `F1` (ou `Ctrl` + `Shift` + `P`) para abrir o menu de comandos.
2.  Digite **Run Task** e dê Enter.
3.  Selecione **▶️ RUN SERVER**.
    * *O terminal abrirá. Aguarde aparecer a mensagem `Built in ... ms`.*
4.  Agora, abra o comando novamente (`F1` -> Run Task) e selecione **🌐 OPEN BROWSER**.
    * *O site abrirá em uma aba lateral dentro do VS Code.*

---

## ✏️ Como Editar seu Perfil

1.  No explorador de arquivos à esquerda, navegue até: `content/authors/`.
2.  **Se você é um novo membro:**
    * Copie a pasta de algum colega existente (ex: `content/authors/modelo`).
    * Renomeie a pasta para o seu nome (ex: `joao-silva`).
    * Edite o arquivo `_index.md` dentro dela com seus dados.
    * Substitua a foto `avatar.jpg` pela sua (mantenha o nome do arquivo como `avatar.jpg` ou `avatar.jpeg`).
3.  **Se já existe:** Basta editar seu arquivo `_index.md`.

> **Dica:** Sempre que você salvar o arquivo (`Ctrl + S`), o site na aba lateral atualizará automaticamente.

---

## 📤 Enviando suas alterações

Quando estiver satisfeito com o resultado, envie suas modificações para aprovação.

### 1. Salvar (Commit)
No terminal do VS Code (parte inferior), execute os comandos abaixo na ordem:

```bash
# 1. Adiciona todos os arquivos que você alterou
git add .

# 2. Salva o pacote com uma mensagem explicando o que você fez
git commit -m "Adicionando perfil de Nome do Aluno"
```

### 2. Enviar (Push)
Isso envia as alterações do Codespace para o seu GitHub.

```bash
git push
```

### 3. Solicitar Aprovação (Pull Request)
Agora você precisa avisar o repositório oficial que tem novidades.

1. Acesse a página do seu repositório no GitHub (github.com/seu-usuario/mraimundo).

2. Você verá um aviso amarelo: "This branch is 1 commit ahead...".

3. Clique em Contribute > Open Pull Request.

4. Revise se está tudo certo e clique em Create Pull Request.

Pronto! Eu serei notificado, revisarei seu perfil e aceitarei a inclusão no site oficial. 🎉