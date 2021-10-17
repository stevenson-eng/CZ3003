FROM python:3.8
ENV MAIL_USERNAME=game.of.thrones.mail.service
ENV MAIL_PASSWORD=game.of.thrones
ENV MAIL_FROM=game.of.thrones.mail.service@gmail.com
ENV MAIL_PORT=587
ENV MAIL_SERVER=smtp.gmail.com
ENV MAIL_FROM_NAME="Game of Thrones Mail Service"
ADD admin_ui /admin_ui/
ADD okteto-stack.yaml /admin_ui/src/okteto-stack.yaml
RUN pip install -r /admin_ui/src/requirements.txt
EXPOSE 8080
WORKDIR /admin_ui/src/
CMD ["uvicorn", "main:app", "--reload", "--port", "8080", "--host", "0.0.0.0"]
