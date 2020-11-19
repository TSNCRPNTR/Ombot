####    GENERIC MESSAGE RESPONSES    ####

# yeah baby, switch functions
# (It's just dictionary mapping, but kinda worse ^-^ )
#   -> *INPUT*: *OUTPUT* <-
# Used for basic one-in one-out type interactions
def messageGet(argument):
    switcher = {
        '/hey ombot': 'hi!!',
        '/boop': 'beep',
        '/beep': 'boop',
        '/hi': "hewwo",
    }

    # Returns what matches up with the input
    return switcher.get(argument)
