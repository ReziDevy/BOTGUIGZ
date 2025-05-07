# BOTGUIGZ - Twitch Bot

Este repositório contém o código para um **bot personalizado da Twitch**, criado para automatizar interações com o chat, responder comandos e gerar links exclusivos para os seguidores. O bot foi desenvolvido como parte de um projeto para um streamer, com o objetivo de criar um sistema simples e funcional.

## Funcionalidades

- **Comando !linkespecial**: Gera um link exclusivo para cada usuário que envia o comando no chat da Twitch. O link redireciona para um formulário onde o usuário pode visualizar informações e completar uma ação.
- O bot é configurado para interagir com o chat da Twitch, utilizando a API da Twitch (TwitchIO) para responder aos comandos.
- Cada link gerado inclui um código único, permitindo um rastreamento individual por usuário.

## Como usar

### 1. Requisitos

- Python 3.8 ou superior.
- Bibliotecas: `twitchio`, `dotenv` (para carregar variáveis de ambiente), `random` (para gerar códigos aleatórios).
- Acesso à **API da Twitch** (token e client ID).
- O link para o formulário (ou qualquer outro link desejado) deve ser configurado nas variáveis de ambiente.

### 2. Instalar Dependências

Primeiro, clone o repositório:

```bash
git clone https://github.com/ReziDevy/BOTGUIGZ.git
cd BOTGUIGZ
Instale as dependências necessárias:
pip install -r requirements.txt
3. Configuração
Crie um arquivo .env com as seguintes variáveis (substituindo pelos seus próprios valores):
BOT_TOKEN=seu_token_aqui
CLIENT_ID=seu_client_id_aqui
BOT_NICK=seu_nick_aqui
4. Rodar o bot
Execute o bot com o comando:
python bot_final.py
O bot se conectará ao chat da Twitch e começará a responder comandos automaticamente.

Personalização
Para personalizar os comandos ou adicionar novas funcionalidades, basta editar o arquivo bot_final.py e ajustar os comportamentos conforme necessário.

Licença
Este projeto é open-source e pode ser utilizado ou modificado de acordo com a licença MIT.

Autor
ReziDevy - Desenvolvedor do projeto. Para contato ou dúvidas, acesse:

GitHub - https://github.com/ReziDevy
