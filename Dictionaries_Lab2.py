#Dictionaries - Lab #2 - Makey_Bot Dictionaries

def main:
makey_bot = {
  'wave_pattern':[45,1,90,1,45,1],
  'eyes_rgb_status': 1,
  'rgb_eye_color_1': 0xff,
  'rgb_eye_color_2': 0x1e,
  '7seg_value': 5,
  'led_1_status': 1,
  'led_1_blink': 1,
  'led_2_status': 1,
  'led_2_blink': 1,
  'led_3_status': 1,
  'led_3_blink': 1,
}
print(makey_bot)


x = True
while x :
  try :
    key = input("Enter a key: ")
    print(makey_bot[key])
    x = False
  except:
    print("Key not found")
else :
  value = input("In this key, enter the value you want to change: ")
  change = input("Enter new value: ")
  
  for x in makey_bot[key]:
      makey_bot.update({makey_bot[value]: change})
  print(makey_bot[key])
  print("Done")
main()
