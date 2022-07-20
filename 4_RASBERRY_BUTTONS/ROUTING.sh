iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE

echo "1" > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -s 192.168.42.1/8 -o wlan1 -j MASQUERADE


