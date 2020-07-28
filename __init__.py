from mycroft import MycroftSkill, intent_file_handler


class Skelapp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skelapp.intent')
    def handle_skelapp(self, message):
        self.speak_dialog('skelapp')


def create_skill():
    return Skelapp()

