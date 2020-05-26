import datetime
import logging
import socket
import tarfile
import threading
import time
import random

CHANNELS = 1
CHUNK = 16384
RATE = 44100
RECORD_SECONDS = 10

queueUrl = 'https://sqs.eu-west-1.amazonaws.com/443793523615/recorders-events.fifo'
bucketName = "clanz-rasp-uploads-goldencare"
deviceName = 'rasp-20'


def send_message(msg_body):
    print_with_ts("sent message " + msg_body)


def compress_file(key):
    try:
        print_with_ts("compressing file " + key)
        compressed_file_name = key + '.ogg'
        convert_format(key, compressed_file_name)
        print_with_ts("converted to " + compressed_file_name)
        clean_up(key)
        print_with_ts("deleted " + key)
        compress_file_gz(compressed_file_name)
        clean_up(compressed_file_name)
        print_with_ts('deleted ' + compressed_file_name)
        return compressed_file_name + ".gz"
    except Exception as e:
        print_with_ts(str(e))
    return None


def compress_file_gz(file_name):
    print_with_ts("converted to " + file_name)
    tf = tarfile.open(file_name + ".gz", mode="w:gz")
    tf.add(file_name)
    tf.close()
    print_with_ts("compressed gz " + file_name)


def clean_up(key):
    print_with_ts("finised cleaning up " + key)


def recording(key):
    frames = []
    print_with_ts("* recording " + key)
    print_with_ts("* done recording " + key)
    return frames


def save_file(frames, key):
    print_with_ts("finished saving file " + key)


# from: https://stackoverflow.com/a/28950776/1824521
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def upload_to_cloud(frames_input, file_name):
    save_file(frames_input, file_name)
    try:
        compressed_file = compress_file(file_name)
        if compressed_file:
            print_with_ts("finished uploading " + compressed_file)
            try:
                clean_up(compressed_file)
            except Exception as err:
                print_with_ts("failed cleaning up " + str(err))
        else:
            print_with_ts('compressed file is None')
    except Exception as err0:
        print_with_ts("failed compressing and uploading file " + str(err0))


def print_with_ts(msg):
    print(msg)
    logging.info(msg=str(datetime.datetime.now()) + "-" + msg)


def convert_format(from_file, to_format):
    print_with_ts('converting finished to ' + to_format)


def clean_file_system():
    print_with_ts('finished cleaned')


if __name__ == "__main__":
    print_with_ts("start program")
    ip = get_ip()
    while True:
        try:
            sending_msg_t = threading.Thread(target=send_message, args=("clanz-" + deviceName + " : " + ip,))

            sending_msg_t.start()

            key = '%s-%s.wav' % (time.strftime("%Y%m%d-%H%M%S"), deviceName)
            frames = recording(key)

            upload_t = threading.Thread(target=upload_to_cloud, args=(frames, key))
            upload_t.start()

            if random.randint(0, 10) >= 9:
                clean_t = threading.Thread(target=clean_file_system)
                clean_t.start()
        except Exception as e:
            print_with_ts("failes " + str(e))

    p.terminate()
