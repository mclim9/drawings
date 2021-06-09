import base64

data = 'eyJjb2RlIjoiZ3JhcGggUkxcbiAgICBoZWxsb1xuICAgIHdvcmxkIiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9'
data = 'eyJjb2RlIjoiZ3JhcGggUkxcbiAgICBoZWxsb1dvcmxkIiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9'

# Standard Base64 Decoding
decodedBytes = base64.b64decode(data)
print(decodedBytes)
decodedStr = str(decodedBytes, "utf-8")

print(decodedStr)