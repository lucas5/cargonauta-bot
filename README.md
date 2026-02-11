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

- Python 3.8+ ou Docker
- Bot Discord configurado ([Portal de Desenvolvedores](https://discord.com/developers/applications))
- Permissões: Manage Roles, Send Messages, Read Message History, Add Reactions
- Intents ativados: PRESENCE, SERVER MEMBERS, MESSAGE CONTENT

## � Instalação e Uso

### Configuração Inicial

Clone e configure:

```bash
git clone https://github.com/lucas5/cargonauta-bot.git
cd cargonauta-bot
cp env.example .env
# Edite o .env com seu token e IDs dos cargos
```

### Executar com Docker (Recomendado)

```bash
docker-compose up -d          # Iniciar
docker-compose logs -f        # Ver logs
docker-compose restart        # Reiniciar
docker-compose down           # Parar
```

### Executar com Python Local

```bash
# Com pyenv (recomendado)
pyenv install 3.14.2
pyenv local 3.14.2

# Instalar dependências
pip install -r requirements.txt

# Rodar
python discord_bot.py
```

## 🎯 Configuração no Discord

**1. Liste os cargos do servidor:**
```
!roles
```
Copie os IDs e adicione no `.env`

**2. Crie a mensagem de auto-cargos:**
```
!setup
```
Copie o ID da mensagem retornado e adicione no `.env` como `WELCOME_MESSAGE_ID`

**3. Reinicie o bot**

**4. Teste!** Reaja aos emojis e veja os cargos sendo atribuídos ✨

## 📝 Comandos Disponíveis

| Comando | Descrição | Permissão |
|---------|-----------|-----------|
| `!setup` | Cria a mensagem de boas-vindas com reações | Administrador |
| `!roles` | Lista todos os cargos do servidor com IDs | Administrador |

## ⚙️ Configuração

**Hierarquia de Cargos:** O cargo do bot deve estar acima dos cargos que ele gerencia nas configurações do servidor.

**Personalizar:** Edite `ROLE_EMOJI_MAP` e a função `setup()` em `discord_bot.py`

## 🐛 Troubleshooting

- **Bot não inicia:** Verifique token no `.env` e dependências instaladas
- **Cargos não adicionam:** Confirme IDs corretos, `WELCOME_MESSAGE_ID` configurado e hierarquia de cargos
- **Reações não funcionam:** Verifique Intents ativados no Discord Developer Portal
- **Logs:** Use `docker-compose logs -f` ou veja output do terminal

## 📁 Estrutura do Projeto

```
cargonauta-bot/
├── discord_bot.py          # Código principal do bot
├── requirements.txt        # Dependências Python
├── Dockerfile              # Configuração do container Docker
├── docker-compose.yml      # Orquestração do Docker
├── .dockerignore          # Arquivos ignorados pelo Docker
├── .env.example           # Template de variáveis de ambiente
├── .env                   # Suas configurações (não commitar!)
├── .gitignore             # Arquivos ignorados pelo Git
├── README.md              # Este arquivo
├── LICENSE                # Licença MIT
└── assets/                # Imagens e recursos
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

## 🚀 Deploy em Produção

```bash
# No servidor (com Docker instalado)
git clone https://github.com/lucas5/cargonauta-bot.git
cd cargonauta-bot
cp env.example .env
# Configure o .env
docker-compose up -d

# Atualizar
git pull && docker-compose up -d --build
```

O bot reinicia automaticamente (`restart: unless-stopped`)

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
