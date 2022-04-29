class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        es = set()

        for email in emails:
            parts = email.split('@')

            es.add(parts[0].split('+')[0].replace('.', '') + "@" + parts[1])

        return len(es)
