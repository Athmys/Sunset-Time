from datetime import date
from astral.sun import sun
from astral import LocationInfo

loc = LocationInfo(name='Paris', region='France', timezone='Europe/Paris', latitude=48.95045378769008, longitude=2.412083338272577)

s = sun(loc.observer, date=date.today(), tzinfo=loc.timezone)

print((
    f'             Aube:  {s["dawn"]}\n'
    f'  Lever du Soleil:  {s["sunrise"]}\n'
    f'             Midi:  {s["noon"]}\n'
    f'Coucher du Soleil:  {s["sunset"]}\n'
    f'       Crépuscule:  {s["dusk"]}\n'
))