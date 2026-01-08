import os
import glob

# Config
# Use relative path for portability or absolute if needed
PROJECT_ROOT = os.getcwd() 
EMOJI_DIR = os.path.join(PROJECT_ROOT, "openmoji-svg-color")
SEARCH_EXTENSIONS = ['.py', '.json', '.txt']
IGNORE_DIRS = ['build', 'openmoji-svg-color', '__pycache__', '.git', '.github', '.vscode']

def load_project_content():
    content = ""
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if any(file.endswith(ext) for ext in SEARCH_EXTENSIONS):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        file_content = f.read()
                        content += file_content
                except Exception as e:
                    print(f"Skipping {path}: {e}")
    return content

def hex_to_char(hex_str):
    # Handle filename parsing
    try:
        if '-' in hex_str:
            parts = hex_str.split('-')
            return "".join([chr(int(p, 16)) for p in parts])
        else:
            return chr(int(hex_str, 16))
    except:
        return None

def main():
    if not os.path.exists(EMOJI_DIR):
        print(f"Emoji directory not found: {EMOJI_DIR}")
        return

    print("Loading project content...")
    all_content = load_project_content()
    print(f"Loaded {len(all_content)} characters of code/data.")
    
    emoji_files = glob.glob(os.path.join(EMOJI_DIR, "*.svg"))
    print(f"Found {len(emoji_files)} emoji files.")
    
    kept = 0
    deleted = 0
    
    for file_path in emoji_files:
        filename = os.path.basename(file_path)
        hex_code = filename.replace('.svg', '')
        
        # 1. Check if the HEX string itself is in the code (e.g. if referenced by '1F600')
        if hex_code in all_content:
            kept += 1
            continue

        # 2. Check if the actual Emoji character is in the code
        emoji_char = hex_to_char(hex_code)
        
        # Special handling for FE0F (Variation Selector-16)
        # If the file is specifically for the variation, but code uses base char, we might miss it if logic isn't aligned.
        # But here we assume if the code has the emoji, we keep the file.
        
        found = False
        if emoji_char and emoji_char in all_content:
            found = True
        
        # Soft match for VS16: if file has NO FE0F, but code HAS FE0F, does 'in' work?
        # 'A' in 'A\uFE0F' -> True.
        # So if file is '26FA.svg' (⛺), valid emoji is ⛺. Code has ⛺\uFE0F. ⛺ is inside. Matched.
        
        # What if file is '26FA-FE0F.svg'? Valid emoji is ⛺\uFE0F. Code has ⛺.
        # '⛺\uFE0F' in '...⛺...' -> False.
        # So we might delete the variation file if the code only uses the base emoji.
        # But 'ui.py' loads base if variation not found. So deleting variation file is fine IF base exists.
        # However, checking if base exists is complex.
        # Let's handle the reverse:
        # If code has '⛺', we keep '26FA.svg'.
        # If code has '⛺', do we keep '26FA-FE0F.svg'?
        # optimize: if `emoji_char` (with FE0F) is not found, try stripping FE0F from `emoji_char` and search again?
        # No, if file IS the FE0F version, we only want to keep it if the code specifically requests/uses FE0F form 
        # OR if our UI loader logic would look for it.
        # UI logic: `filenames = [hex, hex_no_fe0f]`.
        # If code uses `⛺` (no FE0F), it generates `26FA`. It looks for `26FA.svg`.
        # It does NOT look for `26FA-FE0F.svg` (unless `hex` variable had FE0F, which it doesn't).
        # So if code has simple emoji, we only need simple file.
        
        if found:
            kept += 1
        else:
            os.remove(file_path)
            deleted += 1
                
    print(f"Optimization complete. Kept: {kept}, Deleted: {deleted}")

if __name__ == "__main__":
    main()
