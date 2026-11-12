# Python Data Structures Practice — Homework Solutions

Organized solutions matching the **four pages** of the provided homework PDF.

## File organization

```text
Python_Data_Structures_Homework/
├── README.md              # How to use these solutions
├── 01_list.py             # Page 1: List (Tasks 1–6, 8–9)
├── 02_tuple.py            # Page 2: Tuple (Tasks 1–3)
├── 03_set.py              # Page 3: Set (Tasks 1–5)
├── 04_dictionary.py       # Page 4: Dictionary (Tasks 1–8)
├── all_solutions.py       # All sections in one runnable script
└── example_output.txt     # Expected output of all_solutions.py
```

**Note:** Page 1 of the original worksheet jumps from Task 6 to Task 8. Task 7 is not included; its number is not invented here.

## Run all homework

Open a terminal inside this folder and run:

```bash
python all_solutions.py
```

Use `python3` instead of `python` if needed.

## Run individual sections

```bash
python 01_list.py
python 02_tuple.py
python 03_set.py
python 04_dictionary.py
```

## Quick concepts

| Section | Key topics |
| --- | --- |
| List | indexing, `append()`, `insert()`, `remove()`, `pop()`, `copy()`, `sort()` |
| Tuple | indexing, `count()`, `index()`, tuple-to-list conversion |
| Set | difference (`-`), intersection (`&`), symmetric difference (`^`), union (`|`) |
| Dictionary | `get()`, `update()`, `items()`, `pop()`, `setdefault()`, `values()`, `copy()`, `clear()` |

## Notes

- The four standalone scripts each run on their own.
- `all_solutions.py` is intended for convenient full-homework submission.
- In the Set section, `sorted()` formats the output consistently but does not turn the original sets into lists.
- The Dictionary exercise uses example products and stock numbers as allowed by the worksheet.
- There are no third-party dependencies.
