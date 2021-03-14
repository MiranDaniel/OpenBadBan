#######################################################
# MADE BY MIRANDANIEL (u/mirandanielcz, @mirandaniel) #
# DONATIONS:                                          #
# ban_1aws637mb3qnuf9j8swzufq3nj3fttuzkixbd817nmmhyms6a6kt1zyptq87
#######################################################

import os
import sys
sys.path.append("mdbot")
import settings


class login:
    token = ""

class bot:
    prefixes = ['sudo ', '!']
    admins = []
    version = "0.0.1 (MDBv2)"

    class status:
        statuses = ["Banning bad people",""]
        change_interval = 0 # Should not be under 30, if set to 0 the statuses wont change

class sql:
    host =     r""
    database = r""
    user =     r""
    password = r""
    uri =      r""


class extensions:
    initial_extensions = ["cogs.admin",'cogs.master', "cogs.status","cogs.ban"]

class files:
    base_dir = os.path.dirname(os.path.realpath(__file__))