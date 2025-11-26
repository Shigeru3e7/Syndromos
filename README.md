# Sýndromos Discord Bot

Sýndromos is a multifunctional Discord bot developed in Python using the `discord.py` library. It offers a wide range of commands, from mini-games to utility and random commands, enhancing server interaction.

---

## Main Features

### Games 🎮

* `popogame` : potion game with buying and selling mechanics.
* `stickgame` : strategic stick game for 2 or more players.
* `pile_face` : coin flip (Heads or Tails).

### Random Commands 🎲

* `randomsentence` : generates a random sentence.
* `syndrome` : assigns a random "syndrome" to a member.
* `randominteger` : generates a random integer between two numbers.
* `randomdecimal` : generates a random decimal number between two numbers.

### Utility Commands 🛠️

* `say` : the bot repeats what you type.
* `qrcode 'url'` : generates a QR code for the given URL.
* `member_list` : shows server members with their IDs.
* `userinfo (member)` : displays information about a user.
* `bam` : tests the bot's latency.

### Reaction Commands 👒

* `vote (message ID)` : adds 👍 and 👎 reactions to a message.

### Time Capsule ⏳

* `caps` : create a **Time Capsule** with a name and countdown before opening.

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <bot-directory>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file (or equivalent) to store your Discord token:

```
DISCORD_TOKEN=YourTokenHere
```

4. Run the bot:

```bash
python bot.py
```

---

## Prefix and Commands

* Default prefix: `s!`
* Main slash command: `/help` to get the full manual.

---

## Customization and Translations

The bot can be customized and translated. All messages and embeds can be modified directly in the code to adjust responses.

---

## Contributions

Contributions are welcome! You can propose new features, commands, or improve bot stability.

---

## License

This project is open-source. Please credit the main author: **Shisaku**.
