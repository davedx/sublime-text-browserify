import sublime, sublime_plugin, sys, os, re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

import redis

# require './application'
# require 'test'

class NavigateBrowserifyCommand(sublime_plugin.TextCommand):

  def run(self, edit):

    r = redis.Redis()

    current_file = self.view.file_name()

    for region in self.view.sel():

        line = self.view.line(region)
        line_contents = self.view.substr(line)

        m = re.search("require([\s\(])[\'\"](.*)[\'\"]", line_contents)

        if m != None:
            name = m.group(2)

            key = ":".join(["browserify", current_file])

            result = r.hget(key, name)

            if result != None:
              result = result.decode('utf-8')
              print(result)
              self.view.window().open_file(result)
            else:
              print("No module found for path " + name)
