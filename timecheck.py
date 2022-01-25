from datetime import datetime
import pytz


class timeFind:
    def timezone(self):
        locationZone = {
          "UTCP1": {
            "Albania": {"Tirana"},
            "Andorra": {"Andorra la Vella"},
            "Andorra": {"Andorra la Vella"},
            "Angola": {"Luanda"},
            "Austria": {"Vienna"},
            "Belgium": {"Brussels"},
            "Benin": {"Porto-Novo"},
            "Bosnia and Herzegovina": {"Sarajevo"},
            "CAR": {"Bangui"},
            "Cameroon": {"Yaoundé"},
            "Chad": {"N'Djamena"},
            "Congo": {"Brazzaville"},
            "Croatia": {"Zagreb"},
            "Czech Republic": {"Prague"},
            "DR Congo": {"Kinshasa"},
            "Denmark": {"Copenhagen"},
            "Equatorial Guinea": {"Malabo"},
            "France": {"Paris"},
            "Gabon": {"Libreville"},
            "Germany": {"Berlin"},
            "Gibraltar": {"Gibraltar"},
            "Hungary": {"Budapest"},
            "Italy": {"Rome"},
            "Kosovo": {"Pristina"},
            "Liechtenstein": {"Vaduz"},
            "Luxembourg": {"Luxembourg"},
            "Malta": {"Valletta"},
            "Monaco": {"Monaco"},
            "Montenegro": {"Podgorica"},
            "Netherlands": {"Amsterdam"},
            "Niger": {"Niamey"},
            "Nigeria": {"Abuja"},
            "North Macedonia": {"Skopje"},
            "Norway": {"Oslo"},
            "Poland": {"Warsaw"},
            "San Marino": {"City of San Marino"},
            "Slovakia": {"Bratislava"},
            "Slovenia": {"Ljubljana"},
            "Spain": {"Madrid"},
            "Sweden": {"Stockholm"},
            "Switzerland": {"Bern"},
            "Tunisia": {"Tunis"},
            "Vatican": {"Vatican City"},
            "Western Sahara": {"Laayoune"}
          }
        }
    def findTime(self):
        print("""be sure to replace spaces with underscores (ex: new_york)
""")
        country = input("""what country do you live in or do you live in europe
""")
        cityProvince = input(
            """what province/state do you live in or capital of your country if you live in europe
""")
        tz_WP = pytz.timezone(f'{country}/{cityProvince}')
        datetime_WP = datetime.now(tz_WP)
        print("Your time:", datetime_WP.strftime("%H:%M:%S"))


