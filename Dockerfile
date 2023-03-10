FROM python:3.7.7-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python", "./temp_humidity.py" ]

COPY start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]
