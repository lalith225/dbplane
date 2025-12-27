import subprocess
import time
from datetime import datetime
from pymongo import MongoClient

# Define the list of devices (IP addresses or hostnames)
devices = [
    '192.168.1.1', '8.8.8.8', '192.168.1.3',  # Add all your 1000 devices here
]

# MongoDB connection details
mongo_uri = 'mongodb://localhost:27017/'  # Update with your MongoDB URI
database_name = 'ping_database'
collection_name = 'ping_results'


def ping_device(device):
    try:
        # Run the ping command and check the result
        result = subprocess.run(
            ['ping', '-n', '1', device],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )
        output = result.stdout.decode()
        error = result.stderr.decode()

        # Print debugging information
        #print(f'Ping output for {device}:\n{output}')
        #print(f'Ping error for {device}:\n{error}')

        if result.returncode == 0:
            return '100'
        else:
            return '0'
    except subprocess.TimeoutExpired:
        return 'Timeout'
    except Exception as e:
        return f'Error: {str(e)}'


def log_results(results, collection):
    for device, status in results.items():
        document = {
            'device': device,
            'status': status,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Milliseconds
        }
        collection.insert_one(document)


def main():
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]

    while True:
        results = {}
        for device in devices:
            status = ping_device(device)
            results[device] = status
        log_results(results, collection)
        time.sleep(60)


if __name__ == '__main__':
    main()
