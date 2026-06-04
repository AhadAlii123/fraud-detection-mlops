# 1. Official Lightweight Python image use karein
FROM python:3.11-slim

# 2. Container ke andar working directory set karein
WORKDIR /app

# 3. requirements.txt ko container mein copy karein
COPY requirements.txt .

# 4. Required libraries install karein
RUN pip install --no-cache-dir -r requirements.txt

# 5. Hamari main.py aur trained model.pkl file ko container mein copy karein
COPY main.py .
COPY model.pkl .

# 6. Container kis port par network access dega
EXPOSE 8000

# 7. FastAPI server ko container ke andar run karne ki command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]