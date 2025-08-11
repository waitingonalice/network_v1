FROM python:3.12.4-slim-bookworm AS base

ARG APP_DIR=/backup-service

WORKDIR ${APP_DIR}

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential


FROM base AS build-stage

COPY ./requirements.txt ${APP_DIR}

FROM base AS run-stage
# Python buffered output to stdout
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN addgroup --system fastapi \
    && adduser --system --ingroup fastapi fastapi

RUN chown -R fastapi:fastapi ${APP_DIR}

COPY --from=build-stage ${APP_DIR} ${APP_DIR}
RUN pip install --no-cache-dir -r ${APP_DIR}/requirements.txt

COPY ./scripts/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY --chown=fastapi:fastapi ./app ${APP_DIR}/app
COPY --chown=fastapi:fastapi ./alembic.ini ${APP_DIR}/alembic.ini

USER fastapi

ENTRYPOINT ["/entrypoint"]