def get_card_bandeira(card_number: str) -> str:
    card_number = card_number.replace(' ', '').replace('-', '')

    if card_number.startswith(('34', '37')) and len(card_number) == 15:
        return 'American Express'
    elif (card_number.startswith(('36','38')) or ( 300 <= int(card_number[:3]) <= 305)) and len(card_number) == 14:
        return 'Diners Club'
    elif (card_number.startswith('6011') or card_number.startswith('65')) and len(card_number) == 16:
        return 'Discover'
    elif card_number.startswith(('2014', '2149')) and len(card_number) == 15:
        return 'enRoute'
    elif card_number.startswith('35') and 16 <= len(card_number) <= 19:
        return 'JCB'
    elif card_number.startswith('8699') and len(card_number) == 15:
        return 'Voyager'
    elif card_number.startswith(('50')):
        return 'Aura'
    elif card_number.startswith('6062') and len(card_number) == 16:
        return 'HiperCard'
    elif card_number.startswith('4') and len(card_number) in [13, 16, 19]:
        return 'Visa'
    elif (51 <= int(card_number[:2]) <= 55 or 2221 <= int(card_number[:4]) <= 2720) and len(card_number) == 16:
        return 'MasterCard'
    else:
        return 'Unknown'

# Código principal (fora da função)
card_number = input("Enter card number: ")
resultado = get_card_bandeira(card_number)
print(resultado)