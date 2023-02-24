#  Copyright (c) 2011-2014 Exxeleron GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import numpy
from numba.pycc import CC

cc = CC('utils')

cc.verbose = True

@cc.export('uncompress', 'i1[:](i1[:], i4)')
def uncompress(data, uncompressed_size):
    n, r, f, s, p, i, d = 0, 0, 0, 0, 0, 0, 0
    b = numpy.zeros(256, dtype = numpy.int32)
    uncompressed = numpy.zeros(uncompressed_size, dtype = numpy.byte)

    while s < len(uncompressed):
        if i == 0:
            f = 0xff & data[d]
            d = d + 1
            i = 1

        if (f & i) != 0:
            r = b[0xff & data[d]]
            d = d + 1
            uncompressed[s] = uncompressed[r]
            s = s + 1
            r = r + 1
            uncompressed[s] = uncompressed[r]
            s = s + 1
            r = r + 1
            n = 0xff & data[d]
            d = d + 1
            for m in range(n):
                uncompressed[s + m] = uncompressed[r + m]
        else:
            uncompressed[s] = data[d]
            s = s + 1
            d = d + 1

        while p < s - 1:
            b[(0xff & uncompressed[p]) ^ (0xff & uncompressed[p + 1])] = p
            p = p + 1

        if (f & i) != 0:
            s = s + n
            p = s

        i *= 2

        if i == 256:
            i = 0

    return uncompressed
