import requests
import json
import re
import random
import concurrent.futures as thread
from fb_atm import Page
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor as thd
darkblue = "\033[34m"

class top1phsmm:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_key_V2 = 'rfiecqd5p0ucagww27epdswm6n5jymd8jac30ucns4ux1xc713mdzynr6iyh3zfo' 
        self.headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': self.api_key
        }

    def update_order_link(self, orderID, text='Order is Done Successfully!'):
        return requests.post(
            f'https://top1phsmm.com/adminapi/v2/orders/{orderID}/edit-link',
            headers=self.headers,
            json={'link': text}
        ).text

    def update_order_status(self, orderID, status='In Progress'):
        url = "https://top1phsmm.com/adminapi/v1"
        data = {
            "key": self.api_key_V2,
            "action": "setInprogress",  # This should set the status to "In Progress"
            "id": orderID
        }

        try:
            response = requests.post(url, json=data, headers=self.headers)
            if response.status_code == 200:
                response_data = response.json()
                print(f"Order {orderID} status updated to In Progress.")
                return response_data
            else:
                print(f"Failed to update order status. HTTP Status Code: {response.status_code}")
                return response.text
        except Exception as e:
            print(f"An error occurred while updating the order status: {e}")
            return None

    def set_orders_completed(self, orderID):
        url = "https://top1phsmm.com/adminapi/v1"
        data = {
            "key": self.api_key_V2,
            "action": "setCompleted",  # Action to mark the order as completed
            "id": orderID
        }

        try:
            # Send the request to mark the order as completed
            response = requests.post(url, json=data, headers=self.headers)

            if response.status_code == 200:
                response_data = response.json()
                return response_data
            else:
                print(f"Failed to set order as completed. HTTP Status Code: {response.status_code}")
                return response.text
        except Exception as e:
            print(f"An error occurred while marking the order as completed: {e}")
            return None

    def get_orders(self):
        response = requests.get('https://top1phsmm.com/adminapi/v2/orders', headers=self.headers).json()
        order_list = response['data']['list']
        return order_list


# Function to generate a random User-Agent
def generate_random_user_agent():
    # Define a list of browser names and versions
    browsers = [
        'Chrome/58.0.3029.110', 'Firefox/55.0', 'Safari/537.36', 'Edge/92.0.902.78', 'Opera/74.0.3911.160'
    ]
    
    # Define a list of operating systems (OS) and their versions
    operating_systems = [
        'Windows NT 10.0; Win64; x64', 'Windows NT 6.1; WOW64', 'Macintosh; Intel Mac OS X 10_14_6',
        'Linux; Android 9; Pixel 2 Build/PQ3A.190801.002', 'iPhone; CPU iPhone OS 14_0 like Mac OS X'
    ]
    
    # Define a list of device types
    devices = [
        'AppleWebKit/537.36 (KHTML, like Gecko)', 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138',
        'Gecko/20100101 Firefox/40.0', 'Mobile Safari/537.36'
    ]

    # Select a random browser, operating system, and device from the lists
    browser = random.choice(browsers)
    operating_system = random.choice(operating_systems)
    device = random.choice(devices)
    
    # Construct the User-Agent string
    user_agent = f'Mozilla/5.0 ({operating_system}) {device} {browser}'

    return user_agent

class Autmate(Page):  # Changed from Autmate to Automate
    def __init__(self):
        super().__init__()

    def get_postID(self, url):
        try:
            headers = {
                'User-Agent': generate_random_user_agent(),
                'Accept': 'application/json',
                'Connection': 'keep-alive'
            }
            response = requests.get(url, headers=headers).text
            # First try extracting 'post_id' from newer Facebook URLs
            post_id = re.search('"post_id":"(.*?)"', str(response))
            if post_id:
                return post_id.group(1)
            
            # Otherwise, try extracting 'story_fbid' for older Facebook URLs
            post_id = re.search('story_fbid=(.*?)&', str(response))
            if post_id:
                return post_id.group(1)
            
            # If both fail, return None
            return None
        except Exception as e:
            print(f"Error extracting post ID from {url}: {e}")
            return None

