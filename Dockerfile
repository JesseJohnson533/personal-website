# Use the official Python image with Alpine as the base
FROM python:3.13-alpine3.20

RUN apk add --no-cache \
    build-base \
    xz \
    nodejs \
    npm \
    git \
    gnupg

RUN python -m pip install --upgrade pip

# Copy
COPY requirements.txt /app/requirements.txt
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

WORKDIR /app

RUN pip install -r requirements.txt
RUN npm install

CMD ["flask", "run", "--debug"]
