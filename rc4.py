#!/usr/bin/env python2

#  ____   ____ _  _     _                   _
# |  _ \ / ___| || |   (_)___   _ __   ___ | |_   ___  ___  ___ _   _ _ __ ___
# | |_) | |   | || |_  | / __| | '_ \ / _ \| __| / __|/ _ \/ __| | | | '__/ _ \
# |  _ <| |___|__   _| | \__ \ | | | | (_) | |_  \__ \  __/ (__| |_| | | |  __/_
# |_| \_\\____|  |_|   |_|___/ |_| |_|\___/ \__| |___/\___|\___|\__,_|_|  \___( )
#                                                                             |/
#                         _  __
#   _____   _____ _ __   (_)/ _|
#  / _ \ \ / / _ \ '_ \  | | |_
# |  __/\ V /  __/ | | | | |  _|
#  \___| \_/ \___|_| |_| |_|_|

#  _                 _                           _           _
# (_)_ __ ___  _ __ | | ___ _ __ ___   ___ _ __ | |_ ___  __| |
# | | '_ ` _ \| '_ \| |/ _ \ '_ ` _ \ / _ \ '_ \| __/ _ \/ _` |
# | | | | | | | |_) | |  __/ | | | | |  __/ | | | ||  __/ (_| |
# |_|_| |_| |_| .__/|_|\___|_| |_| |_|\___|_| |_|\__\___|\__,_|
#             |_|
#                               _   _
#   ___ ___  _ __ _ __ ___  ___| |_| |_   _
#  / __/ _ \| '__| '__/ _ \/ __| __| | | | |
# | (_| (_) | |  | | |  __/ (__| |_| | |_| |
#  \___\___/|_|  |_|  \___|\___|\__|_|\__, |
#                                     |___/

class rc4():
    "A very simple but insecure random number generator"
    def __init__(self, key=""):
        self.S = list(range(256))
        if len(key) > 0:
            j = 0
            for i in range(256):
                key = map(ord, key)
                j = (j + self.S[i] + key[i % len(key)]) % 256
                self.S[i], self.S[j] = self.S[j], self.S[i]
        self.i = 0
        self.j = 0

    def rand(self):  # random integer mod 256
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.S[self.i]) % 256
        self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
        return self.S[(self.S[self.i] + self.S[self.j]) % 256]
