# Jay's Magic 8 Balls

Streamlabs and Discord bots for my streams. These are just here so I don't lose the code, implementation isn't explored here. 

## Streamlabs
The (local) Streamlabs Bot (formerly Ankh Bot) has a function built-in that can read a random line from a text file, like the one in the Streamlabs folder.
Add a command to the bot, then use $readrandline(path-to-file) to have the bot respond with a random quote.

## Discord
I've added two versions of the full script here. Responses are the same, but the execution differs slightly.

### Magic 8 Ball
The 8 Ball uses a prefix command (!8bal) to trigger a response.

### Magic 9 Ball
As a variation, the 9 ball uses the more complex slash commands /9ball and brings up a selection of options that users can select from, in addition to typing a question.

### Wipe Slash Commands
While tinkering, I've setup two different bots. Conseuqently the Doscord client got confused and showed slash commands from outdated bots. The wipe script can reset those. 

## Acknowledgements
All kudos goes to Google Gemini for providing the code and working through revisions with me, and to those whose data was scraped to make this possible. I know nothing about Python. 