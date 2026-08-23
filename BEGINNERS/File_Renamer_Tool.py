""" You better learn Some shit from this(⁠-⁠_⁠-)"""
import os

def get_files_in_directory(directory):
    """Return list of files in directory. Returns [] if dir not found."""
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        return []  # return [] instead of None so for loop doesn't break
        

def display_files(directory, files):
    """Display files in directory"""
    print(f"{'='*50}")
    print(f"FILES IN {directory}")
    print(f"{'='*50}")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    print(f"{'='*50}")

def rename_file(directory, old_name, new_name):
    """Rename a file"""
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    
    try:
        if os.path.exists(new_path):
            print(f"(⁠눈⁠‸⁠눈⁠) File {new_name} already exists!")
            return False
        
        os.rename(old_path, new_path)
        print(f"(⁠ ⁠╹⁠▽⁠╹⁠ ⁠) Renamed {old_name} to {new_name}")
        return True
    except Exception as e:
        print(f"(⁠눈⁠‸⁠눈⁠)  Error: {e}")
        return False

def batch_rename(directory, pattern, replacement):
    """Rename multiple files with pattern replacement"""
    files = get_files_in_directory(directory)
    if not files:
        return
    
    renamed_count = 0
    
    for file in files:
        if pattern in file:
            new_name = file.replace(pattern, replacement)
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            
            try:
                os.rename(old_path, new_path)
                print(f"(⁠ ⁠╹⁠▽⁠╹⁠ ⁠)  Renamed: {file} → {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"(⁠눈⁠‸⁠눈⁠) Error renaming {file}: {e}")
    
    print(f"Total renamed: {renamed_count} files")

def main():
    print("=" * 50)
    print("✧‎ ✧‎ ✧  FILE RENAMER TOOL‎‎‎✧‎ ✧ ✧")
    print("=" * 50)
    
    directory = input("‎Enter directory path (. for current): ").strip()
    if directory == ".":
        directory = os.getcwd()
    
    if not os.path.isdir(directory):
        print("(⁠눈⁠‸⁠눈⁠) Invalid directory!")
        return
    
    while True:
        files = get_files_in_directory(directory)
        
        if not files:
            print("No files found in this directory.")
            break
        
        print("♡ Options ♡⁠:")
        print("1. ✿ View files")
        print("2. ✿ Rename single file")
        print("3. ✿ Batch rename")
        print("4. ✿ Change directory")
        print("5. ✿ Exit")
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == "1":
            display_files(directory, files)
        
        elif choice == "2":
            display_files(directory, files)
            file_num = input("Enter file number to rename: ").strip()
            try:
                index = int(file_num) - 1
                if 0 <= index < len(files):
                    old_name = files[index]
                    new_name = input(f"Enter new name for {old_name} : ").strip()
                    rename_file(directory, old_name, new_name)
            except ValueError:
                print("Invalid number!")
        
        elif choice == "3":
            pattern = input("Enter pattern to find: ").strip()
            replacement = input("Enter replacement text: ").strip()
            batch_rename(directory, pattern, replacement)
        
        elif choice == "4":
            directory = input("Enter new directory path: ").strip()
            if not os.path.isdir(directory):
                print("(⁠눈⁠‸⁠눈⁠) Invalid directory!")
                directory = os.getcwd()
        
        elif choice == "5":
            print("Thank you for using File Renamer!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()