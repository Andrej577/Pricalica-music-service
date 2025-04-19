from flask import Flask, request, Response, abort, send_file, send_from_directory, jsonify
import os
import mimetypes
import re
from gtts import gTTS

app = Flask(__name__)

app = Flask(__name__)
MUSIC_FOLDER = "music"
os.makedirs(MUSIC_FOLDER, exist_ok=True)

@app.route('/stream')
def stream_audio():
    file_name = request.args.get('file')
    if not file_name:
        return abort(400, description="Missing 'file' query parameter.")

    file_path = os.path.join(MUSIC_FOLDER, file_name)

    if not os.path.isfile(file_path):
        return abort(404, description="File not found.")

    # DEFAULTNO CHUNK SIZE ODREDJUJE KLIJENT - BROWSER 
    # MOZE SE DODAT PARAMETAR KOJI CE BITI CHUNK ALI TO JE TODO
    # PAMETNI ADAPTIVE RANGE ZAHTJEVI (PO KVALITETI VEZE)

    # range daje samo dio podataka 
    range_header = request.headers.get('Range', None)
    if not range_header:
        # Ako nema Range zahtjeva, pošalji cjeli fajl
        return send_file(file_path, mimetype='audio/mpeg')

    #velicina datoteke
    size = os.path.getsize(file_path)

    # byte1 - pocetna vrijednost je 0 bajtova
    # byte2 - ovje je None jer ne znamo koji je iznos u bytovima kraj datoteke
    byte1, byte2 = 0, None

    # regex search koji trazi prema pocetnom i krajnjem baytu iz range_headera
    # \d+ 1 ili vise brojeva - \d* nula ili vise brojeva
    m = re.search(r'bytes=(\d+)-(\d*)', range_header)
    #ako je regex nasao
    if m:
        # ovo ce napraviti tuple
        g = m.groups()
        byte1 = int(g[0])
        if g[1]:
            byte2 = int(g[1])

    #koliko cemo bytova poslati kao chunk
    # KRAJ - POCETAK + 1 = UKUPNA DUZINA
    # size -1 jer su bajtovi indeksirani od nule
    # Dodajemo 1 jer su bajtovi indeksirani od nule, pa kada kazamo od 5 do 7, to su zapravo 3 bajta (5, 6, 7).
    length = (byte2 if byte2 is not None else size - 1) - byte1 + 1

    #otvori file i nadji checkpoint i procitaj duzinu
    with open(file_path, 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    #206 Partial Content
    response = Response(data, 206, mimetype='audio/mpeg')
    response.headers.add('Content-Range', f'bytes {byte1}-{byte1 + length - 1}/{size}')
    response.headers.add('Accept-Ranges', 'bytes')
    response.headers.add('Content-Length', str(length))

    return response

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    text = data.get("text")
    lang = data.get("lang", "hr")
    filename = data.get("filename", "output")

    if not text:
        return jsonify({"error": "Text je obavezan."}), 400

    if not filename.endswith('.mp3'):
        filename += '.mp3'

    filepath = os.path.join(MUSIC_FOLDER, filename)

    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filepath)
        return jsonify({"message": "Uspješno kreirano.", "filename": filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
