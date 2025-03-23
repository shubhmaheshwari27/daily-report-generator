# Daily Report Generator

This project is a tool that simulates **regular contributions** to GitHub by automatically generating and committing updates every few minutes (or based on your desired schedule). The application generates a report file (`report.txt`) with the current timestamp and pushes it to your GitHub repository, making it appear as though you're consistently contributing to the project.

## How It Works:

1. The **GitHub Actions workflow** automatically runs every few minutes (or based on your specified schedule).
2. The script generates a report with the current timestamp and appends it to the `report.txt` file.
3. The report is then committed and pushed to the repository, mimicking ongoing contributions to your project.

## Features:

- Regularly updates a report file with the current timestamp.
- Automatically commits and pushes changes to the repository.
- Configurable schedule for the frequency of updates (e.g., every 5 minutes, 6 hours, etc.).

---

## **Prerequisites**

Before setting up the project, ensure you have the following:

- **GitHub account**: To clone the repository and use GitHub Actions.
- **Python**: Required to run the report generation script locally (optional for testing).

---

## **Steps to Clone and Set Up**

### **1. Clone the Repository:**

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/repository-name.git


## **Changes in auto-contribution.yml file**

Change user.email and user.name
```
