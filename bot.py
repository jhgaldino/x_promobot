import os
import re
import feedparser
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

# Configurar as intenções
intents = discord.Intents.default()
intents.message_content = True

# Carregar variáveis de ambiente
load_dotenv()


#guardando tweets ja enviados
global last_tweets_sent


#url do RSS
feed_url = os.environ.get('FEED_RSS')

# Variável para armazenar o contexto do comando
last_ctx = None


# Configuração do bot Discord
bot = commands.Bot(command_prefix='/', description='Bot de Promoções', intents=intents)


#encontrar links do tweet para remocao
def find_links(tweet):
    links = re.findall(r'https://t\.co/[A-Za-z0-9]{10}', tweet)
    return links

#buscar os últimos tweets do RSS
def get_latest_tweets(feed_url):
    feed = feedparser.parse(feed_url)
    tweets = []

    for entry in feed.entries:
        # o title do RSS é o texto do tweet
        text = entry.title
        # encontrar todos os links do tweet
        all_links = find_links(text)
        # se nao houver links, pular o tweet
        if not len(all_links) > 1:
            continue
        # remover o link de referencia do proprio tweet
        text = text.replace(all_links[-1], '')
        # remover as quebras de linhas duplicadas
        text = text.replace("\n\n", "\n")
        # adicionar o texto do tweet na lista de tweets
        tweets.append(text)

    return tweets

last_tweets_sent = []

#verificar novos tweets
async def check_tweets():
    
    new_tweets = []

    try:
        latest_tweets = get_latest_tweets(feed_url)
        for tweet in latest_tweets:
            # se o tweet nao esta na lista de tweets enviados, adicionar na lista de novos tweets
            if tweet not in last_tweets_sent:
                new_tweets.append(tweet)
    except Exception as e:
        print(f'Erro ao verificar promoções: {str(e)}')
    #adicionar novos tweets na lista de tweets enviados
    last_tweets_sent.extend(new_tweets)
    return new_tweets


#verificar novos tweets a cada 30 minutos
@tasks.loop(minutes=30)
async def tweet_task():
    if not last_ctx:
        return
    new_tweets = await check_tweets()
    if new_tweets :
        for tweet in new_tweets:
            await last_ctx.send(tweet)

#funcao para suprimir o erro de comando nao encontrado
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    tweet_task.start()

#verificar os últimos tweets do RSS
@bot.command("twt")
async def last_tweets(ctx):
    global last_ctx
    last_ctx = ctx
    new_tweets = await check_tweets()
    if not new_tweets:
        await ctx.send('Não há novas promoções')
        return
    for tweet in new_tweets:
        await ctx.send(tweet)

# Iniciar o bot
bot.run(os.environ.get('DISCORD_TOKEN'))