# Groq DevStudio
Uma interface de chat Single Page Application (SPA) construída dentro de um template XML do Blogger, utilizando a API da Groq.

## Desenvolvedor
**Jailton Fonseca** (Brasil)

## Redes Sociais
*   **Instagram:** [instagram.com/jailton_fon](https://instagram.com/jailton_fon)
*   **Facebook:** [facebook.com/jailton.fonseca.507](https://facebook.com/jailton.fonseca.507)
*   **TikTok:** [tiktok.com/@fonsecac41](https://tiktok.com/@fonsecac41)
*   **Twitch:** [twitch.tv/fonsecac41](https://twitch.tv/fonsecac41)
*   **YouTube:** [www.youtube.com/@JailtonFonseca](https://www.youtube.com/@JailtonFonseca)

## Funcionalidades
*   **Chat com IA:** Suporte a Groq, OpenAI e OpenRouter.
*   **Envio de Arquivos:** Carregue arquivos de texto/código para análise da IA.
*   **Publicação no Blogger:** Publique chats como postagens diretamente no blog.
*   **Integração Google:** Login via Google Identity Services.
*   **Mobile Friendly:** Interface responsiva para celulares e tablets.

## Instalação
1.  Abra o arquivo `template.xml` deste repositório e copie todo o seu conteúdo.
2.  Acesse o painel do seu **Blogger**.
3.  Vá em **Tema** -> seta ao lado de "Personalizar" -> **Editar HTML**.
4.  Apague todo o código existente e cole o conteúdo do `template.xml`.
5.  Clique no ícone de **Salvar** (disquete) no canto superior direito.

## Configuração

### 1. Obter Google Client ID (Obrigatório para Publicar)
Para usar o botão "Publicar no Blogger", você precisa configurar um projeto no Google Cloud:
1.  Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2.  Crie um novo projeto.
3.  Vá em **APIs e Serviços** -> **Tela de consentimento OAuth**.
    *   Escolha "Externo".
    *   Preencha os campos obrigatórios (nome do app, email).
    *   Adicione o escopo `https://www.googleapis.com/auth/blogger`.
    *   Adicione seu email como usuário de teste.
4.  Vá em **Credenciais** -> **Criar Credenciais** -> **ID do cliente OAuth**.
    *   Tipo de aplicativo: **Aplicativo da Web**.
    *   **Origens JavaScript autorizadas:** Adicione a URL do seu blog (ex: `https://seu-blog.blogspot.com`).
5.  Copie o **ID do Cliente** gerado (termina em `.apps.googleusercontent.com`).
6.  No Groq DevStudio (seu blog), vá em **Configurações** e cole no campo "Google Client ID".

### 2. Obter Chaves de API (IA)
Você precisa de pelo menos uma chave para conversar:
*   **Groq (Grátis/Rápido):** [console.groq.com](https://console.groq.com/keys)
*   **OpenAI (GPT):** [platform.openai.com](https://platform.openai.com/api-keys)
*   **OpenRouter (Vários modelos):** [openrouter.ai/keys](https://openrouter.ai/keys)

Cole a chave correspondente nas **Configurações** do app.

## Uso
1.  **Chat:** Digite sua mensagem e envie. Use Shift+Enter para pular linha.
2.  **Arquivos:** Clique no ícone de clipe (anexo) para enviar o conteúdo de um arquivo de texto/código para a IA.
3.  **Publicar:** Clique no ícone de nuvem no cabeçalho para postar o chat atual no seu blog. Se você continuar a conversa e clicar novamente, o post será atualizado.
4.  **Código:** Blocos de código nas respostas têm botões para Copiar, Baixar e Executar (Preview HTML).
