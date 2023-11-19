import discord
from discord.ext import commands, tasks
import feedparser
import os
from dotenv import load_dotenv
import re

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
    #tweets = []
    tweets = set()

    for entry in feed.entries:
        #remover links do tweet
        text = entry.title
        all_links = find_links(text)
        if all_links and len(all_links) > 1:
            text = text.replace(all_links[-1], '')
        text = text.replace("\n\n", "\n")
        tweets.add(text)

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


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    tweet_task.start()

#verificar os últimos tweets do RSS
@bot.command("last_tweets")
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