from fetcher import fetch_data
from renderer import render_report
from emailer import send_email

def main():
    data = fetch_data()
    pdf_path = render_report(data)
    send_email(pdf_path)
    print("Report emailed successfully")

if __name__ == "__main__":
    main()