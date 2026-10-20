FROM mcr.microsoft.com/playwright/python:v1.60.0-noble

WORKDIR /app

ENV ENVIRONMENT=QA

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-m", "smoke"]