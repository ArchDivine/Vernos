import requests,json,os,time
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(Fore.RED + """

 /$$    /$$                                                 
| $$   | $$                                                 
| $$   | $$ /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$$
|  $$ / $$//$$__  $$ /$$__  $$| $$__  $$ /$$__  $$ /$$_____/
 \  $$ $$/| $$$$$$$$| $$  \__/| $$  \ $$| $$  \ $$|  $$$$$$ 
  \  $$$/ | $$_____/| $$      | $$  | $$| $$  | $$ \____  $$
   \  $/  |  $$$$$$$| $$      | $$  | $$|  $$$$$$/ /$$$$$$$/
    \_/    \_______/|__/      |__/  |__/ \______/ |_______/                                                     

    """ + Fore.RED)

clear()

self_avatar = ""
base_url = "https://discord.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN"
url = ""

while True:
    option2 = input("""Login:
[1] URL
[2] ID + Token 
""")
    if option2=="1":
        url = input(Fore.RED+"Webhook URL ~> "+Fore.RED)
        break
    elif option2=="2":
        webhook_id = input(Fore.RED+"Webhook ID ~> "+Fore.RED)
        webhook_token = input(Fore.RED + "Webhook Token ~> " + Fore.RED)
        url = base_url.replace("WEBHOOK_ID",webhook_id).replace("WEBHOOK_TOKEN",webhook_token)
        break
    else:
        print(Fore.RED+"Invalid option: "+option2+Fore.RED)

# check webhook
rq = requests.get(url)
if rq.status_code == 200:
    clear()
    print(Fore.RED+"HTTP 200 Token and ID valid. Session Started"+Fore.RED)
    print()
else:
    print(Fore.RED+f"HTTP {rq.status_code}. Token or/and ID might not be valid. Program will now exit.."+Fore.RED)
    exit(0)



while True:
    option=input(f"""Options:
[1] Chat Session
[2] Edit webhook
{Fore.RED}[3] Delete Webhook {Fore.RED}
[4] Spam mode
""")
    if option == "1":
        clear()
        print(Fore.RED+"Session Started! (\'exit\' to exit)")
        while True:
            inp = input(Fore.RED+'~> '+Fore.RED)
            if inp == "exit":
                clear()
                break
            data = {"content": inp}
            if self_avatar!="":
                data['avatar_url']=self_avatar

            x=requests.post(url, data=json.dumps(data), headers={ "Content-Type": "application/json"})
            if x.status_code == 204:
                print(Fore.RED+"HTTP 204: Succes!"+Fore.RED)
            else:
                print(Fore.RED+f"HTTP {x.status_code}: Action might've failed"+Fore.RED)
    elif option == "2":
        print(Fore.RED + "Enter blank for default"+Fore.RED)
        name = input(Fore.RED+"Custom Name ~> "+Fore.RED)
        avatar = input(Fore.RED+"Custom Avatar Url ~> "+Fore.RED)
        data = {"name":name,"avatar":avatar}
        self_avatar=avatar
        x = requests.patch(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        if x.status_code == 200:
            clear()
            print(Fore.RED+"HTTP 200: Succes!"+Fore.RED)
        else:
            print(Fore.RED+f"HTTP {x.status_code}: Action might've failed"+Fore.RED)
    elif option == "3":
        clear()
        yn = input(Fore.RED+"Are you sure? (y/n) ~> "+Fore.RED)
        if yn == "y":
            inp = input(Fore.RED+"Any last words (Leave blank for none) ~> "+Fore.RED)
            if inp != "":
                data = {"content": inp}
                x = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
                if x.status_code == 204:
                    print(Fore.RED + "HTTP 204: Succes!" + Fore.RED)
                else:
                    print(Fore.RED + f"HTTP {x.status_code}: Action might've failed" + Fore.RED)
            print()
            rq = requests.delete(url)
            if rq.status_code == 204:
                print(Fore.RED+"HTTP 204 from Discord: Webhook deleted succesfully. The Program will now exit.."+Fore.RED)
            else:
                print(Fore.RED+f"HTTP {rq.status_code}: Action might've failed. The Program will now exit.."+Fore.RED)
            exit(0)
        else:
            clear()
    if option == "4":
        clear()
    inp = input("\nEnter the message you want to spam. (leave empty for default)\n> ")
    amount = int(input("\nEnter the amount you want to spam the message. (30+ = RATE LIMITED)\n> "))
    data = {"content": inp}
    if self_avatar != "":
        data['avatar_url'] = self_avatar

    count = 1
    while count <= amount:
        x = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        time.sleep(0.1)
        if x.status_code == 204:
            print(Fore.RED + "HTTP 204: Success!" + Fore.RED)
        else:
            print(Fore.RED + f"HTTP {x.status_code}: Action might've failed" + Fore.RED)

        count += 1

    input("\nFinished spamming. Press any key to return to the menu.")
