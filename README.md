# ScornGriefHash
***USE AT YOUR OWN RISK*** 
ScornGriefHash is a Python script designed for forensic analysis, specifically targeting extension mismatches within files. It overwrites all file names in a directory with their MD5 hash values and changes the file extensions to .md5. This tool aids in verifying the effectiveness of forensic tools in detecting extension mismatches and ensures file integrity during analysis.

Features
Extension Mismatch Generator: ScornGriefHash replaces original file names with their MD5 hash values and changes file extensions to .md5, creating extension mismatches for forensic analysis.
MD5 Hash Calculation: The script calculates the MD5 hash of each file to generate a unique identifier based on its contents.
File Renaming: ScornGriefHash systematically renames all files in the specified directory, ensuring uniformity in the naming convention.
Progress Tracking: With the integration of the tqdm library, ScornGriefHash provides real-time progress updates, enhancing transparency and control during the renaming process.

Usage
Ensure you have Python installed on your system.
Copy the ScornGriefHash script to the directory containing the files you want to analyze for extension mismatches.
Open a terminal or command prompt and navigate to the directory containing ScornGriefHash.
Run ScornGriefHash using the following command:
python ScornGriefHash.py

ScornGriefHash will calculate the MD5 hash of each file and rename them accordingly, changing the extensions to .md5.
The script will display progress updates, indicating the number of files renamed and any skipped files.
Once the process completes, all files in the directory will have been renamed with their MD5 hashes and extensions changed to .md5.

Disclaimer
ScornGriefHash is intended for use in forensic analysis and should be employed with caution. It overwrites file names and changes extensions, which may impact the usability of the files. Use this tool at your own risk, and ensure that you have appropriate backups of your data before execution.

Note: Renaming files with MD5 hashes and changing extensions to .md5 may affect file associations and compatibility with certain applications. Exercise caution and verify the integrity of the renamed files as needed.

/VooDooFus/
