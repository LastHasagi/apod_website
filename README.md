## NASA APOD Website

Este projeto é um site que exibe a Foto do Dia da NASA (Astronomy Picture of the Day - APOD). Os usuários podem selecionar uma data específica para visualizar a foto e a explicação correspondente fornecida pela NASA.

### Tecnologias Utilizadas

| Tecnologia      | Descrição                                                                 | Uso no Projeto                                      |
|-----------------|---------------------------------------------------------------------------|-----------------------------------------------------|
| Python          | Linguagem de programação principal.                                       | Utilizada para desenvolver a lógica do backend.     |
| Flask           | Microframework web para Python.                                           | Utilizado para criar o servidor web.                |
| HTML            | Linguagem de marcação padrão para criar páginas web.                      | Utilizado para estruturar o conteúdo da página.     |
| CSS             | Linguagem de estilo para páginas web.                                     | Utilizado para estilizar a página web.              |
| JavaScript      | Linguagem de programação para web.                                        | Utilizado para manipulação do DOM e requisições API.|
| API da NASA     | Serviço web que fornece a Foto do Dia da NASA.                            | Utilizado para obter a foto e a explicação do dia.  |
| python-dotenv   | Biblioteca para carregar variáveis de ambiente de um arquivo [`.env`].    | Utilizado para gerenciar chaves de API e variáveis sensíveis. |
| Uvicorn         | Servidor ASGI rápido para Python.                                         | Utilizado para rodar o servidor Flask em produção no Windows.  |
| Gunicorn         | Servidor ASGI rápido para Python.                                         | Utilizado para rodar o servidor Flask em produção no Windows.  |


### Estrutura do Projeto

```
apod_website/
├── app/
│   ├── static/
│   │   └── index.html
│   ├── __init__.py
│   ├── routes.py
├── venv/
├── .env
├── .gitignore
├── config.py
├── main.py
├── README.md
├── requirements.txt
```

- **app/**: Diretório principal da aplicação.
  - **static/**: Contém arquivos estáticos como HTML, CSS e JavaScript.
    - **index.html**: Página principal do site.
  - **__init__.py**: Inicializa o aplicativo Flask.
  - **routes.py**: Define as rotas da aplicação.
- **venv/**: Ambiente virtual Python.
- **.env**: Arquivo que contém variáveis de ambiente (não incluído no GitHub).
- **.gitignore**: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
- **config.py**: Arquivo de configuração que carrega variáveis de ambiente.
- **main.py**: Arquivo principal que inicia o servidor Flask.
- **README.md**: Este arquivo, que contém informações sobre o projeto.
- **requirements.txt**: Lista de dependências do projeto.

### Como Rodar o Projeto

1. **Clone o repositório:**
   ```CMD
   git clone https://github.com/LastHasagi/apod_website.git
   cd apod_website
   ```

2. **Crie e ative um ambiente virtual:**
   ```CMD
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Instale as dependências:**
   ```CMD
   pip install -r requirements.txt
   ```

4. **Crie um arquivo [`.env`](acesse: https://api.nasa.gov para ter sua chave API) na raiz do projeto e adicione a chave da API:**
   ```
   SECRET_KEY=YOUR_SECRET_KEY
   ```

5. **Execute o servidor:**
   ```CMD
   python main.py
   ```

6. **Acesse a aplicação no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

### Funcionalidades

- **Escolha de Data:** Os usuários podem selecionar uma data específica para visualizar a foto do dia correspondente.
- **Exibição da Foto:** A foto do dia é exibida em uma dimensão padrão.
- **Exibição da Explicação:** A explicação da foto é exibida abaixo da imagem.

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
