import random
from discord.ext import commands
from enigma import enigma_code
from geocoder import get_distance, get_coordinates
from db_handler import create_msg, db_create
from class_db import DataMsg
import db_session

TOKEN = "ODMzNzA5NjA1MDUyNzQzNzcx.YH2Skw.u5xL_TdC08XurBrSS9TppsdKdfY"
dashes = [':point_right:', ':point_left:', ':point_up_2:', ':point_down: ', ':ok_hand:', ':middle_finger:']
YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3',
               'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
emoji = ['⬆️', '⬇️']
bot = commands.Bot(command_prefix='-')


@bot.command(name='roll')
async def roll_dice(ctx):
    res = [random.choice(dashes) for _ in range(int(3))]
    answer = 'You lose, sucker!'
    count_dick = 0
    count_pussy = 0
    for i in res:
        if i == ':middle_finger:':
            count_dick += 1
        elif i == ':ok_hand:':
            count_pussy += 1
    if count_dick >= 2 or count_pussy >= 2:
        answer = 'You won!'
    await ctx.send(" ".join(res))
    await ctx.send(answer)


@bot.command(name='rorg')
async def my_randint(ctx, min_int, max_int):
    num = random.randint(int(min_int), int(max_int))
    await ctx.send(num)


@bot.command(name='n')
async def nahui(ctx, name):
    await ctx.send(f"{ctx.message.author.mention} послал нах*й {name}.")


@bot.command(name='enma')
async def enigma(ctx, rotor, text):
    await ctx.send(f'{enigma_code(rotor, text)}')


@bot.command(name='dis')
async def distance(ctx, name1, name2):
    await ctx.send(f'{round(get_distance(get_coordinates(name1), get_coordinates(name2)))} км')


@bot.command(name='task')
async def distance(ctx, name, end):
    i = 0
    id_s = ctx.guild.id
    msg = await ctx.send(f'{name} - {i}/{end}')
    create_msg(id_s, msg.id, name, i, end)
    for i in range(2):
        await msg.add_reaction(emoji[i])


@bot.event
async def on_raw_reaction_add(payload):
    db_sess = db_session.create_session()
    id_s = payload.guild_id
    user = payload.member
    msgs = 0
    if payload.user_id != bot.user.id:
        for msg in db_sess.query(DataMsg).filter(
                (DataMsg.srv_id == id_s) | (DataMsg.msg_id == int(payload.message_id))):
            msgs = msg
        if msgs != 0:
            channel = bot.get_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            if payload.emoji.name == '⬆️':
                if msgs.i < msgs.end:
                    msgs.i += 1
            else:
                if msgs.i > 0:
                    msgs.i -= 1
            db_sess.commit()
            await msg.edit(content=f'{msgs.name} - {msgs.i}/{msgs.end}')
            for reaction in msg.reactions:
                await reaction.remove(user)
            for i in range(2):
                await msg.add_reaction(emoji[i])


def main():
    bot.run(TOKEN)


if __name__ == '__main__':
    db_create()
    main()
