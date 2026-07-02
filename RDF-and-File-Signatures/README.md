# JPEG File Carving from a Raw Disk Image

## Lab Overview

This project was completed as part of the **Raw Disk Forensics and File Signatures** lab.

In this lab, the objective was to automate the recovery of deleted JPEG files from a raw forensic disk image. Instead of manually locating the beginning and end of each image, the script automatically searches for JPEG file signatures, extracts each image, and saves it as a separate file.

This lab demonstrates how Python can be used to automate repetitive digital forensic tasks while reinforcing concepts such as file signatures, binary file handling, and file carving.

---

# Scenario

As a **Junior Digital Forensic Analyst** at **Sentinel Security Solutions**, the task is to recover deleted JPEG images from a suspect's hard drive.

Investigators suspect that multiple JPEG files still exist within the raw disk image, even though they are no longer accessible through the file system.

Rather than manually finding each file using a hex editor, this script automates the recovery process by locating JPEG headers and footers and extracting each image automatically.

---

# Objectives

The script performs the following tasks:

- Searches a raw disk image for JPEG file headers.
- Searches for matching JPEG footers.
- Automatically extracts every recovered JPEG.
- Saves each recovered image into its own file.
- Displays the offsets where each JPEG was found.
- Creates the output folder automatically if it does not already exist.

Although the lab also discusses validating recovered files with **md5sum** and viewing them with **GIMP**, those steps are performed after running this script and are not automated here.

---

# Tools Used

- Python 3
- Raw forensic disk image (`M2_lab.dd`)
- Hex Editor
- Foremost
- Binwalk
- md5sum
- GIMP

---

# Project Structure

```
project/
│
├── carve_jpg.py
├── README.md
├── M2_lab.dd
└── M2_Lab_recovered_files/
    ├── recovered_0.jpg
    ├── recovered_1.jpg
    └── ...
```

---

# Running the Script

Ensure the forensic image is in the same directory as the script.

Run:

```bash
python3 carve_jpg.py
```

Recovered images will be saved inside:

```
M2_Lab_recovered_files/
```

---

# How the Script Works

## 1. Importing the OS Module

```python
import os
```

The `os` module is used to interact with the operating system. It creates the output directory and builds file paths that work across different operating systems.

---

## 2. Finding JPEG Signatures

```python
def find_signatures(image_path, signature):
```

This function searches the raw disk image for a specific byte signature.

It:

1. Opens the forensic image in binary mode.
2. Reads the entire image.
3. Searches every byte for the specified signature.
4. Returns a list containing every matching offset.

This function is used twice:

- once to find JPEG headers
- once to find JPEG footers

---

## 3. Extracting JPEG Files

```python
def extract_files(image_path, offsets, output_folder):
```

This function performs the file carving process.

For every JPEG header found:

1. Finds the next footer occurring after it.
2. Reads all bytes between the header and footer.
3. Creates a unique filename.
4. Saves the recovered JPEG into the output folder.

If a matching footer cannot be found, the script skips that file to avoid recovering incomplete or corrupted data.

---

## 4. Main Function

```python
def main():
```

The `main()` function coordinates the entire recovery process.

It:

- Specifies the disk image
- Defines the output folder
- Defines the JPEG header and footer signatures
- Searches for signatures
- Displays recovery information
- Calls the extraction function

---

## 5. Program Entry Point

```python
if __name__ == "__main__":
    main()
```

This ensures the script only executes when run directly, not when imported into another Python module.

---

# JPEG File Signatures

The script identifies JPEG images using their hexadecimal signatures.

### JPEG Header

```python
FF D8 FF
```

Represented in Python as:

```python
b"\xFF\xD8\xFF"
```

This marks the beginning of a JPEG file.

### JPEG Footer

```python
FF D9
```

Represented as:

```python
b"\xFF\xD9"
```

This marks the end of a JPEG file.

By locating these signatures, the script can recover deleted images even when file system metadata is missing.

---

# Sample Output

```
JPEG File Offsets Found:
Headers found: 3
Footers found: 3

File 0: Start Offset (Dec): 20480, Hex: 0x5000
File 1: Start Offset (Dec): 81920, Hex: 0x14000

Extracted File 0:
M2_Lab_recovered_files/recovered_0.jpg (24576 bytes)

Extracted File 1:
M2_Lab_recovered_files/recovered_1.jpg (18432 bytes)
```

---

# File Verification

After recovery, the extracted images can be verified using additional forensic tools.

## Verify integrity

Generate MD5 hashes:

```bash
md5sum M2_Lab_recovered_files/*.jpg
```

Comparing hashes helps confirm that files were recovered consistently and without unintended modification.

## Inspect recovered images

Open the recovered files in **GIMP** to verify that they display correctly and are not corrupted or incomplete.

---

# Learning Outcomes

This project demonstrates how to:

- Automate forensic file carving with Python.
- Work with binary files.
- Search for file signatures.
- Extract files using byte offsets.
- Organize code into reusable functions.
- Apply digital forensics concepts to recover deleted data.
- Validate recovered files using cryptographic hashes.
- Inspect recovered evidence using forensic tools.

---

# Conclusion

This project demonstrates a practical application of Python in digital forensics by automating the recovery of JPEG files from a raw disk image. Automating the file carving process reduces manual effort, improves consistency, and illustrates how scripting can support forensic investigations involving deleted or inaccessible files.

---

# License

This lab was provided by Moringa School.