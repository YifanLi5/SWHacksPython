from datetime import datetime
import pyrebase
import motor_control
import temperature
import config
import threading
import servo

def initialize():
    firebase = pyrebase.initialize_app(config.pyrebase_config)
    return firebase

def update_field(key, value):
    db.update({key : value})

def read_field(key): 
    data = db.child(key).get()
    return data.val()

def update_temperature():
    current_temp = temperature.read_temp()
    update_field(config.pyrebase_paths['temperature'], current_temp)
    time_str = "{d:%l}:{d.minute:02}{d:%p}".format(d=datetime.now()).strip()
    update_field(config.pyrebase_paths['temperature_time'], time_str)

def feed_fish():
    current_date = datetime.now().day
    last_date_fed = read_field(config.pyrebase_paths['last_date_fed'])

    if current_date == last_date_fed:
        num_of_feedings = read_field(config.pyrebase_paths['feedings_today'])

        #check if limit of feedings for today is hit
        if num_of_feedings < 2:
            num_of_feedings += 1
            update_field(config.pyrebase_paths['feedings_today'], num_of_feedings)
            #update last feed time
            time_str = "{d:%l}:{d.minute:02}{d:%p}".format(d=datetime.now()).strip()
            update_field(config.pyrebase_paths['feed_time'], time_str)
            servo.turn_bottle()
		
            #with motor_control.Stepper() as s:
            #    s.spin(2)
        else:
            print("max number of feedings hit for today");
    else:
        #update feedings
        update_field(config.pyrebase_paths['feedings_today'], 1)
        update_field(config.pyrebase_paths['last_date_fed'], current_date)
        #update last feed time
        time_str = "{d:%l}:{d.minute:02}{d:%p}".format(d=datetime.now()).strip()
        update_field(config.pyrebase_paths['feed_time'], time_str)

        #turn bottle
        servo.turn_bottle()
    
        #with motor_control.Stepper() as s:
        #    s.spin(2)


def stream_handler(message):
    # {'data': False, 'path': '/', 'event': 'put'}
    if message['event'] == 'put':
        if message['data']:
            feed_fish()
            update_field(config.pyrebase_paths['feed'], False)
    print(message)

def main():
    print("[-] starting stream")
    stream = db.child(config.pyrebase_paths['feed']).stream(stream_handler)

    exit_flag = threading.Event()
    update_temperature()
    while True:
        # wakeup every 5 minutes
        while not exit_flag.wait(timeout=5*60):
            print('[-] updating temperature')
            update_temperature()

def reset_feedings():
    update_field(config.pyrebase_paths['feedings_today'], 0)

fb = initialize()
db = fb.database()

if __name__ == '__main__':
    main()
