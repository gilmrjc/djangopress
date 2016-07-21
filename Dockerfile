FROM gilmrjc/multisite-django:dev-latest

COPY . /usr/src/app

RUN pip install --no-cache-dir -r /usr/src/app/requirements/docker.txt

RUN addgroup django && \
    adduser django -G django -h /usr/src/app -D && \
    chown -R django:django /usr/src/app

USER django

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/manage.py", "runserver"]

CMD ["0.0.0.0:8000"]
