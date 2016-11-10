FROM python:alpine

COPY . /opt/rda_collections_api
WORKDIR /opt/rda_collections_api
RUN pip --no-cache-dir install -r requirements.txt
RUN pip install -e .
RUN python /opt/rda_collections_api/rda_collections_api/make_swagger.py

EXPOSE 8080

CMD ["python", "/opt/rda_collections_api/rda_collections_api"]