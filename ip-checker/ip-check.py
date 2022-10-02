from requests import get
import socket as st

ip = st.gethostbyname(st.gethostname())
pub_ip = get("https://ipv4.icanhazip.com/").text
    
print('>>> private IP : ' + ip + ' <<<')
print('>>> public IP : ' + pub_ip[0:-1] + ' <<<')
