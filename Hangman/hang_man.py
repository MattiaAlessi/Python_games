from termcolor import cprint, colored
from faker import Faker

languages = {
    "ar_AA": "العربية (العالم العربي)", "ar_AE": "العربية (الإمارات)", 
    "ar_BH": "العربية (البحرين)", "ar_DZ": "العربية (الجزائر)", "ar_EG": "العربية (مصر)", 
    "ar_JO": "العربية (الأردن)", "ar_PS": "العربية (فلسطين)", "ar_SA": "العربية (السعودية)",
    "az_AZ": "Azərbaycanca (Azərbaycan)", "bg_BG": "Български (България)", "bn_BD": "বাংলা (বাংলাদেশ)", 
    "bs_BA": "Bosanski (Bosna i Hercegovina)", "cs_CZ": "Čeština (Česká republika)", 
    "da_DK": "Dansk (Danmark)", "de": "Deutsch", "de_AT": "Deutsch (Österreich)",
    "de_CH": "Deutsch (Schweiz)", "de_DE": "Deutsch (Deutschland)", "de_LI": "Deutsch (Liechtenstein)", 
    "de_LU": "Deutsch (Luxemburg)", "dk_DK": "Dansk (Danmark)", "el_CY": "Ελληνικά (Κύπρος)", 
    "el_GR": "Ελληνικά (Ελλάδα)", "en": "English", "en_AU": "English (Australia)", 
    "en_BD": "English (Bangladesh)", "en_CA": "English (Canada)", "en_GB": "English (United Kingdom)", 
    "en_IE": "English (Ireland)", "en_IN": "English (India)", "en_KE": "English (Kenya)", 
    "en_MS": "English (Montserrat)", "en_NG": "English (Nigeria)", "en_NZ": "English (New Zealand)", 
    "en_PH": "English (Philippines)", "en_PK": "English (Pakistan)", "en_TH": "English (Thailand)", 
    "en_US": "English (United States)", "es": "Español", "es_AR": "Español (Argentina)",
    "es_CA": "Español (Canadá)", "es_CL": "Español (Chile)", "es_CO": "Español (Colombia)", 
    "es_ES": "Español (España)", "es_MX": "Español (México)", "et_EE": "Eesti (Eesti)", 
    "fa_IR": "فارسی (ایران)", "fi_FI": "Suomi (Suomi)", "fil_PH": "Filipino (Pilipinas)", 
    "fr_BE": "Français (Belgique)", "fr_CA": "Français (Canada)", "fr_CH": "Français (Suisse)", 
    "fr_DZ": "Français (Algérie)", "fr_FR": "Français (France)", "fr_QC": "Français (Québec)", 
    "ga_IE": "Gaeilge (Éire)", "gu_IN": "ગુજરાતી (ભારત)", "ha_NG": "Hausa (Nijeriya)", 
    "he_IL": "עברית (ישראל)", "hi_IN": "हिन्दी (भारत)", "hr_HR": "Hrvatski (Hrvatska)", 
    "hu_HU": "Magyar (Magyarország)", "hy_AM": "Հայերեն (Հայաստան)", "id_ID": "Bahasa Indonesia (Indonesia)",
    "ig_NG": "Igbo (Naijiria)", "is_IS": "Íslenska (Ísland)", "it_CH": "Italiano (Svizzera)", 
    "it_IT": "Italiano (Italia)", "ja_JP": "日本語 (日本)", "ka_GE": "ქართული (საქართველო)", 
    "ko_KR": "한국어 (대한민국)", "la": "Latina", "lb_LU": "Lëtzebuergesch (Lëtzebuerg)", 
    "lt_LT": "Lietuvių (Lietuva)", "lv_LV": "Latviešu (Latvija)", "mt_MT": "Malti (Malta)", 
    "ne_NP": "नेपाली (नेपाल)", "ng_NG": "Oshindonga (Namibia)", "nl_BE": "Nederlands (België)", 
    "nl_NL": "Nederlands (Nederland)", "no_NO": "Norsk (Norge)", "or_IN": "ଓଡ଼ିଆ (ଭାରତ)", 
    "pl_PL": "Polski (Polska)", "pt_BR": "Português (Brasil)", "pt_PT": "Português (Portugal)", 
    "ro_RO": "Română (România)", "ru_RU": "Русский (Россия)", "sk_SK": "Slovenčina (Slovensko)", 
    "sl_SI": "Slovenščina (Slovenija)", "sq_AL": "Shqip (Shqipëria)", "sv_SE": "Svenska (Sverige)", 
    "sw": "Kiswahili", "ta_IN": "தமிழ் (இந்தியா)", "th": "ไทย", "th_TH": "ไทย (ประเทศไทย)", 
    "tl_PH": "Tagalog (Pilipinas)", "tr_TR": "Türkçe (Türkiye)", "tw_GH": "Twi (Ghana)", 
    "uk_UA": "Українська (Україна)", "uz_UZ": "Oʻzbekcha (Oʻzbekiston)", "vi_VN": "Tiếng Việt (Việt Nam)", 
    "yo_NG": "Yorùbá (Nàìjíríà)", "zh_CN": "简体中文 (中国)", "zh_TW": "繁體中文 (台灣)", 
    "zu_ZA": "isiZulu (Ningizimu Afrika)"
}

def choose_language():
    for i, (key, lang) in enumerate(languages.items()):
        print(f"{i + 1}. {key}: {lang}")

    try:
        inp = int(input("Choose a language by entering the corresponding number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return choose_language()
    if inp < 1 or inp > len(languages):
        print(f"Invalid input. Please enter a number between 1 and {len(languages)}.")
        return choose_language()
    
    return list(languages.keys())[inp - 1]
        
        
def gen_word(language):
    fake = Faker(language) 
    return fake.word()


def game_loop(word):
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You've guessed the word!")
            return

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    print(f"Game over! The word was: {word}")




def play_game():
    cprint(r"""
  ██╗  ██╗  █████╗  ███╗   ██╗  ██████╗  ███╗   ███╗  █████╗  ███╗   ██╗
  ██║  ██║ ██╔══██╗ ████╗  ██║ ██╔════╝  ████╗ ████║ ██╔══██╗ ████╗  ██║
  ███████║ ███████║ ██╔██╗ ██║ ██║  ███╗ ██╔████╔██║ ███████║ ██╔██╗ ██║
  ██╔══██║ ██╔══██║ ██║╚██╗██║ ██║   ██║ ██║╚██╔╝██║ ██╔══██║ ██║╚██╗██║
  ██║  ██║ ██║  ██║ ██║ ╚████║ ╚██████╔╝ ██║ ╚═╝ ██║ ██║  ██║ ██║ ╚████║
  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝
    """, "yellow")


if __name__ == "__main__":
    play_game()
    
    language = choose_language()
    
    game_loop(gen_word(language))