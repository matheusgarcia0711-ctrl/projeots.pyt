ips = {'192.168.0.1', '192.168.0.2', '192.168.0.3'}

ips.add('192.168.0.4')
ips.add('192.168.0.3')  # repetido, não será duplicado

for ip in ips:
    print(ip)

