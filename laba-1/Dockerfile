FROM python:3.6

ENV TARGET_PATH=/usr/src/bsuir/4-sem/isp/laba-1/

RUN mkdir -p "${TARGET_PATH}"

WORKDIR "${TARGET_PATH}"

COPY example.py "${TARGET_PATH}"

RUN set -ex \ pip3 install —no-cache-dir -r requirements.txt \
&& rm requirements.txt

CMD ["python3", "example.py"]
