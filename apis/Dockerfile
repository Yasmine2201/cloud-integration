FROM python:3.10-slim AS deployjoy_api_base_dev
    # Debugging tools
    RUN apt update && apt install -y apt-utils postgresql-client

    WORKDIR /app/
    ADD requirements.txt /app/requirements.txt
    RUN pip install --no-cache-dir -r /app/requirements.txt
    ADD core_models /app/core_models
    
# cd apis
# docker build --target deployjoy_api_auth -t registry.infra.kagescan.fr/s9-cloud-auth .
# docker run -p 8000:8000 -it registry.infra.kagescan.fr/s9-cloud-auth
FROM deployjoy_api_base_dev AS deployjoy_api_auth
    ADD auth_service/manage.py .
    ADD auth_service/auth_service auth_service
    ADD auth_service/authentication authentication
    EXPOSE 8000
    CMD ["sh", "-c", " \
        python manage.py makemigrations core_models \
        && python manage.py migrate \
        && python manage.py runserver 0.0.0.0:8000 \
    "]