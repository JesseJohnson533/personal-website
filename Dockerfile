FROM python:3.10-alpine
WORKDIR /code

# Install dependencies required for building packages
RUN apk add --no-cache gcc musl-dev linux-headers curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set environment variables for Poetry and Flask
ENV PATH="/root/.local/bin:$PATH"
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy Poetry files
COPY pyproject.toml poetry.lock /code/

# Install dependencies via Poetry
RUN poetry install --no-dev --no-root

EXPOSE 5000

# Copy the rest of the application code
COPY . .

# Run the Flask app
CMD ["flask", "run", "--debug"]