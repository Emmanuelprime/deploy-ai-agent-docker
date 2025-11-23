# Base image
FROM python:3.9.23-slim-bullseye

WORKDIR /app

# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

# RUN echo "hello" > index.html

COPY ./src /app

# Start the Python file server
CMD ["python", "-m", "http.server", "8000"]
