import sublime
import sublime_plugin
import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

import redis


class NavigateBrowserifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        s = sublime.load_settings('Browserify Navigate.sublime-settings')

        r = redis.Redis(
            host=s.get('redis_host'),
            port=s.get('redis_port'),
            db=s.get('redis_db'))

        namespace = s.get('namespace')

        current_file = self.view.file_name()

        for region in self.view.sel():

            line = self.view.line(region)
            line_contents = self.view.substr(line)

            m = re.search("require([\s\(])[\'\"](.*)[\'\"]", line_contents)

            if m != None:

                name = m.group(2)

                key = ":".join([namespace, current_file])

                result = r.hget(key, name)

                if result != None:
                    result = result.decode('utf-8')
                    self.view.window().open_file(result)
                else:
                    print("No module found for path " + name)
