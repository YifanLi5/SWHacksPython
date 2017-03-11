import pyrebase



def initialize():
    config = {
        "apiKey" : None,
        "authDomain": None,
        "databaseURL" : "https://swhacksfirebase.firebaseio.com",
        "storageBucket" : None
    }

    firebase = pyrebase.initialize_app(config)
    return firebase

def feed_fish():
    


def update_field(db, key, value):
    db.update({key : value})

def update_temperature(db, temperature):
    update_field(db, "ToAndroid/Temperature", temperature)

def update_time(db, time):
    update_field(db, "ToAndroid/Time", time)

def null():
    temperature = db["ToAndroid/Temperature/"]
    time = fishtank_data["Time"]
    print(temperature, time)
    fishtank_data = fishtank_db.get().val()
    fishtank_data = fishtank_db.get().val()
    time = fishtank_data["Time"]
    print(temperature, time)

    update_time(fishtank_db, "asdfasdf")
    update_temperature(fishtank_db, 99)


def main():
    fb = initialize()
    db = fb.database()
    fishtank_db = db

    def stream_handler(message):
        print(message)

    print("[-] starting stream")
    stream = fishtank_db.child("ToAndroid").stream(stream_handler)


if __name__ == '__main__':
    main()