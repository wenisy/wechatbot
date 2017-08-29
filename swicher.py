def buy_flowers():
    return 'buy flowers'


def about_us():
    return 'about us'


def default_behaviour():
    print "can't find key"


def receive_message(msg):
    switcher = {
        '1': buy_flowers,
        '2': about_us
    }
    return_value = switcher.get(msg['Text'], default_behaviour)()

    return return_value or 'abc'


a = receive_message({'Text': '1'})
# a = receive_message({'Text': '3'})
print a