import random
import smtplib, ssl # built in module for sending emails


port = 465  # For SSL (endpoint)
smtp_server = "smtp.gmail.com" # (outgoing) Simple Mail Transfer Protocol
sender_email = "notificationc593@gmail.com"  
# password = input("Type your password and press enter: ")
password = "Daphney1!"


ball_courts = [ "24 Hour Fitness The Pearl 228", "Overlook Park", "Lloyd Athletic Club", "Wallace Park", "Couch Park", "Matt Dishman Community Center & Pool", "LA Fitness", "Dawson Park"]


# I will choose three locations that I would like to get a notification from if one of my friends go there. I used split by a comma becuase if I just turned user_input into a set without turning it into a list it would have made each letter into a string.
user_1_input = input("what locations would you like to get a notification from?: ").split(",")



# random.choices(ballcourts) is acting as a replacement of my friends going to a basket ball court.
Alex = list(random.choices(ball_courts))
Skylar = list(random.choices(ball_courts))
Doja = list(random.choices(ball_courts))
Levi = list(random.choices(ball_courts))

#  I saved each user input in a list and put them into a set. I saved the set into a variable so that I could use set intersection(). The intersection() method returns a new set with elements that are common to all sets.
def location():
    s1 = set(user_1_input)
    s2 = set(Alex)
    s3 = set(Skylar)
    s4 = set(Doja)
    s5 = set(Levi)
   
  
    if s1.intersection(s2):
        results_s2 = s1.intersection(s2)
        receiver_email = "capstonemini@gmail.com"  # Enter receiver address
        message = f"""\
        Subject: Notification from Alex

        Your friend Alex is on their way to the {results_s2}."""
        context = ssl.create_default_context () # reset to default sett as blank email
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(receiver_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("results_s2", list(results_s2))
            
    elif s1.intersection(s3):     
        results_s3 = s1.intersection(s3)
        receiver_email = "capstonemini@gmail.com"  # Enter receiver address
        message = f"""
        Subject: Notification from Skylar

        Your friend Skylar is on their way to the { results_s3}."""
        context = ssl.create_default_context ()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(receiver_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("results_s3", list(results_s3))
            
        
    elif s1.intersection(s4):
        results_s4 = s1.intersection(s4)
        receiver_email = "capstonemini@gmail.com"  # Enter receiver address
        message = f"""\
        Subject: Notification from Doja

        Your friend Doja is on their way to the {results_s4}."""
        context = ssl.create_default_context ()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(receiver_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("results_s4", list(results_s4))
    elif s1.intersection(s5):
        results_s5 = s1.intersection(s5)
        receiver_email = "capstonemini@gmail.com"  # Enter receiver address
        message = f"""\
        Subject: Notification from Levi

        Your friend Levi is on their way to the {results_s5}."""
        context = ssl.create_default_context ()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(receiver_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("results_s5", list(results_s5))
        
location()

        #   Overlook Park,Wallace Park,LA Fitness  
      


