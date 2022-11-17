# p-sec-individu-opdr
1 Make sure docker is running
2. go to <your dir>/p-sec-individu-opdr/individu project
3. run to build the docker image
```
docker build -t <Name you want> .
```
4. run to start the container
```
docker run -dit -p 5000:5000 <Name you choose>
```
5. to see the website go to [a relative link](http://127.0.0.1:5000)
