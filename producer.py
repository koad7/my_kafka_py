#
# This file will produce to a topic named "test" 
#
# To run this file: poetry run python3 producer.py worker

import faust 
import random

app = faust.App('send_data', broker='kafka://localhost:9092')
topic = app.topic('market_data')

@app.timer(interval=1.0)
async def send_message(message):
    data = {"hello-random": random.randrange(0,100)}
    await topic.send(value=data)

# Start the Faust App
app.main()
