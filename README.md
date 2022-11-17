# p-sec-individu-opdr

##How to implement the docker website
1 Make sure docker is running<br>
2. go to <your dir>/p-sec-individu-opdr/individu project<br>
3. run ```docker build -t <Name you want> .``` to build the docker image<br>
4. run ```docker run -dit -p 5000:5000 <Name you choose>``` to start the container<br>
5. to see the website go to [http://127.0.0.1:5000](http://127.0.0.1:5000) dont go to localhost:5000 because localhost is not in the list of supported domain<br>
  
## To do:
- [x] Make captcha
- [x] Make a limit amount of login attempts system
- [x] Make a log file for the login attempts and the information about the ip that attempted to login to a specific account/user
- [ ] Block ip if it make too many login attempts between a certain interval

##Information
 This website is meant to limit automated brute force attacks by using the recaptcha of google, the limited amount of login attempts and monitor the login attempts to maybe take action in the future or block the ip directly if it make too many login attempts
 
##Disclaimer
Because the website is running on a docker container the ip-api is not able to get the information about your local ip but if the website was running on a deticated webserver the api would get the public ip instead of the private ip
