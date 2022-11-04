#####################################
# TASK 2
# Port the given bash script to Python Code
#####################################

import requests, json

### PART 1
# Get first name as input from user
StudentName = str(input("What is your name?\n"))


# Make call to agify api, convert to json data and store in .json file
agify_url = "https://api.agify.io?name=" + StudentName
r = requests.get(agify_url)
json_data = r.json()
with open("my_agify_info_python.json", "w") as write_file:
    json.dump(json_data, write_file)
    
    
### PART 2
# MAke call to hashicorp for terraform version info in json format
release = requests.get("https://releases.hashicorp.com/terraform/index.json")
release_data = release.json()


# Use the Python dictionary function .keys() and indexes to navigate json data 
# and obtain a list of only the release urls
keys = release_data['versions'].keys()
urls = []

for i in keys:
    string = str(i)
    for k in release_data['versions'][string]['builds']:
        urls.append(k['url'])
        

# Iterate over the list of urls to further refine the results to only releases
# for linux_amd64
linux_urls = []

for i in urls:
    if "linux_amd64" in i:
        linux_urls.append(i)

Latest_TF_URL = linux_urls[-1]


# Check to make sure the Latest_TF_URL varable has a value
# Make get request if value is not assigned
if Latest_TF_URL:
    Filename = Latest_TF_URL
    print("That's all folks!!")
else:
    Filename = requests.get(linux_urls[-1])
    
    
#######################################################
# TASK 3
# Grab information from a public REST API and integrate 
# the data as an enrichment to the ported python application.
#######################################################

# Get local ip info from ipwho.is and display country
my_ip = requests.get("http://ipwho.is")
raw_data = my_ip.json()
print(raw_data['country'])