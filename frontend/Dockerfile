# השתמש בתמונה רשמית של Python
FROM python:3.9-slim

# עדכון pip
RUN pip install --upgrade pip

# התקנת תלויות
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# העתקת קוד ה-UI לתוך הקונטיינר
COPY . /app

# הפעלת Streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
