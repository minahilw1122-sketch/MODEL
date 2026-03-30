FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r Requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]