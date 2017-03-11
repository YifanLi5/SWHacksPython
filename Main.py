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

def update_field(db, key, value):
    db.update({key : value})

def update_temperature(db, temperature):
    update_field(db, "Temperature", temperature)

def update_time(db, time):
    update_field(db, "Time", time)

def null():
    temperature = db["ToAndroid/Temperature/"]
    time = fishtank_data["Time"]
    print(temperature, time)
    fishtank_data = fishtank_db.get().val()
    fishtank_data = fishtank_db.get().val()
    time = fishtank_data["Time"]
    print(temperature, time)


def main():
    fb = initialize()
    db = fb.database()
    fishtank_db = db.child("ToAndroid")
    update_time(fishtank_db, "asdf")


if __name__ == '__main__':
    main()