#  Desktop Notifier Using Python

from plyer import notification
import time

if __name__ == "__main__":
    while True :
        notification.notify(
        title = ' **** TAKE REST ****',
        message = 'Rest is vital for better mental health, incresed concentration and memory.',
        timeout = 5,
       
        )
        time.sleep(20)


# pythonw filename  {Use for to run file in background}