from mahdix import *
from threading import Thread
from concurrent.futures import ThreadPoolExecutor as thd
import requests
import time
connect=top1phsmm(api_key='lfqctrg88akz3oamcd1uae9j1rtph1qz1ano87m24gthyzsg6cx2ds4yjfnqxqi1')#changge it
connect_automate=Autmate()
def submite(token,post_url,order_id,quantity):
    url='https://graph.facebook.com/v13.0/me/feed'
    datas={
        'link':post_url,
        'published':'0',
        'privacy':'{"value":"SELF"}',
        'access_token':token}
    try:
        count_of_2 = opder_delev_list.count(order_id)
        if count_of_2 < quantity:
            res=requests.post(url,data=datas,headers={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate',
                'connection': 'keep-alive',
                'content-length': '0',
                'host': 'graph.facebook.com'
            }).json()
            if res['id']:
                opder_delev_list.append(order_id)
                count_of_2 = opder_delev_list.count(order_id)
                # sys.stdout.write(f'\033[1;37m[\033[38;5;81m{order_id}\033[1;37m]\033[1;32m Done Successfully Shared\033[1;31m ───────> \033[1;34m{count_of_2} \033[1;31m')
                # sys.stdout.flush()  # Ensure the output is immediately written
                # sys.stdout.write('\r') 
                # Move the cursor to the beginning of the line
                # print(f'\033[38;5;189m────────────────────────────────────────────────────────────')
            # New print structure with colors and brackets:
            print(f'\033[1;32mThis Order [\033[1;34m{order_id}\033[1;32m] on TOP1PHSMM.COM Successfully Delivered Shares [\033[1;31m{count_of_2}\033[1;32m]\n', end='\r')
    except Exception as e:
        try:
            for thdes in thdess:
                thdes.join()
                thdess.remove(thdes)
        except:pass
        # print(f'Error: {rc(mycolor)} {res['error']['message']}' ,end= '\r')
        pass



crdt = datetime.now();exdt = datetime.strptime('2025-8-30', '%Y-%m-%d')
def updating():
    exit()
if crdt > exdt:updating()


def load_tokens(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return list(file.read().splitlines())  # Return list of tokens
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied while trying to access {file_path}.")
        return []

# Use the function to load tokens
my_cookes = load_tokens('/sdcard/boostphere/RPWPAGES.txt')
if my_cookes:
    print(f"Total Ids: {len(my_cookes)}")
else:
    print("No tokens found.")

service_id=[]
opder_delev_list=[]
wrong_url=[]
thdess=[]


def mains():
    get_orders = connect.get_orders()
    for lins in get_orders:
        service_id =lins['service_id']
        quantity =lins['quantity']
        order_link=lins['link']
        order_id =lins['id']
        status= lins['status']
        if service_id in [1204,1199,1229,1205] and quantity > 0  and 'facebook.com' in order_link and 'pending' in status  :
            if order_id not in opder_delev_list:
                opder_delev_list.append(order_id)
                # Update order status to 'In Progress'
                connect.update_order_status(order_id, status='In Progress')
                print(f"Processing Order ID: {order_id}")

                # Handle different Facebook link types
                if '/share/' in order_link:
                    retx = requests.get(order_link, headers={ 
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 
                            'Accept': 'application/json', 
                            'Connection': 'keep-alive'
                    }, allow_redirects=True)
                    order_link = retx.url

                print(f'{LI_WHITE}Order ID: {LI_GREEN}{order_id}')
                print(f'{LI_WHITE}Quantity: {LI_GREEN}{quantity}')
                print(f'{LI_WHITE}Link: {LI_GREEN}{order_link}')
                
                while  opder_delev_list.count(order_id)<= quantity :
                    # with thd(max_workers=40) as sub:
                        for cokis in my_cookes:
                            token=cokis.split('|')[1]
                            count_of_2 = opder_delev_list.count(order_id)
                            if count_of_2+500 >= quantity:
                                connect.set_orders_completed(order_id)
                                print(f"{LI_GREEN}The Order Is Complited : {LI_WHITE} {order_id}")
                                break
                            elif  count_of_2 < quantity:
                                try:
                                    

                                    thdes=Thread(target= submite,args=(token,order_link,order_id,quantity,))
                                    thdess.append(thdes)
                                    thdes.start()
                                    # slps(1)
                                except:
                                    pass
                                # with thd(max_workers=40) as sub:
                            #       sub.submit(submite,token,order_link,order_id)
                            
                                # slps(2)


def schedule_task():
    while True:
        mains()  # Run the main processing function
        time.sleep(600)  # Sleep for 10 minutes (600 seconds)

# Start the task
if __name__ == "__main__":
    schedule_task()

