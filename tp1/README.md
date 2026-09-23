# INFO731 : TP 1, modes opératoires de chiffrement par blocs et RSA

Sujet : [`sujet.pdf`](sujet.pdf)

| Partie | Questions | Dossier |
|---|---|---|
| 1. Chiffrement par blocs (AES) | Q1 à Q5 | [`partie1_aes/`](partie1_aes/) |
| 2. Chiffrement asymétrique (RSA) | Q6 à Q8 | [`partie2_rsa/`](partie2_rsa/) |

Les réponses rédigées sont dans le `README.md` de chaque dossier.

## Lancer les scripts

```bash
python3 -m venv ../.venv
../.venv/bin/pip install -r requirements.txt

cd partie1_aes
../../.venv/bin/python q1_q2_images.py        # écrit tux_ecb.ppm et tux_cbc.ppm
../../.venv/bin/python q3_ecb_cpa.py
../../.venv/bin/python q4_cbc_iv_predictible.py

cd ../partie2_rsa
../../.venv/bin/python q6_signature.py
../../.venv/bin/python q7_espace_reduit.py
```
