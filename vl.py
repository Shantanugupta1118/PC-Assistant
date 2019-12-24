from datetime import date
from sound import Sound
'''volume = query.lstrip("set volume to")
volume = volume.rstrip("%")'''
volume = int(input("Volume (0 - 100): "))
volume=int(volume)
Sound.volume_set(volume)