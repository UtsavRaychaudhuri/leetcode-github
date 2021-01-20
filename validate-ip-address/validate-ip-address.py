class Solution:
    def validIPAddress(self, IP: str) -> str:
        def checkIPv4(IP):
            parts=IP.split('.')
            if len(parts)!=4:
                return 'Neither'
            else:
                for part in parts:
                    if len(part)>3 or len(part)<1:
                        return "Neither"
                    if len(part)>1 and part[0]=='0':
                        return "Neither"
                    for i in part:
                        if i not in ('1','2','3','4','5','6','7','8','9','0'):
                            return "Neither"
                    if int(part)>255:
                        return "Neither"
            return "IPv4"
        
        def checkIPv6(IP):
            parts=IP.split(':')
            if len(parts)>8:
                return "Neither"
            else:
                for part in parts:
                    if len(part)>4 or len(part)<1:
                        return "Neither"
                    for i in part:
                        if i not in ('1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','A','B','C','D','E','F'):
                            return "Neither"
            return 'IPv6'
        if '.' in IP:
            return checkIPv4(IP)
        elif ':' in IP:
            return checkIPv6(IP)
        return "Neither"
