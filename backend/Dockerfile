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

# Copy application code
COPY ./src /app
# Copy wait-for-it script
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Start FastAPI app with wait-for-it
CMD ["/wait-for-it.sh", "db_service:5432", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
