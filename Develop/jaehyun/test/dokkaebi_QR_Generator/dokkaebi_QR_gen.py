import qrcode

qr_data = 'yu.ac.kr'

qr_img = qrcode.make(qr_data)    #qrcode.make로 이미지를 만들어 qr_img 변수에 저장합니다.

save_path = qr_data + '.png'        #save_path에 저장될 경로를 저장합니다.

qr_img.save(save_path)