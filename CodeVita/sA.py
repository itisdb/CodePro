def minSwaps(s: str) -> int:
        ans = n = len(s)
        gg, bb = 0, 0
        for c in s:
            if c == 'G':
                gg += 1
            else:
                bb += 1
        if abs(gg - bb) > 1: return -1
        if gg >= bb:
            s1 = 'GB' * (n // 2)
            s1 += 'G' if n % 2 else ''
            cnt = sum(c1 != c for c1, c in zip(s1, s))
            ans = cnt // 2
        if gg <= bb:
            s2 = 'BG' * (n // 2)
            s2 += 'B' if n % 2 else '' 
            cnt = sum(c2 != c for c2, c in zip(s2, s))
            ans = min(ans, cnt // 2)
        return ans

string = input()
print(minSwaps(string),end='')