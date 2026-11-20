# Smart Home Devices (Multiple Inheritance) 
'''A smart home device may have both WiFi connectivity and Voice control features. 
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that 
inherits from both using multiple inheritance.
'''
class WiFiDevice:
    def wifi(self):
        print("WiFi connectivity available")


class VoiceAssistant:
    def voice(self):
        print("Voice control available")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker")


s = SmartSpeaker()

s.display()
s.wifi()
s.voice()
