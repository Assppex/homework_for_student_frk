import re

def format_phone(phone_number: str) -> dict[str, int]:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    
    formatted_phone_number = "".join(re.findall(r'\d+', phone_number))
    
    if formatted_phone_number.startswith('9') and len(formatted_phone_number) == 10:
        
        formatted_phone_number = '8 (9' + formatted_phone_number[1:3] + ') ' + formatted_phone_number[3:6] + '-' + formatted_phone_number[6:8] + '-' + formatted_phone_number[8:10]
        
    elif (formatted_phone_number.startswith('8') or formatted_phone_number.startswith('7')) and len(formatted_phone_number) == 11:
        
        formatted_phone_number = '8 (9' + formatted_phone_number[2:4] + ') ' + formatted_phone_number[4:7] + '-' + formatted_phone_number[7:9] + '-' + formatted_phone_number[9:11]
        
    else:
        return formatted_phone_number
        
    return formatted_phone_number
