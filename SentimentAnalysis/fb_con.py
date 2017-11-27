from facepy import GraphAPI

#client_id ="374xxxxxxxx6101"
#client_secret ="e4d37xxxxxxxxxxxxx88519185e11"
#fb_exchange_token ="EAAFUnazV3t0xfDUwnxxxxxxxxxxxxxxxxxxxxxoGcOb0QhVDMymrmed97Lq8x5KmYDofnb7SAogZD"
#grant_type =fb_exchange_token
#fb token never ending="EAAFUnazV3JUBAJbaZBG0xxxxxxxxxxxxxxxxxxxxxxJV119g1yRTV35eLfT1bZCuhk63qcFxEZD"

def get_con():
    access_token ="EAAFUxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxbrG0ZATBI5umpfROI15EmFy6JQZDZD"
    graph = GraphAPI(access_token)
    return graph
