import discord
import random

# Replace with your bot's token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Replace this with your Discord user ID to restrict the ?end command
BOT_OWNER_ID = 'YOUR_DISCORD_USER_ID'  # e.g., 123456789012345678

# Intents allow the bot to read messages
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Quotes categories
general_quotes = [
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes later becomes never. Do it now.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t wait for opportunity. Create it.",
    "The key to success is to focus on goals, not obstacles.",
]

sport_quotes = [
    "Champions keep playing until they get it right. - Billie Jean King",
    "The only way to prove that you’re a good sport is to lose. - Ernie Banks",
    "The harder the battle, the sweeter the victory. - Les Brown",
    "Winning isn’t everything, but wanting to win is. - Vince Lombardi",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "Hard work beats talent when talent doesn’t work hard. - Tim Notke",
    "If it doesn’t challenge you, it doesn’t change you. - Fred DeVito",
    "You’re never a loser until you quit trying. - Mike Ditka",
    "Winning takes care of everything. - Tiger Woods",
    "You can’t put a limit on anything. The more you dream, the farther you get. - Michael Phelps",
    "It’s not whether you get knocked down; it’s whether you get up. - Vince Lombardi",
    "I’ve failed over and over and over again in my life, and that is why I succeed. - Michael Jordan",
    "Don’t count the days; make the days count. - Muhammad Ali",
    "Excellence is not a skill. It is an attitude. - Ralph Marston",
    "Pain is temporary. Quitting lasts forever. - Lance Armstrong",
]

actual_quotes = [
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Act as if what you do makes a difference. It does. - William James",
    "Never bend your head. Always hold it high. Look the world straight in the eye. - Helen Keller",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Believe you can and you’re halfway there. - Theodore Roosevelt",
    "When you have a dream, you’ve got to grab it and never let go. - Carol Burnett",
    "I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean",
    "No matter what you’re going through, there’s a light at the end of the tunnel. - Demi Lovato",
    "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Try to be a rainbow in someone else’s cloud. - Maya Angelou",
    "You do not find the happy life. You make it. - Camilla Eyring Kimball",
    "Limit your 'always' and your 'nevers.' - Amy Poehler",
    "Nothing is impossible. The word itself says ‘I’m possible!’ - Audrey Hepburn",
]

competitive_quotes = [
    "If you’re not first, you’re last. Keep running. - Unknown",
    "Victory is not an option; it’s the only acceptable outcome. - Unknown",
    "Crush the competition, or they’ll crush you. - Unknown",
    "Be the storm they never saw coming. - Unknown",
    "The crown isn’t given; it’s taken. - Unknown",
    "Every battle is a chance to prove you’re the best. - Unknown",
    "Second place is just the first loser. - Unknown",
    "Dominate, or prepare to be dominated. - Unknown",
    "Winners focus on winning; losers focus on winners. - Unknown",
    "They don’t hand out medals for participation. - Unknown",
    "The only way is forward. Leave no space for failure. - Unknown",
    "No excuses, no limits, no mercy. - Unknown",
    "Winning is a habit. Losing is a choice. - Unknown",
    "You’re either making history or becoming it. - Unknown",
    "If you want to be the best, you have to beat the best. - Unknown",
]

# Helper function to pick a random quote
def get_random_quote(category):
    return random.choice(category)

@client.event
async def on_ready():
    print(f'Bot is online as {client.user}')

@client.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == client.user:
        return

    # Commands
    if message.content.lower() == "?motivateme":
        await message.channel.send(get_random_quote(general_quotes))
    elif message.content.lower() == "?sport":
        await message.channel.send(get_random_quote(sport_quotes))
    elif message.content.lower() == "?actual":
        await message.channel.send(get_random_quote(actual_quotes))
    elif message.content.lower() == "?competitive":
        await message.channel.send(get_random_quote(competitive_quotes))
    elif message.content.lower() == "?random":
        all_quotes = general_quotes + sport_quotes + actual_quotes + competitive_quotes
        await message.channel.send(get_random_quote(all_quotes))
    elif message.content.lower() == "?ping":
        await message.channel.send(f"{message.author.mention}, Pong!")
    elif message.content.lower() == "?help":
        help_text = (
            "**Available Commands:**\n"
            "`?motivateme` - Get a general motivational quote."
            "`?sport` - Get a motivational quote releated to sports."
            "`?actual` - Get a quote from a real person who said the quote."
            "`?competitive` - Get a quote that is competitive"
            "`?random` - Get a random quote from these categories above."
            "`?ping` - Ping user and check if bot is working."
            "`?help` - Display help message like now."
            "`?end` - End session and make bot offline. Only for use of owner."
        )
        await message.channel.send(help_text)
    elif message.content.lower() == "?end":
        if message.author.id == BOT_OWNER_ID:
            await message.channel.send("You are authorised to make bot offline. Logging out...")
            await client.close()
        else:
            await message.channel.send("You are not authorised to make bot offline. Command failed.")

# Run the bot
client.run(TOKEN)

