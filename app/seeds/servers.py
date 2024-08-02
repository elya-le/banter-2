from app.models import db, Server, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_servers():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_server_membership RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.servers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_server_membership"))
        db.session.execute(text("DELETE FROM servers"))
    db.session.commit()

    servers = [
        Server(
            name="Roast My Resume",
            description="Submit your resume and let our experts roast it with sharp, honest feedback.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Roast-My-Resume-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Roast-My-Resume-b.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Post-grad Pad",
            description="For App Academy alumni to network and collaborate.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Post-Grad-Pad-a.jpeg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Post-Grad-Pad-b.jpg",
            category="Networking",
            creator_id=1,
        ),
        Server(
            name="Midjourney",
            description="The official server for Midjourney, a text-to-image AI.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Midjourney-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Midjourney-b.jpg",
            category="Art",
            creator_id=1
        ),
        Server(
            name="TryHackMe",
            description="A place to ask questions and grow your cybersecurity skills.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/TryHackMe-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/TryHackMe-b.jpg",
            category="Education",
            creator_id=1
        ),
        Server(
            name="Lofi Girl",
            description="Join to meet amazing people from all around the world.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Lofi-Girl-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Lofi-Girl-b.jpg",
            category="Music",
            creator_id=1
        ),
        Server(
            name="Pixel Cave",
            description="Connect with like-minded individuals who share your interests.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Pixel-Cave-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Pixel-Cave-b.jpg",
            category="Art",
            creator_id=1
        ),
        Server(
            name="App Academy Instruction: Online Programs",
            description="Class server",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/App-Academy-a.jpeg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/App-Academy-b.png",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Design Buddies",
            description="Meet other designers and level up your design skills.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Design-Buddies-a.png",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Design-Buddies-b.png",
            category="Education",
            creator_id=1
        ),
        Server(
            name="Genshin Impact Official",
            description="Welcome to Teyvat, Traveler! Discuss your favorite game: Genshin Impact!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Genshin-Impact-Official-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Genshin-Impact-Official-b.jpg",
            category="Gaming",
            creator_id=1
        ),
        Server(
            name="Language Sloth",
            description="Learn languages and speak in the voice chat!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Language-Sloth-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Language-Sloth-b.jpg",
            category="Education",
            creator_id=1
        ),
        Server(
            name="Chess.com",
            description="Satisfy all of your Chess needs with fellow Chess fans.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Chess-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Chess-b.jpg",
            category="Gaming",
            creator_id=1
        ),
        Server(
            name="Mini Motorways - Gridlock Gang",
            description="Share your city layouts, discuss strategies, and participate in friendly competitions.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Mini-Motorways-a.webp",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Mini-Motorways-b.avif",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="Learn w/ Leon & Friends",
            description="We provide a 100 percent free path to becoming a software engineer!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Learn-with-Leon-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Learn-with-Leon-b.jpg",
            category="Education",
            creator_id=1
        ),
        Server(
            name="Refactor Retreat",
            description="The road to greenlit does not have to be lonely.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Refactor-Retreat-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Refactor-Retreat-b.webp",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Voltaic",
            description="Voltaic is an educational community with a focus on improvement.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Voltaic-a.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/Voltaic-b.jpg",
            category="Education",
            creator_id=1
        ),
        Server(
            name="Honkai: Star Rail Official",
            description="Honkai: Star Rail is a space fantasy RPG by HoYoverse. Hop aboard the Astral Express and explore the galaxy's wonders!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="VALORANT",
            description="The official VALORANT Discord server, in collaboration with Riot Games. Find the latest news and talk about the game!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="Once Human",
            description="The official Discord server of the game Once Human by Starry Studio. Find the latest news and discuss this game!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="MINECRAFT",
            description="The official Minecraft Discord!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="Deep Rock Galactic",
            description="Official Discord Server for Deep Rock Galactic – a game about dwarven teamwork, mining and shooting aliens.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="Official Fortnite",
            description="Join the largest Fortnite server. LFG, and chat about Fortnite Battle Royale.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="Roblox",
            description="The largest community-run Roblox Discord. Join for both Devs and Creators.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="Wuthering Waves Official",
            description="The official Discord server for Wuthering Waves – a story-rich open-world game by Kuro Games.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="The Forbidden Trove",
            description="The largest server for everything Path of Exile. Trading, Crafting, Help, memes, socializing & much more!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Gaming",
            creator_id=1,
        ),
        Server(
            name="Rythm",
            description="This is the home of Rythm. Here you can play songs in a call, join the latest news on Rythm releases and much more!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Suno",
            description="Make any song you can imagine.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Groovy Community",
            description="Official place of the Groovy Discord bot. Join for events, giveaways, and a cool community.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Müziisyenler",
            description="Bölge müziğini paylaşma, sohbetler edip yeni arkadaşlar edinme şansı tanıtan bir yer.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="BLACKPINK LISA ROCKSTAR",
            description="The place to be for anything BLACKPINK. Stay up-to-date and chat with fellow BLINKs!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Young Multi",
            description="Officially sanctioned server for Young Multiage.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Kenny Beats",
            description="The official fan Discord for Kenny Beats and The Cave.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="World Of Walker",
            description="The official Alan Walker Server. Let’s connect, chat and have fun!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Karaoke Lounge - Singing - Musical Theatre",
            description="The official server of karaoke. Meet new people, have fun singing, and enter weekly contests. There’s something for everyone, regardless of skill!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="New Jeans (뉴진스) Never Die",
            description="A discord server dedicated to ADOR’s girl group, NewJeans! Feel free to join and hang around.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Stray Kids",
            description="The official discord server for Stray Kids. Come and stay!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Ken Carson",
            description="The official Ken Carson discord server.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="#TaylorSwift",
            description="A welcoming community for Taylor Swift fans. Come join us!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="baby no server",
            description="Welcome to the official Discord server for “baby no money”. Hang out with other fans and catch up on what he’s up to!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Music",
            creator_id=1,
        ),
        Server(
            name="Study Together",
            description="The largest study and productivity server on Discord! Study live with others via camera, screenshot or chat!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
         Server(
            name="Mathematics",
            description="A place for people to learn and discuss mathematics.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Game Dev League",
            description="A community-centered server built by Game Developers, for Game Developers!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="The English Hub",
            description="A world of active English learning. Improve your English skills speaking in text and voice.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Language Sloth",
            description="The official discord server for the Language Sloth community on Discord. Learn languages and speak in the voice chat!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Gehar's Guide",
            description="A community dedicated to helping you with your homework or applying to college.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="German Learning and Discussion",
            description="A community-driven server for learning German with native speakers, lessons, and many useful resources!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="OffSec",
            description="The official Discord allows members to learn, share, and connect with others in the OffSec community.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Spanish-English Learning Service",
            description="Learn Spanish and English in this most friendly server! - Aprenda español e inglés en este servidor más amigable!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="ELGATO",
            description="Official Elgato Discord for content creators, YouTubers, and more! Get news and learn more about Elgato products.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Japanese Academy",
            description="We are a tight-knit community where you can receive guidance, assistance, and support in your journey to learning Japanese.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="French - Learn French in a friendly community",
            description="The #1 french community if you are learning or trying to learn the language.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="OverSimplified",
            description="The official Discord server for the OverSimplified YouTube channel. Come join our community!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="MKHBD",
            description="The official community of the Marques Brownlee YouTube channel!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Education",
            creator_id=1,
        ),
        Server(
            name="Viggle",
            description="Visual.ai, making any character move as you want.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="Leonardo.ai",
            description="Leonardo AI is a generative AI platform for content creation. Create game assets, artwork, design elements, and more!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="Opera GX",
            description="The official Discord server of the world's first gaming browser.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="Stable Diffusion",
            description="Welcome to Stable Diffusion, the home of Stable Models and the official Stable AI community!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="HackTheBox",
            description="Get started with hacking in the academy, test your skills against boxes and challenges or chat about infosec with others.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="OpenAI",
            description="A space for developers and enthusiasts to collaborate and share creations built with OpenAI's powerful models.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="TechSource Club",
            description="The official TechSource Discord server for all your tech topics!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="buildapc",
            description="All things PC building, part selection, and troubleshooting. Plus discussions on latest tech and gaming news!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="RoDevs",
            description="RoDevs is a Discord community oriented towards Roblox development, with various members to get help and do business.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="Finalmouse",
            description="The official Finalmouse Discord server.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="PC MASTER RACE",
            description="PCMIR is the biggest PC enthusiast community in the world. Come hang out, chat and/or get help, build OC or help!",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="Home Assistant",
            description="Come discuss home automation that puts local control and privacy first.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="discord.js - Imagine an app",
            description="Support server for discord.js, a powerful API to interact with Discord’s apps.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),
        Server(
            name="VR Discord",
            description="A community for VR enthusiasts and novices alike, regular events and friendly chat.",
            avatar_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            banner_url="https://portfolio-elya.s3.us-east-2.amazonaws.com/banter-server-seeders/placeholder.jpg",
            category="Art",
            creator_id=1,
        ),

    ]

    user = User.query.get(1)

    for server in servers:
        user.joined_servers.append(server)

    db.session.commit()

def undo_servers():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_server_membership RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.servers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_server_membership"))
        db.session.execute(text("DELETE FROM servers"))
    db.session.commit()