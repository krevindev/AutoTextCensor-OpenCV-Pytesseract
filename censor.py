import cv2
import pytesseract

cap = cv2.VideoCapture(0)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = "--tessdata-dir \"C:\\Program Files\\Tesseract-OCR\\tessdata\""

while True:
    ret, frame = cap.read()
    #img = cv2.imread('.\\images\\try3.png')
    frame= cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame, (500,400), interpolation = cv2.INTER_AREA)

    if cv2.waitKey(0) == ord('q'):
        break

    hImg, wImg, _ = frame.shape
    boxes = pytesseract.pytesseract.image_to_data(frame, config=tessdata_dir_config)
    special_characters = "`!\"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{|}~'"
    profanities = ['radiance',
        'puta', 'putangina', 'bobo', 'gago', 'tangina', 'leche', 'pakshet', 'bwisit', 'buwisit', 'pucha', 'ulol', 'lintik', 'punyeta', 'tarantado', 'tang ina',
        'tanga', 'idiot',
        'tae', 'panget', 'pek pek', 'pussy', 'titi', 'penis', 'puwit', 'puwet', 'tarantado', 'stupid',
        'bitch', 'shameless',
        'shit',
        'nigga',
        'nigger',
        'niggers',
        'suck',
        'bullshit',
        'bastard',
        'damn', 'dammit',
        'ass', 'asshole', 'jackass',
        'fuck', 'fucker', 'motherfucker', 'fucked', 'dick'
        ]

    for x,b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                for character in special_characters:
                    if b[-1].__contains__(character):
                        b[-1] = b[-1].replace(character, '').strip()
                if profanities.__contains__(b[-1].lower()):
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(frame, (x,y), (w+x,h+y), (0,0,0), -10)
                else:
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(frame, (x,y), (w+x,h+y), (0,50,255), 1)
    cv2.imshow('Result', frame)
cap.release()
cv2.destroyAllWindows()