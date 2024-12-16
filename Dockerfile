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