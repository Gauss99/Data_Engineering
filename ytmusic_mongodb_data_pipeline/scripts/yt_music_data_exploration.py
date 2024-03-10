from ytmusicapi import YTMusic


yt = YTMusic()


def get_artist_info(artist_name):
    info = yt.search(artist_name, filter='artists')
    return info


Alice_in_Chains = get_artist_info('Alice in Chains')
print(Alice_in_Chains)


