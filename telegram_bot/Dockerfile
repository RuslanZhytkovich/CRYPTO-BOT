FROM python:3.9

WORKDIR telegram_bot/src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "-m", "src.main"]
