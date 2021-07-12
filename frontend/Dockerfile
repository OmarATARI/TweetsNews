FROM python:3.7.3-stretch
RUN mkdir /code

WORKDIR /code
COPY . .

RUN pip3 install --upgrade pip \
  && pip3 install -r requirements.txt

CMD ["python3","./myapp.py"]
