from notify_run import Notify
import webbrowser
import requests
import random

notify = Notify(endpoint="https://notify.run/p115j44S8CcVHt73")
notify.send('Hi there!')