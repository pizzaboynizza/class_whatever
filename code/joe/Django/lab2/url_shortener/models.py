from django.db import models

# ☑ Version 1
# ☑ Version 2
# ☑? Version 3

class UrlShortener(models.Model):
    short_code = models.CharField(unique=True, max_length=7)
    long_link = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return f"{self.short_code} : '{self.long_link}'"


class UserLinkData(models.Model):
    user_ip = models.CharField(max_length=16) # REMOTE_ADDR
    user_agent = models.CharField(max_length=255) # HTTP_USER_AGENT
    link_clicked = models.ForeignKey(UrlShortener, on_delete=models.CASCADE)
    times_clicked = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user_ip}@({self.user_agent}) clicked {self.link_clicked} a total of {self.times_clicked} time(s)"

    def user_str(self):
        return f"{self.user_ip}@({self.user_agent})"