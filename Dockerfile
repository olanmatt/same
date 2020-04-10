FROM python:3

COPY same.py /

ENTRYPOINT ["python3", "same.py"]
CMD ["/a", "/b"]
