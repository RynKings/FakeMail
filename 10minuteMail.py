import urllib.request
import re
import time
import json

print("\n\nSELAMAT DATANG DI MINUTEMAIL\n\n==========================[ Edited by ALFINO~NH ]==========================")
def awaitContinueRequest(action = "continue"):
    input("\nTekan enter untuk melanjutkan " + action + "...\n")

class TenMinuteMailGenerator(object):

    def __init__(self):
        self.SIDCookie = ""

    def get10MinuteMail(self, simulate = False):
        if simulate != True:

            req = urllib.request.Request(
                "https://10minutemail.com/10MinuteMail/index.html", 
                data=None, 
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
                }
            )
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                m = re.search('data-clipboard-text="([a-zA-Z0-9@.]*)" id="copyAddress"', html)
                headers = response.getheaders()
                self.SIDCookie = next(y for x, y in headers if x == "Set-Cookie" and y.startswith("JSESSIONID"))
                return m.group(1)
        else:
            self.SIDCookie = "JSESSIONID=LIKd7IlHq0lhpTOsWJdPY-RPCTpk5vr3qXuvque4.syndi; path=/10MinuteMail; secure; HttpOnly";
            return "r446338@mvrht.net"

    def anyNewMessage(self, currentMessageCount):
        totalPointCount = 3
        pointCount = 1
        while (True):
            req = urllib.request.Request(
                "https://10minutemail.com/10MinuteMail/resources/messages/messageCount", 
                data=None, 
                headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
            )
            req.add_header("Accept", "*/*")
            req.add_header("Connection", "keep-alive")
            req.add_header("cookie", self.SIDCookie)
            with urllib.request.urlopen(req) as response:
                messageCount = response.read().decode('utf-8')
            if int(messageCount) > currentMessageCount:
                print("Ada pesan masuk kang! " + messageCount)
                break;
            else:
                print("Menunggu pesan berikutnya... " + messageCount + " messages" + ('.' * pointCount) + (" " * (totalPointCount - pointCount))+ "\r", end="", flush=True)
            time.sleep(5)
            if pointCount >= totalPointCount:
                pointCount = 1
            else:
                pointCount += 1
        return int(messageCount)

    def getMessage(self, messageID):
        print("getting mail " + str(messageID))
        req = urllib.request.Request(
            "https://10minutemail.com/10MinuteMail/resources/messages/messagesAfter/" + str(messageID), 
            data=None, 
            headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
           )
        req.add_header("Accept", "*/*")
        req.add_header("Connection", "keep-alive")
        req.add_header("cookie", self.SIDCookie)
        with urllib.request.urlopen(req) as response:
            message = response.read().decode('utf-8')
        return json.loads(message);

    def showMessage(self, json):
        return "Pengirim: " + json[0]['primaryFromAddress'] + "\nPerihal: " + json[0]['subject'] #+ "\nMessage: " + json[0]['bodyText'] + "\n"


if __name__ == '__main__':
    awaitContinueRequest("Generate alamat email...")
    Tenmmg = TenMinuteMailGenerator()
    print ("Sedang generate email mu...\n")
    print(Tenmmg.get10MinuteMail())
    i = -1
    while True:
        option = input("Menunggu pesan berikutnya? \n\n+ Tekan [Y]es (Menampilakan pesan dan file json)\n+ Tekan [N]o (Keluar)\n+ Tekan [B]ody (Melihat isi pesan)\n")
        i += 1
        if option.lower().startswith("y"):
           print (Tenmmg.getMessage(Tenmmg.anyNewMessage(i) - 1)) 
        elif option.lower().startswith("b"):
           print (Tenmmg.showMessage(Tenmmg.getMessage(Tenmmg.anyNewMessage(i) - 1)))
        else:
            break;
    
