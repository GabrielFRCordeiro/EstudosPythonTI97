import os
import cv2


def stopPerson():
    file_image = 'person/parado/'
    image = cv2.imread(os.path.join(file_image, 'megaman4.png'))
    cv2.imshow('Parado', image)
    cv2.waitKey(1000)


def startWalking():
    files_images = 'person/andando/'

    personWalking = sorted([img for img in os.listdir(files_images) if img.endswith('.png')])


    for person_name in personWalking:
        image = cv2.imread(os.path.join(files_images, person_name))
        cv2.imshow('Animação', image)
        cv2.waitKey(100)  # milissegundos

if __name__ == '__main__':

    # stopPerson()

    if cv2.waitKey(33) == ord('a'):
        startWalking()
