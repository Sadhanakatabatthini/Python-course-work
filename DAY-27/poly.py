class Hotstar:
    def __init__(self,name):
        print(f"Welcome to Hotstar,{name}---------------------")
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("you can resume the video")
    def ads(self):
        print("add will be run")
    def quality(self):
        print("Ypu have limited quality")
    def download(self):
        print("You cannot download the video")
    def access(self):
        print("limited Access")
    def devices(self):
        print("Limited access for login")


class Premiumhotstar:
    def __init__(self,name):
            print(f"Welcome to Hotstar,{name}---------------------")
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("you can resume the video")
    def ads(self):
        print("No adds")
    def quality(self):
        print("You have high quality")
    def download(self):
        print("You can download the video")
    def access(self):
        print("More Access")
    def devices(self):
        print("Multiple access for login")

sadhana = Hotstar("sadhana")
sadhana.auth()
sadhana.dashboard()
sadhana.search()
sadhana.history()
sadhana.playcontrollers()
sadhana.ads()
sadhana.quality()
sadhana.download()
sadhana.access()
sadhana.devices()

ruthvika = Premiumhotstar("ruthvika")
ruthvika.auth()
ruthvika.dashboard()
ruthvika.search()
ruthvika.history()
ruthvika.playcontrollers()
ruthvika.ads()
ruthvika.quality()
ruthvika.download()
ruthvika.access()
ruthvika.devices()
