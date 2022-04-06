import platform
from os import environ
from os import system
import requests
# from win10toast_click import ToastNotifier
import webbrowser
import time
import datetime

class TwitchLiveCheck:
    def __init__(self, channels, os):
        self.os = os

        # API setting
        self.authUrl = 'https://id.twitch.tv/oauth2/token'
        self.client_id = environ['client_id']
        self.client_secret = environ['client_secret']

        self.baseURL = 'https://www.twitch.tv/'
        self.targetURL = ''

        self.authParams = {
            'client_id' : self.client_id,
            'client_secret' : self.client_secret,
            'grant_type' : 'client_credentials'
        }

        self.authCall = requests.post(url=self.authUrl, params=self.authParams)
        self.accessToken = self.authCall.json()['access_token']
        self.header = {
            'Client-ID' : self.client_id,
            'Authorization' : 'Bearer {}'.format(self.accessToken)
        }

        self.apiBaseURL = 'https://api.twitch.tv/helix/streams?user_login='

        self.channels = channels
        self.status = {channel: False for channel in self.channels}

        self.userName = ''
        self.tmpTitle = ''

        # Win notify
        if self.os == 'Windows':
            self.toaster = ToastNotifier()
        else:
            self.toaster = None


    def macNotify(self, title, text):
        # For MacOS
        system("""
                osascript -e 'display notification "{}" with title "{}" sound name "Default"'
                """.format(text, title))


    def run(self):
        for channel in self.channels:
            tmpStatus = self.check(channel)
            if self.status[channel] == False and tmpStatus:
                self.targetURL = self.baseURL + channel

                if self.os == 'Windows':
                    self.toaster.show_toast(
                        title="{} Online!".format(self.userName),
                        msg=self.tmpTitle,
                        icon_path='twitch_1.ico',    
                        duration=5,
                        callback_on_click=self.open_url
                    )
                elif self.os == 'Darwin':
                    self.macNotify(
                        title='{} Online!'.format(self.userName),
                        text=self.tmpTitle
                    )

            self.status[channel] = tmpStatus 
            time.sleep(5)

        print(datetime.datetime.now().isoformat(), self.status)
    

    def open_url(self):
        webbrowser.open_new(self.targetURL)


    def check(self, channel):
        apiURL = '{}{}'.format(self.apiBaseURL, channel)

        requestResult = requests.get(url=apiURL, headers=self.header).json()['data']

        if requestResult:
            if requestResult[0]['type'] == 'live':
                self.userName = requestResult[0]['user_name']
                self.tmpTitle = requestResult[0]['title']
                return True
            else:
                return False
        else:
            return False
    

def main():
    os_type = platform.system()

    if os_type == 'Windows':
        from win10toast_click import ToastNotifier

    with open('channelList.txt', 'r') as f:
        channels = f.readlines()
    
    for i, ch in enumerate(channels):
        channels[i] = ch.strip('\n')
    
    check = TwitchLiveCheck(channels, os=os_type)

    while True:
        check.run()


if __name__ == '__main__':
    main()
