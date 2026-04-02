
# ── helper classes ──────────────────────────────────────────────────────────────
def pause(msg="Press Enter to continue..."):
    input(f"\n{msg}")


# ── core classes ──────────────────────────────────────────────────────────────
import Presentation.submenuFunctions
class MenuItem:
    """A single entry in a Menu."""

    def __init__(self, label: str, action=None, submenu=None):
        """
        Parameters
        ----------
        label   : Text shown in the menu.
        action  : Callable executed when the item is selected (optional).
        submenu : A Menu instance to navigate into (optional).
                  If both action and submenu are given, action runs first.
        """
        self.label = label
        self.action = action
        self.submenu = submenu
        
    
    def run(self):
        if self.action:
            self.action()
        elif self.submenu:
            self.submenu.run()


class Menu:
    """
    A navigable console menu.

    Parameters
    ----------
    title       : Heading printed above the options.
    items       : List of MenuItem objects.
    exit_label  : Label for the built-in back/quit option (default 'Back / Quit').
    width       : Width of the decorative border (default 40).
    """

    def __init__(
        self,
        title: str,
        items: list,
        exit_label: str = "Back / Quit",
        width: int = 40,
    ):
        self.title = title
        self.items = items
        self.exit_label = exit_label
        self.width = width


    # ── rendering ────────────────────────────────────────────────────────────

    def _render(self):
        

        border = "─" * self.width
        print(f"┌{border}┐")
        print(f"│  {self.title:<{self.width - 2}}│")
        print(f"├{border}┤")

        for i, item in enumerate(self.items, start=1):
            arrow = "▶ " if item.submenu else "  "
            line = f"  {i}. {arrow}{item.label}"
            print(f"│{line:<{self.width}}│")

        print(f"│{'':>{self.width}}│")
        zero_line = f"  0. {self.exit_label}"
        print(f"│{zero_line:<{self.width}}│")
        print(f"└{border}┘")

    # ── input handling ────────────────────────────────────────────────────────

    def get_choice(self):
        try:
            raw = input("\n  Select an option: ").strip()
            value = int(raw)
            if 0 <= value <= len(self.items):
                return value
            else:
                print(f"  ⚠  Please enter a number between 0 and {len(self.items)}.")
        except ValueError:
            print("  ⚠  Invalid input — enter a number.")
        return None

    # ── main loop ─────────────────────────────────────────────────────────────

    def run(self):
        """Display the menu and block until the user exits."""
        while True:
            self._render()
            choice = self.get_choice()

            if choice is None:
                pause()
                continue

            if choice == 0:
                break

            selected = self.items[choice - 1]
            selected.run()
            if not selected.submenu:
                pause()


def start():
    # ── sub-menus ─────────────────────────────────────────────────────────────
    
    student_menu = Menu(
        title="Manage Students",
        items=[
            MenuItem("Add Student", action=Presentation.submenuFunctions.addStudent),
           
        ],
        exit_label="Back",
    )
    
    professor_menu = Menu(
        title="Manage Professors",
        items=[
            MenuItem("Add Professor", action=Presentation.submenuFunctions.addProfessor),
           
        ],
        exit_label="Back",
    )
    class_menu = Menu(
        title="Manage Classes",
        items=[
            MenuItem("Add Class", action=Presentation.submenuFunctions.addClass),
           
        ],
        exit_label="Back",
    )

    
    

    # ── root menu ─────────────────────────────────────────────────────────────

    main_menu = Menu(
        title="Main Menu  —  Demo",
        items=[
            MenuItem("Manage Students",submenu=student_menu),
            MenuItem("Manage Professors",submenu=professor_menu),
            MenuItem("Manage Classes",submenu=class_menu),
        ],
        exit_label="Quit",
    )

    main_menu.run()
    print("  Goodbye!\n")


#start()