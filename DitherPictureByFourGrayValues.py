import cv2
import numpy as np

D_1 = [[0, 56], [84, 28]]
img_name = input("Please the Image name that you want to dithering: ")
img = cv2.imread(img_name)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_size = img_gray.size
img_col_size = img_gray[0].size
img_row_size = int(img_size / img_col_size)
q = np.zeros((img_row_size, img_col_size))
output_img = np.zeros((img_row_size, img_col_size))

for cur_row in range(img_row_size):
    for cur_col in range(img_col_size):
        q[cur_row][cur_col] = int(img_gray[cur_row][cur_col]/85)

for cur_row in range(img_row_size):
    for cur_col in range(img_col_size):
        if (img_gray[cur_row][cur_col] - 85 * q[cur_row][cur_col]) > D_1[cur_row % 2][cur_col % 2]:
            output_img[cur_row][cur_col] = (q[cur_row][cur_col] + 1) * 85
        else:
            output_img[cur_row][cur_col] = (q[cur_row][cur_col] + 0) * 85

        if output_img[cur_row][cur_col] > 255:
            output_img[cur_row][cur_col] = 255
        elif output_img[cur_row][cur_col] < 0:
            output_img[cur_row][cur_col] = 0
cv2.imwrite("B_" + img_name, output_img)
print("Already dithering %s" % (img_name), "by four gray values.")

# cv2.imshow("Origianl Image", img_gray)
# cv2.imshow("New Image", output_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()