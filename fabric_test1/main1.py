# -*- coding: utf-8 -*-
import os
def main1(comm):
    print(comm)
    print(("fab -H localhost host_type:comm='%s' -f piliang.py")%comm)
    mystr = os.popen(("fab -H localhost host_type:comm='%s' -f piliang.py")%comm).read().encode()
    return mystr