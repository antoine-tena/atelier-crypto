import pywasm
import wasi


def sha256(v):
    wasimod = wasi.Wasi(['sha-export.wasm'])
    runtime = pywasm.load('sha-export.wasm', {'wasi_snapshot_preview1': wasimod.imports()})
    mem = runtime.store.memory_list[0].data

    # On reserve de la memoire DANS le bac a sable wasm pour l'entree et la sortie.
    src = runtime.exec('malloc', [len(v)])
    dst = runtime.exec('malloc', [32])

    # On copie l'entree dans la memoire wasm, on appelle SHA256(src, len, dst).
    mem[src:src + len(v)] = v
    runtime.exec('SHA256', [src, len(v), dst])

    # On relit les 32 octets du condensat depuis la memoire wasm.
    return bytes(mem[dst:dst + 32])
