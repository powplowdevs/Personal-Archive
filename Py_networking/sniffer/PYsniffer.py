from kamene.all import *
p = IP(dst = 'www.somesite.ex') / TCP(dport = 80) / Raw(b'Some raw bytes')
sr1(p)