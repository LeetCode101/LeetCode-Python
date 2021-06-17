class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n

        if s[0] == '*':
            dp[0] = 9
        else:
            dp[0] = 1 if s[0] != '0' else 0

        for i in range(1, n):
            one_digit = s[i:i + 1]
            two_digits = s[i - 1:i + 1]

            if one_digit == '*':
                dp[i] += dp[i - 1] * 9
            elif 1 <= int(one_digit) <= 9:
                dp[i] += dp[i - 1]

            if '*' in two_digits:
                if two_digits[1].isdigit():
                    if int(two_digits[1]) <= 6:
                        dp[i] += dp[i - 2] * 2 if i >= 2 else 2
                    else:
                        dp[i] += dp[i - 2] if i >= 2 else 1
                elif two_digits[0].isdigit():
                    if two_digits[0] == '1':
                        dp[i] += dp[i - 2] * 9 if i >= 2 else 9
                    elif two_digits[0] == '2':
                        dp[i] += dp[i - 2] * 6 if i >= 2 else 6
                else:
                    dp[i] += dp[i - 2] * 15 if i >= 2 else 15
            elif 10 <= int(two_digits) <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1

            dp[i] %= 1000000007

        return dp[-1]
