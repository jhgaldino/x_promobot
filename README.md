# x_promobot
Um bot do Discord agregador de feeds RSS.<br><br>

## Configurando o Bot<br><br>
Antes de usar o bot, você precisa configurá-lo corretamente. Siga os passos abaixo:<br>



Clone ou baixe o código-fonte deste repositório em sua máquina.<br>

### Crie um Bot no Portal do Desenvolvedor do Discord<br><br>
[Acesse o Portal do Desenvolvedor do Discord.](https://discord.com/developers/)<br>
Clique em "New Application" para criar um novo aplicativo.<br>
Na guia "Bot", clique em "Add Bot" para adicionar um bot ao seu aplicativo.<br>
Anote o token do seu bot, que será necessário posteriormente.<br>

### Crie um feed RSS para o seu bot<br><br>
Crie um feed RSS com os posts que você deseja que o bot poste no Discord.<br>
Você pode usar um serviço como o [rss.app](https://rss.app) para criar um feed RSS a partir de uma página da web.<br>
Anote o link do feed RSS, que será necessário posteriormente.<br>

### Convide o Bot para o Seu Servidor<br><br>
Na guia "OAuth2" do Portal do Desenvolvedor do Discord, selecione as permissões necessárias para o seu bot (leitura e escrita de mensagens, por exemplo).<br>
Copie o URL gerado e cole-o em um navegador da web. Isso abrirá uma página onde você poderá selecionar o servidor para o qual deseja convidar o bot.<br>

### Configurando o Ambiente Virtual Python<br><br>
Abra o terminal ou prompt de comando e navegue até a pasta onde você baixou o código do bot.<br>
Crie um ambiente virtual Python para este projeto (caso não tenha um ambiente virtual configurado):<br>
```
python -m venv venv
```
### Ative o ambiente virtual:<br>
No Windows:<br>
```
venv\Scripts\activate.bat
```
<details>
<summary>observacao</summary> caso voce tenha o powershell instalado no windows 10 ou esteje com o windows 11, use o comando 

```
venv\Scripts\activate.ps1
```
<br>
</details>
<br>

No macOS e Linux:<br>
```
source venv/bin/activate
```

### Instale as Dependências<br><br>
Use o pip para instalar as dependências do bot a partir do arquivo requirements.txt:<br>
```
pip install -r requirements.txt
```
### Configure o Arquivo .env<br><br>
Crie um arquivo chamado .env na pasta do seu projeto.<br>
Cole as seguintes variáveis de ambiente no arquivo .env, substituindo DISCORD_TOKEN pelo token do seu bot e FEED_RSS pelo link do feed RSS gerado:<br>
```
DISCORD_TOKEN=seu_token_do_discord
FEED_RSS=link_do_feed_rss
```
### Executando o Bot<br><br>
Agora que o bot está configurado, você pode executá-lo com o seguinte comando:<br>
```
python bot.py
```	
O bot estará pronto para usar no seu servidor Discord.<br>

### Comandos do Bot<br>
```
/last_tweets: Use este comando no servidor Discord para obter os últimos tweets dos feeds RSS configurados.
```

## Personalização<br><br>
Você pode personalizar ainda mais o bot para atender às suas necessidades.<br>
Voce pode mudar o tempo em que o bot busca novos posts alterando o tempo na task.<br>
Voce pode configurar o RSS para postar quantos posts voce quiser na pagina do site do RSS em que voce o gerou.<br>
  


