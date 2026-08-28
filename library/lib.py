from pathlib import Path

path = Path("data") / "jmaro_library.json"
print(path)
print(type(path))



from pathlib import Path

path = Path("data") / "jmaro_library.json"

print(path.name)
print(path.suffix)
print(path.exists())
print(path.parent)