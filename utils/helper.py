import discord


def embed_message(string, author=""):
    return discord.Embed(
        description=string, colour=discord.Colour.from_rgb(145, 48, 191)
    ).set_author(name=author)