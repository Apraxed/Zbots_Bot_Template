from cogs import fun_commands, moderation_commands

async def modcmds():
  async def tempban():
    moderation_commands.temp_ban10d
  async def pban():
    moderation_commands.permban
  async def kick():
    moderation_commands.kick

async def funcmds():
    async def meme():
        fun_commands.meme
    async def pp_size():
        fun_commands.pp_size
    async def randomnumgen():
        fun_commands.rng