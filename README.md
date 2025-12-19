# black_jack_game
<pre>♠️ ♥️ Python Blackjack (21)
A command-line implementation of the famous casino card game Blackjack. The goal is to get a card sum as close to 21 as possible without going over ("busting"), while beating the dealer's score.

📖 Description
This project replicates the core mechanics of Blackjack using Python. It simulates a deck of cards, handles user inputs to "Hit" or "Stand," and includes an automated dealer that follows standard casino rules (must draw until the score is 17 or higher).

I built this project to master:

Complex Game Logic: Handling the dual value of Aces (1 or 11).

Lists & Functions: passing lists into functions to modify card values.

The random module: Simulating a shuffled deck.

Control Flow: Using while loops to manage the game state.

⚡ Key Features
Smart Aces: The game automatically detects if an Ace (A) should count as 11 or 1 to prevent you from busting.

Dealer AI: The dealer plays automatically based on the rule: "Dealer must hit on soft 16, stand on 17".

Infinite Deck: The game simulates a shoe with infinite cards, so probabilities remain consistent.

🎮 How to Play
Run the script.

You are dealt 2 cards. You will see all of yours, but only one of the dealer's cards.

Choose your action:

Type y to Hit (take another card).

Type n to Stand (keep your current hand).

If you go over 21, you lose immediately.

If you stand, the dealer reveals their hidden card and draws until they hit 17 or higher.

The winner is decided by who is closest to 21.
Here is a comprehensive README.md for your Blackjack game.

I have highlighted the Ace Logic (changing value from 11 to 1) and the Dealer Rule (drawing until 17) as these are the most complex parts of the logic you implemented, and they look impressive on a GitHub profile.

♠️ ♥️ Python Blackjack (21)
A command-line implementation of the famous casino card game Blackjack. The goal is to get a card sum as close to 21 as possible without going over ("busting"), while beating the dealer's score.

📖 Description
This project replicates the core mechanics of Blackjack using Python. It simulates a deck of cards, handles user inputs to "Hit" or "Stand," and includes an automated dealer that follows standard casino rules (must draw until the score is 17 or higher).

I built this project to master:

Complex Game Logic: Handling the dual value of Aces (1 or 11).

Lists & Functions: passing lists into functions to modify card values.

The random module: Simulating a shuffled deck.

Control Flow: Using while loops to manage the game state.

⚡ Key Features
Smart Aces: The game automatically detects if an Ace (A) should count as 11 or 1 to prevent you from busting.

Dealer AI: The dealer plays automatically based on the rule: "Dealer must hit on soft 16, stand on 17".

Infinite Deck: The game simulates a shoe with infinite cards, so probabilities remain consistent.

🎮 How to Play
Run the script.

You are dealt 2 cards. You will see all of yours, but only one of the dealer's cards.

Choose your action:

Type y to Hit (take another card).

Type n to Stand (keep your current hand).

If you go over 21, you lose immediately.

If you stand, the dealer reveals their hidden card and draws until they hit 17 or higher.

The winner is decided by who is closest to 21.


NOTE:

art2.py file: This game relies on a local module named art2.py for the logo. Ensure this file is in the same folder as your main script.

🚀 Future Improvements
[ ] Add a betting system (chips/money).

[ ] Implement "Split" and "Double Down" functionality.

[ ] Create a graphical interface using Pygame.

👤 Author
Haadil Hayath Basha
</pre>