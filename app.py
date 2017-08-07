import requests

def calc(a, b):
    return sum(a, b)
    
def sum(a, b):
    return a + b
    
def main():
    print "ulaala"
    
def connect_github():
    response = requests.get("https://github.com")
    print response.status_code
    
if __name__ == '__main__':
    connect_github()