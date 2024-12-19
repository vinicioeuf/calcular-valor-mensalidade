# Calcular Valor Mensalidade

![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)

## ✨ Visão Geral

O **Calcular Valor Mensalidade** é um projeto desenvolvido para calcular o custo mensal do transporte da faculdade de Cedro-PE. Este sistema auxilia estudantes e organizadores a determinar valores de forma eficiente e precisa, considerando variáveis como distância, quantidade de passageiros e custos operacionais.

---

## 🔧 Funcionalidades

- Cálculo automático do valor mensal com base nos parâmetros fornecidos.
- Personalização de custos fixos e variáveis.
- Interface amigável e intuitiva.
- Relatórios detalhados sobre os custos.

---

## 📊 Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

- **[Django](https://www.djangoproject.com/)** - para o backend e processamento de dados.
- **[Bootstrap](https://getbootstrap.com/)** - para estilização da interface do usuário.

---

## 🚀 Como Rodar o Projeto

### Requisitos:
- Python 3.x e pip instalados.

### Passos:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/calcular-valor-mensalidade.git
   ```
2. Navegue até o diretório:
   ```bash
   cd calcular-valor-mensalidade
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
7. Acesse no navegador:
   [http://localhost:8000](http://localhost:8000)

---

## 🖊þ Estrutura do Projeto

```plaintext
calcular-valor-mensalidade/
├── app/                  # Aplicação principal
├── templates/            # Arquivos HTML com Bootstrap
├── static/               # Arquivos estáticos (CSS, JS, imagens)
├── manage.py             # Gerenciador do Django
├── requirements.txt      # Dependências do projeto
├── .env                  # Configurações de ambiente
├── db.sqlite3            # Banco de dados SQLite
└── README.md             # Documentação do projeto
```

---

## ✨ Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório.
2. Crie uma branch para sua funcionalidade:
   ```bash
   git checkout -b minha-nova-funcionalidade
   ```
3. Realize suas alterações e faça commit:
   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-nova-funcionalidade
   ```
5. Abra um Pull Request.

---

## 📚 Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).

---

## 🔗 Links Importantes

- [Documentação Oficial](https://github.com/seu-usuario/calcular-valor-mensalidade/wiki)
- [Relatório de Problemas](https://github.com/seu-usuario/calcular-valor-mensalidade/issues)

---

Desenvolvido com ❤ por [Seu Nome].
