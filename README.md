# same

Check see if two directories have the same contents using SHA512. Ignores names, timestamps, etc. and only considers the contents of the file.

Run using Python directly, or by calling it with Docker...

```
docker run -it \
	-v /YOUR_FIRST_DIR:/a:ro \
	-v /YOUR_SECOND_DIR:/b:ro \
	olanmatt/same
```
