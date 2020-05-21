FROM tiangolo/uvicorn-gunicorn-fastapi:latest


# COPY DEPENDENCIES
COPY requirements.txt ./

# COPY PROJECT
COPY ./app /app

# INSTALL DEPENDENCIES
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
