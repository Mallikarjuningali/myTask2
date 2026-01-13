FROM python:3.11-slim
WORKDIR /api
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "apps.py"]

