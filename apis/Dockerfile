FROM python:3.10-slim AS deployjoy_api_base_dev

RUN apt update && apt install -y apt-utils postgresql-client

WORKDIR /app/
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
ADD core_models /app/core_models
RUN pip install core_models

# cd apis
# docker build --target deployjoy_api_auth -t registry.infra.kagescan.fr/s9-cloud-auth .
# docker run -p 8000:8000 -it registry.infra.kagescan.fr/s9-cloud-auth
FROM deployjoy_api_base_dev AS deployjoy_api_auth
ADD auth_service .
EXPOSE 8000
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]

# docker build --target deployjoy_api_publication -t registry.infra.kagescan.fr/s9-cloud-publication .
# docker run -p 8002:8002 -it registry.infra.kagescan.fr/s9-cloud-publication
FROM deployjoy_api_base_dev AS deployjoy_api_publication
ADD publication_service/* .
EXPOSE 8001
CMD ["python","manage.py","runserver", "0.0.0.0:8001"]

# docker build --target deployjoy_api_profile -t registry.infra.kagescan.fr/s9-cloud-profile .
# docker run -p 8002:8002 -it registry.infra.kagescan.fr/s9-cloud-profile
FROM deployjoy_api_base_dev AS deployjoy_api_profile
ADD profile_service/* .
EXPOSE 8002
CMD ["python","manage.py","runserver", "8002"]


