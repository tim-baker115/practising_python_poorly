logs = [
    "INFO api Request completed",
    "ERROR api Database connection failed",
    "INFO worker Job started",
    "ERROR api Database connection failed",
    "WARNING api Slow response",
    "INFO worker Job completed",
    "ERROR worker Job failed",
    "ERROR api Database connection failed",
    "INFO api Request completed",
]

def analyse_logs(logs):
    result = {}
    errors = {}
    result["levels"] = {}
    result["most_common_error"] = {}
    result["errors_by_service"] = {}
    result["error_rate"] = {}
    error_counter = 0
    for log in logs:
        level=log.split()[0]
        service=log.split()[1]
        message=log.split()[2:]
        message_joined=" ".join(message)
        if level not in result["levels"]:
            result["levels"][level] = 1
        else:
            result["levels"][level] += 1
        if level.lower() == "error":
            error_counter += 1
            percentage = round(error_counter/len(logs)*100,3)
            result["error_rate"] = percentage
            if service not in result["errors_by_service"]:
                result["errors_by_service"][service] = 1
            else:
                result["errors_by_service"][service] += 1
            if message_joined not in errors:
                errors[message_joined] = 1
            else:
                errors[message_joined] += 1
        counter = 0
        highest_error = ""
        for error in errors:
            if errors[error] > counter:
                counter = errors[error]
                #highest_error = error
                result["most_common_error"] = error
    return result
print(analyse_logs(logs))