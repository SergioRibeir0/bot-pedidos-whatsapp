# 🤖 Bot de Gerenciamento de Pedidos via WhatsApp

Bot desenvolvido para automatizar o gerenciamento de pedidos via WhatsApp, integrando comunicação em tempo real com armazenamento em banco de dados.

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do portfólio prático durante a graduação em Análise e Desenvolvimento de Sistemas. O bot permite receber, registrar e gerenciar pedidos de clientes via WhatsApp de forma automatizada, eliminando a necessidade de anotações manuais e reduzindo erros operacionais.

---

## ⚙️ Funcionalidades

- Recebimento automático de pedidos via WhatsApp
- Registro dos pedidos em banco de dados MySQL
- Respostas automáticas para o cliente
- Webhook integrado com a API do Twilio
- Gerenciamento de rotas com Flask

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python | Linguagem principal |
| Flask | Framework web / servidor |
| MySQL | Banco de dados |
| Twilio API | Integração com WhatsApp |
| Ngrok | Exposição do servidor local |

---

## 🚀 Como Rodar Localmente

### Pré-requisitos

- Python 3.12+
- MySQL instalado e rodando
- Conta no [Twilio](https://www.twilio.com/) com WhatsApp Sandbox configurado
- [Ngrok](https://ngrok.com/) instalado

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/SergioRibeir0/bot-pedidos-whatsapp.git
cd bot-pedidos-whatsapp
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```env
TWILIO_ACCOUNT_SID=seu_account_sid
TWILIO_AUTH_TOKEN=seu_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
```

**4. Inicie o servidor Flask**
```bash
python run.py
```

**5. Exponha o servidor com Ngrok**
```bash
ngrok http 5000
```

**6. Configure o Webhook no Twilio**

Cole a URL gerada pelo Ngrok no campo de Webhook do seu WhatsApp Sandbox no painel do Twilio.

---

## 📁 Estrutura do Projeto

```
bot-pedidos-whatsapp/
│
├── app/
│   ├── __init__.py       # Inicialização da aplicação Flask
│   ├── database.py       # Conexão e operações com o banco de dados
│   ├── models.py         # Modelos de dados
│   └── routes.py         # Rotas e lógica do webhook
│
├── .gitignore
├── requirements.txt      # Dependências do projeto
├── run.py                # Ponto de entrada da aplicação
└── README.md
```

---

## 👨‍💻 Autor

**Sérgio Luiz Ribeiro dos Santos**  
Graduado em Análise e Desenvolvimento de Sistemas — Impacta Tecnologia  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sergio-ribeiroo/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/SergioRibeir0)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
