# Partie 2 : chiffrement asymétrique RSA

| Question | Script | Réponse |
|---|---|---|
| Q6 | [`q6_signature.py`](q6_signature.py) | [ci-dessous](#q6--vérification-de-signature-rsa) |
| Q7 | [`q7_espace_reduit.py`](q7_espace_reduit.py) | [ci-dessous](#q7--attaque-par-espace-de-messages-réduit) |
| Q8 | — | [ci-dessous](#q8--sécurisation-par-pkcs-1-v15) |

[`tools.py`](tools.py) fournit les utilitaires du TP (`text_to_int`, `int_to_text`, `find_root`,
`combine_moduli`), portés en Python 3.

## Q6 : vérification de signature RSA

- On génère une clé, on l'exporte, puis on relit la clé publique avec `RSA.import_key`. On
  accède à ses composantes via `public_key.n` et `public_key.e`.
- On signe `SHA256(message)` avec la clé privée (PKCS#1 v1.5), puis on vérifie à la main :
  `v = pow(s, e, n)`.
- `v` s'écrit `00 01 FF … FF 00 ‖ DigestInfo(SHA-256) ‖ H`. Son suffixe est bien
  `SHA256.new(message).hexdigest()`. Le script le vérifie avec un `assert` :

```
s^e mod n       : 0001ffff…ff003031300d060960864801650304020105000420d5a602a7…ff8a9b2e
SHA256(message) :                                                 d5a602a7…ff8a9b2e
```

## Q7 : attaque par espace de messages réduit

Textbook RSA est déterministe : `c = m^e mod n`. Avec la clé publique `(n, e)`, n'importe qui
peut chiffrer chaque candidat de `part2_messagespace` et comparer le résultat à `part2_ctext`.

**Résultat : le message intercepté est « attack tomorrow at dawn ».**

## Q8 : sécurisation par PKCS #1 v1.5

Avant le chiffrement, on encode `EM = 00 ‖ 02 ‖ PS ‖ 00 ‖ M`, où `PS` fait au moins 8 octets
aléatoires non nuls, tirés à chaque chiffrement. Puis `c = EM^e mod n`.

- **Le chiffrement devient probabiliste** : un même message `M` donne un chiffré différent à
  chaque fois, car `PS` change.
- Pour refaire l'attaque de la Q7, l'attaquant devrait chiffrer chaque candidat avec le
  **même `PS`** que l'émetteur. Or il ne le connaît pas : il faudrait tester au moins
  `255^8 ≈ 2^64` bourrages par message, et bien plus en pratique, car `PS` remplit tout le
  module (≈ 200 octets aléatoires pour une clé de 2048 bits et un message court).
- Recalculer le chiffré d'un candidat ne donne donc (avec une probabilité écrasante) jamais
  le chiffré intercepté. La comparaison ne révèle plus rien, même avec seulement 3 messages
  possibles. Textbook RSA, lui, est déterministe et ne peut donc pas être CPA-sûr.
