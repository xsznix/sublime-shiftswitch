from sublime_plugin import TextCommand

class ShiftswitchCommand(TextCommand):
  "Abstract base class for commands."

  def set_tab_size(self, ts):
    self.view.run_command('set_setting', {"setting": 'tab_size', "value": ts})

  def set_use_tabs(self, use_tabs):
    self.view.run_command('set_setting', {"setting": 'translate_tabs_to_spaces', "value": True})

  def modify_use_tabs(self, use_tabs):
    if use_tabs:
      self.view.run_command('unexpand_tabs')
    else:
      self.view.run_command('expand_tabs')

class ShiftswitchIndentCommand(ShiftswitchCommand):
  def run(self, edit, ts, use_tabs):
    self.set_tab_size(ts)
    self.set_use_tabs(use_tabs)

class ShiftswitchReindentCommand(ShiftswitchCommand):
  def run(self, edit, ts, use_tabs):
    self.modify_use_tabs(True)
    self.set_tab_size(ts);
    if not use_tabs:
      self.modify_use_tabs(False)
