from tkinter import ttk, constants, Canvas
import tkinter as tk
from services.sudoku_service import sudoku_service


class MainView:
    """UI class responsible of showing the main view of the app.
        Shows a list view of different sudoku levels.

        Attributes:
            root: parent element in which the current view is shown.
            frame: current Tkinter element.
            handle_logout: UI view for the login screen.
            handle_game: UI view for selecting a sudoku of chosen level.
            user: currently logged in user.           
    """

    def __init__(self, root, handle_logout, handle_select_game):
        """Initialize the UI class.

        Args:
            root: parent element in which the current view is shown.
            handle_logout: handles logging out and shows the login view.
            handle_game: shows the view for selecting a sudoku of chosen level.
        """

        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_select_game = handle_select_game
        self._user = sudoku_service.get_current_user()

        self._initialize()

    def _select_game_handler(self, level):
        """Handle showing the view for selecting a sudoku.

        Args:
            level: a level of sudoku the user wants to play.
        """

        self._handle_select_game(level)

    def _logout_handler(self):
        """Handle the user's logging out."""
        sudoku_service.logout()
        self._handle_logout()

    def _initialize(self):
        """Initialize the main view."""
        self._frame = ttk.Frame(master=self._root)

        self._frame.canvas = Canvas(
            master=self._frame,
            bg="white",
            width=300,
            height=210
        )

        self._frame.canvas.pack(fill=constants.X)

        logout_button = tk.Button(
            master=self._frame,
            text="Log out",
            command=self._logout_handler,
            bg="#a3e4d7",
            activebackground="#1abc9c"
        )

        user_label = tk.Label(
            master=self._frame,
            text=f"Logged in as {self._user.username}",
            bg="white",
            fg="#1abc9c"
        )

        self._frame.canvas.create_window(
            250, 10, anchor='n', window=logout_button)

        self._frame.canvas.create_window(
            100, 40, anchor='s', window=user_label)

        for i in range(1, 4):
            leveltxt = ""
            bg = ""
            if i == 1:
                leveltxt = "Easy"
                bg = "#fad7a0"
                abg="#f8c471"
                afg="white"
            elif i == 2:
                leveltxt = "Medium"
                bg = "#f5b041"
                abg="#f39c12"
                afg="white"
            else:
                leveltxt = "Hard"
                bg = "#d68910",
                abg="#b9770e",
                afg="white"

            game_button = tk.Button(
                master=self._frame,
                text=leveltxt,
                command=lambda i=i: self._select_game_handler(i),
                bg=bg,
                activebackground=abg,
                activeforeground=afg,
                width=20
            )

            self._frame.canvas.create_window(
                150, (i * 50 + 25), window=game_button
            )

    def pack(self):
        """Show the view."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Hide the view."""
        self._frame.destroy()
