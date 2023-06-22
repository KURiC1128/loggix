import datetime
from colorama import Fore, Style

SUCCESS = "SUCCESS"
ERROR = "ERROR"
INFO = "INFO"
WARNING = "WARNING"

def log(level, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    colored_timestamp = get_colored_timestamp()
    colored_level = get_colored_level(level)
    colored_message = get_colored_message(level, message)
    formatted_message = f"{colored_timestamp} | {colored_level} | {colored_message}"
    print(formatted_message)

def get_colored_timestamp():
    return f"{Fore.CYAN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}"

def get_colored_level(level):
    if level == SUCCESS:
        return f"{Fore.GREEN}{level}{Style.RESET_ALL}"
    elif level == ERROR:
        return f"{Fore.RED}{level}{Style.RESET_ALL}"
    elif level == INFO:
        return f"{Fore.BLUE}{level}{Style.RESET_ALL}"
    elif level == WARNING:
        return f"{Fore.YELLOW}{level}{Style.RESET_ALL}"
    else:
        return level

def get_colored_message(level, message):
    if level == SUCCESS:
        return f"{Fore.GREEN}{message}{Style.RESET_ALL}"
    elif level == ERROR:
        return f"{Fore.RED + Style.BRIGHT}{message}{Style.RESET_ALL}"
    elif level == INFO:
        return f"{Fore.BLUE}{message}{Style.RESET_ALL}"
    elif level == WARNING:
        return f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
    else:
        return message

def success(message):
    log(SUCCESS, message)

def error(message):
    log(ERROR, message)

def info(message):
    log(INFO, message)

def warning(message):
    log(WARNING, message)