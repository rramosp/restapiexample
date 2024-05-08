FROM python

RUN pip install Flask loguru numpy

RUN mkdir /app

COPY myrestapi.py /app

WORKDIR /app

CMD flask --app myrestapi run --host=0.0.0.0 



