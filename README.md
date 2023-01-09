# Basics (Main)

Files I use as templates or re-use in multiple projects or directories

## Directory Structure

```
.
├── README.md           # This file
├── python              # Python helper files
│   ├── README.md
│   ├── base.py
│   ├── data.py
│   └── setup.py
└── shell               # Shell helper files
    ├── README.md
    └── env.sh          # Conda environment setup guide
```

---

## Various Clean Up Commands

### Merge Files Only

```bash
git checkout branch_name -- folder/file

# Example
git checkout branch_name -- python/__init__.py
git checkout branch_name -- python/base.py
git checkout branch_name -- python/data.py
git checkout branch_name -- python/setup.py
git checkout branch_name -- shell/env.sh
```

### Remove Git Files

```bash
rm -rf .git
rm .gitignore
```

### Remove README Files

```bash
find . -name "README.md" -delete
```