import curses
text1 = """Hello world!
This is a tiny text editor.
Edit me!"""
text = text1.splitlines(keepends = True)
cursor = 0
index = 0
# ---------------- ANSWER ----------------
def draw(screen):
    screen.clear()
    string = ""
    for i in range(0, len(text)):
        lin = text[i]
        if i == index and text[index] == "":
            string += lin + "|"
        elif i == index:
            string +=  lin[:cursor] + "|" + lin[cursor:]
        else:
            string += lin 
    display = string
    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )
    screen.refresh()
# ---------------- ANSWER ----------------
def main(screen):
    global text, cursor, index, back
    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break
        elif key == curses.KEY_LEFT:
            if cursor <= 0 and index == 0:
                pass
            elif cursor <= 0:
                index -= 1
                cursor = len(text[index])
            else:
                cursor -= 1
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_RIGHT:
            if cursor > len(text[index]) - 1 and index == len(text) -1:
                pass
            elif cursor > len(text[index]) - 1:
                index += 1
                cursor = 0
            else:
                cursor += 1
        # ---------------- ANSWER ----------------
        elif key in (8, 127, curses.KEY_BACKSPACE):
            if cursor == 0 and index == 0:
                pass
            elif cursor == 0:
                index -= 1
                text[index] = text[index][:len(text[index])-1]
                cursor = len(text[index])
            else:
                text[index] = text[index][:cursor -1] + text[index][cursor:]
                cursor -=1
        # ---------------- ANSWER ----------------
        elif key == 10:
            if cursor == len(text[index]):
                text.insert(index+1, "\n") 
            else:
                text.insert(index+1, text[index][cursor:])
                text[index] = text[index][:cursor] + "\n"
            index += 1
            cursor = 0
        # ---------------- ANSWER ----------------
        elif 32 <= key <= 126:
            text[index] = text[index][:cursor] + chr(key) + text[index][cursor:]
            cursor += 1
        # ---------------- ANSWER ----------------
        elif key == curses.KEY_UP:
            if index == 0:
                pass
            elif cursor >= len(text[index-1]):
                index -= 1
                cursor = len(text[index]) - 1
            else:
                index -= 1
                
        # ---------------- ANSWER ----------------
        elif key == curses.KEY_DOWN:
            if index == len(text)-1:
                pass
            elif cursor >= len(text[index+1]):
                index += 1
                cursor = len(text[index])
            else:
                index += 1

curses.wrapper(main)



