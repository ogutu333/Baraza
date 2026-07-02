#!/usr/bin/env python3
import os

def find_signatures(image_path, signature):
    """Search for file headers or footers in the raw disk image."""
    with open(image_path, "rb") as f:
        data = f.read()
    return [i for i in range(len(data)) if data[i:i + len(signature)] == signature]

def extract_files(image_path, offsets, output_folder):
    """
    Extract multiple JPEG files from the forensic image.
    Complete this function so that each recovered JPEG is carved as its own
    bounded file and saved in the output folder with a unique name.
    """
    os.makedirs(output_folder, exist_ok=True)
    headers = offsets["headers"]
    footers = offsets["footers"]
    with open(image_path, "rb") as f:
        for i, start in enumerate(headers):
            end = None
            for footer in footers:
                if footer > start:
                    end = footer + 2
                    break
            if end is None:
                print(f"File {i}: No footer found, skipping.")
                continue
            f.seek(start)
            data = f.read(end - start)
            filename = os.path.join(output_folder, f"recovered_{i}.jpg")
            with open(filename, "wb") as out:
                out.write(data)
            print(f"Extracted File {i}: {filename} ({len(data)} bytes)")

def main():
    image_path = "M2_lab.dd"
    output_folder = "M2_Lab_recovered_files"
    jpg_header = b"\xFF\xD8\xFF"
    jpg_footer = b"\xFF\xD9"
    start_offsets = find_signatures(image_path, jpg_header)
    end_offsets = find_signatures(image_path, jpg_footer)
    if not start_offsets:
        print("No JPEG file headers found. File carving not possible.")
    else:
        print("\nJPEG File Offsets Found:")
        print(f"Headers found: {len(start_offsets)}")
        print(f"Footers found: {len(end_offsets)}")
        for i, start_offset in enumerate(start_offsets):
            print(
                f"File {i}: Start Offset (Dec): {start_offset}, "
                f"Hex: {hex(start_offset)}"
            )
        extract_files(
            image_path,
            {"headers": start_offsets, "footers": end_offsets},
            output_folder,
        )

if __name__ == "__main__":
    main()