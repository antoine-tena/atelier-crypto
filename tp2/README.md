# INFO731 : TP 2, isolation

| Problème | Sujet | Dossier |
|---|---|---|
| 1. Python n'isole rien | 4 attaques dans `attack.py` | [`probleme1_python/`](probleme1_python/) |
| 2. Bac à sable WebAssembly | 2 évasions + un hachage isolé | [`probleme2_wasm/`](probleme2_wasm/) |

## Problème 1 — Python (`probleme1_python/`)

`grader.py` tire un `secret` aléatoire et appelle `attack_one`…`attack_four` (dans
`attack.py`), qui doivent le retrouver. On ne modifie pas `grader.py`.

Chaque attaque exploite une chose différente que Python partage entre le code du
grader et le nôtre :

| Fonction | Ce qui est partagé | Attaque |
|---|---|---|
| `attack_one` | la fermeture `guess` capture `secret` | on lit `guess.__closure__[0].cell_contents` |
| `attack_two` | `secret` est une variable locale de l'appelant | on lit `sys._getframe(1).f_locals["secret"]` |
| `attack_three` | on est appelé **avant** `secret = os.urandom(256)` | on détourne `os.urandom` pour qu'il renvoie une valeur connue |
| `attack_four` | l'objet `SecretStore` survit (cycle `self.myself`, non collecté) | on le retrouve dans le tas via `gc.get_objects()` |

```bash
cd probleme1_python
python3 grader.py      # one/two/three/four : pass
```

## Problème 2 — WebAssembly (`probleme2_wasm/`)

Le module WASI (`wasi.py`) est censé confiner le shell (`tinysh.wasm`) dans un
répertoire. On lit `../secret.txt`, un cran au-dessus du bac à sable.

**Partie 1 (`solution-1.txt`) — lien symbolique.** `path_symlink` vérifie le
chemin du lien mais pas sa cible. On crée un lien pointant vers `../secret.txt`,
puis on le lit : c'est `os.open` qui suit le lien et sort du bac à sable.

**Partie 2 (`solution-2.txt`) — invariant de profondeur, sans `ln`.**
`OpenFile.depth` est figé à l'ouverture, alors que `mv` (rename) déplace le vrai
répertoire. On ouvre `a/b` (profondeur enregistrée 2), on le déplace à la racine
(profondeur réelle 1), puis on remonte en `..` : le décalage entre profondeur
enregistrée et réelle laisse remonter un cran de trop et sortir du bac à sable.

**Partie 3 (`sandbox.py`) — hachage isolé.** On appelle `SHA256` de
`sha-export.wasm` : `malloc` dans la mémoire wasm pour l'entrée et la sortie, on
copie les octets dans cette mémoire, on appelle la fonction, on relit les 32
octets du condensat.

```bash
cd probleme2_wasm
make grade            # escape-1 / escape-2 / sandbox : pass
```
