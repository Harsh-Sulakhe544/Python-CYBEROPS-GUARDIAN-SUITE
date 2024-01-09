'''
Psuedo Algorithm
1.Change string to list datatype.
2.Remove last digit (check digit)
3.Reverse remaining digits.
4.Double digits at even indices.
5.Subtract 9 if over 9.
6.Add the check digit back to the list.
7.Sum all digits.
8.If the sum is divisible by 10 then it is valid; otherwise, Invalid

ex : 5555555555554444 - valid 
ex : 1234567890123456 - invalid or any random choice 
'''
import logging

def hide_sensitive_info(card_number: str) -> str:
    """Hide sensitive information in the credit card number. REMEMBER this will ACCEPT only string , not list or tuple or any other things """
    card_str = ''.join(map(str, card_number))
    return card_number[:6] + '*' * 6 + card_number[-4:]

def validate_credit_card(card_number: str) -> bool:
    """This function validates a credit card number."""
    
    # Set up logging to both console and a file
    logging.basicConfig(
        level=logging.INFO,
        # u can have any format for o/p to log file , change the colr , dateformat , asctime
        format='%(asctime)s - %(levelname)s - \033[91m%(levelname)s\033[0m - %(message)s' 
        if logging.getLogger().getEffectiveLevel() != logging.ERROR else '[ERROR] \033[91m%(levelname)s\033[0m - %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),  # Log to console(in terminal )
            logging.FileHandler('credit_card_validator.log')  # Log to file
        ]
    )
    
    try: 
        # card.isdigit() --> will not work directly , so use filter(str.isdigit())
        
        # Preprocess the card number to remove non-digit characters
        card_number = ''.join(filter(str.isdigit, card_number))
        
        if len(card_number) != 16:
            logging.error("Invalid input. Please enter a 16-digit numeric credit card number.")
            return False
            
        if len(card_number) == 16:
            print("Wait Validating ...")    
            
        # 1. Change datatype to list[int]
        card_number = [int(num) for num in card_number]

        # 2. Remove the last digit:
        checkDigit = card_number.pop(-1)

        # 3. Reverse the remaining digits:
        card_number.reverse()

        # 4. Double digits at even indices
        card_number = [num * 2 if idx % 2 == 0
                    else num for idx, num in enumerate(card_number)]

        # 5. Subtract 9 at even indices if digit is over 9
        # (or you can add the digits)
        card_number = [num - 9 if idx % 2 == 0 and num > 9
                    else num for idx, num in enumerate(card_number)]

        # 6. Add the checkDigit back to the list:
        card_number.append(checkDigit)

        # 7. Sum all digits:
        checkSum = sum(card_number)

        # 8. If checkSum is divisible by 10, it is valid.
        
        # to pass to hide_sensitive_info -> we need to convert list to string 
        if checkSum % 10 == 0:
            logging.info("Credit card validation passed: %s",hide_sensitive_info(''.join(map(str, card_number))))
            return True
        
        else:
            logging.warning("Credit card validation failed: %s",hide_sensitive_info(''.join(map(str, card_number))))
            return False
    
    except Exception as e:
        logging.error("An error occurred during credit card validation: %s", str(e))
        return False