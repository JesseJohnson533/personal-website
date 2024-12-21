# Use the official Python image with Alpine as the base
FROM python:3.13-alpine3.20

# Install necessary dependencies
RUN apk add --no-cache \
    build-base \
    xz \
    nodejs \
    npm \
    git \
    gnupg

# Install the latest version of pip
RUN python -m pip install --upgrade pip

# Copy
COPY requirements.txt /app/requirements.txt
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

WORKDIR /app

RUN pip install -r requirements.txt
RUN npm install

# Run flask on debug mode and port 5000
CMD ["flask", "run", "--debug"]
