import qrcode

def Generate_qrcode(data, filename):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img= qr.make_image(fill_color='green',back_color="black")
    img.save(f"{filename}.png")

    
def main():
    data=input("Enter the data for the QR code: ")
    filename=input("Enter the filename for the QR code image: ")
    
    Generate_qrcode(data, filename)
    print(f"QR code saved as {filename}")
    

if __name__=="__main__":
    main()