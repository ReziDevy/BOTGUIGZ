import random
from twitchio.ext import commands

# === CONFIGURAÇÕES DO BOT ===
bot_token = ''  # Token do bot
bot_nickname = 'z3vlr'                              # Nick do bot
client_id = ''         # Client ID da aplicação
canal_twitch = ''                              # Canal onde o bot vai ficar

# === CONFIGURAÇÃO DO FORMULÁRIO ===
# Aqui você coloca o link real do seu Google Forms, por exemplo
FORMULARIO_URL_BASE = "https://forms.gle/nCBrYaY8ocuPJsNi6"

# O link final vai ter ?usuario=nome&codigo=1234
# Esse código pode ser usado pra identificar quem preencheu

# === INSTÂNCIA DO BOT ===
bot = commands.Bot(
    token=bot_token,
    client_id=client_id,
    nick=bot_nickname,
    prefix='!',
    initial_channels=[canal_twitch]
)

@bot.event
async def event_ready():
    print(f'✅ Bot conectado como {bot.nickname}')

@bot.command(name='linkespecial')
async def cmd_linkespecial(ctx):
    user = ctx.author.name
    codigo = random.randint(1000, 9999)  # Código aleatório de 4 dígitos

    # Geração do link personalizado com query string
    link_unico = f"{FORMULARIO_URL_BASE}?usuario={user}&codigo={codigo}"

    # Envia a mensagem no chat
    await ctx.send(
        f"📋 {user}, preencha seu formulário aqui: {link_unico} (Código: {codigo})"
    )

if __name__ == '__main__':
    print("⚡ Bot iniciado - Comando disponível: !linkespecial")
    bot.run()
