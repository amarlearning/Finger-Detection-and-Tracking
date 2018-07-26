import cv2


def main():
    org_image = cv2.imread("../data/house.tiff", 1)
    '''
    SURF is better than SIFT and computes and detects feature fast, 
    but unfortunately both are paid.

    Alternative, we have ORB by OpenCV. Free. OSS.
    PARAM: nfeatures : Number of features to be detected.
                       Default value is around 100.
    '''

    sift = cv2.xfeatures2d.SIFT_create()
    surf = cv2.xfeatures2d.SURF_create()
    orb = cv2.ORB_create(nfeatures=1000)

    kp_sift, decep_sift = sift.detectAndCompute(org_image, None)
    kp_surf, decep_sift = surf.detectAndCompute(org_image, None)
    kp_orb, decep_sift = orb.detectAndCompute(org_image, None)

    org_image_sift = cv2.drawKeypoints(org_image, kp_sift, None)
    org_image_surf = cv2.drawKeypoints(org_image, kp_surf, None)
    org_image_orb = cv2.drawKeypoints(org_image, kp_orb, None)

    cv2.imshow("SIFT Features Detected", org_image_sift)
    cv2.imshow("SURF Features Detected", org_image_surf)
    cv2.imshow("ORB Features Detected", org_image_orb)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
