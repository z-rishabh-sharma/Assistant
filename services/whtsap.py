import pyautogui
import time

def send_whatsapp_message(number, message):
    try:
        # Open WhatsApp web
        pyautogui.hotkey('command', 'space')
        pyautogui.write('Chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('web.whatsapp.com')
        pyautogui.press('enter')
        time.sleep(10)  # Wait for WhatsApp web to load

        # Search for the contact
        pyautogui.click(60, 200)  # Click on search bar
        pyautogui.write(number)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

        # Type and send the message
        pyautogui.click(320, 800)  # Click on message input field
        pyautogui.write(message)
        pyautogui.press('enter')
        print("Message sent successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
number = "916392514381"
message = "This message is for testing purpose, please don't reply."
send_whatsapp_message(number, message)
