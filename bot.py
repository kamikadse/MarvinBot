import discord
import asyncio
import random
import re
import requests

me = 262265526242246657
prokr = 174971163124957184
alyx = 292752219730739201
reglais = 249401382589693952

withelist = [me, prokr, alyx, reglais]
prefix = '!Марвин'

pasteUsrKey = 'e49cb9d0b85cf5b8041a72d92df3703a'
pasteKey = 'Gv73aNbk'
TOKEN = 'NDgyNTY2NzkwOTMzOTA1NDA5.DmGxEA.vxTFbyXyJkvW3d5ubvpkPPrKARE'

request = requests.get("https://pastebin.com/raw/{}".format(pasteKey))
paste = request.text
quotes = paste.split('+')

print(len(quotes))
# print(request.text)
print('-----------')
print('Good morning, Kamikadse')
print('-----------')

client = discord.Client()

# dictionary = ['Все отвратительно', 'Работа тяжела', 'Пиздец', 'Вокруг полно фигни', 'Плавились кони во льду сверхпустот']
marvinSay = (
    'Жизнь! Не говорите мне о жизни...',
    'Мне кажется, вы должны знать, что я в глубокой депрессии.',
    'Мне это не доставит удовольствия.',
    'Забавно, что, как только вы начинаете думать, будто жизнь, пожалуй, не может стать хуже, она внезапно становится хуже.',
    'Вам кажется, что это вы озадачены, но что бы вы делали, если бы сами были роботом с маниакально-депрессивным психозом? Нет, не трудитесь отвечать. Я в пятьдесят тысяч раз разумнее вас, и даже я не знаю ответа. Сама попытка снизойти до уровня вашего мышления доставляет мне головную боль.',
    'Не притворяйтесь, будто хотите со мной поговорить. Я знаю, вы меня ненавидите. ',
    'Вы ненавидите меня, как и все. Так устроена Вселенная. Стоит мне с кем-нибудь поговорить, и он начинает меня ненавидеть. Даже роботы меня ненавидят...',
    'Мощность моего блока счастья можно уместить в спичечный коробок. Не вынимая спичек.',
    'Чтобы мое лицо исказила улыбка, нужно отнести его в мастерскую и часа два поработать над ним кувалдой.',
    'Я хотел бы сказать, что выступить на открытии этого моста для меня большая честь, радость и удача, но не могу - все мои цепи лжи вышли из строя. Я ненавижу и презираю вас всех...',
    'Эта девушка — одно из наименее недоразвитых неразумных живых существ, встречи с которыми я имел неудовольствие не избежать на своем жизненном пути.'
    )
gamesList = ['game 1', 'game 2', 'игра 0']

reqList = ('дай','налей','принеси')
tea = ('чая','чай','чаю')
cookie = ('печеньку','печенек','печенюшку','печенюшек','печенье')
pizza = ('пиццу', 'пиццы')
coffee = ('кофе','эспрессо','латте','американо','капучино','мокачино')
cat = ('кота','котэ','котейку','кошку','кошечку','котенка','котёнка')

reg = re.compile('[^a-zA-Zа-яА-Я ]')
games = reg.sub('',str(gamesList))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #if int(message.author.id) not in withelist: return
    try:
        if message.content == '!Марвин':
            msg = 'Чего вам еще нужно, {0.author.mention}?'.format(message)
            await client.send_message(message.channel, msg)
        if message.content.startswith(prefix) and 'как дела' in message.content:
            msg = random.choice(marvinSay).format(message)
            await client.send_message(message.channel, msg)
        if 'СЕМПА' in message.content:
            await client.send_message(message.channel, 'Notice me, {0.author.mention}'.format(message))
        if message.content.startswith('!цитата'):
            await client.send_message(message.channel, random.choice(quotes).format(message))
    except Exception:
        print("Message wasn't sent, author - {}".format(message.author))


    try:
        if message.content.startswith(prefix) and (set(reqList) & set(message.content.split(' '))):
            req = False
            if set(cookie) & set(message.content.split(' ')):
                await client.add_reaction(message, "\U0001F36A")
                req = True
            if set(message.content.split(' ')) & set(tea):
                await client.add_reaction(message, "\U0001F375")
                req = True
            if set(pizza) & set(message.content.split(' ')):
                await client.add_reaction(message, "\U0001F355")
                req = True
            if set(coffee) & set(message.content.split(' ')):
                await client.add_reaction(message, "\U00002615")
                req = True
            if set(cat) & set(message.content.split(' ')):
                await client.add_reaction(message, "\U0001F408")
                req = True
            if not req:
                await client.add_reaction(message, "\U00002753")
        
    # try:
    #    if message.content.startswith(prefix) and 'дай печеньку' in message.content:
    #        if random.random()< 0.65:
    #            await client.add_reaction(message, "\U0001F36A")
    #        else:
    #            await client.add_reaction(message, "\U0001F1ED")
    #            await client.add_reaction(message, "\U0001F1EA")
    #            await client.add_reaction(message, "\U0001F1F9")
    except Exception:
        print("Reaction wasn't added, author - {}".format(message.author))


        
    if int(message.author.id) in withelist and message.content == '!Марвин спать':
        await client.send_message(message.channel,'Иду спать'.format(message))
        print('EXIT')
        exit(0)
#    if message.content.startswith('!games'):     
#        if games is not None:
#            msg = str(games)
#            await client.send_message(message.channel, msg.capitalize().format(message)) 
#        else:
#            await client.send_message(message.channel, 'Games not found'.format(message))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
