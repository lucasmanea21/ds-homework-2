# Tema 2 - Structuri de Date

> - Manea Lucas - 151
> - Popescu-Ilioniu Andrei - 151

## Obiectiv:

Implementarea a doua structuri eficiente pentru operatiile standard de mulțimi ordonate:

- Inserare (`insert`)
- Stergere (`delete`)
- Căutare (`search`)
- Predecesor (`floor`)
- Succesor (`ceil`)
- Interogare pe interval (`range_query`)

## Structurile implementate:

- `SplayTree`
- `SkipList`

## Structură fișiere

```
├── generator.py 
├── test.py
├── structures/
│ ├── skip_list.py
│ └── splay_tree.py
├── tests/ # Teste generate automat
└── README.md
```

## Testare si generare fisiere

Pentru a valida corectitudinea si performanta structurilor, am generat automat fisiere de test in folderul `tests/` folosind scriptul `generator.py`.

### Rulare generator

```bash
python3 generator.py
```

Aceasta comanda va crea urmatoarele fisiere in directorul tests/:

- `sorted_insertions.in`: inserari in ordine strict crescatoare

- `random_ops.in`: amestec de operatii randomizate (inserari, stergeri, cautari, etc.)

- `repeated_insert_delete.in`: secventa alternanta de inserare/sterge pe aceeasi valoare

- `sparse_insertions.in`: inserari rare (cu distante mari intre valori)

- `heavy_range_queries.in`: multe interogari range_query pe intervale mari

- `dense_range_queries.in`: multe range_query pe intervale mici

- `search_misses.in`: cautari esuate (valori care nu se gasesc in structura)


## Format fisiere .in

Fiecare fisier de test contine:

Prima linie: un numar N — numarul de operatii

Urmatoarele N linii: operatiile propriu-zise sub forma:

- `1 x` — insert(x)

- `2 x` — delete(x)

- `3 x` — search(x)

- `4 x` — floor(x)

- `5 x` — ceil(x)

- `6 x y` — range_query(x, y)

## Rulare benchmark

Dupa generarea testelor, ele pot fi rulate cu:
```bash
python3 test.py
```

## Concluzii

Proiectul demonstreaza functionalitatea si performanta a doua structuri fundamentale folosite in problemele de tip multime ordonata. S-au respectat toate cerintele incluse in problema abce de pe Infoarena.

Am testat pe volume mari de date pentru a evidentia cazuri favorabile si scenarii critice de performanta.


## Link catre prezentare

https://1drv.ms/p/c/e944afeb83164c67/EWZnHVOQumhGmhX4RwDKgmwB-hRChbS_I6kmyBnECZqNBQ?e=ztzwXU
