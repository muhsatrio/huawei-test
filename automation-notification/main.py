from time import sleep
from random import random
from service import notification_service

while (True):
    is_dangerous = random()
    if (is_dangerous > 0.8):
        notification_service.send()
    sleep(5)