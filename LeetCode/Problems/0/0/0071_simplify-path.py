class Solution:
    def simplifyPath(self, path: str) -> str:
        cur = []

        for folder in path.split('/'):
            if folder:
                if folder == '..':
                    if cur:
                        cur.pop()
                elif folder != '.':
                    cur.append(folder)

        return "/" + "/".join(cur)
