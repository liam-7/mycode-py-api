from datetime import datetime

def epoch_to_human_readable(epoch_time):
    try:
        # Convert epoch time to datetime object
        datetime_obj = datetime.utcfromtimestamp(epoch_time)

        # Format the datetime object as a human-readable string
        readable_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S UTC')

        return readable_time
    except Exception as e:
        return f"Error: {e}"

# Example usage
epoch_time_input = int(input("Enter epoch time: "))
result = epoch_to_human_readable(epoch_time_input)
print(f"Human-readable time: {result}")
