
version_code = "0.01b.2025_05_05"
version_name = "pre-alpha " + version_code
release_date = 'Monday, 5 May 2025'

def migrate_loaded_save(save: dict):
    
    _changed = False

    # 0.01b saves
    if "version" not in save or save["version"] is None:
        _changed = True
        save["version"] = "0.01b"
        print(" [!] Applied version to save")

    return _changed