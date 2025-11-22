# Groq DevStudio

Uma interface de chat "Single Page Application" (SPA) moderna e responsiva, construída inteiramente dentro de um template XML do Blogger. Este projeto permite interagir com diversos modelos de Inteligência Artificial (como Llama 3 via Groq, GPT-4o via OpenAI, e outros via OpenRouter) e publicar as conversas diretamente como postagens no seu blog.

## 👨‍💻 Sobre o Desenvolvedor

Desenvolvido por **Jailton Fonseca** (Brasil 🇧🇷).

### Siga-me nas redes sociais:
*   **Instagram:** [@jailton_fon](https://instagram.com/jailton_fon)
*   **Facebook:** [Jailton Fonseca](https://facebook.com/jailton.fonseca.507)
*   **TikTok:** [@fonsecac41](https://tiktok.com/@fonsecac41)
*   **Twitch:** [fonsecac41](https://twitch.tv/fonsecac41)
*   **YouTube:** [Jailton Fonseca](https://www.youtube.com/@JailtonFonseca)

---

## 🚀 Funcionalidades

*   **Múltiplos Provedores:** Suporte para Groq (Llama 3.1), OpenAI (GPT-4o) e OpenRouter (Claude 3.5, Gemini, etc).
*   **Publicação no Blogger:** Publique seus chats interessantes ou códigos gerados diretamente no seu blog com um clique.
*   **Editor de Código:** Visualização de código com syntax highlighting e opção de preview/execução de HTML/JS em tempo real.
*   **Design Responsivo:** Interface otimizada para Desktop e Mobile.
*   **Histórico Local:** Seus chats e configurações são salvos no `localStorage` do navegador.

---

## ⚙️ Instalação e Configuração

Como este projeto é um template do Blogger, a "instalação" consiste em fazer o upload do arquivo XML no seu painel do Blogger.

### Passo 1: Preparar o Blogger
1.  Acesse [blogger.com](https://www.blogger.com).
2.  Crie um novo blog ou selecione um existente.
3.  Vá em **Tema** no menu lateral.
4.  Clique na **seta** ao lado do botão "Personalizar" e selecione **Editar HTML**.
5.  Copie todo o conteúdo do arquivo `template.xml` deste repositório.
6.  Substitua todo o código existente no editor do Blogger pelo código copiado.
7.  Clique no ícone de **Salvar** (disquete).

### Passo 2: Configurar o Google Client ID (Essencial para Publicação)
Para que o botão de "Publicar no Blogger" funcione, você precisa configurar uma credencial OAuth 2.0 no Google Cloud.

1.  Acesse o [Google Cloud Console](https://console.cloud.google.com/apis/credentials).
2.  Crie um novo projeto (ou selecione um existente).
3.  Vá em **APIs e Serviços** > **Biblioteca**.
4.  Pesquise por **"Blogger API v3"** e ative-a.
5.  Vá em **Tela de permissão OAuth** (OAuth consent screen).
    *   Selecione **Externo**.
    *   Preencha os campos obrigatórios (Nome do App, email, etc).
    *   Não é necessário adicionar escopos sensíveis para teste pessoal, mas se pedir, o escopo é `https://www.googleapis.com/auth/blogger`.
    *   Adicione seu email como **Usuário de Teste** (Test User).
6.  Vá em **Credenciais** > **Criar Credenciais** > **ID do cliente OAuth**.
    *   **Tipo de aplicativo:** Aplicativo da Web.
    *   **Origens JavaScript autorizadas:** Adicione a URL do seu blog (ex: `https://meu-blog-ia.blogspot.com`). **Atenção:** Não use barra `/` no final.
    *   Clique em **Criar**.
7.  Copie o **ID do cliente** gerado (algo como `123456-abcde.apps.googleusercontent.com`).

### Passo 3: Configurando no App
1.  Abra seu blog no navegador.
2.  Clique no botão de **Configurações** (ícone de engrenagem) na barra lateral.
3.  Cole seu **Google Client ID** no campo correspondente.
4.  Insira suas chaves de API (API Keys) para os provedores que deseja usar:
    *   **Groq:** [console.groq.com/keys](https://console.groq.com/keys)
    *   **OpenAI:** [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
    *   **OpenRouter:** [openrouter.ai/keys](https://openrouter.ai/keys)
5.  Clique em **Salvar**.

---

## 🛠️ Como Usar

1.  **Chat:** Digite sua mensagem na caixa inferior. Use `Shift+Enter` para quebra de linha.
2.  **Código:** Se a IA gerar código HTML/CSS/JS, você verá botões para **Copiar**, **Baixar** e **Preview** (executar o código numa janela modal).
3.  **Publicar:** Clique no ícone do Blogger no cabeçalho do chat para criar uma postagem com a conversa atual. Será necessário fazer login com sua conta Google na primeira vez (popup do Google).
4.  **Novo Chat:** Clique em "+ Novo Chat" na barra lateral para limpar o contexto.

---

## 📜 Licença

Este projeto é de uso livre. Créditos ao desenvolvedor são apreciados.
