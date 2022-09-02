FROM python:3.10
WORKDIR /OPAP-TelegramBot
COPY requirements.txt /OPAP-TelegramBot/
RUN pip install -r requirements.txt
COPY . /OPAP-TelegramBot
CMD python main.py