import subprocess
import sys
import threading
import time
from queue import Queue, Empty

# Run 'ls -l' command (Unix/macOS) or 'dir /l' (Windows equivalent logic might differ)
# The command is a list of arguments: ['ls', '-l']
# result = subprocess.run(['ls', '-l'])
# print(f"Command exited with return code: {result.returncode}")

def enqueue_output(stream, queue):
    """Function to read line by line from a stream and put it in a queue."""
    for line in iter(stream.readline, b''):
        queue.put(line)
    stream.close()

# def write_to_subprocess(process, message):
#     """Function to write a message to the subprocess's stdin."""
#     # Ensure message ends with a newline and is encoded with bytes
#     process.stdin.write(f"{message.strip()}\n".encode('utf-8'))
#     process.stdin.flush()


def process_stdin_queue(process, stdin_queue):
    """Thread function to write messages from queue to subprocess stdin."""
    while True:
        try:
            message = stdin_queue.get()
            if message is None:
                break
            process.stdin.write(f"{message.strip()}\n".encode('utf-8'))
            process.stdin.flush()
        except Exception as e:
            print(f"Error writing to stdin: {e}", flush=True)
            break

def write_to_subprocess(stdin_queue, message):
    """Function to queue a message to write to subprocess's stdin."""
    stdin_queue.put(message)

# subprocess.run(['open', 'cell.py'])

# subprocess.run(['open', './', '-a', 'Visual Studio Code'])

command = ['/Applications/love.app/Contents/MacOS/love', './']
# command = subprocess.run(['open', '-n', '-a', 'love', './'])
# command = subprocess.run(['ping', '-c', '35', 'google.com'])

process = subprocess.Popen(
    command,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=False,
    bufsize=0
)

stdout_queue = Queue()
stderr_queue = Queue()
stdin_queue = Queue()

stdout_thread = threading.Thread(target=enqueue_output, args=(process.stdout, stdout_queue), daemon=True)
stderr_thread = threading.Thread(target=enqueue_output, args=(process.stderr, stderr_queue), daemon=True)
stdin_thread = threading.Thread(target=process_stdin_queue, args=(process, stdin_queue), daemon=True)
stdout_thread.start()
stderr_thread.start()
stdin_thread.start()

mytime = 0
cookies = 0

# Timing trackers
last_position_time = time.time()
last_get_time = time.time()
last_cookie_time = time.time()

try:
    # example interaction loop
    while True:
        current_time = time.time()
        
        # print("Beans", flush=True)
        # read from stdout (non blocking):
        try:
            line = stdout_queue.get_nowait().decode('utf-8').strip()
            if line:
                if type(line) == "list":
                    print("BEEEBBEE")
                elif "get_time" in str(line):
                    mytime = float(str(line).strip("get_time "))
                    # print(f"my time: {mytime}")
                else:
                    print(f"INPUT: {line}", flush=True)
        except Empty:
            pass

        try:
            line = stderr_queue.get_nowait().decode('utf-8').strip()
            if line:
                print(f"STDERR: {line}", flush=True)
        except Empty:
            pass
            
        # Send get_player_position every 2 seconds
        if current_time - last_position_time >= 2.0:
            command = "get_player_position"
            write_to_subprocess(stdin_queue, command)
            last_position_time = current_time
        
        # Send get_time every 0.15 seconds
        if current_time - last_get_time >= 0.15:
            command = "get_time"
            write_to_subprocess(stdin_queue, command)
            last_get_time = current_time

        # Update cookies every 1 second
        # print(current_time - last_cookie_time)
        if current_time - last_cookie_time >= 1.0:
            cookies += 1
            command = f"set_cookies{cookies}"
            write_to_subprocess(stdin_queue, command)
            last_cookie_time = current_time
        
        # Small sleep to prevent CPU spinning
        time.sleep(0.01)




except KeyboardInterrupt:
    return_code = process.wait()
    print(f"Process finisto with return code: {return_code}")
    process.terminate()
    process.wait()



# while True:
#     output = process.stdout.readline()
#     if output == '' and process.poll() is not None:
#         break
#     if output:
#         # print immediately to the console
#         sys.stdout.write(output)
#         sys.stdout.flush()

