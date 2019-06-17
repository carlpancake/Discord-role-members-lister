import discord
import asyncio

token = 'Ur token here' #with quotes
serverid = 547840113086824527 #no quote
rolename = "My epic role" #role are case-sensitive
botuser = True #set to True if you're using a bot account or to false if you are using a user account

client = discord.Client()
server = client.get_guild(serverid)

@client.event
async def on_ready():
    x = 0
    print('Ready.')
    print('------------')
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rolename):
            role2 = role
            roleid2 = role.id
            x = 1
            print("Found role!")
            print("listing users...")
            with open(str(role.id) + " " + str(role) + ".txt", "w", encoding='utf-8') as text_file:
                for member in role.members:
                    print(member)
                    try:
                        print(member, file=text_file)
                    except Exception as e:
                        print(e)
                        pass
    if x == 0:
        print("The role wasn't found")
        print("Check the name (it's case sensitive)")
    elif x == 1:
        print('------------')
        print("done!")
        print('the list of member of this role is in: "' + str(roleid2) + " " + str(role2) + '.txt"')
    else:
        print("how did you get here?")
                
client.run(token, bot=botuser)