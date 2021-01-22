FROM python:3.7

COPY ./src/ /core/
COPY ./requirements.txt /core/requirements.txt

WORKDIR /core/

RUN python -m pip install -U pip
RUN pip install -r requirements.txt

CMD streamlit run app.py --server.port $PORT
