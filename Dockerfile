FROM python:3

RUN pip3 --no-cache-dir install tqdm
COPY same.py /

ENTRYPOINT ["python3", "same.py"]
CMD ["/a", "/b"]
