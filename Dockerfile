FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expose the port on which the app will run
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver"]
