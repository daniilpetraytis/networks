FROM python:3.8

RUN apt update && apt install -y python3 iputils-ping

WORKDIR /script_code

COPY . .

ENTRYPOINT [ "python3", "script.py" ]