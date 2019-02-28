class Solution:
    def numUniqueEmails(emails) -> int:
        period_char = '.'
        plus_char = '+'
        email_char = '@'
        correct_email = []

        for email in emails:
            print(email)
            start = email.find(plus_char)
            end = email.find(email_char)

            if email.count(period_char) >= 2:
               email =  email.replace('.', '', (email.count(period_char)-1) )

            elif "+" in email:
                print(start)
                email = email[:start] + email[end:]

                correct_email.append(email)
                print(correct_email)

                print(emails)
        return len(emails)

    numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])












