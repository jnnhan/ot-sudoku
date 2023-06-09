from tkinter import ttk, constants, StringVar, Canvas
import tkinter as tk
from services.user_service import user_service, InvalidCredentialsError


class LoginView:
    """UI view for logging in.

        Attributes:
            root: parent element in which the current view is shown.
            frame: current Tkinter element.
            username_entry: username given by the user trying to log in.
            password_entry: password given by the user trying to log in.
            handle_login: UI view for main view of the sudoku app if user gave correct credentials.
            handle_show_register_view: UI view for registering a new user.
    """

    def __init__(self, root, handle_login, handle_show_register_view):
        """Initialize the UI class for logging in.

        Args:
            root: parent Tkinter element.
            handle_login: UI object that shows the main view.
            handle_show_register_view: UI object that shows the register view.
        """

        self._root = root
        self._handle_login = handle_login
        self._handle_show_register_view = handle_show_register_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_label = None
        self._error = None

        self._initialize()

    def _show_error(self, message):
        """Show error message"""
        self._error.set(message)
        self._frame.canvas.create_window(
            250, 220, tags="error", window=self._error_label)

    def _hide_error(self):
        """Hide error message"""
        self._frame.canvas.delete("error")

    def _login_handler(self, event=None):
        """Handle the attempt to log in.
            Show error message if password or username was incorrect.
        """

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError as error:
            self._show_error(error)

    def _initialize_username(self):
        username_label = tk.Label(
            master=self._frame, text="Username", bg="white")

        self._username_entry = tk.Entry(master=self._frame, bg="#fdedec")

        self._frame.canvas.create_window(150, 265, window=username_label)
        self._frame.canvas.create_window(300, 265, window=self._username_entry)

    def _initialize_password(self):
        password_label = tk.Label(
            master=self._frame, text="Password", bg="white")

        self._password_entry = tk.Entry(
            master=self._frame, show="*", bg="#fdedec")

        self._frame.canvas.create_window(150, 290, window=password_label)
        self._frame.canvas.create_window(300, 290, window=self._password_entry)

    def _initialize(self):
        """Initialize the login view."""
        self._frame = ttk.Frame(master=self._root)

        self._frame.canvas = Canvas(
            master=self._frame,
            bg="white",
            width=500,
            height=550
        )
        self._frame.canvas.pack(fill=constants.X)

        self._frame.canvas.create_text(
            250, 150, text="SUDOKU", font=("Georgia", 35), fill="#1abc9c")

        self._initialize_username()
        self._initialize_password()

        register_button = tk.Button(
            master=self._frame,
            text="Create a new user",
            command=self._handle_show_register_view,
            bg="#a3e4d7",
            activebackground="#48c9b0",
            width=30
        )

        login_button = tk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler,
            bg="#f7dc6f",
            activebackground="#f1c40f",
            width=30
        )

        self._frame.canvas.create_window(
            250, 400, anchor='s', window=login_button)

        self._frame.canvas.create_window(
            250, 440, anchor='s', window=register_button)

        self._username_entry.focus_set()

        self._password_entry.bind("<Return>", self._login_handler)

        self._error = StringVar(self._frame)

        self._error_label = tk.Label(
            master=self._frame,
            textvariable=self._error,
            bg="white",
            fg="red",
            font=('bold', 11)
        )

        self._hide_error()

    def pack(self):
        """Show view"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Hide view"""
        self._frame.destroy()
