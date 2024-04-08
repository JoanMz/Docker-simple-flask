#Practice docker volume with simple flask application

**How to run the Dockerfile**

<pre>docker build -t joandatabrick/simpleflaskvolume:v1</pre>

<p>after create the imagen we will create the container</p>

<pre>docker create --name <containername> -p <yourport>:5000 -v ./data:/app/Data
