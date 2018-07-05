import base64


def b64_encode(content_str, altchars=b'-_'):
    return bytes.decode(base64.b64encode(str(content_str).encode('latin-1'), altchars)).replace("=", "")


def b64_decode(content_b64):
    # https://stackoverflow.com/a/9807138/5189486
    # base64编码中末尾的'='号被省略被认为是无损的，但是decode时如果不将'='添加回去，会导致Incorrect padding error
    missing_padding = len(content_b64) % 4
    if missing_padding != 0:
        content_b64 += '=' * (4 - missing_padding)
    return bytes.decode(base64.b64decode(content_b64), 'latin-1')


def uri_to_map(uri_str):
    uri_params = uri_str.split("&")
    return dict(param.split("=", maxsplit=1) for param in uri_params)


def encode_ssr(ssr):
    obfp_base64 = b64_encode(ssr['obfsparam'])
    ptcp_base64 = b64_encode(ssr['protoparam'])
    name_base64 = b64_encode(ssr['remarks'])
    group_base64=b64_encode(ssr["group"])

    password_base64 = b64_encode(ssr['password'])
    param_base64 = "obfsparam={}&protoparam={}&remarks={}&group={}".format(obfp_base64, ptcp_base64,
                                                                  name_base64,group_base64)
    pwd_param = "{}/?{}".format(password_base64, param_base64)

    return "ssr://" + b64_encode("{server}:{port}:{protocol}:{method}:{obfs}:{pwd_param}"
                                 .format(server=ssr["server"], port=ssr["port"],
                                         protocol=ssr["protocol"], method=ssr["method"],
                                         obfs=ssr["obfs"], pwd_param=pwd_param))


def decode_ssr(ssr_url_b64):
    ssr = {}

    ssr_url = b64_decode(ssr_url_b64.lstrip("ssr://").replace("_", "/").replace("-", "+"))
    ssr_arr = ssr_url.split(":")

    ssr['server'] = ssr_arr[0]
    ssr['port'] = int(ssr_arr[1])
    ssr['protocol'] = ssr_arr[2]
    ssr['method'] = ssr_arr[3]
    ssr['obfs'] = ssr_arr[4]

    pwd_b64, param_b64_str = ssr_arr[5].split("/?")
    ssr["password"] = b64_decode(pwd_b64)

    param_map_b64 = uri_to_map(param_b64_str)
    for k, v in param_map_b64.items():
        ssr[k] = b64_decode(v)

    return ssr

#     #


# re = encode_ssr({
#     "method": "rc4-md5-6",
#     "obfs": "http_simple",
#     "obfsparam": "sdf",
#     "password": "password",
#     "port": "1253",
#     "protocol": "auth_aes128_sha1",
#     "protoparam": "",
#     "server": "192.168.1.1",
#     "remarks": "default"
# })
# print(re)
# # re_ssr = decode_ssr(
# #     "ssr://MzEuanAuaGRzb2Nrcy5jbjozMDYwNzphdXRoX2NoYWluX2E6bm9uZTp0bHMxLjJfdGlja2V0X2F1dGg6T0V4cU9YRmlPSGRETVEvP29iZnNwYXJhbT0mcHJvdG9wYXJhbT0mcmVtYXJrcz1NekV1YW5BdWFHUnpiMk5yY3k1amJnJmdyb3VwPQ")
# # print(re_ssr)

# print(decode_ssr(re))