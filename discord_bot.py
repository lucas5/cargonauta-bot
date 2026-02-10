import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Dicionário que mapeia emojis para IDs de cargos
# Você precisará atualizar esses IDs com os IDs reais dos seus cargos
ROLE_EMOJI_MAP = {
    '💬': os.getenv('ID_DO_CARGO_BATE_PAPO'),
    '🍿': os.getenv('ID_DO_CARGO_CINE_AMONG'),
    '🏆': os.getenv('ID_DO_CARGO_TACA_AMONG'),
    '💻': os.getenv('ID_DO_CARGO_HOMEOFFICE'),
    '📖': os.getenv('ID_DO_CARGO_PROGRAMACAO_COMPETITIVA')
}

# ID da mensagem de boas-vindas (carregado do .env)
WELCOME_MESSAGE_ID = os.getenv('WELCOME_MESSAGE_ID')
if WELCOME_MESSAGE_ID:
    WELCOME_MESSAGE_ID = int(WELCOME_MESSAGE_ID)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')
    print(f'ID do Bot: {bot.user.id}')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    """Cria a mensagem de boas-vindas com reações"""

    embed = discord.Embed(
        title="🎮 Bem-vindo ao Servidor Among! 🎮",
        description=(
            "Hey, tripulante! Escolha seus cargos reagindo aos emojis abaixo e fique por dentro de tudo que rola no servidor! Para conseguir visualizar os canais que deseja apenas reaja a essa mensagem de acordo com sua preferência!\n"
            "-"
        ),
        color=0x5865F2  # Discord blurple
    )
    
    # Campo Bate-papo
    embed.add_field(
        name="💬 Bate Papo",
        value=(
            "**Toda dia é dia de socializar!** Se quiser apenas conversar ou companhia para passar o tempo!"
            "\n-"
        ),
        inline=False
    )
    
    # Campo Cineamong
    embed.add_field(
        name="🍿 Cine Among",
        value=(
            "**Toda quinta-feira é dia de cinema!** Participe das votações, escolha os filmes e aproveite a sessão com a galera. Pipoca garantida!"
            "\n-"
        ),
        inline=False
    )
    
    # Campo Taça Among
    embed.add_field(
        name="🏆 Taça Among",
        value=(
            "**Campeonato de LoL toda sexta-feira!** Receba notificações sobre as partidas, formação de times e mostre suas skills no Summoner's Rift!"
            "\n-"
        ),
        inline=False
    )

    # Campo Estudos/Trabalho
    embed.add_field(
        name="💻 Estudos & Trabalho",
        value=("**Modo foco ativado!** Para quem quer estudar ou trabalhar em paz. Participe de sessões de estudo e produtividade!"
               "\n-"
        ),
        inline=False
    )
    
    # Campo Programação Competitiva
    embed.add_field(
        name="📖 Programação Competitiva",
        value=("**Modo foco ativado!** Para quem quer estudar programação e novas tecnologias!"
               "\n-"
        ),
        inline=False
    )
    
    embed.add_field(
        name="",
        value=(
            "**Como funciona?** Clique nos emojis abaixo para receber os cargos! Você pode escolher quantos quiser.\n\n"
            "💬 = Bate Papo\n🍿 = Cine Among\n🏆 = Taça Among\n💻 = Home Office e Estudos\n📖 = Programação Competitiva"
        ),
        inline=False
    )

    message = await ctx.send(embed=embed)

    # Adiciona todas as reações
    for emoji in ROLE_EMOJI_MAP.keys():
        await message.add_reaction(emoji)
    
    print(f"Mensagem de setup criada! ID: {message.id}")
    print(f"Salve este ID e coloque na variável WELCOME_MESSAGE_ID")
    
    await ctx.send(f"✅ Sistema configurado! ID da mensagem: `{message.id}`", delete_after=10)

