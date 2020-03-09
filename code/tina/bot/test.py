class Slapper(commands.Converter):
    async def convert(self, ctx,argument):
        to_slap = random.choice(ctx.guild.members)
        return (f'{3} slapped {1} because *{2}*',(ctx, to_slap, argument))

@bot.command()
async def slap1(ctx, * , reason:Slapper()):
    await ctx.send(reason)





