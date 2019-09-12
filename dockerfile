FROM python:latest

WORKDIR /usr/share/PriceCheck/
COPY . /usr/share/PriceCheck/
RUN pip install -r requierments.txt

ENTRYPOINT [ "python", "main.py" ]