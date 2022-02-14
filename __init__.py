from mycroft import MycroftSkill, intent_file_handler


class Pi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pi.intent')
    def handle_pi(self, message):
        temperature = message.data.get('temperature')
        name = ''
        value = ''

        self.speak_dialog('pi', data={
            'value': value,
            'temperature': temperature,
            'name': name
        })


def create_skill():
    return Pi()

