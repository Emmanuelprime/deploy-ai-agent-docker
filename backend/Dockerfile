# Base image
FROM python:3.9.23-slim-bullseye

WORKDIR /app
# create virtual environment
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH



# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

# RUN echo "hello" > index.html

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY ./src /app
# Start the Python file server
CMD ["python", "-m", "http.server", "8000"]
