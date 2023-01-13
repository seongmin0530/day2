# chapter 4 if

limits = 20
tweets = "pass" * 6
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'글자 수 {abs(diff)} 초과')


