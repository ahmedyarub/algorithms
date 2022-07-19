class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        for l1 in range(ord('a'), ord('z') + 1):
            for l2 in range(ord('a'), ord('z') + 1):
                sep = chr(l1) + chr(l2)
                if all([sep not in str for str in strs]):
                    break

        return sep + sep.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s[2:].split(s[0:2])
