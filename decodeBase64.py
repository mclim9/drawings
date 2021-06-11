import base64

data = 'eyJjb2RlIjoiZ3JhcGggUkxcbiAgICBoZWxsb1xuICAgIHdvcmxkIiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9'
# data = 'eyJjb2RlIjoiZ3JhcGggUkxcbiAgICBoZWxsb1dvcmxkIiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9'
data = 'eNpdTcsKwjAQvPsV8wENJLGn3ApBTz3pxeNiYg3aFNL9f8yjUnRYWHYeOxNF5gMyOPDbY8C5MLCBpkRzVRyxPy1pJgZuGWIchbVVWv2dwxJxabtyA5jWF3YYUh20VL2QKk-Ho3TNGRd--rT7DT0436SAknA_HZu7cteSCLFoW8f3v9Ilq3TL0n8DDHTvPoXCQLE='

# Standard Base64 Decoding
print(len(data))
decodedBytes = base64.b64decode(data)
print(decodedBytes)
decodedStr = str(decodedBytes, "utf-8")

print(decodedStr)
