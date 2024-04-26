FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
EXPOSE 5000
# CMD waitress-serve --listen=127.0.0.1:5000 app:app
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
# CMD python app.py 