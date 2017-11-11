#!/usr/bin/env python2

# Copyright (C) 2017  Martijn Terpstra

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import common
import aes
import rc4
import pkcs7

# Default encryption is AES-256-CTR+SHA256-HMAC
encrypt = aes.encrypt_256_ctr
decrypt = aes.decrypt_256_ctr

# Default hash is SHA56
hash = sha.sha256

# Default rng is AES-128-CTR
rand = aes.rand

__all__ = ["aes",
           "pkcs7",
           "rc4",
           "sha", ]
