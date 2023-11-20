# x_promobot
Um bot do Discord agregador de feeds RSS.

Configurando o Bot
Antes de usar o bot, você precisa configurá-lo corretamente. Siga os passos abaixo:

Baixe o Código Fonte

Clone ou baixe o código-fonte deste repositório em sua máquina.

Crie um Bot no Portal do Desenvolvedor do Discord
Acesse o Portal do Desenvolvedor do Discord.
Clique em "New Application" para criar um novo aplicativo.
Na guia "Bot", clique em "Add Bot" para adicionar um bot ao seu aplicativo.
Anote o token do seu bot, que será necessário posteriormente.

Convide o Bot para o Seu Servidor
Na guia "OAuth2" do Portal do Desenvolvedor, selecione as permissões necessárias para o seu bot (leitura e escrita de mensagens, por exemplo).
Copie o URL gerado e cole-o em um navegador da web. Isso abrirá uma página onde você poderá selecionar o servidor para o qual deseja convidar o bot.

Configurando o Ambiente Virtual Python
Abra o terminal ou prompt de comando e navegue até a pasta onde você baixou o código do bot.
Crie um ambiente virtual Python para este projeto (caso não tenha um ambiente virtual configurado):
python -m venv venv
Ative o ambiente virtual:
No Windows:
venv\Scripts\activate 
obs : caso voce tenha o powershell instalado no windows 10 ou esteje com o windows 11, use activate.ps1
No macOS e Linux:
source venv/bin/activate

Instale as Dependências
Use o pip para instalar as dependências do bot a partir do arquivo requirements.txt:
pip install -r requirements.txt

Configure o Arquivo .env
Crie um arquivo chamado .env na pasta do seu projeto.
Cole as seguintes variáveis de ambiente no arquivo .env, substituindo DISCORD_TOKEN pelo token do seu bot e FEED_RSS pelo link do feed RSS gerado:
DISCORD_TOKEN=seu_token_do_discord
FEED_RSS=link_do_feed_rss

Executando o Bot
Agora que o bot está configurado, você pode executá-lo com o seguinte comando:
python bot.py
O bot estará pronto para usar no seu servidor Discord.

Comandos do Bot
/last_tweets: Use este comando no servidor Discord para obter os últimos tweets dos feeds RSS configurados. 
Personalização
Você pode personalizar ainda mais o bot para atender às suas necessidades.
Voce pode mudar o tempo em que o bot busca novos posts alterando o tempo na task.
Voce pode configurar o RSS para postar quantos posts voce quiser na pagina do site do RSS em que voce o gerou.
  

