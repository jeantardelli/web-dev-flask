FROM python:3.8-alpine

ENV FLASK_APP application.py
ENV FLASK_CONFIG production

RUN adduser -D talita-arqueros
USER talita-arqueros

WORKDIR /home/talita-arqueros

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY application.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
RUN chmod +x boot.sh
ENTRYPOINT ["./boot.sh"]
