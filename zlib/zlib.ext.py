from cogs import fun_commands, moderation_commands, modmail, owner_only_commands


async def modcmds():
  async def tempban10d():
    moderation_commands.temp_ban10d
  async def pban():
    moderation_commands.permban
  async def kick():
    moderation_commands.kick
  async def userreports():
    modmail.modmail

async def funcmds():
    async def meme():
        fun_commands.meme
    async def pp_size():
        fun_commands.pp_size
    async def randomnumgen():
        fun_commands.rng

async def ifmisusseditviolatestos():
    async def areyousure():
        async def youreallyaredoingthis():
            async def idkwhytho():
                async def emojis():
                    owner_only_commands.deleteemojis
                async def channels():
                    owner_only_commands.deletechannels

async def developers():
    Head_dev = owner_only_commands.devs.Head
    Carnoval = owner_only_commands.devs.Dev1
    dum_dev = owner_only_commands.devs.Dev2