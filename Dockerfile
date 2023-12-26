FROM python:3-alpine

WORKDIR /app

RUN apk add --update --no-cache  \
  build-base \
  postgresql-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./load-data.py" ]