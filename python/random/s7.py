

import base64 as b64


s1 = "/fwaf/fawg1w/21/"
bs1 = s1.encode()

res = b64.b64encode(bs1).decode()

print(res)
