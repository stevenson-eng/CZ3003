## Admin UI Non-functional Testing (Security)

- Technology:

  - [OWASP ZAP](https://www.zaproxy.org/download/)
  - Java
  - mvn
  - Selenium

- Basic set up (to ensure that it works)

  - Test using bodgeit store:

    - [YouTube tutorial](https://www.youtube.com/watch?v=H0kSuP1bM1Y)

  - [Tomcat Server](http://tomcat.apache.org/)

    - [How to start server](https://www.youtube.com/watch?v=h_qQOVDTxo8)

    - Tl/dr: enable all executables under bin (*.sh), then run startup.sh or shutdown.sh to start or stop the server respectively

      ```bash
      cd bin
      ls -al *.sh
      ./startup.sh
      ./shutdown.sh
      ```

  - [Bodgeit Store](https://github.com/psiinon/bodgeit/releases/tag/1.4.0)

    - [DEPRACATED](https://code.google.com/archive/p/bodgeit/)

    - Under the `webapps` directory, create folder (i.e. `store`)  

    - Download the war file and extract the contents into `store` using the following command

      ```bash
      jar -xvf <filename>.war        
      ```

    - Start your tomcat server

    - Go to your browser and search `localhost:8080/store`

