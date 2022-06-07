import pgeocode

nomi = pgeocode.Nominatim('tr')
print(nomi.query_postal_code("35090"))

