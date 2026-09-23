# INFO731 : TP 1, modes opératoires de chiffrement par blocs et RSA

Sujet : [`sujet.pdf`](sujet.pdf)

| Partie | Questions | Dossier |
|---|---|---|
| 1. Chiffrement par blocs (AES) | Q1 à Q5 | [`partie1_aes/`](partie1_aes/) |
| 2. Chiffrement asymétrique (RSA) | Q6 à Q8 | [`partie2_rsa/`](partie2_rsa/) |

Les réponses rédigées sont dans le `README.md` de chaque dossier.

## Lancer les scripts

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

.venv/bin/python partie1_aes/q1_q2_images.py        # écrit partie1_aes/resultats/*.ppm
.venv/bin/python partie1_aes/q3_ecb_cpa.py
.venv/bin/python partie1_aes/q4_cbc_iv_predictible.py
.venv/bin/python partie2_rsa/q6_signature.py
.venv/bin/python partie2_rsa/q7_espace_reduit.py
```