@bot.event
async def on_raw_reaction_add(payload):
    """Quando alguém adiciona uma reação"""
    
    print(f"\n🔔 Reação detectada!")
    print(f"   User ID: {payload.user_id}")
    print(f"   Message ID: {payload.message_id}")
    print(f"   Emoji: {payload.emoji}")
    
    # Ignora reações do próprio bot
    if payload.user_id == bot.user.id:
        print(f"   ⏭️ Ignorando (é o próprio bot)")
        return
    
    # Verifica se é a mensagem correta (se você definiu o ID)
    if WELCOME_MESSAGE_ID and payload.message_id != WELCOME_MESSAGE_ID:
        print(f"   ⏭️ Mensagem diferente (esperado: {WELCOME_MESSAGE_ID})")
        return
    
    if WELCOME_MESSAGE_ID is None:
        print(f"   ⚠️ WELCOME_MESSAGE_ID não configurado! Configure no código.")
    
    # Pega o emoji
    emoji = str(payload.emoji)
    
    # Verifica se o emoji está no mapeamento
    if emoji not in ROLE_EMOJI_MAP:
        print(f"   ❌ Emoji {emoji} não está mapeado!")
        print(f"   Emojis disponíveis: {list(ROLE_EMOJI_MAP.keys())}")
        return
    
    # Pega o servidor e o membro
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        print(f"   ❌ Servidor não encontrado!")
        return
    
    member = guild.get_member(payload.user_id)
    if member is None:
        print(f"   ❌ Membro não encontrado!")
        return
    
    print(f"   👤 Membro: {member.name}")
    
    # Pega o cargo
    role_id = ROLE_EMOJI_MAP[emoji]
    
    # Se ainda estiver usando o placeholder, não faz nada
    if isinstance(role_id, str) and role_id.startswith('ID_DO_CARGO'):
        print(f"   ⚠️ Configure os IDs dos cargos primeiro!")
        print(f"   Use !roles para ver os IDs disponíveis")
        return
    
    print(f"   🎯 Procurando cargo ID: {role_id}")
    
    role = guild.get_role(int(role_id))
    
    if role is None:
        print(f"   ❌ Cargo não encontrado com ID: {role_id}")
        print(f"   📋 Use !roles para listar os cargos disponíveis")
        return
    
    print(f"   🎭 Cargo encontrado: {role.name}")
    
    # Verifica hierarquia
    if guild.me.top_role <= role:
        print(f"   ❌ ERRO: O cargo do bot ({guild.me.top_role.name}) está abaixo de {role.name}!")
        print(f"   💡 Mova o cargo do bot para acima de {role.name} nas configurações")
        return
    
    # Adiciona o cargo ao membro
    try:
        await member.add_roles(role)
        print(f"   ✅ Cargo '{role.name}' adicionado a {member.name}!")
    except discord.Forbidden:
        print(f"   ❌ Sem permissão para adicionar cargo!")
        print(f"   💡 Verifique se o bot tem permissão 'Gerenciar Cargos'")
    except Exception as e:
        print(f"   ❌ Erro ao adicionar cargo: {e}")

@bot.event
async def on_raw_reaction_remove(payload):
    """Quando alguém remove uma reação"""
    
    print(f"\n🔕 Reação removida!")
    print(f"   User ID: {payload.user_id}")
    print(f"   Message ID: {payload.message_id}")
    print(f"   Emoji: {payload.emoji}")
    
    # Verifica se é a mensagem correta
    if WELCOME_MESSAGE_ID and payload.message_id != WELCOME_MESSAGE_ID:
        print(f"   ⏭️ Mensagem diferente")
        return
    
    # Pega o emoji
    emoji = str(payload.emoji)
    
    # Verifica se o emoji está no mapeamento
    if emoji not in ROLE_EMOJI_MAP:
        print(f"   ❌ Emoji não mapeado")
        return
    
    # Pega o servidor e o membro
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return
    
    member = guild.get_member(payload.user_id)
    if member is None:
        return
    
    # Pega o cargo
    role_id = ROLE_EMOJI_MAP[emoji]
    
    if isinstance(role_id, str) and role_id.startswith('ID_DO_CARGO'):
        return
    
    role = guild.get_role(int(role_id))
    
    if role is None:
        return
    
    # Remove o cargo do membro
    try:
        await member.remove_roles(role)
        print(f"   🗑️ Cargo '{role.name}' removido de {member.name}!")
    except Exception as e:
        print(f"   ❌ Erro ao remover cargo: {e}")

@bot.command()
@commands.has_permissions(administrator=True)
async def roles(ctx):
    """Lista todos os cargos do servidor com seus IDs"""
    
    embed = discord.Embed(
        title="📋 Cargos do Servidor",
        description="Use esses IDs para configurar o bot:",
        color=discord.Color.blue()
    )
    
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            embed.add_field(
                name=role.name,
                value=f"ID: `{role.id}`",
                inline=False
            )
    
    await ctx.send(embed=embed)

# Execute o bot
# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot
if __name__ == '__main__':
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)
