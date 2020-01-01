#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    matching = {}
    for color in ar:
        if color in matching:
            matching[color] = matching[color] + 1
        else:
            matching[color] = 1
    pairs = 0
    for each in matching.values():
        pairs = pairs + each // 2
    return pairs
