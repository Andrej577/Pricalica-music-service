# Opis

## Server + Klijent

- Server je razvijen u Python 3 koristeći Flask i omogućuje HTTP streaming MP3 datoteka.
- Klijentska aplikacija je izrađena pomoću Tkinter (GUI) i Pygame (audio).

# Detalji

- Server se može pokrenuti samostalno ili putem Docker kontejnera.
- Klijentska aplikacija (`client.py`) ne pokreće se iz Dockera, već direktno na host uređaju.
- Server otvara port 5000 za pristup MP3 streamingu.

# Primjer korištenja

- Kada je server pokrenut u web pregledniku se može napraviti upit na slijedeći način:

```
http://localhost:5000/stream?file=gorila.mp3
```

# Docker

- Docker kontejner pokreće samo server.
- MP3 datoteke se spremaju u lokalnu mapu `/music`.
- Klijent (`client.py`) može se pokrenuti lokalno ili koristiti web preglednik za pristup serveru.

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
| Server | Python 3 + Flask |
| Klijent | Tkinter + Pygame |
| Docker | Docker Compose za server |
| GUI upravljanje | Portainer |
