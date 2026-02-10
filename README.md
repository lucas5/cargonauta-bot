# 🎮 Among Discord Bot - Sistema de Auto-Cargos

Bot para Discord com sistema automático de atribuição de cargos via reações em mensagens. Desenvolvido especificamente para o servidor **Among**, com cargos personalizados para diferentes atividades da comunidade.

## ✨ Funcionalidades

- 🎯 **Auto-atribuição de cargos** via reações em embed
- 💬 **5 cargos personalizados** para o servidor Among
- 🔒 **Configuração segura** via variáveis de ambiente
- 📱 **Interface visual** com embed customizado
- 🔄 **Adicionar e remover** cargos dinamicamente
- 🐛 **Sistema de debug** com logs detalhados

## 🎭 Cargos Disponíveis

| Emoji | Cargo | Descrição |
|-------|-------|-----------|
| 💬 | Bate-papo | Para membros que adoram conversar |
| 🎬 | Cineamong | Sessão de cinema toda quinta-feira |
| 🏆 | Taça Among | Campeonato de LoL toda sexta-feira |
| 🏠 | Home Office | Para quem trabalha remotamente |
| 💻 | Programação Competitiva | Maratonas e desafios de código |

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Conta Discord
- Permissões de administrador no servidor

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/lucas5/cargonauta-bot.git
cd cargonauta-bot
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv bot_env
source bot_env/bin/activate  # Linux/Mac
# ou
bot_env\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o Bot no Discord

1. Acesse o [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications)
2. Clique em **"New Application"**
3. Dê um nome ao bot (ex: "Among Bot")
4. Vá em **"Bot"** no menu lateral
5. Clique em **"Add Bot"**
6. Em **"Privileged Gateway Intents"**, ative:
   - ✅ PRESENCE INTENT
   - ✅ SERVER MEMBERS INTENT
   - ✅ MESSAGE CONTENT INTENT
7. Clique em **"Reset Token"** e copie o token

### 5. Convide o Bot para seu Servidor

1. No Portal de Desenvolvedores, vá em **"OAuth2"** > **"URL Generator"**
2. Em **"Scopes"**, marque:
   - ✅ `bot`
3. Em **"Bot Permissions"**, marque:
   - ✅ Manage Roles
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Add Reactions
4. Copie o URL gerado e cole no navegador
5. Selecione seu servidor e autorize

### 6. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
nano .env  # ou use seu editor preferido
```

Preencha com suas informações:

```env
# Token do bot Discord
DISCORD_TOKEN=seu_token_aqui

# IDs dos cargos (use !roles para descobrir)
ID_DO_CARGO_BATE_PAPO=123456789012345678
ID_DO_CARGO_CINE_AMONG=123456789012345678
ID_DO_CARGO_TACA_AMONG=123456789012345678
ID_DO_CARGO_HOME_OFFICE=123456789012345678
ID_DO_CARGO_PROGRAMACAO_COMPETITIVA=123456789012345678

# ID da mensagem (preencha após rodar !setup)
WELCOME_MESSAGE_ID=123456789012345678
```

## 🎯 Como Usar

### 1. Inicie o bot

```bash
python discord_bot.py
```

Você deve ver:
```
NomeDoBot#1234 está online!
ID do Bot: 123456789...
```

### 2. Liste os cargos do servidor

No Discord, digite:
```
!roles
```

Copie os IDs dos cargos e adicione no arquivo `.env`

### 3. Crie a mensagem de boas-vindas

No canal desejado, digite:
```
!setup
```

O bot criará um embed com todos os emojis e retornará o ID da mensagem. Copie esse ID e adicione no `.env`:

```env
WELCOME_MESSAGE_ID=1234567890123456789
```

### 4. Reinicie o bot

```bash
# Pare o bot (Ctrl+C)
python discord_bot.py
```

### 5. Teste!

Reaja aos emojis na mensagem e veja os cargos sendo atribuídos automaticamente! ✨

## 📝 Comandos Disponíveis

| Comando | Descrição | Permissão |
|---------|-----------|-----------|
| `!setup` | Cria a mensagem de boas-vindas com reações | Administrador |
| `!roles` | Lista todos os cargos do servidor com IDs | Administrador |

## ⚙️ Configuração Avançada

### Personalizar Emojis

Edite o dicionário `ROLE_EMOJI_MAP` em `discord_bot.py`:

```python
ROLE_EMOJI_MAP = {
    '💬': os.getenv('ID_DO_CARGO_BATE_PAPO'),
    '🎬': os.getenv('ID_DO_CARGO_CINE_AMONG'),
    # Adicione mais emojis aqui...
}
```

### Personalizar a Mensagem

Edite a função `setup()` em `discord_bot.py` para customizar cores, textos e campos do embed.

### Hierarquia de Cargos

⚠️ **IMPORTANTE**: O cargo do bot deve estar **acima** dos cargos que ele gerencia!

1. Vá em **Configurações do Servidor** → **Cargos**
2. Arraste o cargo do bot para cima dos outros cargos

## 🐛 Solução de Problemas

### Bot não inicia

- ✅ Verifique se o token no `.env` está correto
- ✅ Certifique-se que o arquivo se chama `.env` (com o ponto no início)
- ✅ Confirme que instalou todas as dependências

### Cargos não são adicionados

- ✅ Verifique se os IDs dos cargos estão corretos
- ✅ Confirme que o `WELCOME_MESSAGE_ID` está configurado (sem `#`)
- ✅ Verifique se o cargo do bot está acima dos outros
- ✅ Certifique-se que o bot tem permissão "Gerenciar Cargos"

### Reações não funcionam

- ✅ Confirme que os **Intents** estão ativados no Discord Developer Portal
- ✅ Verifique se o `WELCOME_MESSAGE_ID` está correto
- ✅ Certifique-se que os emojis estão mapeados corretamente

### Logs de Debug

O bot exibe logs detalhados no terminal. Quando alguém reage, você verá:

```
🔔 Reação detectada!
   User ID: 123...
   Message ID: 456...
   Emoji: 🎬
   👤 Membro: Usuario#1234
   🎯 Procurando cargo ID: 789...
   🎭 Cargo encontrado: Cineamong
   ✅ Cargo 'Cineamong' adicionado a Usuario#1234!
```

## 📁 Estrutura do Projeto

```
cargonauta-bot/
├── discord_bot.py          # Código principal do bot
├── requirements.txt        # Dependências Python
├── .env.example           # Template de variáveis de ambiente
├── .env                   # Suas configurações (não commitar!)
├── README.md              # Este arquivo
└── GUIA_ENV.md           # Guia detalhado de configuração
```

## 🔒 Segurança

⚠️ **NUNCA** commite o arquivo `.env` com seu token!

Adicione ao `.gitignore`:

```gitignore
.env
bot_env/
__pycache__/
*.pyc
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido para o servidor **Among** 🎮

## 🙏 Agradecimentos

- [discord.py](https://github.com/Rapptz/discord.py) - Biblioteca Python para Discord
- Comunidade Discord pela inspiração
- Membros do servidor Among pelo feedback

## 📞 Suporte

Encontrou algum bug ou tem sugestões? Abra uma [issue](https://github.com/lucas5/cargonauta-bot/issues)!

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!
