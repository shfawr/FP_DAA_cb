## Struktur Folder (sesuai repo ini)

> Catatan: versi ini menyimpan file di root agar mudah dijalankan oleh TA.

```
FP-DAA-main/
├── main.py                 # demo game (pygame)
├── asset_load.py           # loader asset + fallback jika asset tidak ada
├── settings.py
├── movement.py
├── ghost_movements.py
├── renderer.py
├── game_state.py
├── home_screen.py
├── map.py
├── algorithms.py           # BFS + A*
├── maze_gen.py             # generator maze untuk benchmark
├── bench_config.py         # konfigurasi benchmark (headless)
├── benchmark.py            # jalankan benchmark -> results/benchmark.csv
├── plot_results.py         # plot -> results/plot.png
├── requirements.txt
└── results/                # auto-generated
```

## Cara Menjalankan

### 1) Install dependency

```bash
py -m pip install -r requirements.txt
```

### 2) Jalankan demo game

```bash
py -3.12 main.py
```

Jika folder `assets/` tidak ada, game tetap bisa jalan dengan **fallback** (tile berwarna).

### 3) Jalankan benchmark (BFS vs A*)

```bash
py -3.12 benchmark.py
```

Output: `results/benchmark.csv`

### 4) Buat plot hasil benchmark

```bash
py -3.12 plot_results.py
```

Output: `results/plot.png`
