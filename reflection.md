# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game was a simple guess game in which the user had to guess the secret number between a given range of numbers (based on the difficulty of the game set) using the hints provided after each guess. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. The hints were backwards. If the secret number is lower than the guessed number, the hint tells the user to go higher and vice versa.
2. When the user changes the difficulty of the game, the range is supposed to change but it doesn't actually change in the game. 
3. If the user clicks "Submit Guess" without typing anything into the box, the user loses an attempt.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot (Agent mode and Inline Chat) within VS Code to refactor code and generate tests. I also used an AI assistant to help me reason through the logic of Streamlit's session state and verify my code structure.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
What the AI suggested: When I needed to fix the backwards hints bug, I used Copilot Agent mode to move the check_guess function from app.py into logic_utils.py. The AI correctly suggested swapping the text so that if guess > secret, it returns "📉 Go LOWER!".

How I verified it: I verified this result by asking the AI to generate a pytest case specifically for this logic (test_backwards_hints_fixed). I ran python -m pytest in the terminal, and the test passed. I also played the game in the browser and confirmed the hints were finally telling the truth.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
What the AI suggested: When fixing the "String/Math" bug in app.py (removing the even/odd string conversion), the AI generated the correct logic to pass st.session_state.secret directly, but it completely messed up the Python indentation. It un-indented the outcome, message = check_guess(...) line so it was no longer safely inside the else: block.

How I verified it: I verified this by reading the generated code before accepting it. Because I know Python relies on strict indentation, I realized that if I ran the AI's code, it would either cause an IndentationError or try to run the game logic even if the user typed invalid letters instead of numbers. I had to manually fix the indentation to make the code safe.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was truly fixed when it passed both manual UI testing and automated unit tests. For example, after fixing the difficulty dropdown bug, I didn't just trust the code; I physically clicked the dropdown in the Streamlit browser to ensure the attempts reset and the text updated correctly. I then relied on pytest to guarantee the underlying math and logic functions were rock solid before moving on.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran a custom pytest case called test_backwards_hints_fixed inside test_game_logic.py. This test passed a guess of 80 against a secret number of 50, and asserted that the outcome was "Too High" and that the message explicitly contained the word "LOWER". Running this test successfully proved to me that my refactored check_guess function was properly handling integer comparisons without getting confused by the old string bugs.

- Did AI help you design or understand any tests? How?
Yes, the AI helped me understand why my initial pytest run was failing. It explained that the original starter tests were expecting a single return value, but my newly refactored check_guess function was returning two things (a tuple with outcome and message). The AI showed me how to rewrite the test assertions to properly "unpack" both variables, which taught me how to align my test cases with my actual function signatures.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Imagine you are talking to a very helpful robot that has severe short-term memory loss. Every single time you press a button or type in a text box, the robot completely forgets everything you just did, wipes its brain clean, and reads its entire instruction manual (your code) from top to bottom again—this is a Streamlit "rerun." Because of this constant amnesia, variables like your game score or the secret number would normally get erased and recreated every click. To fix this, you have to write important information on a special sticky note that survives the brain wipe; in Streamlit, that sticky note is called session_state. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One strategy I absolutely want to reuse is test-driven verification, specifically writing targeted pytest cases for individual functions to prove they work in isolation. In the past, I might have just clicked around the user interface to see if a fix worked, but running automated tests gave me much more confidence that the underlying math was truly fixed. I also plan to keep using multi-step prompts and the @workspace tag in Copilot to ensure the AI understands how my different files connect during refactoring.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will be much more critical of the exact syntax and formatting the AI generates before I accept it. Even when the AI's core logic was completely correct—like when it removed the buggy even/odd string conversion—it messed up the Python indentation, which would have crashed the app if I hadn't caught it. I learned that I need to manually review the structural flow of every generated diff rather than blindly trusting the output.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that AI-generated code isn't a finished, production-ready product, but rather a rough draft that requires a human engineer to review, test, and refine. It proved that while AI is an incredibly powerful assistant for speeding up refactoring, I still have to be the lead detective steering the logic and ensuring the architecture makes sense.
