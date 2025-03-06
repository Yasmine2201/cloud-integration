FROM python:3.10-slim AS deployjoy_api_base_dev

RUN apt update && apt install -y apt-utils postgresql-client

WORKDIR /app/
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
ADD core_models /app/core_models
RUN pip install ./core_models

# cd apis
# docker build --target deployjoy_api_auth -t registry.infra.kagescan.fr/s9-cloud-auth .
# docker run -p 8000:8000 -e USE_SQLITE=1 -it registry.infra.kagescan.fr/s9-cloud-auth
FROM deployjoy_api_base_dev AS deployjoy_api_auth
ADD auth_service .
EXPOSE 8000
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]

# docker build --target deployjoy_api_publication -t registry.infra.kagescan.fr/s9-cloud-publication .
# docker run -p 8002:8002 -e USE_SQLITE=1 -it registry.infra.kagescan.fr/s9-cloud-publication
FROM deployjoy_api_base_dev AS deployjoy_api_publication
ADD publication_service .
EXPOSE 8001
CMD ["python","manage.py","runserver", "0.0.0.0:8001"]

# docker build --target deployjoy_api_profile -t registry.infra.kagescan.fr/s9-cloud-profile .
# docker run -p 8002:8002 -it registry.infra.kagescan.fr/s9-cloud-profile
FROM deployjoy_api_base_dev AS deployjoy_api_profile
ADD profile_service .
EXPOSE 8002
CMD ["python","manage.py","runserver", "0.0.0.0:8002"]

# docker build --target deployjoy_logan -t registry.infra.kagescan.fr/s9-cloud-logan .
# docker run -p 8000:8000 -p 8001:8001 -p 8002:8002 -p 8003:8003 -p 8004:8004 -e USE_SQLITE=1 -it registry.infra.kagescan.fr/s9-cloud-logan
FROM deployjoy_api_base_dev AS deployjoy_logan
    ADD . .
    EXPOSE 8000 8001 8002 8003 8004
    CMD ["./uglydev.sh"]