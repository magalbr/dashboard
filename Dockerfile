#imagem base
FROM python:3.5.3
#cria e "muda" para diretorio /app
WORKDIR /app

#copia o diretorio para dentro do container
ADD . /app
#instala dependencias do projeto
RUN pip install -r requirements.txt

#roda a aplicação
CMD [ "python", "app.py" ]

