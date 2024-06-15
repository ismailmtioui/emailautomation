import smtplib
def send():
    try:
        x=smtplib.SMTP("smtp.gmail.com",587)
        x.starttls()
        x.login("ismailelmtioui2357@gmail.com","klzadxqqwvkdlczl")
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