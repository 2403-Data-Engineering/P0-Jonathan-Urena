from presentation.terminal import Terminal



if __name__ == "__main__":
    
    terminal = Terminal()
    while(terminal.running):
        terminal.current_menu.render()
    print("...Goodbye!")
