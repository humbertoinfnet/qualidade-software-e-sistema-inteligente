<h1>Projeto Full-Stack-Basico Back-End</h1> 

- Projeto que contempla o MVP para o primeiro modulo da PÓS GRADUAÇÃO de Engenharia de Software da PUC
- O MVP pensado nesse modulo é um projeto de cadastro de políticas
- O projeto consiste em cadastrar, atualizar e desativar regras, políticas e demais componentes


[![PyPI](https://img.shields.io/pypi/pyversions/apache-superset.svg?maxAge=2592000)](https://pypi.python.org/pypi/apache-superset)


> Status do Projeto: :heavy_check_mark: Concluido

... 

## Descrição do projeto 

<p align="justify">
  Sistema de classificação de crédito, definindo o risco de inadimplência de acordo com as informações do ciente.
</p>

## Visão Geral da Solução

A solução foi feita abordando 3 partes principais:

- Modelagem: feita com estudos em um notebook jupyter
- Back-end: foi criado um endpoint recebendo com entrada as features do modelo treinado e executando a predição de probabilidade de inadimplência
- Front-end: tela com os campos para informar os valores das features do modelo e a resposta da predição com um gráfico de explicação da classificação


## Pré-requisitos

:warning: [Python 3.11.3](https://www.python.org/downloads/release/python-3113/)


No terminal, clone o projeto: 

```bash
# Clonar o projeto
git clone https://github.com/humbertoinfnet/qualidade-software-e-sistema-inteligente.git
```

## Utilizando VENV
Recomenda-se o uso de um ambiente virtual (virtualenv) para isolar as dependências do projeto. Para configurar e ativar um ambiente virtual, execute os seguintes comandos no terminal:
```bash
# Instalar o virtualenv, se ainda não estiver instalado
pip install virtualenv

# Criar um novo ambiente virtual
virtualenv venv

# Ativar o ambiente virtual (Windows)
venv\Scripts\activate

# Ativar o ambiente virtual (Linux/Mac)
source venv/bin/activate

# Instalação dos pacotes python
pip install -r requirements.txt
```

Rodando a aplicação com venv: 

```bash
# No diretório raiz do projeto executar o comando
python app.py
```
## Utilizando Docker
Criando imagem docker:
```bash
# No diretório raiz do projeto executar o comando
sudo docker build -t application_score .
```

Rodando a aplicação com docker: 

```bash
# No diretório raiz do projeto executar o comando
docker run -p 5678:5678 -p 5000:5000 application_score
```
## Erro na requisição do request-data:

Configurando env:
```bash
# No diretório raiz renomear o arquivo .env_example para .env
# rodar o projeto request-data e verificar o IP atribuido através do docker
docker network inspect bridge

# alterar no arquivo env substituindo a URL de acordo com o IP atribuido ao projeto request-data
```

## Estrutura do Projeto
| Diretorio       | Diretorio              | Diretorio       | Diretorio         | Descrição                                                      |  
|---------------|----------------------|---------------|-----------------|------------------------------------------------------------------------|
| src/          |                      |               |                 | Diretório raiz do projeto                                              |
|               | entities/            |               |                 | Entidades principais do projeto, como classes ou objetos               |
|               | external_interfaces/ |               |                 | Diretório relacionado a configurações de aplicações externas           |
|               |                      | database/     |                 | Código relacionado ao banco de dados                                   |
|               |                      |               | controllers/    | Lógica de execução das consultas SQL                                   |
|               |                      |               | models/         | Definição dos modelos de tabelas                                       |
|               |                      | flask_server/ |                 | Códigos relacionado ao Flask                                           |
|               |                      |               | routers/        | Definição das rotas da API                                             |
|               |                      |               | app             | Configurações do servidor Flask                                        |
|               |                      |               | register_route  | Código para registrar as rotas                                         |
|               | interface_adapters/  |               |                 | Códigos que fazem a interface entre casos de uso e aplicações externas |
|               | log/                 |               |                 | Configuração dos logs                                                  |
|               | use_case/            |               |                 | Casos de uso do projeto                                                |
|               |                      |application_score/     |        | Lógica dos casos de uso relacionados classificação de risco de credito              |
| app           |                      |               |                 | Arquivos específicos da aplicação principal                            |
| requirements  |                      |               |                 | Lista de dependências do projeto                                       |
| gitignore     |                      |               |                 | Arquivo para especificar arquivos e diretórios que devem ser ignorados pelo git |

