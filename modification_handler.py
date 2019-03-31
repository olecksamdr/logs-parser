import re

from watchdog.events import RegexMatchingEventHandler

class ModificationHandler(RegexMatchingEventHandler):
    def __init__(self, watch_path, callback):
      super().__init__(
        regexes=[re.escape(watch_path)],
        ignore_regexes=[],
        ignore_directories=True,
        case_sensitive=True
      )

      self.watch_path = watch_path
      self.callback = callback

    def process(self, event):
        print(event.src_path, event.event_type)
        self.callback(event.src_path)

    def on_modified(self, event):
        if event.src_path == self.watch_path:
          self.process(event)

    def on_created(self, event):
        if event.src_path == self.watch_path:
          self.process(event)

