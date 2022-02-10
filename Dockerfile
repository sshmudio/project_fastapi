FROM python:3.9
WORKDIR /srv
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /srv/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /srv/requirements.txt
COPY ./srv /srv
CMD ["uvicorn", "code.main:app", "--host", "0.0.0.0", "--port", "8000"]