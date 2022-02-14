from mycroft import MycroftSkill, intent_file_handler
import subprocess 

class Pi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pi.intent')
    def handle_pi(self, message):
        property = message.data.get('property')
        self.log.info(f'"Property: "{property}')
        name = ''
        value = ''
        if property == 'model number':
          name = 'model number'
          p4 = subprocess.Popen(['cat','/proc/cpuinfo'],stderr=subprocess.PIPE, universal_newlines=True,stdout=subprocess.PIPE)
          p5 = subprocess.Popen(["grep", "Model"], stdin=p4.stdout, stdout=subprocess.PIPE)
          p6 = subprocess.Popen(['cut','-d',' ','-f','2-'], stdin=p5.stdout, stdout=subprocess.PIPE)
          output = p6.communicate()
          value = output[0].decode('UTF-8') 
        if property == 'serial' number:
          name = 'serial number'
          p1 = subprocess.Popen(['cat','/proc/cpuinfo'],stderr=subprocess.PIPE, universal_newlines=True,stdout=subprocess.PIPE)
          p2 = subprocess.Popen(["grep", "Serial"], stdin=p1.stdout, stdout=subprocess.PIPE)
          p3 = subprocess.Popen(['cut','-d',' ','-f','2'], stdin=p2.stdout, stdout=subprocess.PIPE)
          output = p3.communicate()
          value = output[0].decode('UTF-8') 
        if property == 'temperature':
          name = 'temperature'
          s = subprocess.check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"])
          value = s.decode('UTF-8')
        if property == 'operating system':
          name = 'operating system'
          p7 = subprocess.Popen(['cat','/etc/os-release'],stderr=subprocess.PIPE, universal_newlines=True,stdout=subprocess.PIPE)
          p8 = subprocess.Popen(["grep", "PRETTY_NAME"], stdin=p7.stdout, stdout=subprocess.PIPE)
          p9 = subprocess.Popen(['cut','-d','=','-f','2-'], stdin=p8.stdout, stdout=subprocess.PIPE)
          p10 = subprocess.Popen(['sed','s/["()/]/ /g'], stdin=p9.stdout, stdout=subprocess.PIPE)
          output = p10.communicate()
          value = output[0].decode('UTF-8')
        if property == 'kernel version':
          name = 'kernel version'
          s = subprocess.check_output(["uname", "-r"])
          value = s.decode('UTF-8')
        if property == 'firmware version':
          name = 'firmware version'
          p11 = subprocess.Popen(['vcgencmd','version'],stderr=subprocess.PIPE, universal_newlines=True,stdout=subprocess.PIPE)
          p12 = subprocess.Popen(["grep", "version"], stdin=p11.stdout, stdout=subprocess.PIPE)
          p13 = subprocess.Popen(['cut','-d',' ','-f','2'], stdin=p12.stdout, stdout=subprocess.PIPE)
          output = p13.communicate()
          value = output[0].decode('UTF-8')
        self.speak_dialog('pi', data={
            'name': name,
            'value': value,
            'property': property
        })


def create_skill():
    return Pi()


