import socket
def retBanner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
    f = open('vulns_banner.txt', 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is vulnerable: " + banner.strip('\n')

def main():
    portList = [21,22,25,80,110,443]
    for x in range(1, 255):
        ip = '42.0.0.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print "[+] " + ip + ": " + banner
                checkVulns(banner)

if __name__ == '__main__':
    main()

