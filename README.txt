  Esta aplicación es un esqueleto para servicios CRUD REST escrito en Python con librería flask
la cual corre en máquina local o en contenedor Docker

Para ejecutar en máquina local:
python3 app.py

Para ejecutar en docker
se construye la imagen docker
#docker build -t flaskapp:latest .
#docker run -it flaskapp

Se puede probar con postman
http://localhost:5000/api/v1.0/task/Id/123 con GET,POST,PUT,DELETE


prerequisitos: se debio instalar virtualenv
para levantar virtualenv
#source venv/bin/activate