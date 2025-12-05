# **Automated Email Report Generator**

A Python automation tool that fetches data, generates a PDF report using HTML templates, and emails it automatically on a schedule.

This project demonstrates automation, reporting, templating, PDF generation, and scheduled tasks.

---

## **Features**

* Fetch data from CSV or API
* Generate a styled HTML → PDF report using Jinja2
* Send the report as an email attachment via SMTP
* Run automatically using a scheduler (schedule library or cron)
* Configurable through **config.yaml**

---

## **Tech Stack**

* Python
* Pandas (data processing)
* Jinja2 (HTML templating)
* WeasyPrint (HTML → PDF conversion)
* smtplib / SMTP for email automation
* schedule / cron for periodic execution
* YAML for central configuration

---

## **Project Structure**

```
email-report-generator/
│── data/
│   └── sample_data.csv
│
│── templates/
│   └── report_template.html
│
│── reports/
│   └── (generated PDFs saved here)
│
│── config.yaml
│── fetcher.py
│── renderer.py
│── emailer.py
│── scheduler.py
│── main.py
│── requirements.txt
│── README.md
```

---

## **Installation**

1. Clone repository:

```
git clone https://github.com/yourusername/email-report-generator.git
cd email-report-generator
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Ensure WeasyPrint dependencies are installed:

**macOS:**

```
brew install weasyprint
```

**Linux:**

```
sudo apt install weasyprint
```

---

## **Configuration**

**Modify **config.yaml**:**

```
email:
  sender: "your@gmail.com"
  password: "your-app-password"
  recipient: "recipient@example.com"
  subject: "Automated Daily Report"

report:
  output_path: "reports/daily_report.pdf"

data:
  source_type: "csv"   # csv or api
  csv_path: "data/sample_data.csv"
  api_url: "https://api.example.com/sales"
```

### **Gmail Note**

Use an **App Password** (not your main password).

Guide: Google Account → Security → App Passwords.

---

## **Usage**

To generate report and email immediately:

```
python3 main.py
```

Expected output:

```
Report emailed successfully
```

---

## **Scheduling**

### **Option 1: Python schedule**

Run:

```
python3 scheduler.py
```

### **Option 2: Cron (recommended)**

Open cron editor:

```
crontab -e
```

Add:

```
0 9 * * * python3 /full/path/main.py
```

This emails report every day at 9 AM.

---

## **Template Customization**

Edit the HTML template:

```
templates/report_template.html
```
