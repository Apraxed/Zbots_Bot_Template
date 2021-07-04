from cogs import fun_commands, moderation_commands, modmail, needs_owner_perms, game_commands


async def modcmds():
    async def tempban10d():
        moderation_commands.temp_ban10d
    async def pban():
        moderation_commands.permban
    async def kick():
        moderation_commands.kick
    async def userreports():
        modmail.modmail
    async def purge():
        moderation_commands.purge

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
                    needs_owner_perms.deleteemojis
                async def channels():
                    needs_owner_perms.deletechannels

async def developers():
    async def Head_Dev():
        needs_owner_perms.devs.Head
    async def Carnoval():
        needs_owner_perms.devs.Dev1
    async def dum_dev():
        needs_owner_perms.devs.Dev2

async def games():
    async def rps():
        game_commands.rps
    async def casino():
        game_commands.casino