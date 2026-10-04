import time
import csv
import os
import threading

def follow(file):
    file.seek(0, 2)  # Move to the end of the file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)  # Wait briefly before trying again
            continue
        yield line

def process_data(line, csv_writer_current, csv_writer_all, current_csv_file, data_list, num_analog, num_digital):
    try:
        data = line.strip().split('\t')  # Adjust the delimiter if necessary

        # Ensure the line has the correct number of elements
        if len(data) == num_analog + num_digital:
            # Convert data to floats
            analog_values = [float(data[i]) for i in range(num_analog)]
            digital_raw_values = [float(data[i + num_analog]) for i in range(num_digital)]

            # Convert digital data: 0 -> 0, 1 -> 5
            digital_values = [0 if val == 0 else 5 for val in digital_raw_values]

            # Append data to list for plotting
            data_list.append((analog_values, digital_values))
            if len(data_list) > 100:  # Keep only the last 100 data points
                data_list.pop(0)

            # Write the data to the current CSV file (overwritten every 3KB)
            csv_writer_current.writerow(analog_values + digital_values)
            current_csv_file.flush()  # Ensure data is written immediately

            # Write the data to the sensor_data CSV file (appended continuously)
            csv_writer_all.writerow(analog_values + digital_values)

            # Print the original line as it appears in the LVM file
            print(line.strip())

        else:
            print(f"Unexpected line format: {line}")

    except (IndexError, ValueError) as e:
        print(f"Error processing line: {line}. Error: {e}")

def get_file_size(file_path):
    return os.path.getsize(file_path)

def main():
    lvm_file_path = "Sensor_Data_acquistion.lvm"
    current_csv_file_path = "current_data.csv"
    all_csv_file_path = "sensor_data.csv"

    # Define the number of analog and digital sensors
    num_analog = 6
    num_digital = 6

    # Open the CSV file to store all data
    with open(all_csv_file_path, mode='a', newline='') as csv_file_all:
        csv_writer_all = csv.writer(csv_file_all)

        # Open the CSV file to store current data (will be overwritten)
        data_list = []  # List to store data for plotting

        with open(current_csv_file_path, mode='w', newline='') as current_csv_file:
            csv_writer_current = csv.writer(current_csv_file)

            with open(lvm_file_path, "r") as lvm_file:
                log_lines = follow(lvm_file)
                last_file_size = get_file_size(lvm_file_path)
                file_size_threshold = 3 * 1024  # 3KB

                for line in log_lines:
                    process_data(line, csv_writer_current, csv_writer_all, current_csv_file, data_list, num_analog, num_digital)

                    # Check the file size and overwrite if needed
                    current_file_size = get_file_size(lvm_file_path)
                    if current_file_size // file_size_threshold > last_file_size // file_size_threshold:
                        # Incrementally checking the file size for each 3KB increase
                        print(f"File size reached {file_size_threshold * (current_file_size // file_size_threshold)} bytes. Overwriting file.")

                        # Close the current CSV file and open it again to overwrite
                        current_csv_file.close()
                        current_csv_file = open(current_csv_file_path, mode='w', newline='')
                        csv_writer_current = csv.writer(current_csv_file)
                        current_csv_file.flush()
                        print(f"Data written to {current_csv_file_path}")

                        last_file_size = current_file_size

if __name__ == "__main__":
    main()
