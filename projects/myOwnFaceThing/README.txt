This project will take a video and turn it into an image, every new frame, one sliver of the image is taken and added to one image, eventually creating a full iamge with the width of the amount of frames in the video.
Uses PIL and other libraries 
Instructions:
1.add video file to folder(Preferabbly around 1920 frames long, so 24 fps X 80 seconds will give you a 1920 photo 30 fps x 64 is 64 seconds long, 32 seconds for 60fps, 
longer and it could break, but I haven't tested that yet.)
2.go into tyhe python file and rename the video file to the one that you inserted into the folder, while you're there, rename the output file to something different than the previous 
one or it will be rewritten
3. Run the python file, you need p3, PIL, and cv2 installed to do so, I used the modern versions of all of those, and I believe those should be good for a few more months at least.
4.Your image will be processed and the python file will quit once it's done.

Future ideas: 
Fix the orange/blue stuff(Switches orange and blue only for some reason)
Add it so instead of taking slivers it takes squares. 
Make a UI
make it so taht you can put a video in a folder instead of naming the video file.
