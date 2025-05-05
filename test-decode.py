import json
import zlib

from pyamf import remoting
from io import BytesIO

#with open("other/ChefVilleBotSetup/{app}/tmp_dir/conf.amf", "rb") as f:
#with open(".../Chefville/gameSettings__2513b.amf", "rb") as f:
with open(".../content__a19bb.amf", "rb") as f:
#with open(".../content__b6ad3.amf", "rb") as f:
#with open("other/ChefVilleBotSetup/{app}/tmp_dir/gameSettings2.txt", "rb") as f:

    data = f.read()

#data = zlib.decompress(data)

#data = zlib.compress(data)


# request = remoting.decode(data)
# #print(repr(request))
# reqs = request.bodies[0][1].body
# print(repr(reqs))
# for message in reqs:
#     print(repr(message))
# #     print(message.target, message.body)

# with open("expgamesettings.json", "w") as f:
#     f.write(json.dumps(reqs, indent=2))

# with open("content__a19bb_compressed.amf", "wb") as f:
#     f.write(data)
