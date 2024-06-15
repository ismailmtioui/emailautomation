import smtplib
from mongodbHelper import get_single_document
def send():
    try:
        x=smtplib.SMTP("smtp.gmail.com",587)
        x.starttls()
        config_data=get_single_document("config",{"name":"email_config"},{"username":1,"password":1,"_id":0})
        print(config_data)
        x.login(config_data['username'],config_data['password'])
        subject="testing"
        body_text="DOCKER"
        message="Subject: {}{}".format(subject,body_text)
        x.sendmail("ismailelmtioui2357@gmail.com","ismail.elmtioui@etu.uae.ac.ma",message)
        print("sucess")
    except Exception as exeception:
       print(exeception)
       print("failure")
if __name__ == "__main__":
    send()