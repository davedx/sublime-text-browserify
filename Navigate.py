import sublime
import sublime_plugin
import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

class NavigateBrowserifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        s = sublime.load_settings('Browserify Navigation.sublime-settings')

        namespace = s.get('namespace')

        # start of file:   "./src/vod2/src/vod.js":[function(require,module,exports){

        # },{"./config":"c:\\projects\\dawn\\src\\vod2\\src\\config.js","./dataservice":"c:\\projects\\dawn\\src\\vod2\\src\\dataservice.js","./dawn_integration":"c:\\projects\\dawn\\src\\vod2\\src\\dawn_integration.js","./event":"c:\\projects\\dawn\\src\\vod2\\src\\event.js","./history":"c:\\projects\\dawn\\src\\vod2\\src\\history.js","./input":"c:\\projects\\dawn\\src\\vod2\\src\\input.js","./local_development_settings_manager":"c:\\projects\\dawn\\src\\vod2\\src\\local_development_settings_manager.js","./mixins/crumbtrail_mixin":"c:\\projects\\dawn\\src\\vod2\\src\\mixins\\crumbtrail_mixin.js","./pagetransitions":"c:\\projects\\dawn\\src\\vod2\\src\\pagetransitions.js","./render_helpers":"c:\\projects\\dawn\\src\\vod2\\src\\render_helpers.js","./router":"c:\\projects\\dawn\\src\\vod2\\src\\router.js","./statestore":"c:\\projects\\dawn\\src\\vod2\\src\\statestore.js","./statistics":"c:\\projects\\dawn\\src\\vod2\\src\\statistics.js","./trace":"c:\\projects\\dawn\\src\\vod2\\src\\trace.js"}],"c:\\projects\\dawn\\node_modules\\backbone\\backbone.js":[function(require,module,exports){
        #buffer = open('file.txt','r').read()
        #modules = re.findall(r'""', buffer)

        current_file = self.view.file_name()

        for region in self.view.sel():

            line = self.view.line(region)
            line_contents = self.view.substr(line)

            m = re.search("require([\s\(])[\'\"](.*)[\'\"]", line_contents)

            if m != None:

                name = m.group(2)

                key = ":".join([namespace, current_file])

                self.view.insert(edit, 0, current_file + " -> " + name)
                self.view.window().open_file(name + ".js")

