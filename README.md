# Basics

Files I use as templates or re-use in multiple projects or directories

## Directory Structure

```bash
.
├── README.md           # This file
├── python              # Python helper files & templates
│   ├── README.md       # Extra information
│   ├── base.py         # Template for any python code 
│   ├── data.py         # Misc common data classes (mostly aesthetic)
│   └── setup.py        # Automatic environment checking and setup logging
└── shell               # Shell helper files
    ├── README.md       # Extra information
    └── env.sh          # Conda environment setup guide
```

---

## Various Clean Up Commands

### Merge Files Only

```bash
git checkout branch_name -- folder/file

# Examples
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

### Remove a Git Submodule

1. Delete the relevant line from the `.gitmodules` file.
2. Delete the relevant section from `.git/config`.
3. Run `git rm --cached path_to_submodule` (no trailing slash).
4. Commit and delete the now untracked submodule files.

### Remove a Git Branch (Locally)

```bash
git branch -d branch_name
```

### Remove a Git Branch (Remotely)

```bash
git push origin --delete branch_name
```