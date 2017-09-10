import sublime
from sublime_plugin import EventListener


class PynsisCommand(EventListener):
    def on_load(self, view):
        if (view.file_name().endswith("/installer.cfg")):
            if (view.settings().get("syntax").endswith("Pynsist.sublime-syntax")):
                return

            auto_set_syntax = sublime.load_settings("Pynsist.sublime-settings").get("auto_set_syntax")

            if auto_set_syntax is True:
                view.set_syntax_file("Pynsist.sublime-syntax")
