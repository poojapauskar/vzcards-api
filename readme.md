## vzcards API

### [Register](https://vzcards-api.herokuapp.com/register/)
* New users register on vzcards using their mobile no. 
* Then click on Verify.

### [Verify](https://vzcards-api.herokuapp.com/verify/)
* Onclick of verify the registered user receives an OTP, in order to verify his mobile no. 
* The user then submits his OTP. 
* If the OTP is valid then he can make further calls.

If his mobile number is in DND list or if the user has not received OTP on verify, he makes a call for send again.

### [Send Again](https://vzcards-api.herokuapp.com/send_again/)
* This API is called if the user does not receive an OTP after varify. 
* Onclick of send again the registered user receives an OTP, in order to verify his mobile no. 
* The user then submits his OTP. 
* If the OTP is valid then he can make further calls.

### [Sync](https://vzcards-api.herokuapp.com/sync/)
This API sync all the contacts of the registered users, check his contacts who are registered for vzcards and makes a list of the his vzcard friends.

### [View Profile](https://vzcards-api.herokuapp.com/my_profile/)
The registered user can view his profile details by making a cal to this API.

The user can view his firstname, lastname, email, industry, company, address, city, pin code, photo.

### [Update Profile ](https://vzcards-api.herokuapp.com/my_profile/update/)
A user can edit his profile details by making a cal to this API.

The user can edit and update his firstname, lastname, email, industry, company, address, city, pin code, photo.

### [Add Feeds](https://vzcards-api.herokuapp.com/ticket_create/)
To add a feed or ticket. 

The feed includes question(want or has), item, its description, created date, date validity, ticket id and ticket photo. 

### [Feeds](https://vzcards-api.herokuapp.com/get_list/)
To get all the feeds or tickets created by our vzcard friends.

In this API we can view the feeds of our vzcard friends and the profile details of the vzcard friend who has added the feed.

### [Connect](https://vzcards-api.herokuapp.com/connect/)
This API is used to connect two vzcard friends.

For example: If a vzcard friend A has Item 1 and another vzcard friend B need Item 1, then the user can connect both A and B. 

### [Response](https://vzcards-api.herokuapp.com/response/) 
To get all the response received for our tickets.

* This gives the connecter details, who has connected our ticket to some other ticket. 
* The details of our ticket for which we have got the response, the details of another ticket which we are connected to. 
* And the details of the person whom we are reffered to.

### [Upload Image](https://vzcards-api.herokuapp.com/upload_image/)
Used to upload image for profile and to upload ticket image.




