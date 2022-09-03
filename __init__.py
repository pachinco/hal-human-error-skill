from mycroft import MycroftSkill, intent_file_handler


class HalHumanError(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('error.human.hal.intent')
    def handle_error_human_hal(self, message):
        self.speak_dialog('error.human.hal')


def create_skill():
    return HalHumanError()

