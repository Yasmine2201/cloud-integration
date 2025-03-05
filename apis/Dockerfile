FROM python:3.10-slim AS deployjoy_api_base_dev
    # Debugging tools
    RUN apt update && apt install -y apt-utils postgresql-client

    WORKDIR /app/
    ADD requirements.txt /app/requirements.txt
    RUN pip install --no-cache-dir -r /app/requirements.txt
    ADD core_models /app/core_models

# cd apis
# docker build --target deployjoy_api_migration -t registry.infra.kagescan.fr/s9-cloud-migrator .
# docker run -p 8000:8000 -it registry.infra.kagescan.fr/s9-cloud-migrator
FROM deployjoy_api_base_dev AS deployjoy_api_migrator
    ADD auth_service/manage.py .
    ADD auth_service/auth_service auth_service
    ADD auth_service/authentication authentication
    CMD ["sh", "-c", "python manage.py makemigrations core_models"]

# cd apis
# docker build --target deployjoy_api_auth -t registry.infra.kagescan.fr/s9-cloud-auth .
# docker run -p 8000:8000 -it registry.infra.kagescan.fr/s9-cloud-auth
FROM deployjoy_api_base_dev AS deployjoy_api_auth
    ADD auth_service/manage.py .
    ADD auth_service/authentication authentication
    ADD auth_service/auth_service auth_service
    EXPOSE 8000
    CMD ["sh", "-c", "python manage.py migrate \
        && python manage.py runserver 0.0.0.0:8000 \
    "]

# docker build --target deployjoy_api_publication -t registry.infra.kagescan.fr/s9-cloud-publication .
# docker run -p 8002:8002 -it registry.infra.kagescan.fr/s9-cloud-publication
FROM deployjoy_api_base_dev AS deployjoy_api_publication
    ADD publication_service/manage.py .
    ADD publication_service/publication publication
    ADD publication_service/publication_service publication_service
    EXPOSE 8001
    CMD ["sh", "-c", "python manage.py migrate \
        && python manage.py runserver 0.0.0.0:8001 \
    "]

# docker build --target deployjoy_api_profile -t registry.infra.kagescan.fr/s9-cloud-profile .
# docker run -p 8002:8002 -it registry.infra.kagescan.fr/s9-cloud-profile
FROM deployjoy_api_base_dev AS deployjoy_api_profile
    ADD profile_service/manage.py .
    ADD profile_service/profile_service profile_service
    ADD profile_service/userprofile userprofile
    EXPOSE 8002
    CMD ["sh", "-c", "python manage.py migrate \
        && python manage.py runserver 0.0.0.0:8002 \
    "]
    
# docker build --target deployjoy_logan -t registry.infra.kagescan.fr/s9-cloud-logan .
# docker run -p 8000:8000 -p 8001:8001 -p 8002:8002 -p 8003:8003 -p 8004:8004 -it registry.infra.kagescan.fr/s9-cloud-logan
FROM deployjoy_api_base_dev AS deployjoy_logan
    ADD . .
    EXPOSE 8000 8001 8002 8003 8004
    CMD ["./uglydev.sh"]
