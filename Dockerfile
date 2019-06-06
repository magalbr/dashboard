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

 user = {'cn': 'Lucas','sn': 'Salles','mail': 'lucas.salles@4linux.com.br','uidNumber': '123','gidNumber': '123','uid': 'lucas','homeDirectory': '/home/lucas','userPassword': '4linux'}
objectClass = [ 'top', 'person', 'organizationalPerson','inetOrgPerson', 'posixAccount' ]
cn = 'uid{},dc=dexter,dc=com,dc=br'.format(user['mail'])
objectClass = [ 'top', 'person', 'organizationalPerson',
res = connection.add(cn, objectClass, user)
email = 'lucas.salles@4linux.com.br'
dn = 'uid={},dc=dexter,dc=com,dc=br'format(email)