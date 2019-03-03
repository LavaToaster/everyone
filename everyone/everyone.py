from redbot.core import commands, checks


class Everyone(commands.Cog):

    @commands.command(hidden=True, aliases=["ss"])
    @checks.bot_in_a_guild()
    @checks.guildowner()
    @checks.admin()
    @checks.mod()
    async def silentsay(self, ctx, *, msg: str):
        """Say things as the bot and deletes the command if it can"""
        if ctx.channel.permissions_for(ctx.guild).manage_messages:
            await ctx.message.delete()
        await ctx.send(msg)
