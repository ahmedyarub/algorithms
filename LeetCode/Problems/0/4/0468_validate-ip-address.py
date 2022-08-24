class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip4 = queryIP.split('.')

        if len(ip4) == 4:
            return "IPv4" if all(part.isnumeric() and 0 <= int(part) < 256 and str(int(part)) == part for part in ip4) \
                else "Neither"

        ip6 = queryIP.split(':')

        if len(ip6) == 8:
            return "IPv6" \
                if all(0 < len(part) < 5 and all(c.isnumeric() or ord('a') <= ord(c.lower()) <= ord('f') for c in part)
                       for part in ip6) else "Neither"

        return "Neither"
