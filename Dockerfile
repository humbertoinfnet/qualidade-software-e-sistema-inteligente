# Use a imagem base do Python 3.11.3
FROM python:3.11.3

# Define o diretório de trabalho dentro do contêiner
WORKDIR /

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

# Copia todo o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Comando a ser executado ao iniciar o contêiner
# CMD [ "python", "./app.py" ]
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "app.py"]


#sudo docker build -t application_score .
#docker run -p 5678:5678 -p 5000:5000 application_score