FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
&& pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py"]