##Python Text Game

This is a text-based dungeon game as suggested by [Exercise 36 of Learn Python the Hard Way](http://learnpythonthehardway.org/book/ex36.html).

The goal is to survive a series of mythological creatures and reach the treasure room at the end. Some creatures bestow wisdow or hints. Others may give necessary supplies. Others only bring death. The map is mostly linear, you will not be able to loop back and revisit a room you've already been through.

###To-Do List

- <s>Figure out how I want to solve the Sphinx's riddle</s>
- <s>Finish stubbing out the remaining functions</s>
- Actually writing out the print statements
- <s>Case insensitive user input</s>
- <s>Get user input to recognize only a single letter entry when appropriate</s> Decided against doing this so the user can change their mind before they hit enter.
- <s>`supply_contents` needs to reset to an empty list if the user continues inside `death()`</s>

###Future additions
- Printing the supply list only when user requests it, not at every room
- Expand riddles to include multiple options instead of just the one riddle
- Can the creature order be made random?
- Error checking for user input in a way that does not just use `else: death()`
- <s>Should items be removed from the list `supply_contents` after they have been used?</s> I totally figured out what I wanted to do here right after adding this bullet
