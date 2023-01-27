import requests
from rx import from_, operators

from printer import Printer

params = {
    'apikey': '4d5b0373',
    's': input('Película a buscar')
}

content = requests.get(f'http://www.omdbapi.com/', params=params)

data = content.json()
from_(data['Search']).pipe(
    operators.filter(lambda t: t['Type'] == 'movie'),
    operators.map(lambda t: f'({t["imdbID"][2:]}) - {t["Title"]}: {t["Poster"]} ({t["Year"]})')
).subscribe(Printer())
