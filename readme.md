# Opis

## Server

- Server je razvijen u Python 3 koristeći Flask i omogućuje HTTP streaming MP3 datoteka.
- Sever također ima "text to speech" funkcionalnost

## Klijenti
- U projektu su 2 klijentske aplikaicje:
  - `audio-client.py` - preslušavanje audio snimki HTTP vezom
  - `tts-client.py` - text to speech klijent u kojem se unosi tekst koji kasnije sprema mp3 datoteku u `/music` mapu

# Detalji

- Server se može pokrenuti samostalno ili putem Docker kontejnera.
- Klijentske aplikacije se ne pokreću se iz Dockera, već direktno na host uređaju.
- Server otvara port 5000 za pristup MP3 streamingu i konverziji teksta u audio.

# Primjer korištenja

- Preslušavanje audio datoteke:

```
http://localhost:5000/stream?file=audio.mp3
```

- Konverzija teksta u audio datoteku:

| Element         | Vrijednost |
|:----------------|:-----------|
| URL             | `http://localhost:5000/generate` |
| Metoda          | `POST` |
| Content-Type    | `application/json` |
| Tijelo zahtjeva | `{ "text": "nekakav tekst", "lang": "hr", "filename": "ime_datoteke" }` |

# Docker

- Docker kontejner pokreće samo server.
- MP3 datoteke se spremaju i čitaju iz lokalne mape `/music`.
- Klijenti se mogu pokrenuti lokalno ili koristiti web preglednik za pristup serveru.

## Docker - Pokretanje projekta

Za pokretanje servera putem Dockera iz glavne mape projekta:

```
docker compose up
```

# Extra

- Upravljanje Docker kontejnerima moguće je putem grafičkog sučelja koristeći Portainer.
- Portainer je poseban kontejner koji omogućava jednostavno upravljanje putem web preglednika.
- Preduvjet za korištenje Portainera: Docker mora biti instaliran na uređaju.

# Instalacija Portainera (Ubuntu)

Pokreni sljedeću naredbu za instalaciju Portainera:

```
sudo docker run -d \
  -p 9000:9000 \
  --name portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce
```

# Docker - Portainer komande

- Pokretanje Portainer kontejnera:

```
docker compose -f portainer-compose.yml up -d
```

- Pristup Portainer GUI:

```
http://localhost:9000
```

- Primjer korisničkog imena i lozinke:
  - Username: `admin`
  - Password: `adminadmin12`

# Kratki sažetak

| Komponenta | Tehnologija |
|:--|:--|
| Server | Python3 + Flask |
| TTS | Python3 + gTTS |
| Klijent | Tkinter + Pygame |
| Docker | Docker Compose za server |
| GUI upravljanje | Portainer |
