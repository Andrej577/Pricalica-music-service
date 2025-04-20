import requests

def upload_pdf(file_path, server_url="http://localhost:5000/upload_pdf"):
    print("Upload u tijeku...")
    try:
        with open(file_path, 'rb') as f:
            files = {'pdf': f}
            response = requests.post(server_url, files=files)

        if response.status_code == 200:
            print("✅ Upload uspješan!")
            print("Server response:", response.json())
        else:
            print("⚠️ Greška pri uploadu!")
            print("Status code:", response.status_code)
            print("Server response:", response.json())

    except Exception as e:
        print("Greska:", str(e))

if __name__ == "__main__":
    # Ovdje uneseš putanju do svog PDF-a
    pdf_file_path = input("Unesi putanju do PDF fajla: ")
    upload_pdf(pdf_file_path)
