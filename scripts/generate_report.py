import datetime

def generate_report():
    # Simulate generating a report by writing the current time to the report file
    with open('reports/report.txt', 'a') as f:
        f.write(f"Report generated on: {datetime.datetime.now()}\n")
    
    print("Report generated successfully!")

if __name__ == '__main__':
    generate_report()
